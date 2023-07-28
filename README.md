# Integrador de ferramentas AWP


## Ambiente

Python 3.10+
Ative a sua virtualenv

```bash
pip install -r requirements.txt
pip install -r requirements_dev.txt
pip install -r requirements_test.txt
```

## Testando

```bash
pytest template/tests
```

## Executando

```bash
flask create-db  # rodar uma vez
flask populate-db # rodar uma vez
flask add-user -u admin -p 1234  # adiciona usuario admin
flask run
```

Acesse:

- Website: http://localhost:5000
- Admin: http://localhost:5000/admin/
  - user: admin, senha: 1234
- API GET:
  - https://localhost:5000/api/v1/product/
  - https://localhost:5000/api/v1/product/1
  - https://localhost:5000/api/v1/product/2
  - https://localhost:5000/api/v1/product/3


## Structure

```bash
.
├── Makefile
├── template  (MAIN PACKAGE)
│   ├── app.py  (APP FACTORIES)
│   ├── blueprints  (BLUEPRINT FACTORIES)
│   │   ├── __init__.py
│   │   ├── restapi  (REST API)
│   │   │   ├── __init__.py
│   │   │   └── resources.py
│   │   └── webui  (FRONT END)
│   │       ├── __init__.py
│   │       ├── templates
│   │       │   ├── index.html
│   │       │   └── product.html
│   │       └── views.py
│   ├── ext (EXTENSION FACTORIES)
│   │   ├── admin.py
│   │   ├── appearance.py
│   │   ├── auth.py
│   │   ├── commands.py
│   │   ├── configuration.py
│   │   ├── database.py
│   │   └── __init__.py
│   ├── __init__.py
│   ├── models.py  (DATABASE MODELS)
│   └── tests  (TESTS)
│       ├── conftest.py
│       ├── __init__.py
│       └── test_api.py
├── README.md
├── requirements_dev.txt
├── requirements_test.txt
├── requirements.txt
└── settings.toml  (SETTINGS)

7 directories, 26 files
```
