from extensions.estate_core import bp
from flask import render_template, request, redirect, url_for, flash
from core.extensions import db
from flask_login import current_user
from extensions.landing_page.forms.contact_us import ContactUsForm
from extensions.landing_page.models import TeamMember
from extensions.landing_page.models import ContactUs
from extensions.landing_page.models.testimonial import Testimonial

@bp.route('/', methods=['GET', 'POST'])
def index():
    form = ContactUsForm()
    team_members = TeamMember.query.all()
    testimonials = Testimonial.query.all()

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

        return render_template('public/index.html', form=form, success=True, team_members=team_members, testimonials=testimonials)
    
    return render_template('public/index.html', form=form, team_members=team_members, testimonials=testimonials)

