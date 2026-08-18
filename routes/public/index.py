from extensions.estate_core import bp
from flask import render_template, request, redirect, url_for, flash
from core.extensions import db
from flask_login import current_user
from extensions.estate_core.models.property_types import PropertyType
from extensions.landing_page.forms.contact_us import ContactUsForm
from extensions.landing_page.models import TeamMember
from extensions.landing_page.models import ContactUs
from extensions.landing_page.models.testimonial import Testimonial
from extensions.estate_core.forms.filters.public_property_listing import FilterPublicPropertyListingForm
from extensions.estate_core.models import PropertyListing

@bp.route('/', methods=['GET', 'POST'])
def index():
    form = ContactUsForm()
    filter_form = FilterPublicPropertyListingForm()

    team_members = TeamMember.query.all()
    testimonials = Testimonial.query.all()
    recent_properties = PropertyListing.query.order_by(PropertyListing.created_at.desc()).limit(3).all()

    locations = db.session.query(PropertyListing.location).distinct().all()
    prices = db.session.query(PropertyListing.start_price_range).distinct().order_by(PropertyListing.start_price_range.asc()).all()
    property_types = PropertyType.query.all()
    
    filter_form.property_type.choices = [("", "All Types")] + [(ptype.name, ptype.name) for ptype in property_types]
    filter_form.price.choices = [("", "All Prices")] + [(price[0], f"₱{price[0]:,.2f}") for price in prices]
    filter_form.location.choices = [("", "All Locations")] + [(loc[0], loc[0]) for loc in locations]


    if form.validate_on_submit():
        contact_us_entry = ContactUs(
            first_name=form.first_name.data,
            last_name=form.last_name.data,
            email=form.email.data,
            number_code=form.number_code.data,
            phone_number=form.phone_number.data,
            message=form.message.data
        )
        db.session.add(contact_us_entry)
        db.session.commit()

        return render_template('public/index.html', form=form, success=True, team_members=team_members, testimonials=testimonials, recent_properties=recent_properties, filter_form=filter_form)

    return render_template('public/index.html', form=form, team_members=team_members, testimonials=testimonials, recent_properties=recent_properties, filter_form=filter_form)

