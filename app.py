import os
from flask import Flask, jsonify
from flask_cors import CORS
# from handler import main_handler
from errors import errorsBp

app = Flask(__name__)
CORS(app)

# app.register_blueprint(main_handler)
app.register_blueprint(errorsBp)

@app.route('/', methods=['GET'])
def get_server():
    return jsonify({
        "status" : {
            "code" : 200,
            "message" : "Welcome to the Back-End server of Day Trips Optimization!"
        },
        "data" : None
    }), 200

if __name__ == '__main__':
    app.run(debug=True,
            host="0.0.0.0",
            port=int(os.environ.get("PORT", 5000)))