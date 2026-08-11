import os
from extensions.estate_core import bp
from flask import render_template, request, redirect, url_for, flash
from core.extensions import db
from flask_login import current_user
from core.utils.decorators import roles_required
from flask_login import login_required
from extensions.estate_core.forms.developer import DeveloperForm
from extensions.estate_core.models.developers import Developer
from extensions.estate_core.models.property_types import PropertyType
from extensions.estate_core.forms.property_type import PropertyTypeForm
from flask_wtf.file import FileRequired
from werkzeug.utils import secure_filename
import uuid

@bp.route('/dashboard/estate-core/property-configurations', methods=['GET', 'POST'])
@login_required
@roles_required(['Administrator', 'Editor'])
def manage_developers():
    developers = Developer.query.order_by(Developer.created_at.desc()).all()
    property_types = PropertyType.query.order_by(PropertyType.created_at.desc()).all()

    return render_template('dashboard/property_configurations.html', developers=developers, property_types=property_types)

@bp.route('/dashboard/estate-core/property-type/create', methods=['GET', 'POST'])
@login_required
@roles_required(['Administrator', 'Editor'])
def create_property_type():
    form = PropertyTypeForm()
    if request.method == "POST":
        if form.validate_on_submit():
            new_property_type = PropertyType(
                name=form.name.data,
                description=form.description.data
            )
            db.session.add(new_property_type)
            db.session.commit()
            flash('Property type created successfully!', 'success')
            return redirect(url_for('estate_core.manage_developers'))
        else:
            flash('Error creating property type. Please check the form for errors.', 'danger')
    return render_template('dashboard/create_or_edit_property_type.html', form=form)

@bp.route('/dashboard/estate-core/property-type/<string:property_type_uuid>/delete')
@login_required
@roles_required(['Administrator', 'Editor'])
def delete_property_type(property_type_uuid):
    property_type = PropertyType.query.filter_by(uuid=property_type_uuid).first_or_404()
    db.session.delete(property_type)
    db.session.commit()
    flash('Property type deleted successfully!', 'success')
    return redirect(url_for('estate_core.manage_developers'))

@bp.route('/dashboard/estate-core/property-type/<string:property_type_uuid>/edit', methods=['GET', 'POST'])
@login_required
@roles_required(['Administrator', 'Editor'])
def edit_property_type(property_type_uuid):
    property_type = PropertyType.query.filter_by(uuid=property_type_uuid).first_or_404()
    form = PropertyTypeForm(obj=property_type)

    if request.method == "POST":
        if form.validate_on_submit():
            property_type.name = form.name.data
            property_type.description = form.description.data
            db.session.commit()
            flash('Property type updated successfully!', 'success')
            return redirect(url_for('estate_core.manage_developers'))
        else:
            flash('Error updating property type. Please check the form for errors.', 'danger')

    return render_template('dashboard/create_or_edit_property_type.html', form=form, property_type=property_type, is_edit=True)

@bp.route('/dashboard/estate-core/developers/create', methods=['GET', 'POST'])
@login_required
@roles_required(['Administrator', 'Editor'])
def create_developer():
    form = DeveloperForm()
    form.logo.validators.append(FileRequired(message='Logo is required.'))
    if request.method == "POST":
        if form.validate_on_submit():

            new_developer = Developer(
                name=form.name.data,
                short_description=form.short_description.data
            )

            if form.logo.data:
                logo_file = form.logo.data
                filename = secure_filename(f"{uuid.uuid4().hex}_{logo_file.filename}")
                logo_path = f'media/{filename}'
                logo_file.save(logo_path)
                new_developer.logo = filename

            db.session.add(new_developer)
            db.session.commit()

            flash('Developer created successfully!', 'success')
            return redirect(url_for('estate_core.create_developer'))
        else:
            flash('Error creating developer. Please check the form for errors.', 'danger')
        
    return render_template('dashboard/create_or_edit_developer.html', form=form)

@bp.route('/dashboard/estate-core/developers/<string:developer_uuid>/delete')
@login_required
@roles_required(['Administrator', 'Editor'])
def delete_developer(developer_uuid):
    developer = Developer.query.filter_by(uuid=developer_uuid).first_or_404()
    developer.delete()
    flash('Developer deleted successfully!', 'success')
    return redirect(url_for('estate_core.manage_developers'))

@bp.route('/dashboard/estate-core/developers/<string:developer_uuid>/edit', methods=['GET', 'POST'])
@login_required
@roles_required(['Administrator', 'Editor'])
def edit_developer(developer_uuid):
    developer = Developer.query.filter_by(uuid=developer_uuid).first_or_404()
    form = DeveloperForm(obj=developer)

    if request.method == "POST":
        if form.validate_on_submit():
            developer.name = form.name.data
            developer.short_description = form.short_description.data

            if form.logo.data:
                if developer.logo:
                    old_logo_path = f'media/{developer.logo}'
                    if os.path.exists(old_logo_path):
                        os.remove(old_logo_path)

                logo_file = form.logo.data
                logo_path = f'media/{logo_file.filename}'
                logo_file.save(logo_path)
                developer.logo = logo_file.filename

            db.session.commit()
            flash('Developer updated successfully!', 'success')
            return redirect(url_for('estate_core.manage_developers'))
        else:
            flash('Error updating developer. Please check the form for errors.', 'danger')

    return render_template('dashboard/create_or_edit_developer.html', form=form, developer=developer, is_edit=True)