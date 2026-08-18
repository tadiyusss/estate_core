from extensions.estate_core import bp
from flask import render_template, request, redirect, url_for, flash
from core.extensions import db
from flask_login import current_user
from extensions.landing_page.decorators.visitor_tracker import track_visitor
from extensions.estate_core.models import Developer

@bp.route('/developers')
@track_visitor
def developers():
    developers = Developer.query.all()
    return render_template('public/developers.html', developers=developers)
