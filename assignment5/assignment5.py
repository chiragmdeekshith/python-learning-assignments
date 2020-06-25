from flask import Flask, jsonify, request
from flask_cors import CORS, cross_origin

application = Flask("User Profile")
cors = CORS(application)
application.config['CORS_HEADERS'] = 'Content-Type'

users = []


@application.route("/")
@cross_origin()
def server_status():
    response = {
        "status": "Alive",
        "users": users
    }
    return jsonify(response)


@application.route("/register", methods=['POST'])
@cross_origin()
def register():
    new_user = request.get_json()
    print(new_user)
    users.append(new_user)
    response = {
        "message": "Created"
    }
    return jsonify(response)


@application.route("/login", methods=['POST'])
@cross_origin()
def login():
    credentials = request.get_json()

    user_found = False
    for user in users:
        if user["email"] == credentials["email"] and user["password"] == credentials["password"]:
            user_found = user
            break

    response = {
        "user": user_found
    }
    return jsonify(response)


@application.route("/update", methods=['PUT'])
@cross_origin()
def update():
    updated_user = request.get_json()

    for user in users:
        if user["email"] == updated_user["email"]:
            user["name"] = updated_user["name"]
            user["password"] = updated_user["password"]

    response = {
        "message": "Updated"
    }
    return jsonify(response)


application.debug = True
application.run(host="127.0.0.1", port=9753, debug=True)
