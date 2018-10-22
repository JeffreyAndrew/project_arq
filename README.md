https://github.com/abelthf/inkarri-app

$ git clone  https://github.com/abelthf/inkarri-app
$ cd inkarri-app
$  docker-compose  -f docker-compose-dev.yml up -d --build

docker-compose -f docker-compose-dev.yml run users python manage.py recreate_db

para ingresar a la base de datos:

$ docker-compose -f docker-compose-dev.yml exec users-db psql -U postgres
CONFIGURACION DE PRUEBAS

CREAR el directorio “tests” en el directorio “project” y dentro  crear los archivos:
1. __init__.py
2. base.py
3. test_config.py
4. test_users.py


agregar el framework de pruebas: Flask-Testing==0.6.2 al archivo requirements.txt

agregar en el archivo manage.py, con el objetivo de descubrir y ejecutar las pruebas

@cli.command()
def test():
	“””Ejecuta las pruebas sin cobertura de codigo”””
tests = unittest.TestLoader().discover('project/tests', pattern='test*.py')
    result = unittest.TextTestRunner(verbosity=2).run(tests)
    if result.wasSuccessful():
        return 0
    return 1
(vert github)

$ docker-compose -f docker-compose-dev.yml up -d --build
