from flask_wtf import FlaskForm
from wtforms import SelectField
from extensions.estate_core.models.property_listing import STATUS_CHOICES

class FilterPublicPropertyListingForm(FlaskForm):
    developer = SelectField('Developer', choices=[("", "All Developers")], render_kw={"class": "w-full px-2 py-2 rounded focus:ring-2 focus:ring-emerald-500/50 focus:outline-none md:text-base text-sm [&>option]:text-zinc-900"})
    location = SelectField('Location', choices=[("", "All Locations")], render_kw={"class": "w-full px-2 py-2 rounded focus:ring-2 focus:ring-emerald-500/50 focus:outline-none md:text-base text-sm [&>option]:text-zinc-900"})
    price = SelectField('Price', choices=[("", "All Prices")], render_kw={"class": "w-full px-2 py-2 rounded focus:ring-2 focus:ring-emerald-500/50 focus:outline-none md:text-base text-sm [&>option]:text-zinc-900"})
    status = SelectField('Status', choices=[("", "All Statuses")] + list(STATUS_CHOICES), render_kw={"class": "w-full px-2 py-2 rounded focus:ring-2 focus:ring-emerald-500/50 focus:outline-none md:text-base text-sm [&>option]:text-zinc-900"})
    property_type = SelectField('Property Type', choices=[("", "All Types")], render_kw={"class": "w-full px-2 py-2 rounded focus:ring-2 focus:ring-emerald-500/50 focus:outline-none md:text-base text-sm [&>option]:text-zinc-900"})