import reader


def parse_and_write_info(filename, dex, forms):
    file = open(filename, 'w')

    i = 0
    print("Parsing and writing data into simpler form...")
    for entry in dex:
        order = entry["id"]
        name = parse_name(entry["name"], forms)
        types = parse_types(entry["types"])
        abilities = parse_abilities(entry["abilities"])
        stats = parse_stats(entry["stats"])

        write_info(name, order, types, abilities, stats, file)
        i += 1
        print("Parsed and wrote data for Pokémon #" + str(i))

    file.close()
    print("Parsing and writing data complete!")


def parse_name(raw_name, forms):
    if forms["all"]:
        forms = reader.set_all_true(forms)
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

    name = raw_name.replace("-", " ")
    name = name.title()
    match name:
        # Names with special characters
        case "Farfetchd":
            name = "Farfetch'd"
        case "Mr Mime":
            name = "Mr. Mime"
        case "Mime Jr":
            name = "Mime Jr."
        case "Mr Rime":
            name = "Mr. Rime"
        case "Ho Oh":
            name = "Ho-Oh"
        case "Porygon Z":
            name = "Porygon-Z"
        case "Type Null":
            name = "Type: Null"
        case "Jangmo O":
            name = "Jangmo-o"
        case "Hakamo O":
            name = "Hakamo-o"
        case "Kommo O":
            name = "Kommo-o"
        case "Ting Lu":
            name = "Ting-Lu"
        case "Chien Pao":
            name = "Chien-Pao"
        case "Wo Chien":
            name = "Wo-Chien"
        case "Chi Yu":
            name = "Chi-Yu"

        # Gendered Forms
        case "Meowstic Male":
            name = "Meowstic"
        case "Indeedee Male":
            name = "Indeedee"
        case "Basculegion Male":
            name = "Basculegion"

        # Pokémon with alternate forms
        case "Deoxys Normal":
            if not alt:
                name = "Deoxys"
        case "Wormadam Plant":
            name = "Wormadam"
        case "Giratina Altered":
            name = "Giratina"
        case "Shaymin Land":
            name = "Shaymin"
        case "Basculin Red Striped":
            name = "Basculin"
        case "Darmanitan Standard":
            name = "Darmanitan"
        case "Tornadus Incarnate":
            name = "Tornadus"
        case "Thundurus Incarnate":
            name = "Thundurus"
        case "Landorus Incarnate":
            name = "Landorus"
        case "Keldeo Ordinary":
            name = "Keldeo"
        case "Meloetta Aria":
            name = "Meloetta"
        case "Flabebe":
            if not aesthetic:
                name = "Flabébé"
            else:
                name = "Red Flower Flabébé"
        case "Aegislash Shield":
            name = "Aegislash"
        case "Pumpkaboo Average":
            name = "Pumpkaboo"
        case "Gourgeist Average":
            name = "Gourgeist"
        case "Zygarde 50":
            name = "Zygarde"
        case "Oricorio Baile":
            name = "Oricorio"
        case "Lycanroc Midday":
            name = "Lycanroc"
        case "Wishiwashi Solo":
            name = "Wishiwashi"
        case "Minior Red Meteor":
            name = "Minior"
        case "Mimikyu Disguised":
            name = "Mimikyu"
        case "Toxtricity Amped":
            name = "Toxtricity"
        case "Morpeko Full Belly":
            name = "Morpeko"
        case "Urshifu Single Strike":
            name = "Urshifu"
        case "Enamorus Incarnate":
            name = "Enamorus"

        # Alolan Forms
        case "Rattata Alola":
            name = "Alolan Rattata"
        case "Raticate Alola":
            name = "Alolan Raticate"
        case "Raichu Alola":
            name = "Alolan Raichu"
        case "Sandshrew Alola":
            name = "Alolan Sandshrew"
        case "Sandslash Alola":
            name = "Alolan Sandshrew"
        case "Vulpix Alola":
            name = "Alolan Vulpix"
        case "Ninetales Alola":
            name = "Alolan Ninetales"
        case "Diglett Alola":
            name = "Alolan Diglett"
        case "Dugtrio Alola":
            name = "Alolan Dugtrio"
        case "Meowth Alola":
            name = "Alolan Meowth"
        case "Persian Alola":
            name = "Alolan Persian"
        case "Geodude Alola":
            name = "Alolan Geodude"
        case "Graveler Alola":
            name = "Alolan Graveler"
        case "Golem Alola":
            name = "Alolan Golem"
        case "Grimer Alola":
            name = "Alolan Grimer"
        case "Muk Alola":
            name = "Alolan Muk"
        case "Exeggutor Alola":
            name = "Alolan Exeggutor"
        case "Marowak Alola":
            name = "Alolan Marowak"

        # Galarian Forms
        case "Meowth Galar":
            name = "Galarian Meowth"
        case "Ponyta Galar":
            name = "Galarian Ponyta"
        case "Rapidash Galar":
            name = "Galarian Rapidash"
        case "Slowpoke Galar":
            name = "Galarian Slowpoke"
        case "Slowbro Galar":
            name = "Galarian Slowbro"
        case "Farfetchd Galar":
            name = "Galarian Farfetch'd"
        case "Weezing Galar":
            name = "Galarian Weezing"
        case "Mr Mime Galar":
            name = "Galarian Mr. Mime"
        case "Articuno Galar":
            name = "Galarian Articuno"
        case "Zapdos Galar":
            name = "Galarian Zapdos"
        case "Moltres Galar":
            name = "Galarian Moltres"
        case "Slowbro Galar":
            name = "Galarian Slowbro"
        case "Corsola Galar":
            name = "Galarian Corsola"
        case "Zigzagoon Galar":
            name = "Galarian Zigzagoon"
        case "Linoone Galar":
            name = "Galarian Linoone"
        case "Darumaka Galar":
            name = "Galarian Darumaka"
        case "Darmanitan Galar":
            name = "Galarian Darmanitan"
        case "Darmanitan Galar Zen":
            name = "Galarian Zen Mode Darmanitan"
        case "Yamask Galar":
            name = "Galarian Yamask"
        case "Stunfisk Galar":
            name = "Galarian Stunfisk"

        # Hisuian Forms
        case "Growlithe Hisui":
            name = "Hisuian Growlithe"
        case "Arcanine Hisui":
            name = "hisuian Growlithe"
        case "Voltorb Hisui":
            name = "Hisuian Voltorb"
        case "Electrode":
            name = "Hisuian Electrode"
        case "Typhlosion Hisui":
            name = "Hisuian Typhlosion"
        case "Qwilfish Hisui":
            name = "Hisuian Qwilfish"
        case "Sneasel Hisui":
            name = "Hisuian Sneasel"
        case "Samurott Hisui":
            name = "Hisuian Samurott"
        case "Lilligant Hisui":
            name = "Hisuian Lilligant"
        case "Basculin White Striped":
            name = "White-Striped Basculin"
        case "Zorua Hisui":
            name = "Hisuian Zorua"
        case "Zoraork Hisui":
            name = "Hisuian Zoroark"
        case "Braviary Hisui":
            name = "Hisuian Braviary"
        case "Sliggoo Hisui":
            name = "Hisuian Sliggoo"
        case "Goodra Hisui":
            name = "Hisuian Goodra"
        case "Avalugg Hisui":
            name = "Hisuian Avalugg"
        case "Decidueye Hisui":
            name = "Hisuian Decidueye"

        # Paldean Forms
        case "Tauros Paldea Combat Breed":
            name = "Combat Breed Paldean Tauros"
        case "Tauros Paldea Blaze Breed":
            name = "Blaze Breed Paldean Tauros"
        case "Tauros Paldea Aqua Breed":
            name = "Aqua Breed Paldean Tauros"
        case "Wooper Paldea":
            name = "Paldean Wooper"

        # Mega Pokémon
        case "Venusaur Mega":
            name = "Mega Venusaur"
        case "Charizard Mega X":
            name = "Mega Charizard X"
        case "Charizard Mega Y":
            name = "Mega Charizard Y"
        case "Blastoise Mega":
            name = "Mega Blastoise"
        case "Beedrill Mega":
            name = "Mega Beedrill"
        case "Pidgeot Mega":
            name = "Mega Pidgeot"

        # Gigantamax Pokémon
        case "Venusaur Gmax":
            name = "Gigantamax Venusaur"
        case "Charizard Gmax":
            name = "Gigantamax Charizard"
        case "Blastoise Gmax":
            name = "Gigantamax Blastoise"
        case "Butterfree Gmax":
            name = "Gigantamax Butterfree"
        case "Pikachu Gmax":
            name = "Gigantamax Pikachu"

        # Totem Pokémon
        case "Raticate Totem Alola":
            name = "Totem Alolan Raticate"

        # Partner Pokémon
        case "Pikachu Starter":
            name = "Partner Pikachu"
        case "Eevee Starter":
            name = "Partner Eevee"

        # Cosplay Pikachu
        case "Pikachu Cosplay":
            name = "Cosplay Pikachu"
        case "Pikachu Phd":
            name = "Pikachu, Ph.D."

        # Pikachu in a Cap
        case "Pikachu Original Cap":
            name = "Original Cap Pikachu"
        case "Pikachu Hoenn Cap":
            name = "Hoenn Cap Pikachu"
        case "Pikachu Sinnoh Cap":
            name = "Sinnoh Cap Pikachu"
        case "Pikachu Unova Cap":
            name = "Unova Cap Pikachu"
        case "Pikachu Kalos Cap":
            name = "Kalos Cap Pikachu"
        case "Pikachu Alola Cap":
            name = "Alola Cap Pikachu"
        case "Pikachu Partner Cap":
            name = "Partner Cap Pikachu"
        case "Pikachu World Cap":
            name = "World Cap Pikachu"

        # Template
        case "case":
            name = "name"
    return name


