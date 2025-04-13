from flask import Flask, request, jsonify, abort

app = Flask(__name__)

@app.route('/api/v1.0/predict', methods=['GET'])
def predict():
    try:
        num1 = float(request.args.get('num1', 0))
        num2 = float(request.args.get('num2', 0))
    except ValueError:
        abort(400)

    total = num1 + num2
    prediction = 1 if total > 5.8 else 0

    return jsonify({
        "prediction": prediction,
        "features": {"num1": num1, "num2": num2}})

@app.errorhandler(400)
def bad_request(error):
    return jsonify({"error": "Bad Request - Invalid input. Please provide numerical values."}), 400

@app.errorhandler(404)
def not_found(error):
    return jsonify({"error": "Not Found"}), 404

if __name__ == '__main__':
    app.run()
