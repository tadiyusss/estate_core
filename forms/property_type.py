from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import DataRequired, Length

class PropertyTypeForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired(), Length(max=100)], render_kw={'class': 'fd-input'}, description="Condo, House, Apartment, etc.")
    description = StringField('Description', validators=[DataRequired(), Length(max=255)], render_kw={'class': 'fd-input'}, description="A brief description of the property type.")