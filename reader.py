import json
import requests


def read_api(limit, forms):
    dex = []

    print("Gathering data...")
    for x in range(limit):
        i = str(x + 1)
        dex = create_request(i, forms, dex)
        print("Gathered data for Pokémon #" + i)

    print("Gathering data complete!\n")
    return dex


def create_request(i, forms, dex):
    if forms["all"]:
        forms = set_all_true(forms)
    alt = forms["forms"]
    aesthetic = forms["aesthetic only"]
    gender = forms["gender-based"]
    regional = forms["regional variant"]
    mega = forms["mega evolution"]
    primal = forms["primal"]
    gmax = forms["gigantamax"]
    unique = forms["unique"]
    totem = forms["totem"]
    partner = forms["partner"]
    cosplay = forms["cosplay pikachu"]
    cap = forms["pikachu in a cap"]
    ash = forms["ash greninja"]
    disguise = forms["disguise"]
    eternamax = forms["eternamax"]

    dex = get_response(i, i, dex)
    match i:  # Go through each Pokémon in National Dex order
        case "3":
            if mega:
                dex = get_response(i, "venusaur-mega", dex)
            if gmax:
                dex = get_response(i, "venusaur-gmax", dex)
        case "6":
            if mega:
                dex = get_response(i, "charizard-mega-x", dex)
                dex = get_response(i, "charizard-mega-y", dex)
            if gmax:
                dex = get_response(i, "charizard-gmax", dex)
        case "9":
            if mega:
                dex = get_response(i, "blastoise-mega", dex)
            if gmax:
                dex = get_response(i, "blastoise-gmax", dex)
        case "12":
            if gmax:
                dex = get_response(i, "butterfree-gmax", dex)
        case "15":
            if mega:
                dex = get_response(i, "beedrill-mega", dex)
        case "18":
            if mega:
                dex = get_response(i, "pidgeot-mega", dex)
        case "19":
            if regional:
                dex = get_response(i, "rattata-alola", dex)
        case "20":
            if regional:
                dex = get_response(i, "raticate-alola", dex)
            if totem:
                dex = get_response(i, "raticate-totem-alola", dex)
        case "25":
            if cosplay:
                dex = get_response(i, "pikachu-cosplay", dex)
                dex = get_response(i, "pikachu-rock-star", dex)
                dex = get_response(i, "pikachu-belle", dex)
                dex = get_response(i, "pikachu-pop-star", dex)
                dex = get_response(i, "pikachu-phd", dex)
                dex = get_response(i, "pikachu-libre", dex)
            if cap:
                dex = get_response(i, "pikachu-original-cap", dex)
                dex = get_response(i, "pikachu-hoenn-cap", dex)
                dex = get_response(i, "pikachu-sinnoh-cap", dex)
                dex = get_response(i, "pikachu-unova-cap", dex)
                dex = get_response(i, "pikachu-kalos-cap", dex)
                dex = get_response(i, "pikachu-alola-cap", dex)
                dex = get_response(i, "pikachu-partner-cap", dex)
                dex = get_response(i, "pikachu-world-cap", dex)
            if partner:
                dex = get_response(i, "pikachu-starter", dex)
            if gmax:
                dex = get_response(i, "pikachu-gmax", dex)
        case "26":
            if regional:
                dex = get_response(i, "raichu-alola", dex)
        case "27":
            if regional:
                dex = get_response(i, "sandshrew-alola", dex)
        case "28":
            if regional:
                dex = get_response(i, "sandslash-alola", dex)
        case "37":
            if regional:
                dex = get_response(i, "vulpix-alola", dex)
        case "38":
            if regional:
                dex = get_response(i, "ninetales-alola", dex)
        case "50":
            if regional:
                dex = get_response(i, "diglett-alola", dex)
        case "51":
            if regional:
                dex = get_response(i, "dugtrio-alola", dex)
        case "52":
            if regional:
                dex = get_response(i, "meowth-alola", dex)
                dex = get_response(i, "meowth-galar", dex)
            if gmax:
                dex = get_response(i, "meowth-gmax", dex)
        case "53":
            if regional:
                dex = get_response(i, "persian-alola", dex)
        case "58":
            if regional:
                dex = get_response(i, "growlithe-hisui", dex)
        case "59":
            if regional:
                dex = get_response(i, "arcanine-hisui", dex)
        case "65":
            if mega:
                dex = get_response(i, "alakazam-mega", dex)
        case "68":
            if gmax:
                dex = get_response(i, "machamp-gmax", dex)
        case "74":
            if regional:
                dex = get_response(i, "geodude-alola", dex)
        case "75":
            if regional:
                dex = get_response(i, "geodude-graveler", dex)
        case "76":
            if regional:
                dex = get_response(i, "geodude-golem", dex)
        case "77":
            if regional:
                dex = get_response(i, "ponyta-galar", dex)
        case "78":
            if regional:
                dex = get_response(i, "rapidash-galar", dex)
        case "79":
            if regional:
                dex = get_response(i, "slowpoke-galar", dex)
        case "80":
            if mega:
                dex = get_response(i, "slowbro-mega", dex)
            if regional:
                dex = get_response(i, "slowbro-galar", dex)
        case "83":
            if regional:
                dex = get_response(i, "farfetchd-galar", dex)
        case "88":
            if regional:
                dex = get_response(i, "grimer-alola", dex)
        case "89":
            if regional:
                dex = get_response(i, "muk-alola", dex)
        case "94":
            if mega:
                dex = get_response(i, "gengar-mega", dex)
            if gmax:
                dex = get_response(i, "gengar-gmax", dex)
        case "99":
            if gmax:
                dex = get_response(i, "kingler-gmax", dex)
        case "100":
            if regional:
                dex = get_response(i, "voltorb-hisui", dex)
        case "101":
            if regional:
                dex = get_response(i, "electrode-hisui", dex)
        case "103":
            if regional:
                dex = get_response(i, "exeggutor-alola", dex)
        case "105":
            if regional:
                dex = get_response(i, "marowak-alola", dex)
            if totem:
                dex = get_response(i, "marowak-totem", dex)
        case "110":
            if regional:
                dex = get_response(i, "weezing-galar", dex)
        case "115":
            if mega:
                dex = get_response(i, "kangaskhan-mega", dex)
        case "122":
            if regional:
                dex = get_response(i, "mr-mime-galar", dex)
        case "127":
            if mega:
                dex = get_response(i, "pinsir-mega", dex)
        case "128":
            if regional:
                dex = get_response(i, "tauros-paldea-combat-breed", dex)
                dex = get_response(i, "tauros-paldea-blaze-breed", dex)
                dex = get_response(i, "tauros-paldea-aqua-breed", dex)
        case "130":
            if mega:
                dex = get_response(i, "gyarados-mega", dex)
        case "131":
            if gmax:
                dex = get_response(i, "lapras-gmax", dex)
        case "133":
            if partner:
                dex = get_response(i, "eevee-starter", dex)
            if gmax:
                dex = get_response(i, "eevee-gmax", dex)
        case "142":
            if mega:
                dex = get_response(i, "aerodactyl-mega", dex)
        case "143":
            if gmax:
                dex = get_response(i, "snorlax-gmax", dex)
        case "144":
            if regional:
                dex = get_response(i, "articuno-galar", dex)
        case "145":
            if regional:
                dex = get_response(i, "zapdos-galar", dex)
        case "146":
            if regional:
                dex = get_response(i, "moltres-galar", dex)
        case "150":
            if mega:
                dex = get_response(i, "mewtwo-mega-x", dex)
                dex = get_response(i, "mewtwo-mega-y", dex)

        case "157":
            if regional:
                dex = get_response(i, "typhlosion-hisui", dex)
        case "172":
            if unique:
                dex = get_response(i, "pichu-spiky-eared", dex)
        case "181":
            if mega:
                dex = get_response(i, "ampharos-mega", dex)
        case "194":
            if regional:
                dex = get_response(i, "wooper-paldea", dex)
        case "181":
            if mega:
                dex = get_response(i, "ampharos-mega", dex)
        case "199":
            if regional:
                dex = get_response(i, "slowking-galar", dex)
        case "201":
            if aesthetic:
                dex = get_response(i, "unown-b", dex)
                dex = get_response(i, "unown-c", dex)
                dex = get_response(i, "unown-d", dex)
                dex = get_response(i, "unown-e", dex)
                dex = get_response(i, "unown-f", dex)
                dex = get_response(i, "unown-g", dex)
                dex = get_response(i, "unown-h", dex)
                dex = get_response(i, "unown-i", dex)
                dex = get_response(i, "unown-j", dex)
                dex = get_response(i, "unown-k", dex)
                dex = get_response(i, "unown-l", dex)
                dex = get_response(i, "unown-m", dex)
                dex = get_response(i, "unown-n", dex)
                dex = get_response(i, "unown-o", dex)
                dex = get_response(i, "unown-p", dex)
                dex = get_response(i, "unown-q", dex)
                dex = get_response(i, "unown-r", dex)
                dex = get_response(i, "unown-s", dex)
                dex = get_response(i, "unown-t", dex)
                dex = get_response(i, "unown-u", dex)
                dex = get_response(i, "unown-v", dex)
                dex = get_response(i, "unown-w", dex)
                dex = get_response(i, "unown-x", dex)
                dex = get_response(i, "unown-y", dex)
                dex = get_response(i, "unown-z", dex)
                dex = get_response(i, "unown-exclamation", dex)
                dex = get_response(i, "unown-question", dex)
        case "208":
            if mega:
                dex = get_response(i, "steelix-mega", dex)
        case "211":
            if regional:
                dex = get_response(i, "qwilfish-hisui", dex)
        case "212":
            if mega:
                dex = get_response(i, "scizor-mega", dex)
        case "214":
            if mega:
                dex = get_response(i, "heracross-mega", dex)
        case "215":
            if regional:
                dex = get_response(i, "sneasel-hisui", dex)
        case "222":
            if regional:
                dex = get_response(i, "corsola-galar", dex)
        case "229":
            if mega:
                dex = get_response(i, "houndoom-mega", dex)
        case "248":
            if mega:
                dex = get_response(i, "tyranitar-mega", dex)

        case "254":
            if mega:
                dex = get_response(i, "sceptile-mega", dex)
        case "257":
            if mega:
                dex = get_response(i, "blaziken-mega", dex)
        case "260":
            if mega:
                dex = get_response(i, "swampert-mega", dex)
        case "263":
            if regional:
                dex = get_response(i, "zigzagoon-galar", dex)
        case "264":
            if regional:
                dex = get_response(i, "linoone-galar", dex)
        case "282":
            if mega:
                dex = get_response(i, "gardevoir-mega", dex)
        case "302":
            if mega:
                dex = get_response(i, "sableye-mega", dex)
        case "303":
            if mega:
                dex = get_response(i, "mawile-mega", dex)
        case "306":
            if mega:
                dex = get_response(i, "aggron-mega", dex)
        case "308":
            if mega:
                dex = get_response(i, "medicham-mega", dex)
        case "310":
            if mega:
                dex = get_response(i, "manectric-mega", dex)
        case "319":
            if mega:
                dex = get_response(i, "sharpedo-mega", dex)
        case "323":
            if mega:
                dex = get_response(i, "camerupt-mega", dex)
        case "334":
            if mega:
                dex = get_response(i, "altaria-mega", dex)
        case "351":
            if alt:
                dex = get_response(i, "castform-sunny", dex)
                dex = get_response(i, "castform-rainy", dex)
                dex = get_response(i, "castform-snowy", dex)
        case "354":
            if mega:
                dex = get_response(i, "banette-mega", dex)
        case "359":
            if mega:
                dex = get_response(i, "absol-mega", dex)
        case "362":
            if mega:
                dex = get_response(i, "glalie-mega", dex)
        case "373":
            if mega:
                dex = get_response(i, "salamence-mega", dex)
        case "376":
            if mega:
                dex = get_response(i, "metagross-mega", dex)
        case "380":
            if mega:
                dex = get_response(i, "latias-mega", dex)
        case "381":
            if mega:
                dex = get_response(i, "latios-mega", dex)
        case "382":
            if primal:
                dex = get_response(i, "kyogre-mega", dex)
        case "383":
            if primal:
                dex = get_response(i, "groudon-mega", dex)
        case "384":
            if mega:
                dex = get_response(i, "rayquaza-mega", dex)
        case "384":
            if mega:
                dex = get_response(i, "rayquaza-mega", dex)
        case "386":
            if alt:
                dex = get_response(i, "deoxys-attack", dex)
                dex = get_response(i, "deoxys-defense", dex)
                dex = get_response(i, "deoxys-speed", dex)

        case "412":
            if aesthetic:
                dex = get_response(i, "burmy-sandy", dex)
                dex = get_response(i, "burmy-trash", dex)
        case "413":
            if alt:
                dex = get_response(i, "wormadam-sandy", dex)
                dex = get_response(i, "wormadam-trash", dex)
        case "421":
            if aesthetic:
                dex = get_response(i, "cherrim-sunshine", dex)
        case "422":
            if aesthetic:
                dex = get_response(i, "shellos-east", dex)
        case "423":
            if aesthetic:
                dex = get_response(i, "gastrodon-east", dex)
        case "428":
            if mega:
                dex = get_response(i, "lopunny-mega", dex)
        case "445":
            if mega:
                dex = get_response(i, "garchomp-mega", dex)
        case "448":
            if mega:
                dex = get_response(i, "lucario-mega", dex)
        case "460":
            if mega:
                dex = get_response(i, "abomasnow-mega", dex)
        case "475":
            if mega:
                dex = get_response(i, "gallade-mega", dex)
        case "479":
            if alt:
                dex = get_response(i, "rotom-heat", dex)
                dex = get_response(i, "rotom-wash", dex)
                dex = get_response(i, "rotom-frost", dex)
                dex = get_response(i, "rotom-fan", dex)
                dex = get_response(i, "rotom-mow", dex)
        case "483":
            if alt:
                dex = get_response(i, "dialga-origin", dex)
        case "484":
            if alt:
                dex = get_response(i, "palkia-origin", dex)
        case "487":
            if alt:
                dex = get_response(i, "giratina-origin", dex)
        case "492":
            if alt:
                dex = get_response(i, "shaymin-sky", dex)
        case "493":
            if alt:
                dex = get_response(i, "arceus-bug", dex)
                dex = get_response(i, "arceus-dark", dex)
                dex = get_response(i, "arceus-dragon", dex)
                dex = get_response(i, "arceus-electric", dex)
                dex = get_response(i, "arceus-fighting", dex)
                dex = get_response(i, "arceus-fire", dex)
                dex = get_response(i, "arceus-flying", dex)
                dex = get_response(i, "arceus-ghost", dex)
                dex = get_response(i, "arceus-grass", dex)
                dex = get_response(i, "arceus-ground", dex)
                dex = get_response(i, "arceus-ice", dex)
                dex = get_response(i, "arceus-poison", dex)
                dex = get_response(i, "arceus-psychic", dex)
                dex = get_response(i, "arceus-rock", dex)
                dex = get_response(i, "arceus-steel", dex)
                dex = get_response(i, "arceus-water", dex)
                dex = get_response(i, "arceus-fairy", dex)

        case "502":
            if regional:
                dex = get_response(i, "samurott-hisui", dex)
        case "531":
            if mega:
                dex = get_response(i, "audino-mega", dex)
        case "549":
            if regional:
                dex = get_response(i, "lilligant-hisui", dex)
        case "550":
            if aesthetic:
                dex = get_response(i, "basculin-blue-striped", dex)
                dex = get_response(i, "basulin-white-striped", dex)
        case "554":
            if regional:
                dex = get_response(i, "darumaka-galar", dex)
        case "555":
            if alt:
                dex = get_response(i, "darmanitan-zen", dex)
            if regional:
                dex = get_response(i, "darmanitan-galar", dex)
            if alt and regional:
                dex = get_response(i, "darmanitan-garar-zen", dex)
        case "561":
            if regional:
                dex = get_response(i, "yamask-galar", dex)
        case "569":
            if gmax:
                dex = get_response(i, "garbodor-gmax", dex)
        case "570":
            if regional:
                dex = get_response(i, "zorua-hisui", dex)
        case "571":
            if regional:
                dex = get_response(i, "zoroark-hisui", dex)
        case "585":
            if aesthetic:
                dex = get_response(i, "deerling-summer", dex)
                dex = get_response(i, "deerling-autumn", dex)
                dex = get_response(i, "deerling-winter", dex)
        case "586":
            if aesthetic:
                dex = get_response(i, "sawsbuck-summer", dex)
                dex = get_response(i, "sawsbuck-autumn", dex)
                dex = get_response(i, "sawsbuck-winter", dex)
        case "618":
            if regional:
                dex = get_response(i, "stunfisk-galarian", dex)
        case "628":
            if regional:
                dex = get_response(i, "braviary-hisui", dex)
        case "641":
            if alt:
                dex = get_response(i, "tornadus-therian", dex)
        case "642":
            if alt:
                dex = get_response(i, "thundurus-therian", dex)
        case "645":
            if alt:
                dex = get_response(i, "landorus-therian", dex)
        case "646":
            if alt:
                dex = get_response(i, "kyurem-black", dex)
                dex = get_response(i, "kyurem-white", dex)
        case "647":
            if aesthetic:
                dex = get_response(i, "keldeo-resolute", dex)
        case "648":
            if alt:
                dex = get_response(i, "meloetta-pirouette", dex)
        case "649":
            if aesthetic:
                dex = get_response(i, "genesect-douse", dex)
                dex = get_response(i, "genesect-shock", dex)
                dex = get_response(i, "genesect-burn", dex)
                dex = get_response(i, "genesect-chill", dex)

        case "658":
            if unique:
                dex = get_response(i, "greninja-battle-bond", dex)
            if ash:
                dex = get_response(i, "greninja-ash", dex)
        case "666":
            if aesthetic:
                dex = get_response(i, "vivillon-icy-snow", dex)
                dex = get_response(i, "vivillon-polar", dex)
                dex = get_response(i, "vivillon-tundra", dex)
                dex = get_response(i, "vivillon-continental", dex)
                dex = get_response(i, "vivillon-garden", dex)
                dex = get_response(i, "vivillon-elegant", dex)
                dex = get_response(i, "vivillon-modern", dex)
                dex = get_response(i, "vivillon-marine", dex)
                dex = get_response(i, "vivillon-archipelago", dex)
                dex = get_response(i, "vivillon-high-plains", dex)
                dex = get_response(i, "vivillon-sandstorm", dex)
                dex = get_response(i, "vivillon-river", dex)
                dex = get_response(i, "vivillon-monsoon", dex)
                dex = get_response(i, "vivillon-savanna", dex)
                dex = get_response(i, "vivillon-sun", dex)
                dex = get_response(i, "vivillon-ocean", dex)
                dex = get_response(i, "vivillon-jungle", dex)
                dex = get_response(i, "vivillon-fancy", dex)
                dex = get_response(i, "vivillon-poke-ball", dex)
        case "669":
            if aesthetic:
                dex = get_response(i, "flabebe-yellow", dex)
                dex = get_response(i, "flabebe-orange", dex)
                dex = get_response(i, "flabebe-blue", dex)
                dex = get_response(i, "flabebe-white", dex)
        case "670":
            if aesthetic:
                dex = get_response(i, "floette-yellow", dex)
                dex = get_response(i, "floette-orange", dex)
                dex = get_response(i, "floette-blue", dex)
                dex = get_response(i, "floette-white", dex)
            if unique:
                dex = get_response(i, "floette-eternal")
        case "671":
            if aesthetic:
                dex = get_response(i, "florges-yellow", dex)
                dex = get_response(i, "florges-orange", dex)
                dex = get_response(i, "florges-blue", dex)
                dex = get_response(i, "florges-white", dex)
        case "676":
            if aesthetic:
                dex = get_response(i, "furfrou-heart", dex)
                dex = get_response(i, "furfrou-star", dex)
                dex = get_response(i, "furfrou-diamond", dex)
                dex = get_response(i, "furfrou-matron", dex)
                dex = get_response(i, "furfrou-dandy", dex)
                dex = get_response(i, "furfrou-la-reine", dex)
                dex = get_response(i, "furfrou-pharaoh", dex)
        case "678":
            if gender:
                dex = get_response(i, "meowstic-female", dex)
        case "681":
            if alt:
                dex = get_response(i, "aegislash-blade", dex)
        case "705":
            if regional:
                dex = get_response(i, "sliggoo-hisui", dex)
        case "706":
            if regional:
                dex = get_response(i, "goodra-hisui", dex)
        case "710":
            if alt:
                dex = get_response(i, "pumpkaboo-small", dex)
                dex = get_response(i, "pumpkaboo-large", dex)
                dex = get_response(i, "pumpkaboo-super", dex)
        case "711":
            if alt:
                dex = get_response(i, "gourgeist-small", dex)
                dex = get_response(i, "gourgeist-large", dex)
                dex = get_response(i, "gourgeist-super", dex)
        case "713":
            if regional:
                dex = get_response(i, "avalugg-hisui", dex)
        case "716":
            if aesthetic:
                dex = get_response(i, "xerneas-neutral", dex)
        case "718":
            if alt:
                dex = get_response(i, "zygarde-10-power-construct", dex)
                dex = get_response(i, "zygarde-50-power-construct", dex)
                dex = get_response(i, "zygarde-complete", dex)
                dex = get_response(i, "zygarde-10", dex)
        case "719":
            if mega:
                dex = get_response(i, "diancie-mega", dex)
        case "720":
            if alt:
                dex = get_response(i, "hoopa-unbound", dex)

        case "???":
            if gender:
                dex = get_response(i, "indeedee-female", dex)
        case "???":
            if gender:
                dex = get_response(i, "basculegion-female", dex)

        case "???":
            if gender:
                dex = get_response(i, "oinkologne-female", dex)

    return dex


def set_all_true(forms):
    forms["forms"] = True
    forms["aesthetic only"] = True
    forms["gender-based"] = True
    forms["regional variant"] = True
    forms["mega evolution"] = True
    forms["primal"] = True
    forms["gigantamax"] = True
    forms["unique"] = True
    forms["totem"] = True
    forms["partner"] = True
    forms["cosplay pikachu"] = True
    forms["pikachu in a cap"] = True
    forms["ash greninja"] = True
    forms["disguise"] = True
    forms["eternamax"] = True

    return forms


def get_response(index, name, dex):
    base_url = 'https://pokeapi.co/api/v2/pokemon/'

    response = requests.get(base_url + name + '/')
    entry = json.loads(response.text)
    entry["id"] = index
    dex.append(entry)
    return dex
