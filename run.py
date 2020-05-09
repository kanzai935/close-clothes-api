import os

from app import create_app

app = create_app(os.environ['APP_ENV'])
app.secret_key = 'sfjejj!djl04939rj#'

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
