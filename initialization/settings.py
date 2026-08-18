from core.utils.settings import SettingCategory, SettingItem
from wtforms import FileField
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
    )
]

def register_settings():
    for category in SETTINGS:
        register_category(category)
