from flask import Flask, jsonify
#from dotenv import load_dotenv
from database import get_drivers
from flask import Flask, render_template


#load_dotenv()

app = Flask(__name__)


@app.route("/")
def home():
   vehicles = get_drivers()
   return render_template('map.html', vehicles=vehicles)

app.static_folder = 'static'

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
