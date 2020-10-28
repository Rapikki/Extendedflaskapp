from setuptools import setup

# Metadata goes in setup.cfg. These are here for GitHub's dependency graph.
requires = (
    "flask>=1.1.1"
    "flask_sqlalchemy>=2.4.1",
    "Jinja2>=2.10.1",
    "flask_script>=2.0.1",
    "flask_migrate>=2.5.1",
    "boto3>=1.15.1",
    "psycopg2"
)

setup(
    name = "Flask_app",
    version = "0.0.1",
    author = "Daria Oliinik",
    description = ("useless"),
    keywords = "application with Flask and PostgreSQL",
    install_requires=requires,
    #long_description=read('README.md'),
)