def parse_types(types_info):
    types = ["none", "none"]
    for listed_type in types_info:
        pokemon_type = listed_type["type"]
        name = pokemon_type["name"]
        name = name.title()
        slot = listed_type["slot"] - 1
        types[slot] = name
    return types


def parse_abilities(ability_info):
    abilities = ["none", "none", "none"]
    for listed_ability in ability_info:
        pokemon_ability = listed_ability["ability"]
        name = pokemon_ability["name"]
        name = name.replace("-", " ")
        name = name.title()
        name = name.replace("Soul Heart", "Soul-Heart")
        name = name.replace("Well Baked Body", "Well-Baked Body")
        slot = listed_ability["slot"] - 1
        abilities[slot] = name
    return abilities


def parse_stats(stats_info):
    stats = [0, 0, 0, 0, 0, 0]
    for listed_stat in stats_info:
        stat = listed_stat["stat"]
        name = stat["name"]
        base_stat = listed_stat["base_stat"]
        match name:
            case "hp":
                stats[0] = base_stat
            case "attack":
                stats[1] = base_stat
            case "defense":
                stats[2] = base_stat
            case "special-attack":
                stats[3] = base_stat
            case "special-defense":
                stats[4] = base_stat
            case "speed":
                stats[5] = base_stat
            case _:
                raise ValueError(name + " was not  expected here.")
    return stats


def write_info(name, id_number, types, abilities, stats, file):
    info1 = "{:>4} || {:>30} ||"\
        .format(id_number, name)
    if types[1] != "none":
        info2 = " {:>8}/{:<8} ||"\
            .format(types[0], types[1])
    else:
        info2 = " {:>8}          ||"\
            .format(types[0])
    info3 = " {:>16}, {:>16}, {:>16} ||"\
        .format(abilities[0], abilities[1], abilities[2])
    info4 = " {:>3}, {:>3}, {:>3}, {:>3}, {:>3}, {:>3}\n"\
        .format(stats[0], stats[1], stats[2],
                stats[3], stats[4], stats[5])
    info_line = info1 + info2 + info3 + info4

    file.write(info_line)
