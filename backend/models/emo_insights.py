from datetime import datetime
from db import db

class EmoInsights(db.Model):
    __tablename__ = 'emo_insights'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    happy = db.Column(db.Integer, nullable=False)
    sad = db.Column(db.Integer, nullable=False)
    angry = db.Column(db.Integer, nullable=False)
    anxious = db.Column(db.Integer, nullable=False)
    confused = db.Column(db.Integer, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow, nullable=False)

    def __repr__(self):
        return f"<EmoInsights(id={self.id}, happiness={self.happiness}, sadness={self.sadness}, anger={self.anger}, anxiety={self.anxiety}, confusion={self.confusion}, created_at={self.created_at})>"

    def to_dict(self):
        return {
            'happy': self.happy,
            'sad': self.sad,
            'angry': self.angry,
            'anxious': self.anxious,
            'confused': self.confused
        }
