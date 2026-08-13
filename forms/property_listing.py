from flask_wtf import FlaskForm
from wtforms import StringField, FileField, TextAreaField, SelectField, IntegerField, FieldList
from wtforms.validators import DataRequired, Length
from flask_wtf.file import FileAllowed
from extensions.estate_core.models import Developer
from extensions.estate_core.models import PropertyType


class CreatePropertyForm(FlaskForm):
    developer = SelectField('Developer', validators=[DataRequired()], render_kw={'class': 'fd-input'}, choices=[(developer.id, developer.name) for developer in Developer.query.all()])
    property_type = SelectField('Property Type', validators=[DataRequired()], render_kw={'class': 'fd-input'}, choices=[(property_type.id, property_type.name) for property_type in PropertyType.query.all()])

    location = StringField('Location', validators=[DataRequired(), Length(max=255)], render_kw={'class': 'fd-input', 'placeholder': 'BGC, Taguig City, Metro Manila, etc...'})
    status = SelectField('Status', validators=[DataRequired()], render_kw={'class': 'fd-input'}, choices=[('pre_selling', 'Pre-selling'), ('under_construction', 'Under Construction'), ('ready_for_occupancy', 'Ready for Occupancy')])

    min_lot_size = IntegerField('Lot Size (sq meters)', render_kw={'class': 'fd-input'})
    max_lot_size = IntegerField('Max Lot Size (sq meters)', render_kw={'class': 'fd-input'})

    min_floor_area = IntegerField('Min Floor Area (sq meters)', render_kw={'class': 'fd-input'})
    max_floor_area = IntegerField('Max Floor Area (sq meters)', render_kw={'class': 'fd-input'})

    start_price_range = IntegerField('Start Price Range', validators=[DataRequired()], render_kw={'class': 'fd-input', 'placeholder': '₱100,000'})
    end_price_range = IntegerField('End Price Range', validators=[DataRequired()], render_kw={'class': 'fd-input', 'placeholder': '₱10,000,000'})

    name = StringField('Name', validators=[DataRequired(), Length(max=100)], render_kw={'class': 'fd-input', 'placeholder': 'ACME Residences, Amaia Scapes, etc...'})
    description = TextAreaField('Description', validators=[DataRequired(), Length(max=1000)], render_kw={'class': 'fd-input', 'rows': 10, 'placeholder': "Whether you're looking for a comfortable home or a valuable investment..."})
    features = FieldList(StringField('Feature', render_kw={'class': 'fd-input'}), min_entries=1, max_entries=50)
    