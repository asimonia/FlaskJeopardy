# Set the path
import os
from app import create_app, db
from app.models import Questionbank, Tile, Category, Player, Game
from flask.ext.script import Manager, Server

app = create_app('default')
manager = Manager(app)

# Turn on debugger by default and reloader
manager.add_command("runserver", Server(
    use_debugger=True,
    use_reloader=True,
    host='0.0.0.0')
)

if __name__ == "__main__":
    manager.run()