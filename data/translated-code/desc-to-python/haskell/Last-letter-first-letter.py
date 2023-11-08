```python
# Define a list of all Pokémon names as ByteStrings
pokemon_names = [b'Bulbasaur', b'Ivysaur', b'Venusaur', b'Charmander', b'Charmeleon', b'Charizard', b'Squirtle', b'Wartortle', b'Blastoise']

# Create a function to grow chains of Pokémon names based on their last and first letters
def growChains(pokemon_names):
    chains = []
    for name1 in pokemon_names:
        for name2 in pokemon_names:
            if name1 != name2 and name1[-1] == name2[0]:
                chains.append(name1 + b' -> ' + name2)
    return chains

# Main function to print the resulting chains of Pokémon names
def main():
    chains = growChains(pokemon_names)
    for chain in chains:
        print(chain)

main()
```