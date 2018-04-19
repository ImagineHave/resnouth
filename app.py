from flask import Flask, request, jsonify
import os
from flask_jwt_extended import JWTManager
from flask_jwt_extended import (create_access_token, create_refresh_token, jwt_required, jwt_refresh_token_required, get_jwt_identity, get_raw_jwt)


app = Flask(__name__)

app.config['JWT_SECRET_KEY'] = os.environ['JWT_SECRET_KEY']

jwt = JWTManager(app)

@app.route('/protectedResouce', methods=['GET'])
@jwt_access_token_required
def getProtectedResource():
    return jsonify({'resouce': 'This is the protected resource'})
