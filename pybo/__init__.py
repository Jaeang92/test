from flask import Flask

# orm +
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import MetaData
# 마크다운 안됨
# from flaskext.markdown import Markdown


# ... rest of your code using Markup

import config


# db = SQLAlchemy()
# migrate = Migrate()

naming_convention = {
    "ix": 'ix_%(column_0_label)s',
    "uq": "uq_%(table_name)s_%(column_0_name)s",
    "ck": "ck_%(table_name)s_%(column_0_name)s",
    "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
    "pk": "pk_%(table_name)s"
}
db = SQLAlchemy(metadata=MetaData(naming_convention=naming_convention))
migrate = Migrate()
# 1 
# app = Flask(__name__)

# @app.route('/')
# def hello_pybo():
#     return 'Hello, Pybo!'

# 2
# def create_app():
#     app = Flask(__name__)

#     @app.route('/')
#     def hello_pybo():
#         return 'Hello, Pybo!!!'

#     return app

# 3 
def create_app():
    app = Flask(__name__)
    # orm +
    # app.config.from_object(config)
    # 변경
    app.config.from_envvar('APP_CONFIG_FILE')
    
    # orm
    db.init_app(app)
    if app.config['SQLALCHEMY_DATABASE_URI'].startswith("sqlite"):
        migrate.init_app(app, db, render_as_batch=True)
    else:
        migrate.init_app(app, db)
    migrate.init_app(app, db)
    from . import models
    
    # blue print
    from .views import main_views, question_views, answer_views, auth_views
    app.register_blueprint(main_views.bp)
    app.register_blueprint(question_views.bp)
    app.register_blueprint(answer_views.bp)
    app.register_blueprint(auth_views.bp)

    # 필터
    from .filter import format_datetime
    app.jinja_env.filters['datetime'] = format_datetime
    
    # #markdown
    # Markdown(app, extensions=['nl2br', 'fenced_code'])
    
    return app