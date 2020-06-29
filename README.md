# The Art Shop

## Description
This is an art website where you can look at art works  and their descriptions and log in in order to donate money.

## Technologies
- Python
- Flask
    - HTML
    - CSS
    - Jinja2 
- SQLite

## Run it yourself
1. Clone this repository
```bash
git clone https://github.com/Yeyekiki/toraaura.git art-shop
cd art-shop
```
2. Create and activate virtual environment
```bash
python3 -m venv venv
source venv/bin/activate
```

3. Install requirements
```bash
pip install -r requirements.txt
```

4. Initialise Database
```bash
python init-db.py
# Hi! Please choose a username: username
# Choose a password: 
# Please repeat your password: 
```

5. Set FLASK_SECRET_KEY environment variable and run flask app
```bash
export FLASK_SECRET_KEY=yoursupersecretkey
python run.py

# Serving Flask app "main" (lazy loading)
#  * Environment: production
#    WARNING: This is a development server. Do not use it in a production deployment.
#    Use a production WSGI server instead.
#  * Debug mode: on
#  * Running on http://0.0.0.0:4000/ (Press CTRL+C to quit)
```