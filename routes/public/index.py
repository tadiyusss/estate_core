from extensions.estate_core import bp
from flask import render_template, request, redirect, url_for, flash
from core.extensions import db
from flask_login import current_user


@bp.route('/', methods=['GET', 'POST'])
def index():
    return render_template('public/index.html')

