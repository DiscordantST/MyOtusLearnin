from flask import Flask


def create_app():
    application = Flask(__name__)
    return application


app = create_app()


@app.route("/")
def index():
    return "Hello!!!"


if __name__ == "__main__":
    app.run()
