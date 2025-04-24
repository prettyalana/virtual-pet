# Define dictionaries that hold the pet's attributes

lamb = {"name": "Lolly", "breed": "Babydoll Lamb", "fullness": 10, "happiness": 20}

axolotl = {"name": "Pink", "breed": "Salamander", "fullness": 100, "happiness": 50}

# Define a list that holds all of our pets
pets = [lamb, axolotl]


def welcome_prompt():
    print("Welcome to the Pet Land Adoption Center")
    choose_pet = int(
        input(
            f"""Please choose a pet: 
            1. {pets[0]["name"]}: {pets[0]["breed"]} 
            2. {pets[1]["name"]}: {pets[1]["breed"]}
            """
        )
    )


# Define functions that increase a pet's attributes
def feed_pet(pet):
    pet["fullness"] = min(pet["fullness"] + 10, 100)


def groom_pet(pet):
    pet["happiness"] = min(pet["happiness"] + 10, 100)


def play_with_pet(pet):
    pet["happiness"] = min(pet["happiness"] + 10, 100)


# Decrease a pet's attributes


def needs_a_bath(pet):
    pet["happiness"] = max(pet["happiness"] - 10, 0)


def feels_neglected(pet):
    pet["happiness"] = max(pet["happiness"] - 10, 0)


def hungry(pet):
    pet["fullness"] = max(pet["fullness"] - 10, 0)


# Prompt the user to interact with pet

welcome_prompt()

while True:

    print(
        f"""Name: {lamb['name']}, Breed: {lamb['breed']}, Fullness Level: {lamb["fullness"]}, Happiness Level: {lamb['happiness']}"""
    )

    choice = int(
        input(
            f"""1. Feed {lamb['name']} 
2. Pet {lamb['name']} 
3. Play fetch with {lamb['name']} 
4. Shear {lamb['name']} 
5. Bathe {lamb['name']} 
6. Do nothing """
        )
    )

    if choice == 1:
        feed_pet(lamb)
    elif choice == 2:
        play_with_pet(lamb)
    elif choice == 3:
        play_with_pet(lamb)
    elif choice == 4:
        groom_pet(lamb)
    elif choice == 5:
        groom_pet(lamb)
    else:
        needs_a_bath(lamb)
        feels_neglected(lamb)
        hungry(lamb)
