from flask_restful import Resource, reqparse
from models.score import ScoreModel
from flask_jwt import jwt_required


class Score(Resource):
    def get(self, type_risk):
        score = ScoreModel.find_by_name(type_risk)
        if score:
            return score.json()
        return {'message': 'Score not found'}, 404

    @jwt_required()
    def post(self, type_risk):
        if ScoreModel.find_by_name(type_risk):
            return {
                'message': "A score with type_risk '{}' \
                    already exists.".format(type_risk)}, 400

        score = ScoreModel(type_risk)
        try:
            score.save_to_db()
        except:
            return {"message": "An error occurred creating the score."}, 500

        return score.json(), 201

    @jwt_required()
    def delete(self, type_risk):
        score = ScoreModel.find_by_name(type_risk)
        if score:
            score.delete_from_db()

        return {'message': 'Score deleted'}


class ScoreList(Resource):
    @jwt_required()
    def get(self):
        return {
            'scores': list(map(lambda x: x.json(), ScoreModel.query.all()))}
