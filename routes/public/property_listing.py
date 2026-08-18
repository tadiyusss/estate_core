from extensions.estate_core import bp
from flask import render_template, request, redirect, url_for, flash
from core.extensions import db
from extensions.estate_core.models import PropertyListing
from extensions.estate_core.forms.filters.public_property_listing import FilterPublicPropertyListingForm
from extensions.estate_core.models import PropertyType, Developer
from extensions.landing_page.decorators.visitor_tracker import track_visitor

@bp.app_template_global()
def format_price(price):
    """
    Format a price value as a string with commas and a currency symbol.
    :param price: The price value to format.
    :return: A formatted price string.
    """
    return f"₱{price:,.2f}"

@bp.route('/property-listing', methods=['GET', 'POST'])
@track_visitor
def property_listing():
    form = FilterPublicPropertyListingForm()
    property_listings = PropertyListing.query

    locations = db.session.query(PropertyListing.location).distinct().all()
    prices = db.session.query(PropertyListing.start_price_range).distinct().order_by(PropertyListing.start_price_range.asc()).all()
    property_types = PropertyType.query.all()
    developers = db.session.query(Developer.name).distinct().all()

    form.property_type.choices = [("", "All Types")] + [(ptype.name, ptype.name) for ptype in property_types]
    form.price.choices = [("", "All Prices")] + [(price[0], f"₱{price[0]:,.2f}") for price in prices]
    form.location.choices = [("", "All Locations")] + [(loc[0], loc[0]) for loc in locations]
    form.developer.choices = [("", "All Developers")] + [(dev[0], dev[0]) for dev in developers]

    if request.args.get('location'):
        property_listings = property_listings.filter_by(location=request.args.get('location'))
        form.location.data = request.args.get('location')
    if request.args.get('price'):
        property_listings = property_listings.filter_by(start_price_range=request.args.get('price'))
        form.price.data = request.args.get('price')
    if request.args.get('status'):
        property_listings = property_listings.filter_by(status=request.args.get('status'))
        form.status.data = request.args.get('status')
    if request.args.get('property_type'):
        property_type = PropertyType.query.filter_by(name=request.args.get('property_type')).first()
        if property_type:
            property_listings = property_listings.filter_by(property_type=property_type)
        form.property_type.data = request.args.get('property_type')
    if request.args.get('developer'):
        developer_name = request.args.get('developer')
        property_listings = property_listings.join(PropertyListing.developer).filter_by(name=developer_name)
        form.developer.data = developer_name

    return render_template('public/property_listing.html', property_listings=property_listings.all(), form=form)


@bp.route('/property-listing/<string:property_uuid>', methods=['GET'])
@track_visitor
def property_listing_detail(property_uuid):
    property_listing = PropertyListing.query.filter_by(uuid=property_uuid).first_or_404()
    similar_properties = (
        PropertyListing.query.filter(
            PropertyListing.uuid != property_listing.uuid
        )
        .filter(
            (PropertyListing.location == property_listing.location)
            | (PropertyListing.start_price_range == property_listing.start_price_range)
            | (PropertyListing.developer_id == property_listing.developer_id)
        )
        .limit(3)
        .all()
    )
    return render_template('public/property_listing_detail.html', property_listing=property_listing, similar_properties=similar_properties)