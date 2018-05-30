from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager, Server
from app import app

# Enable flask-manager
manager = Manager(app)
manager.add_command("threaded", Server(threaded=True))
    
if __name__ == "__main__":
    manager.run()