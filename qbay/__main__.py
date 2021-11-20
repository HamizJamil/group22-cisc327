from qbay.__init__ import app
from qbay.models import *
from qbay.controllers import *


FLASK_PORT = 8081

if __name__ == "__main__":
    db.create_all()
    # app.run(debug=True, port=FLASK_PORT)
    app.run(debug=True, port=FLASK_PORT, host='0.0.0.0')