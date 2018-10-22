import unittest, coverage

from flask.cli import FlaskGroup

from project import create_app, db 
from project.api.models import User 

# configurando informes de covertura con coverage 4.5.1
COV = coverage.coverage(
    branch=True,
    include='project/*',
    omit=[
        'project/tests/*',
        'project/config.py',
    ]
)
COV.start()

app = create_app() 
cli = FlaskGroup(create_app=create_app) 

@cli.command()
def recreate_db():
    db.drop_all()
    db.create_all()
    db.session.commit()
    
@cli.command()
def test():
    """ Ejecuta las pruebas sin cobertura de código """
    tests = unittest.TestLoader().discover('project/tests', pattern='test*.py')
    result = unittest.TextTestRunner(verbosity=2).run(tests)
    if result.wasSuccessful():
        return 0
    return 1

@cli.command()
def seed_db():
    """sembrando la base de datos"""
    db.session.add(User(username='jeffrey', email="jeffreyvargas@upeu.edu.pe"))
    db.session.add(User(username='andrew', email="andrew@gmail.com"))
    db.session.commit()

@cli.command()
def cov():
    """Ejecuta las pruebas unitarias con covertura."""
    tests = unittest.TestLoader().discover('project/tests')
    result = unittest.TextTestRunner(verbosity=2).run(tests)
    if result.wasSuccessful():
        COV.stop()
        COV.save()
        print('Resumen de covertura:')
        COV.report()
        COV.html_report()
        COV.erase()
        return 0
    return 1    

if __name__ == '__main__':
    cli()
