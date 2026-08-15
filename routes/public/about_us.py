from extensions.estate_core import bp
from flask import render_template, request, redirect, url_for, flash
from core.extensions import db
from flask_login import current_user


@bp.route('/about-us', methods=['GET', 'POST'])
def about_us():
    return render_template('public/about_us.html')

