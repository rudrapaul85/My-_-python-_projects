inventory =["steel sword", "shadow dagger", "steel axe", "shadow bow"]
for weapon in inventory :
    if "shadow"   in weapon:
        print("found a legendary item",weapon)
        
    elif "steel" in weapon :
        print("and basic weapon :",weapon)