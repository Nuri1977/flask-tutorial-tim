import decimal
import json
from datetime import datetime, date

from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_jwt_extended import JWTManager


db = SQLAlchemy()
migrate = Migrate()
jwt = JWTManager()


def setup_custom_json_encoder():
    json_encoder_old = json.JSONEncoder.default

    def json_encoder_custom(self, obj):
        if isinstance(obj, decimal.Decimal):
            return float(obj)
        if isinstance(obj, datetime):
            return datetime.isoformat(obj)
        if isinstance(obj, date):
            return obj.isoformat()
        return json_encoder_old(self, obj)

    json.JSONEncoder.default = json_encoder_custom