from flask_wtf import FlaskForm
from wtforms import StringField, SelectField
from wtforms.validators import Length
from extensions.estate_core.models.property_listing import STATUS_CHOICES

class FilterPropertyForm(FlaskForm):
    query = StringField('Query', validators=[Length(max=100)], render_kw={'class': 'fd-input', 'placeholder': 'Search by name...'})
    developer = SelectField('Developer', choices=[], render_kw={'class': 'fd-input'})
    property_type = SelectField('Property Type', choices=[], render_kw={'class': 'fd-input'})
    status = SelectField('Status', choices=STATUS_CHOICES, render_kw={'class': 'fd-input'})