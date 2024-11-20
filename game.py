import random

def create_character():
    """
    Create a character with user-input attributes
    Returns a dictionary representing the character
    """
    print("🎮 Welcome to Character Creation")
    name = input("Enter character name: ")
    health = random.randint(50, 100)
    attack_points = random.randint(10, 30)
    defense = random.randint(5, 20)
    
    character = {
        'name': name,
        'health': health,
        'attack_points': attack_points,
        'defense': defense
    }
    
    return character

def display_characters(character_list):
    """
    Display all characters in the list
    
    Args:
    character_list (list): List of character dictionaries
    """
    print("\n🏆 Character Roster:")
    for index, character in enumerate(character_list, 1):
        print(f"\nCharacter {index}:")
        print()
        for key, value in character.items():
            print(f"{key.capitalize()}: {value}")

def battle(attacker, defender):
    """
    Simulate a battle between two characters
    
    Args:
    attacker (dict): Character dictionary of the attacking character
    defender (dict): Character dictionary of the defending character
    
    Returns:
    tuple: Updated attacker and defender dictionaries
    """
    damage = max(0, attacker['attack_points'] - defender['defense'] // 2)
    defender['health'] = max(0, defender['health'] - damage)
    
    print(f"\n⚔️ {attacker['name']} attacks {defender['name']}!")
    print(f"🎯 {damage} damage dealt!")
    
    return attacker, defender

def information(choice1):
    while True:
        print("1. Location")
        print("2. Lifespan")
        print("3. Characteristics")
        print("4. Food it eats")

        choice = input("Select an option (1-4):")
        break        
    else: 
        print("🚫 Please enter a valid option! 🚫")

def squirrels():
    while True:
        print()
        print("🥜 Welcome to Squirrel information! 🥜")
        print("-------------------------------------")
        print("1. American Red Squirrel")
        print("2. Eastern Gray Squirrel")
        print("3. Abert's Squirrel")
        print("4. African Ground Squirrel")
        print("5. Indian Giant Squirrel")
        print("6. Exit")


        choice = input("Select an option (1-5): ")



        if choice == '1':
            print("What do you want to know about the American Red Squirrel?")
            information()
            choice1 = input("Select an option (1-4): ")
            if choice1 =='1':
                print("Found in the North American Continent")
            elif choice1 =='2':
                print("The lifespan is 3-5 years")
            elif choice1 =='3':
                print("Rich, reddish-brown fur")
                print("White eye ring around black eyes")
                print("Bushy and curling tail")
                print("Small but stout body")
                print("Erect ears with small tufts of fur")
            elif choice1 =='4':
                print("Acorns, hazelnuts, seeds, berries, birds' eggs, and mushrooms")
            else:
                break

                
        elif choice == '2':
            print("What do you want to know about the Eastern Gray Squirrel")
            information()

        elif choice == '3':
            print("What do you want to know about the Abert's Squirrel")
            information()

        elif choice == '4':
            print("What do you want to know about the African Ground Squirrel")
            information()

        elif choice == '5':
            print("What do you want to know about the Indian Giant Squirrel")
            information()

        elif choice == '6':
            print("🚫 Squirrel Information has been closed 🚫")
            break        
        else: 
            print("🚫 Please enter a valid option! 🚫")
        

def main():
    """
    Main game loop with character creation and battle mechanics
    """
    characters = []
    
    while True:
        print("\n🥜 Squirrel Sanctuary's Game Menu 🥜")
        print("-------------------------------------")
        print("1. Squirrel Information")        
        print("2. Create Characters")
        print("3. Display Characters")
        print("4. Battles")
        print("5. Exit Game")
        print("-------------------------------------")

 
        
        choice = input("Select an option (1-5): ")
        
        if choice == '1':
            squirrels()


        elif choice == '2':
            new_character = create_character()
            characters.append(new_character)
            print(f"✨ {new_character['name']} created successfully!")
        
        elif choice == '3':
            if characters:
                display_characters(characters)
            else:
                print("🚫 No characters have been created yet! 🚫")
        
        elif choice == '4':
            if len(characters) < 2:
                print("🚫 Need at least 2 characters to battle! 🚫")
                continue
            
            print("Select characters to battle:")
            display_characters(characters)
            
            try:
                attacker_index = int(input("Choose attacker (enter number): ")) - 1
                defender_index = int(input("Choose defender (enter number): ")) - 1
                
                if 0 <= attacker_index < len(characters) and 0 <= defender_index < len(characters):
                    characters[attacker_index], characters[defender_index] = battle(
                        characters[attacker_index], 
                        characters[defender_index]
                    )
                    
                    # Check for character defeat
                    if characters[defender_index]['health'] <= 0:
                        print(f"💀 {characters[defender_index]['name']} has been defeated!")
                        characters.pop(defender_index)
                else:
                    print("🚫 Invalid character selection! 🚫")
            
            except ValueError:
                print("🚫 Please enter valid numbers! 🚫")
        
        elif choice == '5':
            print("👋 Thanks for playing!")
            break
        
        else:
            print("🚫 Invalid option. Try again. 🚫")

if __name__ == "__main__":
    main()