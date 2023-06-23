import reader


def parse_and_write_info(filename, dex, forms):
    file = open(filename, 'w', encoding="utf-8")

    # i = 0
    print("Parsing and writing data into simpler form...")
    for entry in dex:
        order = entry["id"]
        name = parse_name(entry["name"], forms)
        types = parse_types(entry["types"])
        abilities = parse_abilities(entry["abilities"])
        stats = parse_stats(entry["stats"])

        write_info(name, order, types, abilities, stats, file)
        # i += 1
        print("Parsed and wrote data for Pokémon #" + str(order))

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
            if gender:
                name = "Male Meowstic"
            else:
                name = "Meowstic"
        case "Meowstic Female":
            name = "Female Meowstic"
        case "Indeedee Male":
            if gender:
                name = "Male Indeedee"
            else:
                name = "Indeedee"
        case "Indeedee Female":
            name = "Female Indeedee"
        case "Basculegion Male":
            if gender:
                name = "Male Basculegion"
            else:
                name = "Basculegion"
        case "Basculegion Female":
            name = "Female Basculegion"
        case "Oinkologne":
            if gender:
                name = "Male Oinkologne"
        case "Oinkologne Female":
            name = "Female Oinkologne"

        # Pokémon with alternate forms
        # case "Unown":
        #     if aesthetic:
        #         name = "Unown A"
        # case "Unown Exclamation":
        #     name = "Unown !"
        # case "Unown Question":
        #     name = "Unown ?"
        case "Castform":
            if alt:
                name = "Normal Castform"
        case "Castform Sunny":
            name = "Sunny Form Castform"
        case "Castform Rainy":
            name = "Rainy Form Castform"
        case "Castform Snowy":
            name = "Snowy Form Castform"
        case "Deoxys Normal":
            if alt:
                name = "Normal Forme Deoxys"
            else:
                name = "Deoxys"
        case "Deoxys Attack":
            name = "Attack Forme Deoxys"
        case "Deoxys Defense":
            name = "Defense Forme Deoxys"
        case "Deoxys Speed":
            name = "Speed Forme Deoxys"
        # case "Burmy":
        #     if aesthetic:
        #         name = "Plant Cloak Burmy"
        # case "Burmy Sandy":
        #     name = "Sandy Cloak Burmy"
        # case "Burmy Trash":
        #     name = "Trash Cloak Burmy"
        case "Wormadam Plant":
            if alt:
                name = "Plant Cloak Wormadam"
            else:
                name = "Wormadam"
        case "Wormadam Sandy":
            name = "Sandy Cloak Wormadam"
        case "Wormadam Trash":
            name = "Trash Cloak Wormadam"
        # case "Cherrim":
        #     if aesthetic:
        #         name = "Overcast Form Cherrim"
        # case "Cherrim Sunshine":
        #     name = "Sunshine Form Cherrim"
        # case "Shellos":
        #     if aesthetic:
        #         name = "West Sea Shellos"
        #     else:
        #         name = "Shellos"
        # case "Shellos East":
        #     name = "East Sea Shellos"
        # case "Gastrodon":
        #     if aesthetic:
        #         name = "West Sea Gastrodon"
        #     else:
        #         name = "Gastrodon"
        # case "Gastrodon East":
        #     name = "East Sea Gastrodon"
        case "Rotom Heat":
            name = "Heat Rotom"
        case "Rotom Wash":
            name = "Wash Rotom"
        case "Rotom Frost":
            name = "Frost Rotom"
        case "Rotom Fan":
            name = "Fan Rotom"
        case "Rotom Mow":
            name = "Mow Rotom"
        case "Dialga Origin":
            name = "Origin Forme Dialga"
        case "Palkia Origin":
            name = "Origin Forme Palkia"
        case "Giratina Altered":
            if not alt:
                name = "Giratina"
            else:
                name = "Altered Forme Giratina"
        case "Giratina Origin":
            name = "Origin Forme Giratina"
        case "Shaymin Land":
            if alt:
                name = "Land Forme Shaymin"
            else:
                name = "Shaymin"
        case "Shaymin Sky":
            name = "Sky Forme Shaymin"
        # case "Arceus":
        #     if alt:
        #         name = "Normal-type Arceus"
        # case "Arceus Bug":
        #     name = "Bug-type Arceus"
        # case "Arceus Dark":
        #     name = "Dark-type Arceus"
        # case "Arceus Dragon":
        #     name = "Dragon-type Arceus"
        # case "Arceus Electric":
        #     name = "Electric-type Arceus"
        # case "Arceus Fighting":
        #     name = "Fighting-type Arceus"
        # case "Arceus Fire":
        #     name = "Fire-type Arceus"
        # case "Arceus Flying":
        #     name = "Flying-type Arceus"
        # case "Arceus Ghost":
        #     name = "Ghost-type Arceus"
        # case "Arceus Grass":
        #     name = "Grass-type Arceus"
        # case "Arceus Ground":
        #     name = "Ground-type Arceus"
        # case "Arceus Ice":
        #     name = "Ice-type Arceus"
        # case "Arceus Poison":
        #     name = "Poison-type Arceus"
        # case "Arceus Psychic":
        #     name = "Psychic-type Arceus"
        # case "Arceus Rock":
        #     name = "Rock-type Arceus"
        # case "Arceus Steel":
        #     name = "Steel-type Arceus"
        # case "Arceus Water":
        #     name = "Water-type Arceus"
        # case "Arceus Fairy":
        #     name = "Fairy-type Arceus"
        case "Basculin Red Striped":
            if alt:
                name = "Red-Striped Basculin"
            else:
                name = "Basculin"
        case "Basculin Blue Striped":
            name = "Blue-Striped Basculin"
        case "Darmanitan Standard":
            if alt:
                name = "Standard Mode Darmanitan"
            else:
                name = "Darmanitan"
        case "Darmanitan Zen":
            name = "Zen Mode Darmanitan"
        # case "Deerling":
        #     if aesthetic:
        #         name = "Spring Form Deerling"
        # case "Deerling Summer":
        #     name = "Summer Form Deerling"
        # case "Deerling Autumn":
        #     name = "Autumn Form Deerling"
        # case "Deerling Winter":
        #     name = "Winter Form Deerling"
        # case "Sawsbuck":
        #     if aesthetic:
        #         name = "Spring Form Sawsbuck"
        # case "Sawsbuck Summer":
        #     name = "Summer Form Sawsbuck"
        # case "Sawsbuck Autumn":
        #     name = "Autumn Form Sawsbuck"
        # case "Sawsbuck Winter":
        #     name = "Winter Form Sawsbuck"
        case "Tornadus Incarnate":
            if alt:
                name = "Incarnate Forme Tornadus"
            else:
                name = "Tornadus"
        case "Tornadus Therian":
            name = "Therian Forme Tornadus"
        case "Thundurus Incarnate":
            if alt:
                name = "Incarnate Forme Thundurus"
            else:
                name = "Thundurus"
        case "Thundurus Therian":
            name = "Therian Forme Thundurus"
        case "Landorus Incarnate":
            if alt:
                name = "Incarnate Forme Landorus"
            else:
                name = "Landorus"
        case "Landorus Therian":
            name = "Therian Forme Landorus"
        case "Kyurem White":
            name = "White Kyurem"
        case "Kyurem Black":
            name = "Black Kyurem"
        case "Keldeo Ordinary":
            if aesthetic:
                name = "Ordinary Form Keldeo"
            else:
                name = "Keldeo"
        case "Keldeo Resolute":
            name = "Resolute Form Keldeo"
        case "Meloetta Aria":
            if alt:
                name = "Aria Forme Meloetta"
            else:
                name = "Meloetta"
        case "Meloetta Pirouette":
            name = "Pirouette Forme Meloetta"
        # case "Genesect Douse":
        #     name = "Douse Drive Genesect"
        # case "Genesect Shock":
        #     name = "Shock Drive Genesect"
        # case "Genesect Burn":
        #     name = "Burn Drive Genesect"
        # case "Genesect Chill":
        #     name = "Chill Drive Genesect"
        # case "Vivillon":
        #     if aesthetic:
        #         name = "Meadow Pattern Vivillon"
        # case "Vivillon Icy Snow":
        #     name = "Icy Snow Pattern Vivillon"
        # case "Vivillon Polar":
        #     name = "Polar Pattern Vivillon"
        # case "Vivillon Tundra":
        #     name = "Tundra Pattern Vivillon"
        # case "Vivillon Continental":
        #     name = "Continental Pattern Vivillon"
        # case "Vivillon Garden":
        #     name = "Garden Pattern Vivillon"
        # case "Vivillon Elegant":
        #     name = "Elegant Pattern Vivillon"
        # case "Vivillon Modern":
        #     name = "Modern Pattern Vivillon"
        # case "Vivillon Marine":
        #     name = "Marine Pattern Vivillon"
        # case "Vivillon Archipelago":
        #     name = "Archipelago Pattern Vivillon"
        # case "Vivillon High Plains":
        #     name = "High Plains Pattern Vivillon"
        # case "Vivillon Sandstorm":
        #     name = "Sandstorm Pattern Vivillon"
        # case "Vivillon River":
        #     name = "River Pattern Vivillon"
        # case "Vivillon Monsoon":
        #     name = "Monsoon Pattern Vivillon"
        # case "Vivillon Savanna":
        #     name = "Savanna Pattern Vivillon"
        # case "Vivillon Sun":
        #     name = "Sun Pattern Vivillon"
        # case "Vivillon Ocean":
        #     name = "Ocean Pattern Vivillon"
        # case "Vivillon Jungle":
        #     name = "Jungle Pattern Vivillon"
        # case "Vivillon Fancy":
        #     name = "Fancy Pattern Vivillon"
        # case "Vivillon Poke Ball":
        #     name = "Poké Ball Pattern Vivillon"
        case "Flabebe":
            name = "Flabébé"
            # if aesthetic:
            #     name = "Red Flower Flabébé"
            # else:
            #     name = "Flabébé"
        # case "Flabebe Yellow":
        #     name = "Yellow Flower Flabébé"
        # case "Flabebe Orange":
        #     name = "Orange Flower Flabébé"
        # case "Flabebe Blue":
        #     name = "Blue Flower Flabébé"
        # case "Flabebe White":
        #     name = "White Flower Flabébé"
        # case "Floette":
        #     if aesthetic:
        #         name = "Red Flower Floette"
        #     else:
        #         name = "Floette"
        # case "Floette Yellow":
        #     name = "Yellow Flower Floette"
        # case "Floette Orange":
        #     name = "Orange Flower Floette"
        # case "Floette Blue":
        #     name = "Blue Flower Floette"
        # case "Floette White":
        #     name = "White Flower Floette"
        # case "Florges":
        #     if aesthetic:
        #         name = "Red Flower Florges"
        #     else:
        #         name = "Florges"
        # case "Florges Yellow":
        #     name = "Yellow Flower Florges"
        # case "Florges Orange":
        #     name = "Orange Flower Florges"
        # case "Florges Blue":
        #     name = "Blue Flower Florges"
        # case "Florges White":
        #     name = "White Flower Florges"
        # case "Furfrou":
        #     if aesthetic:
        #         name = "Furfrou Natural Form"
        #     else:
        #         name = "Furfrou"
        # case "Furfrou Heart":
        #     name = "Heart Trim Furfrou"
        # case "Furfrou Star":
        #     name = "Star Trim Furfrou"
        # case "Furfrou Diamond":
        #     name = "Diamond Trim Furfrou"
        # case "Furfrou Debutante":
        #     name = "Debutante Trim Furfrou"
        # case "Furfrou Matron":
        #     name = "Matron Trim Furfrou"
        # case "Furfrou Dandy":
        #     name = "Dandy Trim Furfrou"
        # case "Furfrou La Reine":
        #     name = "La Reine Trim Furfrou"
        # case "Furfrou Kabuki":
        #     name = "Kabuki Trim Furfrou"
        # case "Furfrou Pharaoh":
        #     name = "Pharaoh Trim Furfrou"
        case "Aegislash Shield":
            if alt:
                name = "Shield Forme Aegislash"
            else:
                name = "Aegislash"
        case "Aegislash Blade":
            name = "Blade Forme Aegislash"
        case "Pumpkaboo Average":
            if alt:
                name = "Average Size Pumpkaboo"
            else:
                name = "Pumpkaboo"
        case "Pumpkaboo Small":
            name = "Small Size Pumpkaboo"
        case "Pumpkaboo Large":
            name = "Large Size Pumpkaboo"
        case "Pumpkaboo Super":
            name = "Super Size Pumpkaboo"
        case "Gourgeist Average":
            if alt:
                name = "Average Size Gourgeist"
            else:
                name = "Gourgeist"
        case "Gourgeist Small":
            name = "Small Size Gourgeist"
        case "Gourgeist Large":
            name = "Large Size Gourgeist"
        case "Gourgeist Super":
            name = "Super Size Gourgeist"
        # case "Xerneas":
        #     if aesthetic:
        #         name = "Active Mode Xerneas"
        #     else:
        #         name = "Xerneas"
        # case "Xerneas Neutral":
        #     name = "Neutral Mode Xerneas"
        case "Zygarde 50":
            if alt:
                name = "Zygarde 50% Forme"
            else:
                name = "Zygarde"
        case "Zygarde 10":
            name = "Zygarde 10% Forme"
        case "Zygarde 50 Power Construct":
            name = "Power Construct Zygarde 50% Forme"
        case "Zygarde 10 Power Construct":
            name = "Power Construct Zygarde 10% Forme"
        case "Zygarde Complete":
            name = "Zygarde Complete Forme"
        case "Hoopa":
            if alt:
                name = "Hoopa Confined"
            else:
                name = "Hoopa"
        case "Oricorio Baile":
            if alt:
                name = "Baile Style Oricorio"
            else:
                name = "Oricorio"
        case "Oricorio Pom Pom":
            name = "Pom-Pom Style Oricorio"
        case "Oricorio Pau":
            name = "Pau Style Oricorio"
        case "Oricorio Sensu":
            name = "Sensu Style Oricorio"
        case "Lycanroc Midday":
            if alt:
                name = "Midday Form Lycanroc"
            else:
                name = "Lycanroc"
        case "Lycanroc Midnight":
            name = "Midnight Form Lycanroc"
        case "Lycanroc Dusk":
            name = "Dusk Form Lycanroc"
        case "Wishiwashi Solo":
            if alt:
                name = "Solo Form Wishiwashi"
            else:
                name = "Wishiwashi"
        case "Wishiwashi School":
            name = "School Form Wishiwashi"
        # case "Silvally":
        #     if alt:
        #         name = "Normal-type Silvally"
        # case "Silvally Fighting":
        #     name = "Fighting-type Silvally"
        # case "Silvally Flying":
        #     name = "Flying-type Silvally"
        # case "Silvally Poison":
        #     name = "Poison-type Silvally"
        # case "Silvally Ground":
        #     name = "Ground-type Silvally"
        # case "Silvally Rock":
        #     name = "Rock-type Silvally"
        # case "Silvally Bug":
        #     name = "Bug-type Silvally"
        # case "Silvally Ghost":
        #     name = "Ghost-type Silvally"
        # case "Silvally Steel":
        #     name = "Steel-type Silvally"
        # case "Silvally Fire":
        #     name = "Fire-type Silvally"
        # case "Silvally Water":
        #     name = "Water-type Silvally"
        # case "Silvally Grass":
        #     name = "Grass-type Silvally"
        # case "Silvally Electric":
        #     name = "Electric-type Silvally"
        # case "Silvally Psychic":
        #     name = "Psychic-type Silvally"
        # case "Silvally Ice":
        #     name = "Ice-type Silvally"
        # case "Silvally Dragon":
        #     name = "Dragon-type Silvally"
        # case "Silvally Dark":
        #     name = "Dark-type Silvally"
        # case "Silvally Fairy":
        #     name = "Fairy-type Silvally"
        case "Minior Red Meteor":
            if alt:
                name = "Meteor Form Minior"
            else:
                name = "Minior"
        case "Minior Red":
            name = "Core Form Minior"
            # if aesthetic:
            #     name = "Red Core Minior"
            # else:
            #     name = "Core Form Minior"
        # case "Minior Orange":
        #     name = "Orange Core Minior"
        # case "Minior Yellow":
        #     name = "Yellow Core Minior"
        # case "Minior Green":
        #     name = "Green Core Minior"
        # case "Minior Blue":
        #     name = "Blue Core Minior"
        # case "Minior Indigo":
        #     name = "Indigo Core Minior"
        # case "Minior Violet":
        #     name = "Violet Core Minior"
        case "Necrozma Dusk":
            name = "Dusk Mane Necrozma"
        case "Necrozma Dawn":
            name = "Dawn Wings Necrozma"
        case "Necrozma Ultra":
            name = "Ultra Necrozma"
        case "Magearna Original":
            name = "Original Color Magearna"
        case "Cramorant Gulping":
            name = "Gulping Form Cramorant"
        case "Cramorant Gorging":
            name = "Gorging Form Cramorant"
        case "Toxtricity Amped":
            if alt:
                name = "Amped Form Toxtricity"
            else:
                name = "Toxtricity"
        case "Toxtricity Low Key":
            name = "Low Key Form Toxtricity"
        case "Toxtricity Amped Gmax":
            name = "Gigantamax Toxtricity"
        # case "Sinistea":
        #     if aesthetic:
        #         name = "Phony Form Sinistea"
        # case "Sinistea Antique":
        #     name = "Antique Form Sinistea"
        # case "Polteageist":
        #     if aesthetic:
        #         name = "Phony Form Polteageist"
        # case "Polteageist Antique":
        #     name = "Antique Form Polteageist"
        # case "Alcremie":
        #     if aesthetic:
        #         name = "Vanilla Cream Alcremie"
        # case "Alcremie Ruby Cream":
        #     name = "Ruby Cream Alcremie"
        # case "Alcremie Matcha Cream":
        #     name = "Matcha Cream Alcremie"
        # case "Alcremie Mint Cream":
        #     name = "Mint Cream Alcremie"
        # case "Alcremie Lemon Cream":
        #     name = "Lemon Cream Alcremie"
        # case "Alcremie Salted Cream":
        #     name = "Salted Cream Alcremie"
        # case "Alcremie Ruby Swirl":
        #     name = "Ruby Swirl Alcremie"
        # case "Alcremie Caramel Swirl":
        #     name = "Caramel Swirl Alcremie"
        # case "Alcremie Rainbow Swirl":
        #     name = "Rainbow Swirl Alcremie"
        case "Eiscue Ice":
            if alt:
                name = "Ice Face Form Eiscue"
            else:
                name = "Eiscue"
        case "Eiscue Noice":
            name = "Noice Face Form Eiscue"
        case "Morpeko Full Belly":
            if alt:
                name = "Full Belly Mode Morpeko"
            else:
                name = "Morpeko"
        case "Morpeko Hangry":
            name = "Hangry Mode Morpeko"
        case "Zacian":
            if alt:
                name = "Hero of Many Battles Zacian"
        case "Zacian Crowned":
            name = "Crowned Sword Zacian"
        case "Zamazenta":
            if alt:
                name = "Hero of Many Battles Zamazenta"
        case "Zamazenta Crowned":
            name = "Crowned Shield Zamazenta"
        case "Urshifu Single Strike":
            if alt:
                name = "Single Strike Style Urshifu"
            else:
                name = "Urshifu"
        case "Urshifu Rapid Strike":
            name = "Rapid Strike Style Urshifu"
        case "Zarude Dada":
            name = "Dada Zarude"
        case "Calyrex Ice":
            name = "Ice Rider Calyrex"
        case "Calyrex Shadow":
            name = "Shadow Rider Calyrex"
        case "Enamorus Incarnate":
            if alt:
                name = "Incarnate Forme Enamorus"
            else:
                name = "Enamorus"
        case "Enamorus Therian":
            name = "Therian Forme Enamorus"
        case "Maushold":
            if aesthetic:
                name = "Family of Four Maushold"
            else:
                name = "Maushold"
        case "Maushold Family Of Three":
            name = "Family of Three Maushold"
        case "Squawkabilly":
            if aesthetic:
                name = "Green Plumage Squawkabilly"
        case "Squawkabilly Blue Plumage":
            name = "Blue Plumage Squawkabilly"
        case "Squawkabilly Yellow Plumage":
            name = "Yellow Plumage Squawkabilly"
        case "Squawkabilly White Plumage":
            name = "White Plumage Squawkabilly"
        case "Palafin":
            if alt:
                name = "Zero Form Palafin"
            else:
                name = "Palafin"
        case "Palafin Hero":
            name = "Hero Form Palafin"
        case "Tatsugiri":
            if aesthetic:
                name = "Curly Form Tatsugiri"
            else:
                name = "Tatsugiri"
        case "Tatsugiri Droopy":
            name = "Droopy Form Tatsugiri"
        case "Tatsugiri Stretchy":
            name = "Stretchy Form Tatsugiri"
        case "Dudunsparce":
            if aesthetic:
                name = "Two-Segment Form Dudunsparce"
        case "Dudunsparce Three Segment":
            name = "Three Segment Form Dudunsparce"
        case "Gimmighoul":
            if alt:
                name = "Chest Form Gimmighoul"
            else:
                name = "Gimmighoul"
        case "Gimmighoul Roaming":
            name = "Roaming Form Gimmighoul"
        case "Koraidon":
            if mounts:
                name = "Apex Build Koraidon"
        case "Koraidon Limited Build":
            name = "Limited Build Koraidon"
        case "Koraidon Sprinting Build":
            name = "Sprinting Build Koraidon"
        case "Koraidon Swimming Build":
            name = "Swimming Build Koraidon"
        case "Koraidon Gliding Build":
            name = "Gliding Build Koraidon"
        case "Miraidon":
            if mounts:
                name = "Ultimate Mode Miraidon"
        case "Miraidon Low-Power Mode":
            name = "Low-Power Mode Miraidon"
        case "Miraidon Drive Mode":
            name = "Drive Mode Miraidon"
        case "Miraidon Aquatic Mode":
            name = "Aquatic Mode Miraidon"
        case "Miraidon Glide Mode":
            name = "Glide Mode Miraidon"

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
            name = "Alolan Sandslash"
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
        case "Darmanitan Galar Standard":
            if alt:
                name = "Galarian Standard Mode Darmanitan"
            else:
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
            name = "Hisuian Arcanine"
        case "Voltorb Hisui":
            name = "Hisuian Voltorb"
        case "Electrode Hisui":
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
        case "Slowbro Mega":
            name = "Mega Slowbro"
        case "Alakazam Mega":
            name = "Mega Alakazam"
        case "Gengar Mega":
            name = "Mega Gengar"
        case "Kangaskhan Mega":
            name = "Mega Kangaskhan"
        case "Pinsir Mega":
            name = "Mega Pinsir"
        case "Gyarados Mega":
            name = "Mega Gyarados"
        case "Aerodactyl Mega":
            name = "Mega Aerodactyl"
        case "Mewtwo Mega X":
            name = "Mega Mewtwo X"
        case "Mewtwo Mega Y":
            name = "Mega Mewtwo Y"
        case "Ampharos Mega":
            name = "Mega Ampharos"
        case "Steelix Mega":
            name = "Mega Steelix"
        case "Scizor Mega":
            name = "Mega Scizor"
        case "Heracross Mega":
            name = "Mega Heracross"
        case "Houndoom Mega":
            name = "Mega Houndoom"
        case "Tyranitar Mega":
            name = "Mega Tyranitar"
        case "Sceptile Mega":
            name = "Mega Sceptile"
        case "Blaziken Mega":
            name = "Mega Blaziken"
        case "Swampert Mega":
            name = "Mega Swampert"
        case "Gardevoir Mega":
            name = "Mega Gardevoir"
        case "Sableye Mega":
            name = "Mega Sableye"
        case "Mawile Mega":
            name = "Mega Mawile"
        case "Aggron Mega":
            name = "Mega Aggron"
        case "Medicham Mega":
            name = "Mega Medicham"
        case "Manectric Mega":
            name = "Mega Manectric"
        case "Sharpedo Mega":
            name = "Mega Sharpedo"
        case "Camerupt Mega":
            name = "Mega Camerupt"
        case "Altaria Mega":
            name = "Mega Altaria"
        case "Banette Mega":
            name = "Mega Banette"
        case "Absol Mega":
            name = "Mega Absol"
        case "Glalie Mega":
            name = "Mega Glalie"
        case "Salamence Mega":
            name = "Mega Salamence"
        case "Metagross Mega":
            name = "Mega Metagross"
        case "Latias Mega":
            name = "Mega Latias"
        case "Latois Mega":
            name = "Mega Latios"
        case "Rayquaza Mega":
            name = "Mega Rayquaza"
        case "Lopunny Mega":
            name = "Mega Lopunny"
        case "Garchomp Mega":
            name = "Mega Garchomp"
        case "Lucario Mega":
            name = "Mega Lucario"
        case "Abomasnow Mega":
            name = "Mega Abomasnow"
        case "Gallade Mega":
            name = "Mega Gallade"
        case "Audino Mega":
            name = "Mega Audino"
        case "Diancie Mega":
            name = "Mega Diancie"

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
        case "Meowth Gmax":
            name = "Gigantamax Meowth"
        case "Machamp Gmax":
            name = "Gigantamax Machamp"
        case "Gengar Gmax":
            name = "Gigantamax Gengar"
        case "Kingler Gmax":
            name = "Gigantamax Kingler"
        case "Lapras Gmax":
            name = "Gigantamax Lapras"
        case "Eevee Gmax":
            name = "Gigantamax Eevee"
        case "Snorlax Gmax":
            name = "Gigantamax Snorlax"
        case "Garbodor Gmax":
            name = "Gigantamax Garbodor"
        case "Melmetal Gmax":
            name = "Gigantamax Melemetal"
        case "Rilaboom Gmax":
            name = "Gigantamax Rilaboom"
        case "Cinderace Gmax":
            name = "Gigantamax Cinderace"
        case "Inteleon Gmax":
            name = "Gigantamax Inteleon"
        case "Corviknight Gmax":
            name = "Gigantamax Corviknight"
        case "Orbeetle Gmax":
            name = "Gigantamax Orbeetle"
        case "Drednaw Gmax":
            name = "Gigantamax Drednaw"
        case "Coalossal Gmax":
            name = "Gigantamax Coalossal"
        case "Flapple Gmax":
            name = "Gigantamax Flapple"
        case "Appletun Gmax":
            name = "Gigantamax Appletun"
        case "Sandaconda Gmax":
            name = "Gigantamax Sandaconda"
        case "Totricity Amped Gmax":
            name = "Gigantamax Toxtricity"
        # case "Toxtricity Low Key Gmax":
        #     name = "Gigantamax Toxtricity"
        case "Centiskorch Gmax":
            name = "Gigantamax Centiskorch"
        case "Hatterene Gmax":
            name = "Gigantamax Hatterene"
        case "Grimmsnarl Gmax":
            name = "Gigantamax Grimmsnarl"
        case "Alcremie Gmax":
            name = "Gigantamax Alcremie"
        case "Copperajah Gmax":
            name = "Gigantamax Copperajah"
        case "Duraludon Gmax":
            name = "Gigantamax Duraludon"
        case "Urshifu Single Strike Gmax":
            name = "Gigantamax Single Strike Style Urshifu"
        case "Urshifu Rapid Strike Gmax":
            name = "Gigantamax Rapid Strike Style Urshifu"

        # Primal Pokémon
        case "Kyogre Primal":
            name = "Primal Kyogre"
        case "Groudon Primal":
            name = "Primal Groudon"

        # Unique Pokémon
        case "Pichu Spiky Eared":
            name = "Spiky-eared Pichu"
        case "Greninja Battle Bond":
            name = "Battle Bond Greninja"
        case "Floette Eternal":
            name = "Eternal Flower Floette"
        case "Rockruff Own Tempo":
            name = "Own Tempo Rockruff"

        # Totem Pokémon
        case "Raticate Totem Alola":
            name = "Totem Alolan Raticate"
        case "Marowak Totem":
            name = "Totem Alolan Marowak"
        case "Gumshoos Totem":
            name = "Totem Gumshoos"
        case "Vikavolt Totem":
            name = "Totem Vikavolt"
        case "Ribombee Totem":
            name = "Totem Ribombee"
        case "Araquanid Totem":
            name = "Totem Araquanid"
        case "Lurantis Totem":
            name = "Totem Lurantis"
        case "Salazzle Totem":
            name = "Totem Salazzle"
        case "Togedemaru Totem":
            name = "Totem Togedemaru"
        case "Mimikyu Totem Disguised":
            if disguise:
                name = "Disguised Totem Mimikyu"
            else:
                name = "Totem Mimikyu"
        case "Mimikyu Totem Busted":
            name = "Busted Totem Mimikyu"
        case "Kommo O Totem":
            name = "Totem Kommo-o"

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

        # Mounts
        case "Koraidon Limited Build":
            name = "Limited Build Koraidon"
        case "Koraidon Sprinting Build":
            name = "Sprinting Build Koraidon"
        case "Koraidon Swimming Build":
            name = "Swimming Build Koraidon"
        case "Koraidon Gliding Build":
            name = "Gliding Build Koraidon"
        case "Miraidon Low Power Mode":
            name = "Low-Power Mode Miraidon"
        case "Miraidon Drive Mode":
            name = "Drive Mode Miraidon"
        case "Miraidon Aquatic Mode":
            name = "Aquatic Mode Miraidon"
        case "Miraidon Gliding Mode":
            name = "Gliding Mode Miraidon"

        # Other Pokémon
        case "Greninja Ash":
            name = "Ash-Greninja"
        case "Mimikyu Disguised":
            if disguise:
                name = "Disguised Mimikyu"
            else:
                name = "Mimikyu"
        case "Mimikyu Busted":
            name = "Busted Mimikyu"
        case "Eternatus Eternamax":
            name = "Eternamax Eternatus"

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
        name = name.replace("As One Glastrier", "As One")
        name = name.replace("As One Spectrier", "As One")
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
    info1 = "{:>4} || {:>38} ||" \
        .format(id_number, name)
    if types[1] != "none":
        info2 = " {:>8}/{:<8} ||" \
            .format(types[0], types[1])
    else:
        info2 = " {:>8}          ||" \
            .format(types[0])
    info3 = " {:>16}, {:>16}, {:>16} ||" \
        .format(abilities[0], abilities[1], abilities[2])
    info4 = " {:>4}: {:>3}, {:>3}, {:>3}, {:>3}, {:>3}, {:>3}\n" \
        .format(calc_bst(stats),
                stats[0], stats[1], stats[2],
                stats[3], stats[4], stats[5])
    info_line = info1 + info2 + info3 + info4

    file.write(info_line)


def calc_bst(stats):
    return int(stats[0]) + int(stats[1]) + int(stats[2])\
        + int(stats[3]) + int(stats[4]) + int(stats[5])
