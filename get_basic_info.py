import api_reader
import check_params
import json_reader
import parser_and_writer

input_file = "params.json"

params = json_reader.read_json(input_file)
check_params.verify(params)
output_file = params["output"]
start = params["start"]
end = params["end"]
forms = params["forms"]
check_params.validate(output_file, start, end, forms)

# output_file = "test.txt"
# start = 1
# end = 1010
# forms = {
#     "all": True,  # will overwrite all other options below, including "none"
#     "none": False,  # will overwrite all other options below if "all" is False
#     "forms": False,  # Deoxys, Wormadam, etc.
#     "aesthetic only": False,  # Burmy, Shellos, etc.
#     "gender-based": False,  # Meowstic, Indeedee, Oinkologne
#     "regional variant": False,
#     "mega evolution": False,
#     "primal": False,
#     "gigantamax": False,
#
#     "unique": False,  # Eternal Floette, Own Tempo Rockruff, etc.
#     "totem": False,
#     "partner": False,  # Pikachu and Eevee starters from Let's Go!
#
#     "cosplay pikachu": False,
#     "pikachu in a cap": False,
#     "ash greninja": False,  # Ash Greninja was removed in Gen IX
#     "disguise": False,
#
#     "eternamax": False,
#     "mounts": False  # Koraidon and Miraidon non-battle forms
# }

print("Will now write basic data of Pokémon #{} to #{} to the file {}.\n"
      .format(str(start), str(end), output_file))

dex = api_reader.read_api(start, end, forms)
parser_and_writer.parse_and_write_info(output_file, dex, forms)
