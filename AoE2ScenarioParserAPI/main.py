import time
from argparse import ArgumentParser

from AoE2ScenarioParser.scenarios.aoe2_de_scenario import AoE2DEScenario
from flask import Flask
from flask_restful import Api

from AoE2ScenarioParserAPI import glob
from AoE2ScenarioParserAPI.endpoints.effects import Effects, Effect
from AoE2ScenarioParserAPI.endpoints.triggers import Triggers, Trigger

parser = ArgumentParser()
parser.add_argument("-f", "--file", dest="filename", help="The aoe2scenario file to read", metavar="FILE")
args = parser.parse_args()

filename = args.filename

glob.scenario = AoE2DEScenario.from_file(filename)

print("\nStarting API...")
time.sleep(.5)

app = Flask(__name__)
api = Api(app)

api.add_resource(Triggers, '/triggers/')
api.add_resource(Trigger, '/triggers/<int:tid>')
api.add_resource(Effects, '/triggers/<int:tid>/effects/')
api.add_resource(Effect, '/triggers/<int:tid>/effects/<int:eid>')

if __name__ == '__main__':
    app.run()
