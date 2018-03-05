from flask_restful import Resource, reqparse
from flask_jwt import jwt_required
from flasgger import swag_from
from models.customer import CustomerModel


class Customer(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument(
        'debtor_value',
        type=float,
        required=True,
        help="This field cannot be left blank!"
    )
    parser.add_argument(
        'score_id',
        type=int,
        required=True,
        help="Every customer needs a score_id."
    )
    parser.add_argument(
        'name',
        type=str,
        required=True,
        help="Every customer needs a name."
    )
    parser.add_argument(
        'customer_defaulter',
        type=bool,
        required=True,
        help="Every customer needs a customer_defaulter."
    )

    @swag_from("../docs/customers/customers_get.yml")
    def get(self, tax_id):
        customer = CustomerModel.find_by_taxid(tax_id)
        if customer:
            return customer.json()
        return {'message': 'Customer not found'}, 404

    @jwt_required()
    @swag_from("../docs/customers/customers_post.yml")
    def post(self, tax_id):
        if CustomerModel.find_by_taxid(tax_id):
            return {
                'message':
                "An customer with cpf '{}' already exists.".format(
                    tax_id)}, 400

        data = Customer.parser.parse_args()

        customer = CustomerModel(
            tax_id,
            data['debtor_value'],
            data['score_id'], data['name'], data['customer_defaulter'])

        try:
            customer.save_to_db()
        except:
            return {
                "message": "An error occurred inserting the customer."}, 500

        return customer.json(), 201

    @jwt_required()
    @swag_from("../docs/customers/customers_delete.yml")
    def delete(self, tax_id):
        customer = CustomerModel.find_by_taxid(tax_id)
        if customer:
            customer.delete_from_db()

        return {'message': 'Customer deleted'}

    @jwt_required()
    @swag_from("../docs/customers/customers_put.yml")
    def put(self, tax_id):
        data = Customer.parser.parse_args()

        customer = CustomerModel.find_by_taxid(tax_id)

        if customer:
            customer.debtor_value = data['debtor_value']
            customer.customer_defaulter = data['customer_defaulter']
        else:
            customer = CustomerModel(tax_id, data['debtor_value'])

        customer.save_to_db()

        return customer.json()


class CustomerList(Resource):
    @jwt_required()
    def get(self):
        return {
            'customers':
            list(map(lambda x: x.json(), CustomerModel.query.all()))}
