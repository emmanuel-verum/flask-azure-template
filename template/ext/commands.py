import click
from template.ext.database import db
from template.ext.auth import create_user
from template.models import Product


def create_db():
    """Creates database"""
    db.create_all()


def drop_db():
    """Cleans database"""
    db.drop_all()


def populate_db():
    """Populate db with sample data"""
    data = [
        Product(id=1, name="Product 1", price="10", description="Descrption 1"),
        Product(id=2, name="Product 2", price="15", description="Descrption 1"),
        Product(id=3, name="Product 3", price="20", description="Descrption 1"),
    ]
    db.session.bulk_save_objects(data)
    db.session.commit()
    return Product.query.all()


def init_app(app):
    # add multiple commands in a bulk
    for command in [create_db, drop_db, populate_db]:
        app.cli.add_command(app.cli.command()(command))

    # add a single command
    @app.cli.command()
    @click.option('--username', '-u')
    @click.option('--password', '-p')
    def add_user(username, password):
        return create_user(username, password)