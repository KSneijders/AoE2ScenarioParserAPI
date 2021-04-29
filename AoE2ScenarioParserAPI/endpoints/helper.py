from AoE2ScenarioParser.objects.support.trigger_select import TS

from AoE2ScenarioParserAPI import glob


def get_trigger(tid):
    return glob.scenario.trigger_manager.get_trigger(TS.index(tid))
