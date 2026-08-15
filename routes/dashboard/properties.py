from wtforms import FormField
from extensions.estate_core import bp
from flask import render_template, request, redirect, url_for, flash
from core.extensions import db
from core.utils.decorators import roles_required
from flask_login import login_required
from extensions.estate_core.forms.property_listing import AmenitiesForm, CreatePropertyForm
from extensions.estate_core.models import Developer, PropertyType, PropertyListing, Amenity, PropertyImage
from extensions.estate_core.forms.filters.property_listing import FilterPropertyForm
from extensions.estate_core.models.property_listing import STATUS_CHOICES
from extensions.estate_core.forms.confirm_delete_property import ConfirmDeletePropertyForm
from werkzeug.utils import secure_filename
import uuid

@bp.route('/dashboard/estate-core/properties')
@login_required
@roles_required(['Administrator', 'Editor'])
def manage_properties():
    filter_form = FilterPropertyForm(request.args)
    filter_form.developer.choices = [(developer.id, developer.name) for developer in Developer.query.all()] if Developer.query.count() > 0 else []
    filter_form.developer.choices.insert(0, ('', 'All Developers'))
    filter_form.property_type.choices = [(property_type.id, property_type.name) for property_type in PropertyType.query.all()] if PropertyType.query.count() > 0 else []
    filter_form.property_type.choices.insert(0, ('', 'All Property Types'))
    filter_form.status.choices.insert(0, ('', 'All Statuses'))
    status_choices = dict(STATUS_CHOICES)
    per_page = 10

    query = PropertyListing.query.order_by(PropertyListing.created_at.desc())

    if filter_form.query.data:
        query = query.filter(PropertyListing.name.contains(filter_form.query.data) | PropertyListing.description.contains(filter_form.query.data) | PropertyListing.location.contains(filter_form.query.data))

    if filter_form.developer.data:
        query = query.filter(PropertyListing.developer_id == filter_form.developer.data)
        
    if filter_form.property_type.data:
        query = query.filter(PropertyListing.property_type_id == filter_form.property_type.data)

    if filter_form.status.data:
        query = query.filter(PropertyListing.status == filter_form.status.data)

    filter_form.process()  
    page = request.args.get('page', 1, type=int)
    properties = query.paginate(page=page, per_page=per_page)
    filters_get_values = request.args.to_dict()
    filters_get_values.pop('page', None)
    
    return render_template('dashboard/properties.html', properties=properties, filter_form=filter_form, filters_get_values=filters_get_values, per_page=per_page, pagination=properties, status_choices=status_choices)

@bp.route('/dashboard/estate-core/properties/confirm-delete/<string:property_uuid>', methods=['GET', 'POST'])
@login_required
@roles_required(['Administrator', 'Editor'])
def confirm_delete_property(property_uuid):
    property_listing = PropertyListing.query.filter_by(uuid=property_uuid).first_or_404()
    form = ConfirmDeletePropertyForm()

    if request.method == "POST":
        if form.validate_on_submit():
            if form.property_name.data == property_listing.name:
                db.session.delete(property_listing)
                db.session.commit()
                flash('Property deleted successfully!', 'success')
                return redirect(url_for('estate_core.manage_properties'))
            else:
                flash('Property name does not match. Please try again.', 'danger')
        else:
            flash('Please correct the errors in the form.', 'danger')

    return render_template('dashboard/confirm_delete_property.html', property_listing=property_listing, form=form)

