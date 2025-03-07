"""
def most_endangered(species_list):
    lowest = float("inf")
    lowest_name = ""

    for species in species_list:
        if species["population"] < lowest:
            lowest = species["population"]
            lowest_name = species["name"]
    
    return lowest_name
        

species_list = [
    {"name": "Amur Leopard",
     "habitat": "Temperate forests",
     "population": 84
    },
    {"name": "Javan Rhino",
     "habitat": "Tropical forests",
     "population": 72
    },
    {"name": "Vaquita",
     "habitat": "Marine",
     "population": 10
    }
]

print(most_endangered(species_list))
"""

"""
def count_endangered_species(endangered_species, observed_species):
    count = 0
    observed = set()
    for i in endangered_species:
        if i not in observed:
            observed.add(i)
    
    for x in observed_species:
        if x in observed:
            count += 1

    return count

endangered_species1 = "aA"
observed_species1 = "aAAbbbb"

endangered_species2 = "z"
observed_species2 = "ZZ"

print(count_endangered_species(endangered_species1, observed_species1)) 
print(count_endangered_species(endangered_species2, observed_species2))
"""

