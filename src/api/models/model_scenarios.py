#!/usr/bin/python
# -*- coding: utf-8 -*-

from api.utils.database import db
from marshmallow_sqlalchemy import ModelSchema
from marshmallow import fields


class Scenario(db.Model):
    __tablename__ = 'scenarios'

    ID = db.Column(db.Integer, primary_key=True, autoincrement=True)
    NAME = db.Column(db.String)
    DESCRIPTION = db.Column(db.String)
    LAST_UPDATED_DATE = db.Column(db.String)
    LAST_UPDATED_BY = db.Column(db.String)
    PROJECT = db.Column(db.String)
    TYPE = db.Column(db.String)
    STATUS = db.Column(db.String)
    APPROVED = db.Column(db.String)
    APPROVED_DATE = db.Column(db.String)
    APPROVER = db.Column(db.String)
    CONDITIONS = db.Column(db.String)
    LAST_UPDATED_BY_NAME = db.Column(db.String)



    def __init__(self, NAME, DESCRIPTION, LAST_UPDATED_DATE, LAST_UPDATED_BY, PROJECT, TYPE, STATUS, APPROVED, APPROVED_DATE, APPROVER, CONDITIONS, LAST_UPDATED_BY_NAME):
        self.NAME = NAME
        self.DESCRIPTION = DESCRIPTION
        self.LAST_UPDATED_DATE = LAST_UPDATED_DATE
        self.LAST_UPDATED_BY = LAST_UPDATED_BY
        self.PROJECT = PROJECT
        self.TYPE = TYPE
        self.STATUS = STATUS
        self.APPROVED = APPROVED
        self.APPROVED_DATE = APPROVED_DATE
        self.APPROVER = APPROVER
        self.CONDITIONS = CONDITIONS
        self.LAST_UPDATED_BY_NAME = LAST_UPDATED_BY_NAME


    def create(self):
        db.session.add(self)
        db.session.commit()
        return self


class ScenarioSchema(ModelSchema):
    # class Meta(ModelSchema.Meta):
    #     model = Scenario
    #     sqla_session = db.session

    ID = fields.Number(dump_only=True)
    NAME = fields.String(required=True)
    DESCRIPTION = fields.String(required=True)
    LAST_UPDATED_DATE = fields.String(dump_only=True)
    LAST_UPDATED_BY = fields.String(dump_only=True)
    PROJECT = fields.String(dump_only=True)
    TYPE = fields.String(dump_only=True)
    STATUS = fields.String(dump_only=True)
    APPROVED = fields.String(dump_only=True)
    APPROVED_DATE = fields.String(dump_only=True)
    CONDITIONS = fields.String(dump_only=True)
    LAST_UPDATED_BY_NAME = fields.String(dump_only=True)
