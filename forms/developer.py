
from flask_wtf import FlaskForm
from wtforms import StringField, FileField, TextAreaField
from wtforms.validators import DataRequired, Length
from flask_wtf.file import FileAllowed, FileRequired

ALLOWED_LOGO_EXTENSIONS = ['jpg', 'jpeg', 'png', 'gif', 'svg', 'webp']

class DeveloperForm(FlaskForm):
    logo = FileField('Logo', validators=[FileAllowed(ALLOWED_LOGO_EXTENSIONS, 'Only image files are allowed.'), FileRequired('Logo is required.')], render_kw={'class': 'fd-file-input'})
    name = StringField('Name', validators=[DataRequired(), Length(max=100)], render_kw={'class': 'fd-input'})
    short_description = StringField('Short Description', validators=[DataRequired(), Length(max=255)], render_kw={'class': 'fd-input'})
    
