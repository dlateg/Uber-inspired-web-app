from flask import Flask

app = Flask(__name__)

#blueprint idea inspired from chatgpt
from map import app as map_app
app.register_blueprint(map_app)

from bookHandler import app as book_app
app.register_blueprint(book_app)


if __name__ == "__main__":
    from database import create_db_and_tables, create_drivers
    create_db_and_tables()
    create_drivers()

    app.run(host="0.0.0.0", port=5000, debug=True, use_reloader=True, use_debugger=True)