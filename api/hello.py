from flask import Flask
from flask import jsonify

app = Flask(__name__)


@app.route("/api/users")
def users():
    return jsonify(
        [
            {"id": 1, "name": "Bret", "email": "Sincere@april.biz"},
            {"id": 2, "name": "Antonette", "email": "Shanna@melissa.tv"},
        ]
    )


if __name__ == "__main__":
    app.run(host="0.0.0.0")
