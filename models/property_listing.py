from datetime import datetime
from core.extensions import db
import uuid
from extensions.estate_core.models import PropertyType

STATUS_CHOICES = ('pre_selling', 'Pre-selling'), ('under_construction', 'Under Construction'), ('ready_for_occupancy', 'Ready for Occupancy')

from extensions.estate_core.models import Developer

class PropertyListing(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    uuid = db.Column(db.String(36), unique=True, nullable=False, default=lambda: str(uuid.uuid4()))

    developer_id = db.Column(db.Integer, db.ForeignKey(Developer.id), nullable=False)
    property_type_id = db.Column(db.Integer, db.ForeignKey(PropertyType.id), nullable=False)

    developer = db.relationship('Developer', backref=db.backref('properties', lazy=True))
    property_type = db.relationship('PropertyType', backref=db.backref('properties', lazy=True))

    name = db.Column(db.String(100), unique=False, nullable=False)
    description = db.Column(db.String(1000), nullable=False)
    status = db.Column(db.Enum(*[choice[0] for choice in STATUS_CHOICES]), nullable=False)
    location = db.Column(db.String(255), nullable=False)

    start_price_range = db.Column(db.Integer, nullable=False)
    end_price_range = db.Column(db.Integer, nullable=False)

    min_lot_size = db.Column(db.Integer, nullable=True)
    max_lot_size = db.Column(db.Integer, nullable=True)
    min_floor_area = db.Column(db.Integer, nullable=True)
    max_floor_area = db.Column(db.Integer, nullable=True)

    created_at = db.Column(db.DateTime, default=datetime.utcnow)