from flask import Blueprint, current_app, jsonify, request, url_for
from flask_cors import cross_origin
from .models import Vehicle, Response, Meta, Links

utils_app = Blueprint('utils', __name__)

@utils_app.route(current_app.config['HEALTH_API'], methods=['GET'])
@cross_origin()
def health():
    #request_args = request.args
    #checking_kargs(**request_args)
    return "OK\n", 200

def checking_kargs(**kwargs):
    test = kwargs.pop('blabla', '')
    print(f'{test} asc')
    for i,j in kwargs.items():
        print(i,'is ',j)