@bp.route('/dashboard/estate-core/properties/create', methods=['GET', 'POST'])
@login_required
@roles_required(['Administrator', 'Editor'])
def create_property():
    form = CreatePropertyForm()
    form.developer.choices = [(developer.id, developer.name) for developer in Developer.query.all()] if Developer.query.count() > 0 else []
    form.property_type.choices = [(property_type.id, property_type.name) for property_type in PropertyType.query.all()] if PropertyType.query.count() > 0 else []

    if request.method == "POST":
        if form.validate_on_submit():
            
            new_property = PropertyListing(
                developer_id=form.developer.data,
                property_type_id=form.property_type.data,
                name=form.name.data,
                description=form.description.data,
                status=form.status.data,
                location=form.location.data,
                start_price_range=form.start_price_range.data,
                end_price_range=form.end_price_range.data,
                min_lot_size=form.min_lot_size.data,
                max_lot_size=form.max_lot_size.data,
                min_floor_area=form.min_floor_area.data,
                max_floor_area=form.max_floor_area.data
            )
            db.session.add(new_property)
            db.session.commit()

            for amenity_form in form.amenities_list.entries:
                amenity_name = amenity_form.form.amenities.data
                if amenity_name:
                    new_amenity = Amenity(amenity=amenity_name, property_listing_id=new_property.id)
                    db.session.add(new_amenity)
            db.session.commit()

            for image in form.images.data:
                if image:
                    filename = secure_filename(image.filename)
                    unique_filename = f"{uuid.uuid4().hex}_{filename}"
                    image.save(f"media/{unique_filename}")
                    new_image = PropertyImage(property_id=new_property.id, image_filename=unique_filename)
                    db.session.add(new_image)
            db.session.commit()

            flash('Property created successfully!', 'success')
            return redirect(url_for('estate_core.manage_properties'))
        else:
            flash('Please correct the errors in the form.', 'danger')
    return render_template('dashboard/create_or_edit_property.html', form=form, is_edit=False, property_listing=None)


@bp.route('/dashboard/estate-core/properties/edit/<string:property_uuid>', methods=['GET', 'POST'])
@login_required
@roles_required(['Administrator', 'Editor'])
def edit_property(property_uuid):
    property_listing = PropertyListing.query.filter_by(uuid=property_uuid).first_or_404()
    form = CreatePropertyForm(obj=property_listing)
    form.developer.choices = [(developer.id, developer.name) for developer in Developer.query.all()] if Developer.query.count() > 0 else []
    form.property_type.choices = [(property_type.id, property_type.name) for property_type in PropertyType.query.all()] if PropertyType.query.count() > 0 else []

    if request.method == "POST":
        if form.validate_on_submit():
            print(form.images.data)
            property_listing.developer_id = form.developer.data
            property_listing.property_type_id = form.property_type.data
            property_listing.name = form.name.data
            property_listing.description = form.description.data
            property_listing.status = form.status.data
            property_listing.location = form.location.data
            property_listing.start_price_range = form.start_price_range.data
            property_listing.end_price_range = form.end_price_range.data
            property_listing.min_lot_size = form.min_lot_size.data
            property_listing.max_lot_size = form.max_lot_size.data
            property_listing.min_floor_area = form.min_floor_area.data
            property_listing.max_floor_area = form.max_floor_area.data

            db.session.commit()

            Amenity.query.filter_by(property_listing_id=property_listing.id).delete()
            for amenity_form in form.amenities_list.entries:
                amenity_name = amenity_form.form.amenities.data
                if amenity_name:
                    new_amenity = Amenity(amenity=amenity_name, property_listing_id=property_listing.id)
                    db.session.add(new_amenity)
            db.session.commit()

            for image in form.images.data:
                if image:
                    filename = secure_filename(image.filename)
                    unique_filename = f"{uuid.uuid4().hex}_{filename}"
                    image.save(f"media/{unique_filename}")
                    new_image = PropertyImage(property_id=property_listing.id, image_filename=unique_filename)
                    db.session.add(new_image)
            db.session.commit()

            flash('Property updated successfully!', 'success')
            return redirect(url_for('estate_core.manage_properties'))
        else:
            flash('Please correct the errors in the form.', 'danger')

    return render_template('dashboard/create_or_edit_property.html', form=form, property_uuid=property_uuid, property_listing=property_listing, is_edit=True)

@bp.route('/dashboard/estate-core/properties/delete-image/<string:image_uuid>')
@login_required
@roles_required(['Administrator', 'Editor'])
def delete_property_image(image_uuid):
    image = PropertyImage.query.filter_by(uuid=image_uuid).first_or_404()
    image.delete_image_file()
    db.session.delete(image)
    db.session.commit()
    flash('Property image deleted successfully!', 'success')
    return redirect(url_for('estate_core.edit_property', property_uuid=image.property_listing.uuid))