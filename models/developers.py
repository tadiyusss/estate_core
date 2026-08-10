from datetime import datetime
from core.extensions import db
import uuid
import os

class Developer(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    uuid = db.Column(db.String(36), unique=True, nullable=False, default=lambda: str(uuid.uuid4()))

    logo = db.Column(db.String(255), nullable=False)
    name = db.Column(db.String(100), nullable=False)
    short_description = db.Column(db.String(255), nullable=False)

    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    def delete(self):
        if self.logo:
            logo_path = os.path.join('media', self.logo)
            if os.path.exists(logo_path):
                os.remove(logo_path)

        db.session.delete(self)
        db.session.commit()