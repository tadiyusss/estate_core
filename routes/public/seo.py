from extensions.estate_core import bp
from flask import Response, url_for, render_template
from extensions.estate_core.models import PropertyListing, Developer


@bp.route('/sitemap.xml')
def handle_sitemap():
    property_listings = PropertyListing.query.all()
    developers = Developer.query.all()

    static_urls = [
        url_for('estate_core.index', _external=True),
        url_for('estate_core.about_us', _external=True),
        url_for('estate_core.developers', _external=True),
        url_for('estate_core.property_listing', _external=True),
        url_for('estate_core.contact_us', _external=True),
    ]

    developers_url = [url_for('estate_core.developers', developer_name=developer.name, _external=True) for developer in developers]
    property_listings_url = [url_for('estate_core.property_listing_detail', developer_name=property_listing.developer.name, property_name=property_listing.name, _external=True) for property_listing in property_listings]

    sitemap_xml = render_template('public/sitemap.xml', static_urls=static_urls, developers_url=developers_url, property_listings_url=property_listings_url)
    return Response(sitemap_xml, mimetype='application/xml')

@bp.route('/robots.txt')
def handle_robots():
    robots_text = """User-agent: *
Disallow: /dashboard/
Sitemap: {sitemap_url}""".format(sitemap_url=url_for('estate_core.handle_sitemap', _external=True))
    return Response(robots_text, mimetype='text/plain')