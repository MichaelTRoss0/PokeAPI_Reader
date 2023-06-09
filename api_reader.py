import json
import requests


def read_api(start, end, forms):
    dex = []

    print("Gathering data...")
    for x in range(start, end + 1):
        i = str(x)
        dex = create_request(i, forms, dex)
        print("Gathered data for Pokémon #" + i)

    print("Gathering data complete!\n")
    return dex


def create_request(i, forms, dex):
    if forms["all"]:
        forms = set_all_true(forms)
    elif forms["none"]:
        forms = set_all_false(forms)
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
    mounts = forms["mounts"]

    dex.append(get_response(i, i))
    match i:  # Go through each Pokémon in National Dex order
        case "3":
            if mega:
                dex.append(get_response(i, "venusaur-mega"))
            if gmax:
                dex.append(get_response(i, "venusaur-gmax"))
        case "6":
            if mega:
                dex.append(get_response(i, "charizard-mega-x"))
                dex.append(get_response(i, "charizard-mega-y"))
            if gmax:
                dex.append(get_response(i, "charizard-gmax"))
        case "9":
            if mega:
                dex.append(get_response(i, "blastoise-mega"))
            if gmax:
                dex.append(get_response(i, "blastoise-gmax"))
        case "12":
            if gmax:
                dex.append(get_response(i, "butterfree-gmax"))
        case "15":
            if mega:
                dex.append(get_response(i, "beedrill-mega"))
        case "18":
            if mega:
                dex.append(get_response(i, "pidgeot-mega"))
        case "19":
            if regional:
                dex.append(get_response(i, "rattata-alola"))
        case "20":
            if regional:
                dex.append(get_response(i, "raticate-alola"))
            if regional and totem:
                dex.append(get_response(i, "raticate-totem-alola"))
        case "25":
            if cosplay:
                dex.append(get_response(i, "pikachu-cosplay"))
                dex.append(get_response(i, "pikachu-rock-star"))
                dex.append(get_response(i, "pikachu-belle"))
                dex.append(get_response(i, "pikachu-pop-star"))
                dex.append(get_response(i, "pikachu-phd"))
                dex.append(get_response(i, "pikachu-libre"))
            if cap:
                dex.append(get_response(i, "pikachu-original-cap"))
                dex.append(get_response(i, "pikachu-hoenn-cap"))
                dex.append(get_response(i, "pikachu-sinnoh-cap"))
                dex.append(get_response(i, "pikachu-unova-cap"))
                dex.append(get_response(i, "pikachu-kalos-cap"))
                dex.append(get_response(i, "pikachu-alola-cap"))
                dex.append(get_response(i, "pikachu-partner-cap"))
                dex.append(get_response(i, "pikachu-world-cap"))
            if partner:
                dex.append(get_response(i, "pikachu-starter"))
            if gmax:
                dex.append(get_response(i, "pikachu-gmax"))
        case "26":
            if regional:
                dex.append(get_response(i, "raichu-alola"))
        case "27":
            if regional:
                dex.append(get_response(i, "sandshrew-alola"))
        case "28":
            if regional:
                dex.append(get_response(i, "sandslash-alola"))
        case "37":
            if regional:
                dex.append(get_response(i, "vulpix-alola"))
        case "38":
            if regional:
                dex.append(get_response(i, "ninetales-alola"))
        case "50":
            if regional:
                dex.append(get_response(i, "diglett-alola"))
        case "51":
            if regional:
                dex.append(get_response(i, "dugtrio-alola"))
        case "52":
            if regional:
                dex.append(get_response(i, "meowth-alola"))
                dex.append(get_response(i, "meowth-galar"))
            if gmax:
                dex.append(get_response(i, "meowth-gmax"))
        case "53":
            if regional:
                dex.append(get_response(i, "persian-alola"))
        case "58":
            if regional:
                dex.append(get_response(i, "growlithe-hisui"))
        case "59":
            if regional:
                dex.append(get_response(i, "arcanine-hisui"))
        case "65":
            if mega:
                dex.append(get_response(i, "alakazam-mega"))
        case "68":
            if gmax:
                dex.append(get_response(i, "machamp-gmax"))
        case "74":
            if regional:
                dex.append(get_response(i, "geodude-alola"))
        case "75":
            if regional:
                dex.append(get_response(i, "graveler-alola"))
        case "76":
            if regional:
                dex.append(get_response(i, "golem-alola"))
        case "77":
            if regional:
                dex.append(get_response(i, "ponyta-galar"))
        case "78":
            if regional:
                dex.append(get_response(i, "rapidash-galar"))
        case "79":
            if regional:
                dex.append(get_response(i, "slowpoke-galar"))
        case "80":
            if mega:
                dex.append(get_response(i, "slowbro-mega"))
            if regional:
                dex.append(get_response(i, "slowbro-galar"))
        case "83":
            if regional:
                dex.append(get_response(i, "farfetchd-galar"))
        case "88":
            if regional:
                dex.append(get_response(i, "grimer-alola"))
        case "89":
            if regional:
                dex.append(get_response(i, "muk-alola"))
        case "94":
            if mega:
                dex.append(get_response(i, "gengar-mega"))
            if gmax:
                dex.append(get_response(i, "gengar-gmax"))
        case "99":
            if gmax:
                dex.append(get_response(i, "kingler-gmax"))
        case "100":
            if regional:
                dex.append(get_response(i, "voltorb-hisui"))
        case "101":
            if regional:
                dex.append(get_response(i, "electrode-hisui"))
        case "103":
            if regional:
                dex.append(get_response(i, "exeggutor-alola"))
        case "105":
            if regional:
                dex.append(get_response(i, "marowak-alola"))
            if regional and totem:
                dex.append(get_response(i, "marowak-totem"))
        case "110":
            if regional:
                dex.append(get_response(i, "weezing-galar"))
        case "115":
            if mega:
                dex.append(get_response(i, "kangaskhan-mega"))
        case "122":
            if regional:
                dex.append(get_response(i, "mr-mime-galar"))
        case "127":
            if mega:
                dex.append(get_response(i, "pinsir-mega"))
        case "128":
            if regional:
                dex.append(get_response(i, "tauros-paldea-combat-breed"))
            if regional and alt:
                dex.append(get_response(i, "tauros-paldea-blaze-breed"))
                dex.append(get_response(i, "tauros-paldea-aqua-breed"))
        case "130":
            if mega:
                dex.append(get_response(i, "gyarados-mega"))
        case "131":
            if gmax:
                dex.append(get_response(i, "lapras-gmax"))
        case "133":
            if partner:
                dex.append(get_response(i, "eevee-starter"))
            if gmax:
                dex.append(get_response(i, "eevee-gmax"))
        case "142":
            if mega:
                dex.append(get_response(i, "aerodactyl-mega"))
        case "143":
            if gmax:
                dex.append(get_response(i, "snorlax-gmax"))
        case "144":
            if regional:
                dex.append(get_response(i, "articuno-galar"))
        case "145":
            if regional:
                dex.append(get_response(i, "zapdos-galar"))
        case "146":
            if regional:
                dex.append(get_response(i, "moltres-galar"))
        case "150":
            if mega:
                dex.append(get_response(i, "mewtwo-mega-x"))
                dex.append(get_response(i, "mewtwo-mega-y"))

        case "157":
            if regional:
                dex.append(get_response(i, "typhlosion-hisui"))
        # case "172":
        #     if unique:
        #         dex.append(get_response(i, "pichu-spiky-eared"))
        case "181":
            if mega:
                dex.append(get_response(i, "ampharos-mega"))
        case "194":
            if regional:
                dex.append(get_response(i, "wooper-paldea"))
        case "181":
            if mega:
                dex.append(get_response(i, "ampharos-mega"))
        case "199":
            if regional:
                dex.append(get_response(i, "slowking-galar"))
        # case "201":
        #     if aesthetic:
        #         dex.append(get_response(i, "unown-b"))
        #         dex.append(get_response(i, "unown-c"))
        #         dex.append(get_response(i, "unown-d"))
        #         dex.append(get_response(i, "unown-e"))
        #         dex.append(get_response(i, "unown-f"))
        #         dex.append(get_response(i, "unown-g"))
        #         dex.append(get_response(i, "unown-h"))
        #         dex.append(get_response(i, "unown-i"))
        #         dex.append(get_response(i, "unown-j"))
        #         dex.append(get_response(i, "unown-k"))
        #         dex.append(get_response(i, "unown-l"))
        #         dex.append(get_response(i, "unown-m"))
        #         dex.append(get_response(i, "unown-n"))
        #         dex.append(get_response(i, "unown-o"))
        #         dex.append(get_response(i, "unown-p"))
        #         dex.append(get_response(i, "unown-q"))
        #         dex.append(get_response(i, "unown-r"))
        #         dex.append(get_response(i, "unown-s"))
        #         dex.append(get_response(i, "unown-t"))
        #         dex.append(get_response(i, "unown-u"))
        #         dex.append(get_response(i, "unown-v"))
        #         dex.append(get_response(i, "unown-w"))
        #         dex.append(get_response(i, "unown-x"))
        #         dex.append(get_response(i, "unown-y"))
        #         dex.append(get_response(i, "unown-z"))
        #         dex.append(get_response(i, "unown-exclamation"))
        #         dex.append(get_response(i, "unown-question"))
        case "208":
            if mega:
                dex.append(get_response(i, "steelix-mega"))
        case "211":
            if regional:
                dex.append(get_response(i, "qwilfish-hisui"))
        case "212":
            if mega:
                dex.append(get_response(i, "scizor-mega"))
        case "214":
            if mega:
                dex.append(get_response(i, "heracross-mega"))
        case "215":
            if regional:
                dex.append(get_response(i, "sneasel-hisui"))
        case "222":
            if regional:
                dex.append(get_response(i, "corsola-galar"))
        case "229":
            if mega:
                dex.append(get_response(i, "houndoom-mega"))
        case "248":
            if mega:
                dex.append(get_response(i, "tyranitar-mega"))

        case "254":
            if mega:
                dex.append(get_response(i, "sceptile-mega"))
        case "257":
            if mega:
                dex.append(get_response(i, "blaziken-mega"))
        case "260":
            if mega:
                dex.append(get_response(i, "swampert-mega"))
        case "263":
            if regional:
                dex.append(get_response(i, "zigzagoon-galar"))
        case "264":
            if regional:
                dex.append(get_response(i, "linoone-galar"))
        case "282":
            if mega:
                dex.append(get_response(i, "gardevoir-mega"))
        case "302":
            if mega:
                dex.append(get_response(i, "sableye-mega"))
        case "303":
            if mega:
                dex.append(get_response(i, "mawile-mega"))
        case "306":
            if mega:
                dex.append(get_response(i, "aggron-mega"))
        case "308":
            if mega:
                dex.append(get_response(i, "medicham-mega"))
        case "310":
            if mega:
                dex.append(get_response(i, "manectric-mega"))
        case "319":
            if mega:
                dex.append(get_response(i, "sharpedo-mega"))
        case "323":
            if mega:
                dex.append(get_response(i, "camerupt-mega"))
        case "334":
            if mega:
                dex.append(get_response(i, "altaria-mega"))
        case "351":
            if alt:
                dex.append(get_response(i, "castform-sunny"))
                dex.append(get_response(i, "castform-rainy"))
                dex.append(get_response(i, "castform-snowy"))
        case "354":
            if mega:
                dex.append(get_response(i, "banette-mega"))
        case "359":
            if mega:
                dex.append(get_response(i, "absol-mega"))
        case "362":
            if mega:
                dex.append(get_response(i, "glalie-mega"))
        case "373":
            if mega:
                dex.append(get_response(i, "salamence-mega"))
        case "376":
            if mega:
                dex.append(get_response(i, "metagross-mega"))
        case "380":
            if mega:
                dex.append(get_response(i, "latias-mega"))
        case "381":
            if mega:
                dex.append(get_response(i, "latios-mega"))
        case "382":
            if primal:
                dex.append(get_response(i, "kyogre-primal"))
        case "383":
            if primal:
                dex.append(get_response(i, "groudon-primal"))
        case "384":
            if mega:
                dex.append(get_response(i, "rayquaza-mega"))
        case "384":
            if mega:
                dex.append(get_response(i, "rayquaza-mega"))
        case "386":
            if alt:
                dex.append(get_response(i, "deoxys-attack"))
                dex.append(get_response(i, "deoxys-defense"))
                dex.append(get_response(i, "deoxys-speed"))

        # case "412":
        #     if aesthetic:
        #         dex.append(get_response(i, "burmy-sandy"))
        #         dex.append(get_response(i, "burmy-trash"))
        case "413":
            if alt:
                dex.append(get_response(i, "wormadam-sandy"))
                dex.append(get_response(i, "wormadam-trash"))
        # case "421":
        #     if aesthetic:
        #         dex.append(get_response(i, "cherrim-sunshine"))
        # case "422":
        #     if aesthetic:
        #         dex.append(get_response(i, "shellos-east"))
        # case "423":
        #     if aesthetic:
        #         dex.append(get_response(i, "gastrodon-east"))
        case "428":
            if mega:
                dex.append(get_response(i, "lopunny-mega"))
        case "445":
            if mega:
                dex.append(get_response(i, "garchomp-mega"))
        case "448":
            if mega:
                dex.append(get_response(i, "lucario-mega"))
        case "460":
            if mega:
                dex.append(get_response(i, "abomasnow-mega"))
        case "475":
            if mega:
                dex.append(get_response(i, "gallade-mega"))
        case "479":
            if alt:
                dex.append(get_response(i, "rotom-heat"))
                dex.append(get_response(i, "rotom-wash"))
                dex.append(get_response(i, "rotom-frost"))
                dex.append(get_response(i, "rotom-fan"))
                dex.append(get_response(i, "rotom-mow"))
        case "483":
            if alt:
                dex.append(get_response(i, "dialga-origin"))
        case "484":
            if alt:
                dex.append(get_response(i, "palkia-origin"))
        case "487":
            if alt:
                dex.append(get_response(i, "giratina-origin"))
        case "492":
            if alt:
                dex.append(get_response(i, "shaymin-sky"))
        # case "493":
        #     if alt:
        #         dex.append(get_response(i, "arceus-bug"))
        #         dex.append(get_response(i, "arceus-dark"))
        #         dex.append(get_response(i, "arceus-dragon"))
        #         dex.append(get_response(i, "arceus-electric"))
        #         dex.append(get_response(i, "arceus-fighting"))
        #         dex.append(get_response(i, "arceus-fire"))
        #         dex.append(get_response(i, "arceus-flying"))
        #         dex.append(get_response(i, "arceus-ghost"))
        #         dex.append(get_response(i, "arceus-grass"))
        #         dex.append(get_response(i, "arceus-ground"))
        #         dex.append(get_response(i, "arceus-ice"))
        #         dex.append(get_response(i, "arceus-poison"))
        #         dex.append(get_response(i, "arceus-psychic"))
        #         dex.append(get_response(i, "arceus-rock"))
        #         dex.append(get_response(i, "arceus-steel"))
        #         dex.append(get_response(i, "arceus-water"))
        #         dex.append(get_response(i, "arceus-fairy"))

        case "502":
            if regional:
                dex.append(get_response(i, "samurott-hisui"))
        case "531":
            if mega:
                dex.append(get_response(i, "audino-mega"))
        case "549":
            if regional:
                dex.append(get_response(i, "lilligant-hisui"))
        case "550":
            if alt:
                dex.append(get_response(i, "basculin-blue-striped"))
            if regional:
                dex.append(get_response(i, "basculin-white-striped"))
        case "554":
            if regional:
                dex.append(get_response(i, "darumaka-galar"))
        case "555":
            if alt:
                dex.append(get_response(i, "darmanitan-zen"))
            if regional:
                dex.append(get_response(i, "darmanitan-galar-standard"))
            if alt and regional:
                dex.append(get_response(i, "darmanitan-galar-zen"))
        case "562":
            if regional:
                dex.append(get_response(i, "yamask-galar"))
        case "569":
            if gmax:
                dex.append(get_response(i, "garbodor-gmax"))
        case "570":
            if regional:
                dex.append(get_response(i, "zorua-hisui"))
        case "571":
            if regional:
                dex.append(get_response(i, "zoroark-hisui"))
        # case "585":
        #     if aesthetic:
        #         dex.append(get_response(i, "deerling-summer"))
        #         dex.append(get_response(i, "deerling-autumn"))
        #         dex.append(get_response(i, "deerling-winter"))
        # case "586":
        #     if aesthetic:
        #         dex.append(get_response(i, "sawsbuck-summer"))
        #         dex.append(get_response(i, "sawsbuck-autumn"))
        #         dex.append(get_response(i, "sawsbuck-winter"))
        case "618":
            if regional:
                dex.append(get_response(i, "stunfisk-galar"))
        case "628":
            if regional:
                dex.append(get_response(i, "braviary-hisui"))
        case "641":
            if alt:
                dex.append(get_response(i, "tornadus-therian"))
        case "642":
            if alt:
                dex.append(get_response(i, "thundurus-therian"))
        case "645":
            if alt:
                dex.append(get_response(i, "landorus-therian"))
        case "646":
            if alt:
                dex.append(get_response(i, "kyurem-white"))
                dex.append(get_response(i, "kyurem-black"))
        case "647":
            if aesthetic:
                dex.append(get_response(i, "keldeo-resolute"))
        case "648":
            if alt:
                dex.append(get_response(i, "meloetta-pirouette"))
        # case "649":
        #     if aesthetic:
        #         dex.append(get_response(i, "genesect-douse"))
        #         dex.append(get_response(i, "genesect-shock"))
        #         dex.append(get_response(i, "genesect-burn"))
        #         dex.append(get_response(i, "genesect-chill"))

        case "658":
            if unique:
                dex.append(get_response(i, "greninja-battle-bond"))
            if ash:
                dex.append(get_response(i, "greninja-ash"))
        # case "666":
        #     if aesthetic:
        #         dex.append(get_response(i, "vivillon-icy-snow"))
        #         dex.append(get_response(i, "vivillon-polar"))
        #         dex.append(get_response(i, "vivillon-tundra"))
        #         dex.append(get_response(i, "vivillon-continental"))
        #         dex.append(get_response(i, "vivillon-garden"))
        #         dex.append(get_response(i, "vivillon-elegant"))
        #         dex.append(get_response(i, "vivillon-modern"))
        #         dex.append(get_response(i, "vivillon-marine"))
        #         dex.append(get_response(i, "vivillon-archipelago"))
        #         dex.append(get_response(i, "vivillon-high-plains"))
        #         dex.append(get_response(i, "vivillon-sandstorm"))
        #         dex.append(get_response(i, "vivillon-river"))
        #         dex.append(get_response(i, "vivillon-monsoon"))
        #         dex.append(get_response(i, "vivillon-savanna"))
        #         dex.append(get_response(i, "vivillon-sun"))
        #         dex.append(get_response(i, "vivillon-ocean"))
        #         dex.append(get_response(i, "vivillon-jungle"))
        #         dex.append(get_response(i, "vivillon-fancy"))
        #         dex.append(get_response(i, "vivillon-poke-ball"))
        # case "669":
        #     if aesthetic:
        #         dex.append(get_response(i, "flabebe-yellow"))
        #         dex.append(get_response(i, "flabebe-orange"))
        #         dex.append(get_response(i, "flabebe-blue"))
        #         dex.append(get_response(i, "flabebe-white"))
        case "670":
            # if aesthetic:
            #     dex.append(get_response(i, "floette-yellow"))
            #     dex.append(get_response(i, "floette-orange"))
            #     dex.append(get_response(i, "floette-blue"))
            #     dex.append(get_response(i, "floette-white"))
            if unique:
                dex.append(get_response(i, "floette-eternal"))
        # case "671":
        #     if aesthetic:
        #         dex.append(get_response(i, "florges-yellow"))
        #         dex.append(get_response(i, "florges-orange"))
        #         dex.append(get_response(i, "florges-blue"))
        #         dex.append(get_response(i, "florges-white"))
        # case "676":
        #     if aesthetic:
        #         dex.append(get_response(i, "furfrou-heart"))
        #         dex.append(get_response(i, "furfrou-star"))
        #         dex.append(get_response(i, "furfrou-diamond"))
        #         dex.append(get_response(i, "furfrou-debutante"))
        #         dex.append(get_response(i, "furfrou-matron"))
        #         dex.append(get_response(i, "furfrou-dandy"))
        #         dex.append(get_response(i, "furfrou-la-reine"))
        #         dex.append(get_response(i, "furfrou-kabuki"))
        #         dex.append(get_response(i, "furfrou-pharaoh"))
        case "678":
            if gender:
                dex.append(get_response(i, "meowstic-female"))
        case "681":
            if alt:
                dex.append(get_response(i, "aegislash-blade"))
        case "705":
            if regional:
                dex.append(get_response(i, "sliggoo-hisui"))
        case "706":
            if regional:
                dex.append(get_response(i, "goodra-hisui"))
        case "710":
            if alt:
                dex.append(get_response(i, "pumpkaboo-small"))
                dex.append(get_response(i, "pumpkaboo-large"))
                dex.append(get_response(i, "pumpkaboo-super"))
        case "711":
            if alt:
                dex.append(get_response(i, "gourgeist-small"))
                dex.append(get_response(i, "gourgeist-large"))
                dex.append(get_response(i, "gourgeist-super"))
        case "713":
            if regional:
                dex.append(get_response(i, "avalugg-hisui"))
        # case "716":
        #     if aesthetic:
        #         dex.append(get_response(i, "xerneas-neutral"))
        case "718":
            if alt:
                dex.append(get_response(i, "zygarde-10"))
                dex.append(get_response(i, "zygarde-50-power-construct"))
                dex.append(get_response(i, "zygarde-10-power-construct"))
                dex.append(get_response(i, "zygarde-complete"))
        case "719":
            if mega:
                dex.append(get_response(i, "diancie-mega"))
        case "720":
            if alt:
                dex.append(get_response(i, "hoopa-unbound"))

        case "724":
            if regional:
                dex.append(get_response(i, "decidueye-hisui"))
        case "735":
            if totem:
                dex.append(get_response(i, "gumshoos-totem"))
        case "738":
            if totem:
                dex.append(get_response(i, "vikavolt-totem"))
        case "741":
            if alt:
                dex.append(get_response(i, "oricorio-pom-pom"))
                dex.append(get_response(i, "oricorio-pau"))
                dex.append(get_response(i, "oricorio-sensu"))
        case "743":
            if totem:
                dex.append(get_response(i, "ribombee-totem"))
        case "744":
            if unique:
                dex.append(get_response(i, "rockruff-own-tempo"))
        case "745":
            if alt:
                dex.append(get_response(i, "lycanroc-midnight"))
                dex.append(get_response(i, "lycanroc-dusk"))
        case "746":
            if alt:
                dex.append(get_response(i, "wishiwashi-school"))
        case "752":
            if totem:
                dex.append(get_response(i, "araquanid-totem"))
        case "754":
            if totem:
                dex.append(get_response(i, "lurantis-totem"))
        case "758":
            if totem:
                dex.append(get_response(i, "salazzle-totem"))
        # case "773":
        #     if alt:
        #         dex.append(get_response(i, "silvally-fighting"))
        #         dex.append(get_response(i, "silvally-flying"))
        #         dex.append(get_response(i, "silvally-poison"))
        #         dex.append(get_response(i, "silvally-ground"))
        #         dex.append(get_response(i, "silvally-rock"))
        #         dex.append(get_response(i, "silvally-bug"))
        #         dex.append(get_response(i, "silvally-ghost"))
        #         dex.append(get_response(i, "silvally-steel"))
        #         dex.append(get_response(i, "silvally-fire"))
        #         dex.append(get_response(i, "silvally-water"))
        #         dex.append(get_response(i, "silvally-grass"))
        #         dex.append(get_response(i, "silvally-electric"))
        #         dex.append(get_response(i, "silvally-psychic"))
        #         dex.append(get_response(i, "silvally-ice"))
        #         dex.append(get_response(i, "silvally-dragon"))
        #         dex.append(get_response(i, "silvally-dark"))
        #         dex.append(get_response(i, "silvally-fairy"))
        case "774":
            # if aesthetic:
            #     dex.append(get_response(i, "minior-orange-meteor"))
            #     dex.append(get_response(i, "minior-yellow-meteor"))
            #     dex.append(get_response(i, "minior-green-meteor"))
            #     dex.append(get_response(i, "minior-blue-meteor"))
            #     dex.append(get_response(i, "minior-indigo-meteor"))
            #     dex.append(get_response(i, "minior-violet-meteor"))
            if alt:
                dex.append(get_response(i, "minior-red"))
            # if aesthetic and alt:
            #     dex.append(get_response(i, "minior-orange"))
            #     dex.append(get_response(i, "minior-yellow"))
            #     dex.append(get_response(i, "minior-green"))
            #     dex.append(get_response(i, "minior-blue"))
            #     dex.append(get_response(i, "minior-indigo"))
            #     dex.append(get_response(i, "minior-violet"))
        case "777":
            if totem:
                dex.append(get_response(i, "togedemaru-totem"))
        case "778":
            if disguise:
                dex.append(get_response(i, "mimikyu-busted"))
            if totem:
                dex.append(get_response(i, "mimikyu-totem-disguised"))
            if totem and disguise:
                dex.append(get_response(i, "mimikyu-totem-busted"))
        case "784":
            if totem:
                dex.append(get_response(i, "kommo-o-totem"))
        case "800":
            if alt:
                dex.append(get_response(i, "necrozma-dusk"))
                dex.append(get_response(i, "necrozma-dawn"))
                dex.append(get_response(i, "necrozma-ultra"))
        case "801":
            if aesthetic:
                dex.append(get_response(i, "magearna-original"))
        case "809":
            if gmax:
                dex.append(get_response(i, "melmetal-gmax"))

        case "812":
            if gmax:
                dex.append(get_response(i, "rillaboom-gmax"))
        case "815":
            if gmax:
                dex.append(get_response(i, "cinderace-gmax"))
        case "818":
            if gmax:
                dex.append(get_response(i, "inteleon-gmax"))
        case "823":
            if gmax:
                dex.append(get_response(i, "corviknight-gmax"))
        case "826":
            if gmax:
                dex.append(get_response(i, "orbeetle-gmax"))
        case "834":
            if gmax:
                dex.append(get_response(i, "drednaw-gmax"))
        case "839":
            if gmax:
                dex.append(get_response(i, "coalossal-gmax"))
        case "841":
            if gmax:
                dex.append(get_response(i, "flapple-gmax"))
        case "842":
            if gmax:
                dex.append(get_response(i, "appletun-gmax"))
        case "844":
            if gmax:
                dex.append(get_response(i, "sandaconda-gmax"))
        case "845":
            if alt:
                dex.append(get_response(i, "cramorant-gulping"))
                dex.append(get_response(i, "cramorant-gorging"))
        case "849":
            if alt:
                dex.append(get_response(i, "toxtricity-low-key"))
            if gmax:
                dex.append(get_response(i, "toxtricity-amped-gmax"))
            # if alt and gmax:
            #     dex.append(get_response(i, "toxtricity-low-key-gmax"))
        case "851":
            if gmax:
                dex.append(get_response(i, "centiskorch-gmax"))
        # case "854":
        #     if aesthetic:
        #         dex.append(get_response(i, "sinistea-antique"))
        # case "855":
        #     if aesthetic:
        #         dex.append(get_response(i, "polteageist-antique"))
        case "858":
            if gmax:
                dex.append(get_response(i, "hatterene-gmax"))
        case "861":
            if gmax:
                dex.append(get_response(i, "grimmsnarl-gmax"))
        case "869":
            # if aesthetic:
            #     dex.append(get_response(i, "alcremie-ruby-cream"))
            #     dex.append(get_response(i, "alcremie-matcha-cream"))
            #     dex.append(get_response(i, "alcremie-mint-cream"))
            #     dex.append(get_response(i, "alcremie-lemon-cream"))
            #     dex.append(get_response(i, "alcremie-salted-cream"))
            #     dex.append(get_response(i, "alcremie-ruby-swirl"))
            #     dex.append(get_response(i, "alcremie-caramel-swirl"))
            #     dex.append(get_response(i, "alcremie-rainbow-swirl"))
            if gmax:
                dex.append(get_response(i, "alcremie-gmax"))
        case "875":
            if alt:
                dex.append(get_response(i, "eiscue-noice"))
        case "876":
            if gender:
                dex.append(get_response(i, "indeedee-female"))
        case "877":
            if alt:
                dex.append(get_response(i, "morpeko-hangry"))
        case "879":
            if gmax:
                dex.append(get_response(i, "copperajah-gmax"))
        case "884":
            if gmax:
                dex.append(get_response(i, "duraludon-gmax"))
        case "888":
            if alt:
                dex.append(get_response(i, "zacian-crowned"))
        case "889":
            if alt:
                dex.append(get_response(i, "zamazenta-crowned"))
        case "875":
            if eternamax:
                dex.append(get_response(i, "eternatus-eternamax"))
        case "892":
            if alt:
                dex.append(get_response(i, "urshifu-rapid-strike"))
            if gmax:
                dex.append(get_response(i, "urshifu-single-strike-gmax"))
            if alt and gmax:
                dex.append(get_response(i, "urshifu-rapid-strike-gmax"))
        case "893":
            if aesthetic:
                dex.append(get_response(i, "zarude-dada"))
        case "898":
            if alt:
                dex.append(get_response(i, "calyrex-ice"))
                dex.append(get_response(i, "calyrex-shadow"))
        case "902":
            if gender:
                dex.append(get_response(i, "basculegion-female"))
        case "905":
            if alt:
                dex.append(get_response(i, "enamorus-therian"))

        case "916":
            if gender:
                dex.append(get_response(i, "oinkologne-female"))
        case "925":
            if aesthetic:
                dex.append(get_response(i, "maushold-family-of-three"))
        case "931":
            if alt:
                dex.append(get_response(i, "squawkabilly-blue-plumage"))
                dex.append(get_response(i, "squawkabilly-yellow-plumage"))
                dex.append(get_response(i, "squawkabilly-white-plumage"))
        case "964":
            if alt:
                dex.append(get_response(i, "palafin-hero"))
        case "978":
            if aesthetic:
                dex.append(get_response(i, "tatsugiri-droopy"))
                dex.append(get_response(i, "tatsugiri-stretchy"))
        case "982":
            if aesthetic:
                dex.append(get_response(i, "dudunsparce-three-segment"))
        case "999":
            if alt:
                dex.append(get_response(i, "gimmighoul-roaming"))
        case "1007":
            if mounts:
                dex.append(get_response(i, "koraidon-limited-build"))
                dex.append(get_response(i, "koraidon-sprinting-build"))
                dex.append(get_response(i, "koraidon-swimming-build"))
                dex.append(get_response(i, "koraidon-gliding-build"))
        case "1008":
            if mounts:
                dex.append(get_response(i, "miraidon-low-power-mode"))
                dex.append(get_response(i, "miraidon-drive-mode"))
                dex.append(get_response(i, "miraidon-aquatic-mode"))
                dex.append(get_response(i, "miraidon-glide-mode"))

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
    forms["mounts"] = True

    return forms


def set_all_false(forms):
    forms["forms"] = False
    forms["aesthetic only"] = False
    forms["gender-based"] = False
    forms["regional variant"] = False
    forms["mega evolution"] = False
    forms["primal"] = False
    forms["gigantamax"] = False
    forms["unique"] = False
    forms["totem"] = False
    forms["partner"] = False
    forms["cosplay pikachu"] = False
    forms["pikachu in a cap"] = False
    forms["ash greninja"] = False
    forms["disguise"] = False
    forms["eternamax"] = False
    forms["mounts"] = False

    return forms


def get_response(index, name):
    base_url = 'https://pokeapi.co/api/v2/pokemon/'

    response = requests.get(base_url + name + '/')
    entry = json.loads(response.text)
    entry["id"] = index
    # dex.append(entry)
    return entry
