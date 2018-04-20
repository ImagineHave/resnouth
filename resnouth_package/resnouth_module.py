from flask import Flask, request, jsonify
import os
from flask_jwt_extended import JWTManager
from flask_jwt_extended import (jwt_required)

resnouth_instance = Flask(__name__)

resnouth_instance.config['JWT_SECRET_KEY'] = os.environ['JWT_SECRET_KEY']

jwt = JWTManager(resnouth_instance)

@resnouth_instance.route('/protectedResouce', methods=['GET'])
@jwt_required
def getProtectedResource():
    return jsonify({'resouce': 'This is the protected resource'})
