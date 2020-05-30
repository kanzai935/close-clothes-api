import os

from app import create_app

app = create_app(os.environ['APP_ENV'])
app.secret_key = os.environ['APP_KEY']

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=bool(os.environ['DEBUG']))
