import reader
import parser_and_writer

filename = "pokemon_data.txt"
# limit = 1010
# limit = 1281
limit = 1010
forms = {
    "all": True,  # If True, will overwrite all other options below
    "forms": False,  # Deoxys, Wormadam, etc.
    "aesthetic only": False,  # Burmy, Shellos, etc.
    "gender-based": False,  # Meowstic, Indeedee, Oinkologne
    "regional variant": False,
    "mega evolution": False,
    "primal": False,
    "gigantamax": False,

    "unique": False,  # Eternal Floette, Own Tempo Rockruff, etc.
    "totem": False,
    "partner": False,  # Pikachu and Eevee starters from Let's Go!

    "cosplay pikachu": False,
    "pikachu in a cap": False,
    "ash greninja": False,  # Ash Greninja was removed in Gen IX
    "disguise": False,

    "eternamax": False,
    "mounts": False  # Koraidon and Miraidon non-battle forms
}

print("Will now write basic data of the first " + str(limit) + " Pokémon to file.\n")

dex = reader.read_api(limit, forms)
parser_and_writer.parse_and_write_info(filename, dex, forms)
