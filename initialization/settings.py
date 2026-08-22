from core.utils.settings import SettingCategory, SettingItem
from wtforms import FileField, StringField
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
    )
]

def register_settings():
    for category in SETTINGS:
        register_category(category)
