from core.utils.settings import SettingCategory, SettingItem
from wtforms import FileField, StringField, TextAreaField
from core.utils.registry.settings import register_category

SETTINGS = [
    SettingCategory(
        name="hero_section",
        nice_name="Hero Section",
        description="Settings related to the hero section.",
        settings=[
            SettingItem(
                key="hero_section_background_video",
                name="Hero Section Background Video",
                value="",
                field=FileField(
                    "Hero Section Background Video",
                    description="The background video for the hero section.",
                    render_kw={
                        "class": "fd-file-input"
                    }
                ),
                category_name="hero_section"
            )
        ]
    ),
    SettingCategory(
        name="map_configuration",
        nice_name="Map Configuration",
        description="Settings related to the Google Maps configuration.",
        settings=[
            SettingItem(
                key="google_maps_api_key",
                name="Google Maps API Key",
                value="",
                field=StringField(
                    "Google Maps API Key",
                    description="The API key for the Google Maps configuration.",
                    render_kw={
                        "class": "fd-input"
                    }
                ),
                category_name="map_configuration"
            )
        ]
    ),
    SettingCategory(
        name="seo_settings",
        nice_name="SEO Settings",
        description="Settings related to SEO.",
        settings=[
            SettingItem(
                key="title_prefix",
                name="Title Prefix",
                value="| Ayala Land Properties in the Philippines",
                field=StringField(
                    "Title Prefix",
                    description="The prefix for the page titles.",
                    render_kw={
                        "class": "fd-input"
                    }
                ),
                category_name="seo_settings"
            ),
            SettingItem(
                key="home_meta_description",
                name="Home Meta Description",
                value="Explore Ayala Land properties in the Philippines, from condominiums and house-and-lot communities to residential lots in prime locations.",
                field=TextAreaField(
                    "Home Page Meta Description",
                    description="The meta description for the home page.",
                    render_kw={
                        "class": "fd-input",
                        "rows": 6
                    }
                ),
                category_name="seo_settings"
            ),
            SettingItem(
                key="about_us_meta_description",
                name="About Us Meta Description",
                value="Meet our real estate sales team and learn how we help buyers and investors explore Ayala Land and Alveo properties across the Philippines.",
                field=TextAreaField(
                    "About Us Page Meta Description",
                    description="The meta description for the About Us page.",
                    render_kw={
                        "class": "fd-input",
                        "rows": 6
                    }
                ),
                category_name="seo_settings"
            ),
            SettingItem(
                key="developers_meta_description",
                name="Developers Meta Description",
                value="Explore leading real estate developers in the Philippines and discover their residential communities, condominiums, and property developments.",
                field=TextAreaField(
                    "Developers Page Meta Description",
                    description="The meta description for the Developers page.",
                    render_kw={
                        "class": "fd-input",
                        "rows": 6
                    }
                ),
                category_name="seo_settings"
            ),
            SettingItem(
                key="property_listing_meta_description",
                name="Property Listing Meta Description",
                value="Browse Ayala Land and Alveo properties in the Philippines, with detailed listings for condominiums, houses, lots, and residential communities.",
                field=TextAreaField(
                    "Property Listing Page Meta Description",
                    description="The meta description for the Property Listing page.",
                    render_kw={
                        "class": "fd-input",
                        "rows": 6
                    }
                ),
                category_name="seo_settings"
            ),
            SettingItem(
                key="contact_us_meta_description",
                name="Contact Us Meta Description",
                value="Get in touch with our real estate sales team to inquire about Ayala Land properties in the Philippines, including condominiums, houses, and residential communities.",
                field=TextAreaField(
                    "Contact Us Page Meta Description",
                    description="The meta description for the Contact Us page.",
                    render_kw={
                        "class": "fd-input",
                        "rows": 6
                    }
                ),
                category_name="seo_settings"
            )
        ]   
    )
]

def register_settings():
    for category in SETTINGS:
        register_category(category)
