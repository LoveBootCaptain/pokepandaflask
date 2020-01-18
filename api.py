#!/usr/bin/env python
# -*- coding: utf-8 -*-
from flask import Flask, jsonify
from pokepanda import get_pokemon


app = Flask(__name__)


@app.route('/')
def index():
    return jsonify(hello='coding berlin meetup')


@app.route('/api/<poke_id>/')
def poke_detail_api(poke_id):
    current_pokemon = get_pokemon(poke_id)
    return jsonify(current_pokemon)


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=4545, threaded=True)
