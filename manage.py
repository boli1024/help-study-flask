import os
from app import create_app, db
from app.models import User, Progress, Direction, Course
from flask_script import Manager, Shell
from flask_migrate import Migrate, MigrateCommand
from lib.insert import insert


app = create_app(os.getenv('FLASK_CONFIG') or 'default')

manager = Manager(app)
migrate = Migrate(app, db)


def make_shell_context():
    return dict(app=app, db=db, User=User, Progress=Progress, Direction=Direction, Course=Course)


manager.add_command("shell", Shell(make_context=make_shell_context))  # 此处 make_shell_context 后不用加括号
manager.add_command('db', MigrateCommand)


@manager.command
def insert_data():
    insert()


if __name__ == '__main__':
    manager.run()
