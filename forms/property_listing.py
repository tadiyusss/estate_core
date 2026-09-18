from flask_wtf import FlaskForm
from wtforms import StringField, FileField, TextAreaField, SelectField, DecimalField, FieldList, Form, FormField
from wtforms.validators import DataRequired, Length, Optional
from flask_wtf.file import FileAllowed, FileSize, MultipleFileField
from extensions.estate_core.models import Developer
from extensions.estate_core.models import PropertyType
from extensions.estate_core.models.property_listing import STATUS_CHOICES

IMAGES_ALLOWED = ['jpg', 'jpeg', 'png', 'gif', 'svg', 'webp', 'avif']
MAX_FILE_SIZE = 100 * 1024 * 1024

class AmenitiesForm(Form):
    amenities = StringField('Amenities', validators=[DataRequired(), Length(max=100)], render_kw={'class': 'fd-input', 'placeholder': 'Swimming Pool, Gym, etc...'})

class CreatePropertyForm(FlaskForm):
    developer = SelectField('Developer', validators=[DataRequired()], render_kw={'class': 'fd-input'})
    property_type = SelectField('Property Type', validators=[DataRequired()], render_kw={'class': 'fd-input'})

    location = StringField('Location', validators=[DataRequired(), Length(max=255)], render_kw={'class': 'fd-input', 'placeholder': 'BGC, Taguig City, Metro Manila, etc...'}, description="Required")
    status = SelectField('Status', validators=[DataRequired()], render_kw={'class': 'fd-input'}, choices=STATUS_CHOICES)

    min_lot_size = DecimalField('Lot Size (sq meters)', validators=[Optional()], render_kw={'class': 'fd-input'}, description="Optional")
    max_lot_size = DecimalField('Max Lot Size (sq meters)', validators=[Optional()], render_kw={'class': 'fd-input'}, description="Optional")

    min_floor_area = DecimalField('Min Floor Area (sq meters)', validators=[Optional()], render_kw={'class': 'fd-input'}, description="Optional")
    max_floor_area = DecimalField('Max Floor Area (sq meters)', validators=[Optional()], render_kw={'class': 'fd-input'}, description="Optional")

    start_price_range = DecimalField('Start Price Range', validators=[DataRequired()], render_kw={'class': 'fd-input', 'placeholder': '₱100,000'}, description="Required")
    end_price_range = DecimalField('End Price Range', validators=[Optional()], render_kw={'class': 'fd-input', 'placeholder': '₱10,000,000'}, description="Optional")

    name = StringField('Name', validators=[DataRequired(), Length(max=100)], render_kw={'class': 'fd-input', 'placeholder': 'ACME Residences, Amaia Scapes, etc...'}, description="Required")
    description = TextAreaField('Description', validators=[DataRequired(), Length(max=1000)], render_kw={'class': 'fd-input w-full', 'rows': 10, 'placeholder': "Whether you're looking for a comfortable home or a valuable investment..."}, description="Required")
    amenities_list = FieldList(FormField(AmenitiesForm), min_entries=1, max_entries=50)

    images = MultipleFileField('Property Images', render_kw={'class': 'hidden', '@change': 'handle_file_change($event)'}, validators=[FileAllowed(IMAGES_ALLOWED, 'Invalid file type. Please upload a valid image. (JPG, PNG, GIF, SVG, WEBP)'), FileSize(max_size=MAX_FILE_SIZE, message="File size must be less than 100MB")], description="Required. You can upload multiple images.")

    longitude = DecimalField('Longitude', validators=[], render_kw={'class': 'hidden', 'x-model': 'longitude'}, description="Required")
    latitude = DecimalField('Latitude', validators=[], render_kw={'class': 'hidden', 'x-model': 'latitude'}, description="Required")