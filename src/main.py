from flask_restful import Api
from resources import HealthCheck, \
    UserList, User
from models import User as UserModel, db
from flask_migrate import Migrate
from app import create_app
from flask_talisman import Talisman


app = create_app()
migrate = Migrate(app, db)
csp = {
    'default-src': '\'self\''
}

# API
talisman = Talisman(app, content_security_policy=csp)
api = Api(app)
api.add_resource(HealthCheck, '/healthcheck')
api.add_resource(UserList, '/api/users')
api.add_resource(User, '/api/user/<username>')

# CLI for migrations
@app.shell_context_processor
def make_shell_context():
    return dict(app=app, db=db, User=UserModel)
