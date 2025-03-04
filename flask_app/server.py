import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from flask_app import app


from flask_app import app
from flask_app.controllers import controller_user, controller_listing, controller_message

if __name__ == "__main__":
    app.run(debug=True)