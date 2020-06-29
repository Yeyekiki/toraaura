import os

from main import app

if __name__ == "__main__":
    app.secret_key = os.getenv("FLASK_SECRET_KEY")
    app.run(debug=True,host='0.0.0.0', port=4000)