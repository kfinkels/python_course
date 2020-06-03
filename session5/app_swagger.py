import connexion
import logging

from swagger.pets_database import init_db, db_session

logging.basicConfig(level=logging.INFO)
app = connexion.App(__name__)
app.add_api('swagger.yaml')
application = app.app


if __name__ == '__main__':
    init_db()
    app.run(port=8080)


@app.teardown_appcontext
def shutdown_session(exception=None):
    db_session.remove()
