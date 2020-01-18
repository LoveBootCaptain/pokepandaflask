#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json
import pandas as pd


pokemon_species_names = pd.read_csv('data/pokemon_species_names.csv')

language_id = 6


def get_pokemon(id_):

    localised_names = pokemon_species_names.loc[pokemon_species_names.loc[:, 'local_language_id'] == language_id, :]
    localised_pokemon = localised_names.loc[pokemon_species_names.loc[:, 'pokemon_species_id'] == int(id_), :]

    pokemon_data = localised_pokemon.loc[:, ['pokemon_species_id', 'name', 'genus']]\
        .to_json(orient='table', index=False, indent=4)

    pokemon = json.loads(pokemon_data)['data'][0]

    return pokemon


if __name__ == '__main__':
    print(get_pokemon(1))
