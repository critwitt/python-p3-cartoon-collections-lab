def roll_call_dwarves(dwarves):
    for dwarf in dwarves:
        print(f'{dwarves.index(dwarf) + 1}. {dwarf}')

def summon_captain_planet(planateers):
    return [f'{planateer.title()}!' for planateer in planateers]

def long_planeteer_calls(words):
    for word in words:
        if len(word) > 4:
            return True
    return False

def find_the_cheese(snacks):
    for cheese in snacks:
        if cheese == "cheddar" or cheese == "gouda" or cheese == "camembert":
            return cheese
    return None
