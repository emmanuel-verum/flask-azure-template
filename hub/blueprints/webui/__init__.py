from flask import Blueprint

from .views import index, projetos, home
from .views import home

bp = Blueprint(
    "webui", 
    __name__, 
    template_folder='templates'
)

bp.add_url_rule("/", view_func=home)

bp.add_url_rule(
    "/projeto/<project_id>", view_func=projetos, endpoint="projectview"
)


def init_app(app):
    app.register_blueprint(bp)
