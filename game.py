import random

def create_character():
    """
    Create a character with user-input attributes
    Returns a dictionary representing the character
    """
    print("🎮 Character Creation")
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

def main():
    """
    Main game loop with character creation and battle mechanics
    """
    characters = []
    
    while True:
        print("\n🎲 Character Game Menu")
        print("1. Create Character")
        print("2. Display Characters")
        print("3. Battle")
        print("4. Exit Game")
        
        choice = input("Select an option (1-4): ")
        
        if choice == '1':
            new_character = create_character()
            characters.append(new_character)
            print(f"✨ {new_character['name']} created successfully!")
        
        elif choice == '2':
            if characters:
                display_characters(characters)
            else:
                print("🚫 No characters created yet!")
        
        elif choice == '3':
            if len(characters) < 2:
                print("🚫 Need at least 2 characters to battle!")
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
                    print("🚫 Invalid character selection!")
            
            except ValueError:
                print("🚫 Please enter valid numbers!")
        
        elif choice == '4':
            print("👋 Thanks for playing!")
            break
        
        else:
            print("🚫 Invalid option. Try again.")

if __name__ == "__main__":
    main()