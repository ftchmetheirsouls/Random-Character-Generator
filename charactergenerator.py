import random

# --- Data Lists ---
species_list = [
    "Fox", "Wolf", "Dog", "Dragon", "Cat", "Tiger", "Lion", "Raccoon",
    "Rabbit", "Skunk", "Bear", "Otter", "Horse", "Coyote", "Cheetah",
    "Hyena", "Snow Leopard", "Kangaroo", "Bird", "Rat", "Gryphon", 
    "Leopard", "Lynx", "Ferret", "Cougar", "Dinosaur", "Squirrel", "Jackal", "Deer", "Bat"
]

body_type_list = ["Slim", "Chubby", "Stocky", "Athletic", "Muscular", "Curvy", "Femboy"]
fur_color_list = ["Grey", "Tan", "White", "Blue", "Auburn", "Orange", "Blonde", "Purple", "Brown"]
hair_color_list = ["Grey", "Tan", "White", "Blue", "Auburn", "Orange", "Blonde", "Purple"]
eye_color_list = ["Blue", "Pink", "Orange", "Yellow", "Purple", "Green"]
gender_list = ["Male", "Female"]

cock_size_list = ["Small (<4\")", "Average (<9\")", "Large (<13\")", "Huge (<20\")", "Gigantic (<30\")"]
cock_size_weights = [20, 49, 30, 1, 1]  # weighted chance example

balls_list = ["Small (Coin Purse)", "Average (Tight)", "Large (Saggy)", "Heavy (Baggy+Clean)", "Gigantic (Dragging)"]
balls_weights = [20, 49, 30, 1, 1]

breasts_list = ["Small", "Average", "Large", "Gifted"]
breasts_weights = [20, 40, 40, 40]

booty_list = ["Small", "Average", "Large", "Plump"]

sensitive_zones_male = ["Back/Wings", "Shoulders", "Shaft", "Balls", "Belly", "Head/Ears", "Flare/Knot", "Arms", "Legs", "Chest", "Ass", "Tail Base", "Thigh", "Nipples", "Neck"]
sensitive_zones_female = ["Back/Wings", "Shoulders", "Pussy", "Arms", "Legs", "Chest/Breasts", "Clit", "Ass", "Tail Base", "Belly", "Thigh", "Head/Ears", "Nipples", "Neck"]

fetishes = [
    "Bondage", "Pet Play", "Exhibitionism", "Voyeurism", "Rape", "Rough Sex", "Gentle Sex",
    "Body Worship", "Breast Worship", "Ass Worship", "Spanking", "Bathing, Shower and Beach",
    "Role Playing", "Molestation", "Group Sex", "Gangbang", "Oil", "Impregnation",
    "Bareback", "Garment", "Lactation", "Magic", "Infidelity", "Blackmail", "Bukkake",
    "Slavery", "Pornography", "Drugs", "Drunk", "Glory Hole", "Stranger", "Authority",
    "Forced Masturbation", "Oral Sex", "Vaginal Sex", "Anal Sex", "Femdom", "Bestiality",
    "Chest Worship", "Genital Worship", "Sex Machines", "Swinging", "Risk", "Dirty Talk",
    "Hair Pulling", "Biting", "Lingerie", "Younger Partners", "Older Partners",
    "Smaller Partners", "Bigger Partners", "Dominant Male", "Dominant Female",
    "Submissive Male", "Submissive Female"
]

# Occupations, fears, goals, clothing
occupations = ["None", "Cashier", "Merchant", "Teaching", "Music", "Physical Laborer", "Craftsman", "Shady", "Law", "Student", "Sports", "Mercenary", "Freelancer", "Police/Guard", "Management", "Academics", "Food", "Entertainment", "Traveler", "Government", "Military", "Sexual", "Theater", "Movies", "Business", "Mechanics"]
clothing_styles = ["Adventurous", "Elegant", "Tidy", "Gloomy", "Rebellious", "Formal", "Flamboyant", "Shabby", "Seductive", "Casual", "Conservative", "Fashionable", "Plain", "Sporty", "Professional", "Cute", "Skimpy"]
fears = ["Failure", "Criticism", "Being forgotten", "Death", "Losing Loved ones", "Oppression", "Being hated", "Injury", "Weakness", "Rejection"]
specific_fears = ["Being Alone", "Hospitals", "Tight Spaces", "Magic", "Heights", "Public Speaking", "Diseases", "The Dark", "Supernatural", "Commitment", "Abandonment", "Thunder", "Pregnancy", "Aging", "Work", "Clowns", "Zombies", "Buried Alive", "Love", "Needles", "Animals", "The Future", "Monsters", "Tentacles", "Demons", "Criminals", "Eldritch Abominations", "Cultists", "Snakes", "Ghosts"]
goals = ["Love", "Power", "Respect", "Independence", "Friendship", "Fame", "Strength", "Acceptance", "Knowledge", "Wealth", "Freedom"]

