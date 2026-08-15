from core.extensions import db
import uuid
from extensions.estate_core.models import PropertyListing
from datetime import datetime

class Amenity(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    uuid = db.Column(
        db.String(36),
        unique=True,
        nullable=False,
        default=lambda: str(uuid.uuid4())
    )

    property_listing_id = db.Column(
        db.Integer,
        db.ForeignKey(PropertyListing.id),
        nullable=False
    )

    property_listing = db.relationship(
        PropertyListing,
        backref=db.backref(
            'amenities',
            cascade='all, delete-orphan'
        )
    )

    amenity = db.Column(db.String(100), nullable=False)

    created_at = db.Column(db.DateTime, default=datetime.utcnow)
