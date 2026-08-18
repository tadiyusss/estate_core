from extensions.estate_core import bp
from core.extensions import db
from flask import render_template
from extensions.landing_page.decorators.visitor_tracker import track_visitor
from extensions.landing_page.forms.contact_us import ContactUsForm
from extensions.landing_page.models import ContactUs
from extensions.landing_page.models.office_location import OfficeLocation
from extensions.landing_page.models.phone_number import PhoneNumber
from extensions.estate_core.models import PropertyListing

@bp.route('/contact-us', methods=['GET', 'POST'])
@track_visitor
def contact_us():
    form = ContactUsForm()
    office_locations = OfficeLocation.query.order_by(OfficeLocation.created_at.desc()).all()
    phone_numbers = PhoneNumber.query.order_by(PhoneNumber.created_at.desc()).all()
    recent_properties = PropertyListing.query.order_by(PropertyListing.created_at.desc()).limit(3).all()

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

        return render_template('public/contact_us.html', form=form, success=True, office_locations=office_locations, phone_numbers=phone_numbers, recent_properties=recent_properties)

    return render_template('public/contact_us.html', form=form, office_locations=office_locations, phone_numbers=phone_numbers, recent_properties=recent_properties)