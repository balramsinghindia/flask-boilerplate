#!/usr/bin/python
# -*- coding: utf-8 -*-

from api.utils.database import db
from marshmallow_sqlalchemy import ModelSchema
from marshmallow import fields


class Config(db.Model):
    __tablename__ = 'config'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    FEATURE_DISABLE_PRICING = db.Column(db.String)


    def __init__(self, FEATURE_DISABLE_PRICING):
        self.FEATURE_DISABLE_PRICING = FEATURE_DISABLE_PRICING

    def create(self):
        db.session.add(self)
        db.session.commit()
        return self


class ConfigSchema(ModelSchema):
    class Meta(ModelSchema.Meta):
        model = Config
        sqla_session = db.session

    id = fields.Number(dump_only=True)
    FEATURE_DISABLE_PRICING = fields.Boolean(required=True)

