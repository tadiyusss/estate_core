from extensions.estate_core import bp
from flask import render_template, request, redirect, url_for, flash
from core.extensions import db
from core.utils.decorators import roles_required
from flask_login import login_required
from extensions.estate_core.forms.property_listing import CreatePropertyForm

@bp.route('/dashboard/estate-core/properties')
@login_required
@roles_required(['Administrator', 'Editor'])
def manage_properties():
    return render_template('dashboard/properties.html')


@bp.route('/dashboard/estate-core/properties/create', methods=['GET', 'POST'])
@login_required
@roles_required(['Administrator', 'Editor'])
def create_property():
    form = CreatePropertyForm()

    return render_template('dashboard/create_property.html', form=form)