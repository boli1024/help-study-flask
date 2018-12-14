from flask import Flask
# from flask_bootstrap import Bootstrap, WebCDN, ConditionalCDN, BOOTSTRAP_VERSION, JQUERY_VERSION, HTML5SHIV_VERSION, RESPONDJS_VERSION
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from config import config


bootstrap = Bootstrap()
db = SQLAlchemy()

login_manager = LoginManager()
login_manager.session_protection = 'strong'
login_manager.login_view = 'auth.login'


def create_app(config_name):
    app = Flask(__name__)

    app.config.from_object(config[config_name])
    config[config_name].init_app(app)

    from .routes.project import main as route_project
    from .routes.film import main as route_film
    from .routes.video import main as route_video
    from .auth import auth as route_auth
    from .routes.test import test as route_test
    from .routes.manage_student import main as route_manage_student
    from .routes.manage_direction import main as route_manage_direction
    from .routes.student import main as route_student
    app.register_blueprint(route_student, url_prefix='/student')
    app.register_blueprint(route_manage_student, url_prefix='/studentManage')
    app.register_blueprint(route_manage_direction, url_prefix='/directionManage')
    app.register_blueprint(route_project, url_prefix='')
    app.register_blueprint(route_film, url_prefix='/film')
    app.register_blueprint(route_video, url_prefix='/video')
    app.register_blueprint(route_auth, url_prefix='/auth')
    app.register_blueprint(route_test, url_prefix='/test')

    bootstrap.init_app(app)
    # change_cdn_domestic(app)
    db.init_app(app)
    login_manager.init_app(app)

    return app


def change_cdn_domestic(tar_app):
    static = tar_app.extensions['bootstrap']['cdns']['static']
    local = tar_app.extensions['bootstrap']['cdns']['local']

    # def change_one(tar_lib, tar_ver, fallback):
    #     tar_js = ConditionalCDN('BOOTSTRAP_SERVE_LOCAL', fallback, WebCDN('//cdn.bootcss.com/' + tar_lib + '/' + tar_ver + '/'))
    #     tar_app.extensions['bootstrap']['cdns'][tar_lib] = tar_js
    #
    # libs = {'jquery': {'ver': JQUERY_VERSION, 'fallback': local},
    #         'bootstrap': {'ver': BOOTSTRAP_VERSION, 'fallback': local},
    #         'html5shiv': {'ver': HTML5SHIV_VERSION, 'fallback': static},
    #         'respond.js': {'ver': RESPONDJS_VERSION, 'fallback': static}}
    # for lib, par in libs.items():
    #     change_one(lib, par['ver'], par['fallback'])
