from flask import Flask, make_response
from src.poke_api.processing.data_processing import get_all_berry_data, process_berry_data

app = Flask(__name__)


@app.route("/")
def index():
    return "<p>Berry Cool API</p>"


@app.route("/allBerryStates", methods=["GET"])
def all_berry_stats():
    berry_data = get_all_berry_data()
    response = make_response(process_berry_data(berry_data))
    response.headers['Content-Type'] = 'application/json'
    return response
