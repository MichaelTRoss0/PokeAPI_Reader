# TODO: Rewrite functions to work with or without forms.
def parse_and_write_info(filename, dex, all_forms):
    file = open(filename, 'w')

    i = 0
    print("Parsing and writing data into simpler form...")
    for entry in dex:
        order = entry["id"]
        name = parse_name(entry["name"], all_forms)
        types = parse_types(entry["types"])
        abilities = parse_abilities(entry["abilities"])
        stats = parse_stats(entry["stats"])

        write_info(name, order, types, abilities, stats, file)
        i += 1
        print("Parsed and wrote data for Pokémon #" + str(i))

    file.close()
    print("Parsing and writing data complete!")


def parse_name(raw_name, all_forms):
    name = raw_name.replace("-", " ")
    name = name.title()
    match name:
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

        case "Deoxys Normal":
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
            name = "Flabébé"
        case "Meowstic Male":
            name = "Meowstic"
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
        case "Indeedee Male":
            name = "Indeedee"
        case "Morpeko Full Belly":
            name = "Morpeko"
        case "Urshifu Single Strike":
            name = "Urshifu"
        case "Basculegion Male":
            name = "Basculegion"
        case "Enamorus Incarnate":
            name = "Enamorus"
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
    info1 = "{:>4} || {:>12} ||"\
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
