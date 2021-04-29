from flask import request
from flask_restful import Resource

from AoE2ScenarioParserAPI import glob
from AoE2ScenarioParserAPI.other.helper import get_trigger


class Triggers(Resource):
    def get(self):
        return {
                   'triggers': [{
                       'name': trigger.name,
                       'id': trigger.trigger_id
                   } for trigger in glob.scenario.trigger_manager.triggers]
               }, 200

    def post(self):
        glob.scenario.trigger_manager.add_trigger(**request.form)
        return 200


class Trigger(Resource):
    def get(self, tid):
        try:
            return {'name': get_trigger(tid).name}, 200
        except IndexError:
            return {}, 404

    def put(self, tid):
        for key, value in request.form.items():
            setattr(get_trigger(tid), key, value)
        return 200
