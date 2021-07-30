# AoE2ScenarioParserAPI

This project is a helper project for [AoE2ScenarioParserGUI]. 

This module reads an `aoe2scenario` file and sets up a Flask API which can be used to query information about the scenario.


## How it works

When calling this module from the command line, it requires an argument: (`-f` or `--file`).
This can be a relative or absolute path to any given `aoe2scenario` file.

The project [AoE2ScenarioParserGUI] uses this project internally. So downloading this is not necessary.

[---- LINKS ----]: ()

[AoE2ScenarioParserGUI]: (https://github.com/KSneijders/AoE2ScenarioParserGUI)