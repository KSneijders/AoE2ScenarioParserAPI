from AoE2ScenarioParser.objects.data_objects.condition import Condition
from AoE2ScenarioParser.objects.data_objects.effect import Effect
from AoE2ScenarioParser.objects.data_objects.trigger import Trigger


def transform(obj, keys, mode="normal"):
    def set_entry(attr_from, attr_to):
        if mode == "normal":
            result[attr_to] = getattr(obj, attr_from)
        elif mode == "bool":
            result[attr_to] = getattr(obj, attr_from) == 1

    result = {}
    if type(keys) is list:
        for attr in keys:
            set_entry(attr, attr)
    elif type(keys) is dict:
        for before, after in keys.items():
            set_entry(before, after)

    return result


def trigger_to_dict(trigger: Trigger):
    exact = [
        'name', 'description', 'description_stid', 'short_description', 'short_description_stid', 'description_order'
    ]
    to_bool = ['enabled', 'looping', 'display_as_objective', 'display_on_screen', 'header', 'mute_objectives']
    convert = {
        'trigger_id': 'id'
    }

    effects = [effect_to_dict(e) for e in trigger.effects]
    conditions = [condition_to_dict(c) for c in trigger.conditions]

    return {
        **transform(trigger, exact),
        **transform(trigger, to_bool, 'bool'),
        **transform(trigger, convert),
        'conditions': conditions,
        'condition_order': trigger.condition_order,
        'effects': effects,
        'effect_order': trigger.effect_order,
    }


def effect_to_dict(effect: Effect):
    exact = [
        "effect_type", "ai_script_goal", "armour_attack_quantity", "armour_attack_class", "quantity", "tribute_list",
        "diplomacy", "object_list_unit_id", "source_player", "target_player", "technology", "string_id", "display_time",
        "trigger_id", "location_x", "location_y", "location_object_reference", "area_x1", "area_y1", "area_x2",
        "area_y2", "object_group", "object_type", "instruction_panel_position", "attack_stance", "time_unit",
        "enabled", "food", "wood", "stone", "gold", "item_id", "flash_object", "force_research_technology",
        "visibility_state", "scroll", "operation", "object_list_unit_id_2", "button_location", "ai_signal_value",
        "object_attributes", "variable", "timer", "facet", "play_sound", "player_color", "color_mood", "message",
        "sound_name", "selected_object_ids"
    ]
    to_bool = []
    convert = {}

    return {
        **transform(effect, exact),
        **transform(effect, to_bool, 'bool'),
        **transform(effect, convert),
    }


def condition_to_dict(condition: Condition):
    exact = [
        "condition_type", "quantity", "attribute", "unit_object", "next_object", "object_list", "source_player",
        "technology", "timer", "area_x1", "area_y1", "area_x2", "area_y2", "object_group", "object_type", "ai_signal",
        "inverted", "variable", "comparison", "target_player", "unit_ai_action", "xs_function",
    ]
    to_bool = []
    convert = {}

    return {
        **transform(condition, exact),
        **transform(condition, to_bool, 'bool'),
        **transform(condition, convert),
    }
