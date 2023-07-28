import click
from hub.ext.database import db
from hub.ext.auth import create_user
from hub.models import Projetos


def create_db():
    """Creates database"""
    db.create_all()


def drop_db():
    """Cleans database"""
    db.drop_all()


def populate_db():
    """Populate db with sample data"""
    data = [
        Projetos(id=1, nome="Onça Puma", ativo=True, descricao="Descrption 1"),
        Projetos(id=2, nome="SudestCraft", ativo=True, descricao="Descrption 2"),
        Projetos(id=3, nome="Projeto Teste", ativo=False, descricao="Descrption 3"),
    ]
    db.session.bulk_save_objects(data)
    db.session.commit()
    return Projetos.query.all()


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