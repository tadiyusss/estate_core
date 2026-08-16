from extensions.estate_core import bp
from flask import render_template, request, redirect, url_for, flash
from core.extensions import db
from extensions.estate_core.models import PropertyListing

@bp.app_template_global()
def format_price(price):
    """
    Format a price value as a string with commas and a currency symbol.
    :param price: The price value to format.
    :return: A formatted price string.
    """
    return f"₱{price:,.2f}"

@bp.route('/property-listing', methods=['GET', 'POST'])
def property_listing():
    property_listings = PropertyListing.query.all()
    return render_template('public/property_listing.html', property_listings=property_listings)

