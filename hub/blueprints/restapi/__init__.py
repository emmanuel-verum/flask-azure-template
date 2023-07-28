from flask import Blueprint
from flask_restful import Api

from .resources import ProjectResource, ProjectItemResource

bp = Blueprint("restapi", __name__, url_prefix="/api/v1")
api = Api(bp)


def init_app(app):
    api.add_resource(ProjectResource, "/projeto/")
    api.add_resource(ProjectItemResource, "/projeto/<project_id>")
    app.register_blueprint(bp)
