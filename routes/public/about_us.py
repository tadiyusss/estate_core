from extensions.estate_core import bp
from flask import render_template
from extensions.landing_page.models import TeamMember, OfficeLocation, PhoneNumber
from extensions.landing_page.decorators.visitor_tracker import track_visitor


@bp.route('/about-us')
@track_visitor
def about_us():
    team_members = TeamMember.query.order_by(TeamMember.placement_order.asc()).all()
    office_locations = OfficeLocation.query.order_by(OfficeLocation.created_at.desc()).all()
    phone_numbers = PhoneNumber.query.order_by(PhoneNumber.created_at.desc()).all()
    return render_template('public/about_us.html', team_members=team_members, office_locations=office_locations, phone_numbers=phone_numbers)

