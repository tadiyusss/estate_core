from flask_wtf import FlaskForm
from wtforms import StringField, FileField, TextAreaField
from wtforms.validators import DataRequired

class ConfirmDeletePropertyForm(FlaskForm):
    property_name = StringField('Property Name', validators=[DataRequired()], render_kw={'class': 'fd-input', 'placeholder': 'Enter the property name to confirm deletion'})
    
