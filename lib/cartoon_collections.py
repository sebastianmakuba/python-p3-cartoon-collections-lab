def roll_call_dwarves(name):
    for index,item in enumerate(name):
        print(f"{index + 1}. {item}")
    pass
roll_call_dwarves(["Dopey", "Grumpy", "Bashful"])


def summon_captain_planet(planeteer_calls):
    return ([call.capitalize() + "!" for call in planeteer_calls])
summon_captain_planet(["carrot", "cucumber", "pepper"])

def long_planeteer_calls(calls):
    return any(len(call) > 4 for call in calls)
    pass

def find_the_cheese(strings):
    cheese = ["cheddar", "gouda", "camembert"]
    for item in strings:
        if item in cheese:
            return item
    pass
