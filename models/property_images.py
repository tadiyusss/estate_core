from datetime import datetime
from core.extensions import db
import uuid
from extensions.estate_core.models import PropertyListing
import os

class PropertyImage(db.Model):

    id = db.Column(
        db.Integer,
        primary_key=True
    )

    uuid = db.Column(
        db.String(36),
        unique=True,
        nullable=False,
        default=lambda: str(uuid.uuid4())
    )

    property_id = db.Column(
        db.Integer,
        db.ForeignKey("property_listing.id"),
        nullable=False
    )

    image_filename = db.Column(
        db.String(255),
        nullable=False
    )

    created_at = db.Column(
        db.DateTime,
        default=datetime.utcnow
    )

    property_listing = db.relationship(
        "PropertyListing",
        back_populates="images",
        lazy="joined"
    )

    def delete_image_file(self):
        try:
            os.remove(
                f"media/{self.image_filename}"
            )
        except FileNotFoundError:
            pass