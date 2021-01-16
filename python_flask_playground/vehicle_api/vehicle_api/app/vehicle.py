from flask import Blueprint, current_app, jsonify, request, url_for
from flask_cors import cross_origin
from .models import Vehicle, Response, Meta, Links

vehicle_app = Blueprint('vehicle', __name__)

@vehicle_app.route(current_app.config['VEHICLE_API'], methods=['GET'])
@cross_origin()
def vehicle():
    request_args = request.args
    data = []
    links = []
    meta = {}

    vehicles = Vehicle.query_with_filter_sorting_paginating(**request_args)
    if vehicles.items:
        data = vehicles.items
        links = Links(
            self_=url_for('vehicle.vehicle', page=vehicles.page, per_page=vehicles.per_page), 
            first=url_for('vehicle.vehicle', page=1, per_page=vehicles.per_page), 
            last=url_for('vehicle.vehicle', page=vehicles.pages, per_page=vehicles.per_page), 
            previous=url_for('vehicle.vehicle', page=vehicles.prev_num if vehicles.has_prev else 1, per_page=vehicles.per_page), 
            next_=url_for('vehicle.vehicle', page=vehicles.next_num if vehicles.has_next else vehicles.pages, per_page=vehicles.per_page)
            )
        meta = Meta(
            page=vehicles.page, 
            per_page=vehicles.per_page,
            page_count=vehicles.pages,
            total=vehicles.total,
            links=links
            )

    return jsonify(Response(meta=meta, data=data))

