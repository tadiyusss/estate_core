from flask_wtf import FlaskForm
from wtforms import StringField, FileField, TextAreaField, SelectField, DecimalField, FieldList, Form, FormField
from wtforms.validators import DataRequired, Length
from flask_wtf.file import FileAllowed
from extensions.estate_core.models import Developer
from extensions.estate_core.models import PropertyType
from extensions.estate_core.models.property_listing import STATUS_CHOICES

class AmenitiesForm(Form):
    amenities = StringField('Amenities', validators=[DataRequired(), Length(max=100)], render_kw={'class': 'fd-input', 'placeholder': 'Swimming Pool, Gym, etc...'})

class CreatePropertyForm(FlaskForm):
    developer = SelectField('Developer', validators=[DataRequired()], render_kw={'class': 'fd-input'})
    property_type = SelectField('Property Type', validators=[DataRequired()], render_kw={'class': 'fd-input'})

    location = StringField('Location', validators=[DataRequired(), Length(max=255)], render_kw={'class': 'fd-input', 'placeholder': 'BGC, Taguig City, Metro Manila, etc...'}, description="Required")
    status = SelectField('Status', validators=[DataRequired()], render_kw={'class': 'fd-input'}, choices=STATUS_CHOICES)

    min_lot_size = DecimalField('Lot Size (sq meters)', render_kw={'class': 'fd-input'}, description="Optional")
    max_lot_size = DecimalField('Max Lot Size (sq meters)', render_kw={'class': 'fd-input'}, description="Optional")

    min_floor_area = DecimalField('Min Floor Area (sq meters)', render_kw={'class': 'fd-input'}, description="Optional")
    max_floor_area = DecimalField('Max Floor Area (sq meters)', render_kw={'class': 'fd-input'}, description="Optional")

    start_price_range = DecimalField('Start Price Range', validators=[DataRequired()], render_kw={'class': 'fd-input', 'placeholder': '₱100,000'}, description="Required")
    end_price_range = DecimalField('End Price Range', validators=[DataRequired()], render_kw={'class': 'fd-input', 'placeholder': '₱10,000,000'}, description="Required")

    name = StringField('Name', validators=[DataRequired(), Length(max=100)], render_kw={'class': 'fd-input', 'placeholder': 'ACME Residences, Amaia Scapes, etc...'}, description="Required")
    description = TextAreaField('Description', validators=[DataRequired(), Length(max=1000)], render_kw={'class': 'fd-input w-full', 'rows': 10, 'placeholder': "Whether you're looking for a comfortable home or a valuable investment..."}, description="Required")
    amenities_list = FieldList(FormField(AmenitiesForm), min_entries=1, max_entries=50)