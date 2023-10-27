"""Practice with creating a new dictionary."""
ice_cream: dict[str, int] = {"chocalte": 12, "vanilla": 8, "strawberry": 5}

ice_cream["mint"] = 3

ice_cream.pop("mint")

ice_cream["vanilla"] = 10

print(ice_cream)



for i in ice_cream:
    print(i + "\n" + str(ice_cream[i]))
