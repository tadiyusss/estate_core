from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField
from wtforms.validators import DataRequired, Length

class PropertyTypeForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired(), Length(max=100)], render_kw={'class': 'fd-input'}, description="Condo, House, Apartment, etc.")
    description = TextAreaField('Description', validators=[DataRequired(), Length(max=255)], render_kw={'class': 'fd-input', 'rows': 5}, description="A brief description of the property type.")