from db import db


class ScoreModel(db.Model):
    __tablename__ = 'scores'

    id = db.Column(db.Integer, primary_key=True)
    type_risk = db.Column(db.String(80))

    customers = db.relationship('CustomerModel', lazy='dynamic')

    def __init__(self, type_risk):
        self.type_risk = type_risk

    def json(self):
        return {
            'type_risk': self.type_risk,
            'customers': [
                customer.json() for customer in self.customers.all()]}

    @classmethod
    def find_by_name(cls, type_risk):
        return cls.query.filter_by(type_risk=type_risk).first()

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()
