from qbay.__init__ import app
from qbay.models import *
from qbay.controllers import *
import os


FLASK_PORT = 8081

if __name__ == "__main__":
    app.run(debug=True, port=FLASK_PORT)