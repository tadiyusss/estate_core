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
    if request.method == "POST":
        if form.validate_on_submit():
            # show all fields that has errors
            print(form.errors)
            print(form.data)
            flash('Property created successfully!', 'success')
            return redirect(url_for('estate_core.manage_properties'))
        else:
            print(form.errors)
            flash('Please correct the errors in the form.', 'danger')
    return render_template('dashboard/create_property.html', form=form)