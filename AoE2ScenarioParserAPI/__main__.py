import time
from argparse import ArgumentParser

from AoE2ScenarioParser import settings
from AoE2ScenarioParser.datasets.players import PlayerId
from AoE2ScenarioParser.datasets.trigger_lists import ColorMood
from AoE2ScenarioParser.scenarios.aoe2_de_scenario import AoE2DEScenario
from AoE2ScenarioParser.datasets.effects import attributes as effect_attributes, effect_names
from AoE2ScenarioParser.datasets.conditions import attributes as condition_attributes, condition_names
from flask import Flask, request
from flask_restful import Api

from AoE2ScenarioParserAPI import glob
from AoE2ScenarioParserAPI.other.json_converter import trigger_to_dict

settings.PRINT_STATUS_UPDATES = False

parser = ArgumentParser()
parser.add_argument("-f", "--file", dest="filename", help="The aoe2scenario file to read", metavar="FILE")
args = parser.parse_args()


filename = ""
if __name__ == '__main__':
    filename = "C:/Users/Kerwin Sneijders/Games/Age of Empires 2 " \
               "DE/76561198140740017/resources/_common/scenario/test1212.aoe2scenario "
filename = args.filename or filename

glob.scenario = AoE2DEScenario.from_file(filename)
glob.scenario.trigger_manager.add_trigger("NEW TIRGGER").new_effect.display_instructions(
    message="Awesome messgaeeee :)",
)
glob.scenario.trigger_manager.add_trigger("TEST").new_effect.change_color_mood(color_mood=ColorMood.AUTUMN)
glob.scenario.trigger_manager.triggers[-1].new_condition.objects_in_area(quantity=4, source_player=PlayerId.ONE)

app = Flask(__name__)
api = Api(app)


# Todo rename endpoint
@app.route('/file')
def get_file():
    triggers = [trigger_to_dict(trigger) for trigger in glob.scenario.trigger_manager.triggers]
    trigger_display_order = glob.scenario.trigger_manager.trigger_display_order

    return {
               'triggerInformation': {
                   'triggers': triggers,
                   'triggerDisplayOrder': trigger_display_order
               }
           }, 200


# Todo: Combine these to general info
@app.route('/effect/attributes')
def get_effect_attributes():
    return effect_attributes


@app.route('/condition/attributes')
def get_condition_attributes():
    return condition_attributes


@app.route('/effect/names')
def get_effect_names():
    return dict(effect_names)


@app.route('/condition/names')
def get_condition_names():
    return dict(condition_names)


# Todo rename endpoint
@app.route('/login', methods=['POST'])
def write_file():
    print(request.data)
    print(request.form)
    print(request.get_data())
    return {}, 200


if __name__ == '__main__':
    app.run()
