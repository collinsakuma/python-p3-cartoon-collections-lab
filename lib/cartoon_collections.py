def roll_call_dwarves(dwarves):
    for dwarf in dwarves:
        print(f"{dwarves.index(dwarf) + 1}. {dwarf}")

def summon_captain_planet(planeteers):
    return [planeteer.title() + "!" for planeteer in planeteers]

def long_planeteer_calls(words):
    for word in words:
        if (len(word) > 4):
            return True
    else:
        return False

def find_the_cheese(snacks):
    # for snack in snacks:
    #     if (snack == "cheddar"):
    #         return snack
    #     elif (snack == "gouda"):
    #         return snack
    #     elif (snack == "camembert"):
    #         return snack
    # else:
    #     None
    lst = ["cheddar", "gouda", "camembert"]
    for snack in snacks:
        if snack in lst: 
            return snack
    else:
        return None
