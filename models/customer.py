from db import db


class CustomerModel(db.Model):
    __tablename__ = 'customers'

    id = db.Column(db.Integer, primary_key=True)
    tax_id = db.Column(db.String(80))
    name = db.Column(db.String(80))
    debtor_value = db.Column(db.Float(precision=2))
    customer_defaulter = db.Column(db.Boolean, default=True)

    score_id = db.Column(db.Integer, db.ForeignKey('scores.id'))
    score = db.relationship('ScoreModel')

    def __init__(
            self, tax_id, debtor_value, score_id, name, customer_defaulter):
        self.name = name
        self.tax_id = tax_id
        self.debtor_value = debtor_value
        self.score_id = score_id
        self.customer_defaulter = customer_defaulter

    def json(self):
        return {
            'name': self.name,
            'debtor_value': self.debtor_value,
            'tax_id': self.tax_id,
            'customer_defaulter': self.customer_defaulter
        }

    @classmethod
    def find_by_taxid(cls, tax_id):
        return cls.query.filter_by(tax_id=tax_id).first()

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()
