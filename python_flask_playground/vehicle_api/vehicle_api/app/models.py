from dataclasses import dataclass, field
from typing import List
from enum import Enum
from sqlalchemy import text
from sqlalchemy.dialects.postgresql import UUID
from flask_sqlalchemy import SQLAlchemy
import uuid

from vehicle_api import db


class StatusEnum(Enum):
    AVAILABLE = "available"
    ON_RENT = "on_rent"
    MAINTENANCE = "maintenance"

@dataclass
class Vehicle(db.Model):
    id: str
    last_mileage_reported: int
    license_plate_number: str
    license_plate_state: str
    make: str
    vehicle_class: str
    status: str
    model: str
    miles_until_service: int

    id = db.Column('id', db.Text(length=36), default=lambda: str(uuid.uuid4()), primary_key=True)
    last_mileage_reported =  db.Column(db.Integer)
    license_plate_number = db.Column(db.String(8), index=True, unique=True)
    license_plate_state = db.Column(db.String(2))
    make = db.Column(db.String(50))
    vehicle_class = db.Column(db.String(50))
    status = db.Column(db.String(12))
    model = db.Column(db.String(50))
    miles_until_service = db.Column(db.Integer)

    def __repr__(self):
        return '<Vehicle {}>'.format(self.license_plate_number)
    
    @classmethod
    def query_with_filter_sorting_paginating(cls, **kwargs):
        # init query
        q = cls.query
        
        # sorting
        sort = kwargs.pop('sort', '')
        if sort == 'miles_until_service':
            sort = f'{sort} asc'
            q = q.order_by(text(sort))
        
        # extracting pagination details
        page = kwargs.pop('page', '1')
        per_page = kwargs.pop('per_page', '20')

        # filtering
        if kwargs:
            allowed = {'make', 'model', 'vehicle_class', 'status', 'license_plate_number', 'license_plate_state'}
            kwargs_copy = kwargs.copy()
            for key in kwargs_copy:
                if key not in allowed:
                    kwargs.pop(key, '')
        if kwargs:
            q = q.filter_by(**kwargs)
        
        # paginating
        q = q.paginate(int(page), int(per_page), error_out=False)
        
        return q

@dataclass
class Links:
    self_: str
    first: str
    last: str
    previous: str = "//"
    next_: str = "//"

@dataclass
class Meta():
    links: Links
    per_page: int
    page_count: int
    total: int
    page: int

@dataclass
class Response():
    meta: Meta = field(default_factory="")
    data: List[Vehicle] = field(default_factory=list)