# --- Character Generator Function ---
def generate_character():
    character = {}
    character["Gender"] = random.choice(gender_list)
    character["Species"] = random.choice(species_list)
    character["FurColor"] = random.choice(fur_color_list)
    character["HairColor"] = random.choice(hair_color_list)
    character["EyeColor"] = random.choice(eye_color_list)
    character["BodyType"] = random.choice(body_type_list)
    character["Height"] = random.choice(["Small (4'5-5'0)", "Average (5'1-5'10)", "Tall (6'0-6'7)", "Big (6'11-7'6)"])
    character["Frame"] = random.choice(["Small", "Medium", "Large"])
    character["BodyMass"] = random.choice(["Chubby", "Slim", "Curvy", "Athletic", "Muscular", "Stocky", "Skinny", "Burly"])
    character["Age"] = random.choice(["Young Adult (18-30)", "Older Adult (30-50)", "Elderly (50-80)"])
    character["ClothingStyle"] = random.choice(clothing_styles)
    character["Occupation"] = random.choice(occupations)
    character["Fear"] = random.choice(fears)
    character["SpecificFears"] = random.sample(specific_fears, k=3)
    character["Goals"] = random.sample(goals, k=3)
    
    # NSFW traits
    if character["Gender"] == "Male":
        character["CockSize"] = random.choices(cock_size_list, weights=cock_size_weights, k=1)[0]
        character["Balls"] = random.choices(balls_list, weights=balls_weights, k=1)[0]
        character["SensitiveZones"] = random.sample(sensitive_zones_male, k=4)
    else:
        character["Breasts"] = random.choices(breasts_list, weights=breasts_weights, k=1)[0]
        character["Booty"] = random.choice(booty_list)
        character["SensitiveZones"] = random.sample(sensitive_zones_female, k=4)
    
    character["Fetishes"] = random.sample(fetishes, k=4)

    return character

# --- Formatter ---
def format_character(char):
    output = f"<b>Gender:</b> {char['Gender']}<br>"
    output += f"<b>Species:</b> {char['Species']}<br>"
    output += f"<b>Fur Color:</b> {char['FurColor']}<br>"
    output += f"<b>Hair Color:</b> {char['HairColor']}<br>"
    output += f"<b>Eye Color:</b> {char['EyeColor']}<br>"
    output += f"<b>BodyType:</b> {char['BodyType']}<br>"
    output += f"<b>Body Mass:</b> {char['BodyMass']}<br>"
    output += f"<b>Frame:</b> {char['Frame']}<br>"
    output += f"<b>Height:</b> {char['Height']}<br>"
    output += f"<b>Age:</b> {char['Age']}<br>"
    output += f"<b>Clothing Style:</b> {char['ClothingStyle']}<br>"
    output += f"<b>Occupation:</b> {char['Occupation']}<br>"
    output += f"<b>Fear:</b> {char['Fear']}<br>"
    output += f"<b>Specific Fears:</b> {', '.join(char['SpecificFears'])}<br>"
    output += f"<b>Goals:</b> {', '.join(char['Goals'])}<br>"
    
    if char["Gender"] == "Male":
        output += f"<b>Cock Size:</b> {char['CockSize']}<br>"
        output += f"<b>Balls:</b> {char['Balls']}<br>"
    else:
        output += f"<b>Breasts:</b> {char['Breasts']}<br>"
        output += f"<b>Booty:</b> {char['Booty']}<br>"
    
    output += f"<b>Sensitive Zones:</b> {', '.join(char['SensitiveZones'])}<br>"
    output += f"<b>Fetishes:</b> {', '.join(char['Fetishes'])}<br>"
    
    return output

# --- Generate and Print Example ---
npc = generate_character()
print(format_character(npc))