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
    exact = ['name', 'description', 'description_stid', 'short_description', 'short_description_stid',
             'description_order']
    to_bool = ['enabled', 'looping', 'display_as_objective', 'display_on_screen', 'header', 'mute_objectives']
    convert = {
        'trigger_id': 'id'
    }

    # conditions
    # condition_order
    # effects
    # effect_order

    result = {
        **transform(trigger, exact),
        **transform(trigger, to_bool, 'bool'),
        **transform(trigger, convert),
    }
    return result
