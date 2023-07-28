from flask import abort, jsonify
from flask_restful import Resource

from hub.models import Projetos


class ProjectResource(Resource):
    def get(self):
        products = Projetos.query.all() or abort(204)
        return jsonify(
            {"products": [product.to_dict() for product in products]}
        )


class ProjectItemResource(Resource):
    def get(self, project_id):
        product = Projetos.query.filter_by(id=project_id).first() or abort(404)
        return jsonify(product.to_dict())
