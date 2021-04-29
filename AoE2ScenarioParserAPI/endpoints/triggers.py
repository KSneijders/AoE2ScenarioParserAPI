from flask import request
from flask_restful import Resource

from AoE2ScenarioParserAPI import glob
from AoE2ScenarioParserAPI.other.helper import get_trigger
from AoE2ScenarioParser.objects.data_objects.trigger import Trigger as TriggerObject

from AoE2ScenarioParserAPI.other.json_converter import trigger_to_dict


class Triggers(Resource):
    def get(self):
        trigger: TriggerObject
        return {'triggers': [trigger_to_dict(trigger) for trigger in glob.scenario.trigger_manager.triggers]}, 200

    def post(self):
        glob.scenario.trigger_manager.add_trigger(**request.form)
        return 200


class Trigger(Resource):
    def get(self, tid):
        try:
            return trigger_to_dict(get_trigger(tid)), 200
        except IndexError:
            return {}, 404

    def put(self, tid):
        for key, value in request.form.items():
            setattr(get_trigger(tid), key, value)
        return 200
