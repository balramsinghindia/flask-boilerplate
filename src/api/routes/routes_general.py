#!/usr/bin/python
# -*- coding: utf-8 -*-

from flask import Blueprint
from flask import request
from api.utils.responses import response_with
from api.utils import responses as resp
from api.models.model_scenarios import Scenario, ScenarioSchema
from api.models.model_config import Config, ConfigSchema
from api.models.model_current_user import CurrentUser, CurrentUserSchema

route_path_general = Blueprint("route_path_general", __name__)


#
# # Generic method to get API response from DB
# def get_api_response(route, type, schema, model, modelSchema, requestParameter = None):
#     if(requestParameter):
#         @route_path_general.route(route+'/'+requestParameter, methods=[type])
#         def get_response_details():
#             fetched = model.query.filter_by(id=requestParameter).first()
#             model_schema = modelSchema()
#             models, error = model_schema.dump(fetched)
#             return response_with(resp.SUCCESS_200, value={"model": models})
#     else:
#         @route_path_general.route(route, methods=[type])
#         def get_response_list():
#             fetched = model.query.all()
#             model_schema = modelSchema(many=True, only=schema)
#             models, error = model_schema.dump(fetched)
#             return response_with(resp.SUCCESS_200, value={"model": models})
#
#
# #Scenario API
# schema = ['NAME', 'DESCRIPTION', 'LAST_UPDATED_DATE', 'LAST_UPDATED_BY', 'PROJECT', 'TYPE', 'STATUS', 'APPROVED', 'APPROVED_DATE', 'APPROVER', 'CONDITIONS', 'LAST_UPDATED_BY_NAME']
# get_api_response('/v1.0/scenarios', 'GET', schema, Scenario, ScenarioSchema)
#
# # Config API
# get_api_response('/v1.0/config', 'GET', None, Config, ConfigSchema, '1')
#
# # Current User
# # get_api_response('/v1.0/current-user', 'GET', None, CurrentUser, CurrentUserSchema, '1')
#






# Scenarios
@route_path_general.route('/v1.0/scenarios', methods=['GET'])
def get_scenario_list():
    fetched = Scenario.query.all()
    scenario_schema = ScenarioSchema(many=True, only=['NAME', 'DESCRIPTION', 'LAST_UPDATED_DATE', 'LAST_UPDATED_BY', 'PROJECT', 'TYPE', 'STATUS', 'APPROVED', 'APPROVED_DATE', 'APPROVER', 'CONDITIONS', 'LAST_UPDATED_BY_NAME'])
    scenarios, error = scenario_schema.dump(fetched)
    return response_with(resp.SUCCESS_200, value={"scenarios": scenarios})


# Config
@route_path_general.route('/v1.0/config/<int:config_id>', methods=['GET'])
def get_config_detail(config_id):
    fetched = Config.query.filter_by(id=config_id).first()
    config_schema = ConfigSchema()
    config, error = config_schema.dump(fetched)
    return response_with(resp.SUCCESS_200, value={"config": config})

# Current User
@route_path_general.route('/v1.0/current-user/<int:current_user_id>', methods=['GET'])
def get_current_user_detail(current_user_id):
    fetched = CurrentUser.query.filter_by(id=current_user_id).first()
    current_user_schema = CurrentUserSchema()
    current_user, error = current_user_schema.dump(fetched)
    return response_with(resp.SUCCESS_200, value={"current_user": current_user})


#
# def my_model(route):
#     if route in '/v1.0/scenarios':
#         @route_path_general.route('/v1.0/scenarios', methods=['GET'])
#         def get_scenario_list():
#             fetched = Scenario.query.all()
#             scenario_schema = ScenarioSchema(many=True, only=['NAME', 'DESCRIPTION', 'LAST_UPDATED_DATE', 'LAST_UPDATED_BY', 'PROJECT', 'TYPE', 'STATUS', 'APPROVED', 'APPROVED_DATE', 'APPROVER', 'CONDITIONS', 'LAST_UPDATED_BY_NAME'])
#             scenarios, error = scenario_schema.dump(fetched)
#             return response_with(resp.SUCCESS_200, value={"scenarios": scenarios})
#     elif route in '/v1.0/config':
#         @route_path_general.route('/v1.0/config', methods=['GET'])
#         def get_config_detail(config_id):
#             fetched = Config.query.filter_by(id=config_id).first()
#             config_schema = ConfigSchema()
#             config, error = config_schema.dump(fetched)
#             return response_with(resp.SUCCESS_200, value={"config": config})
#
#     elif route in '/v1.0/current-user':
#         @route_path_general.route('/v1.0/current-user', methods=['GET'])
#         def get_current_user_detail(current_user_id):
#             fetched = CurrentUser.query.filter_by(id=current_user_id).first()
#             current_user_schema = CurrentUserSchema()
#             current_user, error = current_user_schema.dump(fetched)
#             return response_with(resp.SUCCESS_200, value={"current_user": current_user})
#     else:
#         # Do the default
#
# my_model('/v1.0/scenarios')