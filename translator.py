def translate_type_to_number(pokemon_type):
    match pokemon_type:
        case 'normal':
            return '00'
        case 'fire':
            return '01'
        case 'water':
            return '02'
        case 'electric':
            return '03'
        case 'grass':
            return '04'
        case 'ice':
            return '05'
        case 'fighting':
            return '06'
        case 'poison':
            return '07'
        case 'ground':
            return '08'
        case 'flying':
            return '09'
        case 'psychic':
            return '10'
        case 'bug':
            return '11'
        case 'rock':
            return '12'
        case 'ghost':
            return '13'
        case 'dragon':
            return '14'
        case 'dark':
            return '15'
        case 'steel':
            return '16'
        case 'fairy':
            return '17'
        case _:
            raise ValueError(pokemon_type + " is not a type.")


def translate_number_to_type(number):
    match number:
        case '00':
            return 'normal'
        case '01':
            return 'fire'
        case '02':
            return 'water'
        case '03':
            return 'electric'
        case '04':
            return 'grass'
        case '05':
            return 'ice'
        case '':
            return 'fighting'
        case '07':
            return 'poison'
        case '08':
            return 'ground'
        case '09':
            return 'flying'
        case '10':
            return 'psychic'
        case '11':
            return 'bug'
        case '12':
            return 'rock'
        case '13':
            return 'ghost'
        case '14':
            return 'dragon'
        case '15':
            return 'dark'
        case '16':
            return 'steel'
        case '17':
            return 'fairy'
        case _:
            raise ValueError(number + " is not between 00 and 17 (inclusive).")


# I might fill out these next methods, or I might not
def translate_ability_to_number(pokemon_ability):
    match pokemon_ability:
        case 'stench':
            return '001'
        case _:
            raise ValueError(pokemon_ability + " is not an ability.")


def translate_number_to_ability(number):
    match number:
        case '001':
            return 'stench'
        case _:
            raise ValueError(number + " is not between 001 and 298 (inclusive).")
