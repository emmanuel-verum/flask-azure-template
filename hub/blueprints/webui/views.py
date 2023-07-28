from flask import abort, render_template, url_for
from hub.models import Projetos


def index():
    products = Projetos.query.all()
    return render_template("index.html", products=products)


def home():
    return render_template("demo.html")


def projetos(project_id):
    product = Projetos.query.filter_by(id=project_id).first() or abort(
        404, "Projeto nao encontrado"
    )
    return render_template("product.html", product=product)

