from extensions.estate_core import bp
from flask import render_template, request, redirect, url_for, flash
from core.extensions import db
from flask_login import current_user
from core.utils.decorators import roles_required
from flask_login import login_required
from extensions.estate_core.forms.developer import DeveloperForm
from extensions.estate_core.models.developers import Developer

@bp.route('/dashboard/estate-core/developers', methods=['GET', 'POST'])
@login_required
@roles_required(['Administrator', 'Editor'])
def manage_developers():
    developers = Developer.query.order_by(Developer.created_at.desc()).all()
    return render_template('dashboard/developers.html', developers=developers)

@bp.route('/dashboard/estate-core/developers/create', methods=['GET', 'POST'])
@login_required
@roles_required(['Administrator', 'Editor'])
def create_developer():
    form = DeveloperForm()

    if request.method == "POST":
        if form.validate_on_submit():

            new_developer = Developer(
                name=form.name.data,
                short_description=form.short_description.data
            )

            if form.logo.data:
                logo_file = form.logo.data
                logo_path = f'media/{logo_file.filename}'
                logo_file.save(logo_path)
                new_developer.logo = logo_file.filename

            db.session.add(new_developer)
            db.session.commit()

            flash('Developer created successfully!', 'success')
            return redirect(url_for('estate_core.create_developer'))
        else:
            flash('Error creating developer. Please check the form for errors.', 'danger')
        
    return render_template('dashboard/create_or_edit_developer.html', form=form)