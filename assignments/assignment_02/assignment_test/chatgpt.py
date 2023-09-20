import requests
import random

# Function to fetch Pokémon data
def get_pokemon_data(pokemon_name):
    url = f"https://pokeapi.co/api/v2/pokemon/{pokemon_name.lower()}"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        return data
    else:
        print(f"Error: Couldn't fetch data for {pokemon_name}.")
        return None

# Function to save Pokémon names and moves to a file
def save_to_file(filename, pokemon_data):
    with open(filename, "w") as file:
        for pokemon in pokemon_data:
            file.write(f"Name: {pokemon['name'].capitalize()}\n")
            file.write("Moves:\n")
            for move in pokemon['moves']:
                file.write(f"- {move['move']['name'].capitalize()}\n")
            file.write("\n")

# Main program
def main():
    print("Welcome to the Pokémon data retrieval program!")
    print("Let's start by fetching some Pokémon data.\n")

    # Ask the user for Pokémon names
    pokemon_names = []
    while True:
        user_input = input("Enter a Pokémon name (or type 'random' for a random Pokémon): ").strip().lower()
        
        if user_input == 'random':
            # Generate a random Pokémon name
            random_pokemon = random.choice(pokemon_names)
            print(f"You've chosen a random Pokémon: {random_pokemon.capitalize()}!")
            pokemon_names = [random_pokemon]  # Only use the random Pokémon
            break
        elif user_input == 'pikachu':
            print("Pikachu is a great choice!")
        elif user_input in pokemon_names:
            print(f"You've already chosen {user_input.capitalize()}.")
        else:
            pokemon_names.append(user_input)

        continue_input = input("Do you want to add another Pokémon? (yes/no): ").strip().lower()
        if continue_input != 'yes':
            break

    # Fetch Pokémon data
    pokemon_data = []
    for name in pokemon_names:
        data = get_pokemon_data(name)
        if data:
            pokemon_data.append(data)

    if not pokemon_data:
        print("No valid Pokémon data to save.")
        return

    # Save Pokémon data to a file
    save_filename = "pokemon_data.txt"
    save_to_file(save_filename, pokemon_data)
    print(f"\nPokémon data has been saved to {save_filename}.")

if __name__ == "__main__":
    main()
