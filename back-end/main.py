from app import app
from db import db_energy_consumption
from flask import jsonify
from flask import request


@app.route('/get', methods=['GET'])
def get_by_date():
    """
       GET a list of energy consumption for a specific day.

       Returns the hour, energy consumption, prevision J and prevision J-1.
    """
    args = request.args
    date = args.get("date")
    docs = db_energy_consumption.find({'date': date},
                                      {"hour": 1, "consumption": 1, "forecastingD": 1, "forecastingD_1": 1,
                                       "_id": 0})
    response = list(docs)
    return {'response': response}


@app.route('/get-by-range', methods=['GET'])
def get_by_date_range():
    """
       GET a list of energy consumption between two dates.

       Returns the date, the hour, energy consumption, prevision J and prevision J-1.
    """
    args = request.args
    start_date = args.get("start")
    end_date = args.get("end")
    docs = db_energy_consumption.find({'date': {'$gte': start_date, '$lt': end_date}},
                                      {"date": 1, "hour": 1, "consumption": 1, "forecastingD": 1, "forecastingD_1": 1,
                                       "_id": 0})
    response = list(docs)
    return {'response': response}


@app.errorhandler(404)
def showMessage(error=None):
    message = {
        'status': 404,
        'message': 'Record not found: ' + request.url,
    }
    respone = jsonify(message)
    respone.status_code = 404
    return respone


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)
