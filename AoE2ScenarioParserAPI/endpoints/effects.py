from flask_restful import Resource

from AoE2ScenarioParserAPI.other.helper import get_trigger


class Effects(Resource):
    def get(self, tid):
        try:
            effects = get_trigger(tid).effects
            return {
                       'effects': [[index, EffectId(effect.effect_type).name] for index, effect in enumerate(effects)]
                   }, 200
        except IndexError:
            return {}, 404


class Effect(Resource):
    def get(self, tid, eid):
        try:
            effect = get_trigger(tid).get_effect(eid)
            return {'effect_type': EffectId(effect.effect_type).name}, 200
        except IndexError:
            return {}, 404
