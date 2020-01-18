# pokepandaflask

a small demo for a coding berlin meetup to show how to build a pokedex with pandas and make it restful with flask

## create and activate virtual environment in python3 (3.8.1)
```
python3 -m venv venv

source venv/bin/activate
```

## install dependencies
```
pip install --upgrade pip

pip install -r requirements.txt
```
## start jupyter notebook
```
jupyter-notebook
```
more detailed documentation is in the jupyter notebook.

have a look and try it out. :)


## start the demo api
```
python api.py
```
open your browser http://0.0.0.0:4545

test out some pokemon names by calling the api with the pokemon ID

for Bulbasaur use [http://0.0.0.0:4545/api/1/](http://0.0.0.0:4545/api/1/)


## credits

thx for some very good data

* [PokeAPI](https://github.com/PokeAPI/pokeapi)
* [veekun](https://github.com/veekun/pokedex) 
