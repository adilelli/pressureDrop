from formatcontroller.pressureArray import pressureArrayController
from formatcontroller.pressureDropController import pressureController
from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/pressureDrop', methods=['POST'])
def pressureRoute():
    pressure_drop = pressureController() 
    response = {'result in Pa': pressure_drop }
    return jsonify(response), 200

@app.route('/pressureArray', methods=['POST'])
def pressureArrayRoute():
    pressure_drop = pressureArrayController()
    response = {'result in Pa': pressure_drop }
    return jsonify(response), 200

if __name__ == '__main__':
    app.run()
