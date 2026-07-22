# Hardcoded values for the season and plant type
season = input("Season: ")  # Prompt the user to enter a season
plant_type = input("Plant type: ") # Prompt the user to enter a plant type

# Variable to hold gardening advice
advice = ""

# Determine advice based on the season
if season == "summer":  # checks if user chose summer as the season
    advice += "Water your plants regularly and provide some shade.\n"  # gives advice arccording
    # to the season

elif season == "winter":  # checks if user chose winter as the season
    advice += "Protect your plants from frost with covers.\n"  # gives advice arccording
    # to the season

else:
    advice += "No advice for this season.\n"  # if neither summer nor winter was entered
    # no advice is given

# Determine advice based on the plant type
if plant_type == "flower":  # checks if user chose flower as the plant
    advice += "Use fertiliser to encourage blooms."  # gives advice arccording
    # to the plant type

elif plant_type == "vegetable":  # checks if user chose vegetable as the plant
    advice += "Keep an eye out for pests!"  # gives advice arccording
    # to the plant type

else:
    advice += "No advice for this type of plant."  # if neither flower nor vegetable was entered
    # no advice is given

# Print the generated advice
print(advice)
