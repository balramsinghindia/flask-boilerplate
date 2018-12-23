#!/usr/bin/python
# -*- coding: utf-8 -*-

from api.utils.database import db
from marshmallow_sqlalchemy import ModelSchema
from marshmallow import fields


class CurrentUser(db.Model):
    __tablename__ = 'current_user'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    EMAIL = db.Column(db.String)
    FILE_ID = db.Column(db.String)
    Name = db.Column(db.String)
    scope = db.Column(db.String)


    def __init__(self, EMAIL, FILE_ID, Name, scope):
        self.EMAIL = EMAIL
        self.FILE_ID = FILE_ID
        self.Name = Name
        self.scope = scope

    def create(self):
        db.session.add(self)
        db.session.commit()
        return self


class CurrentUserSchema(ModelSchema):
    class Meta(ModelSchema.Meta):
        model = CurrentUser
        sqla_session = db.session

    id = fields.Number(dump_only=True)
    EMAIL = fields.String(required=True)
    FILE_ID = fields.String(required=True)
    Name = fields.String(required=True)
    scope = fields.String(required=True)

