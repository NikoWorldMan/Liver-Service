import random

class English:
    weapon_name_first_half: list[str] = ['Great', 'Thunder', 'Storming', 'Storm', 'Vortex', 'Fury', 'Eclipse', 'Abyss', 'Abyssal', 'Radiance', 'Ghost', 'Flaming', 'Crescent', 'Morning', 'The', 'Long', 'Short', 'True', 'Apocalyptic', 'Meteor', 'Twilight', 'Smiting', 'Solar', 'Sonar', 'Crystal', 'Menacing', 'Ominous', 'Tempest', 'Dive', 'Angry', 'Apocalypse']
    weapon_name_second_half: list[str] = ['Weapon', 'Blast', 'Flare', 'Staff', 'Cane', 'Lance', 'Pike', 'Blade', 'Saber', 'Quarterstaff', 'Scythe', 'Star', 'Zweihander', 'Shortsword', 'Longsword', 'Excalibur', 'Nightfall', 'Serpent', 'Kanana', 'Strike', 'Spring', 'Summer', 'Autumn', 'Winter', 'Rocket Launcher', 'Launcher', 'Pumpkin', 'Cast']

class Norsk:
    weapon_name_first_half: list[str] = ['Lumske', 'De Vandødes', 'Siste', 'Virvlende', 'Forhekset', 'vræde', 'Fantastisk', 'Merkelig', 'Månemannen\'s', ]
    weapon_name_second_half: list[str] = ['Skrekk', 'Dyp', 'Sprell', 'Tryllestav', 'Bestikk', 'Værktøy', 'Vrede', 'Utstråling']


def random_choice(list: list) -> any:
    return random.choice(list)

name = f'{random_choice(English.weapon_name_first_half)} {random_choice(English.weapon_name_second_half)}'

print(f'\nBehold, {name}\n')