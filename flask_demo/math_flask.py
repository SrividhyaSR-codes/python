from flask import Flask, request, jsonify

app = Flask(__name__)


@app.route("/")
def home():
    return "Welcome to Math Operations API"


@app.route("/calculate", methods=["GET", "POST"])
def calculate():
    if request.method == "POST":
        data = request.get_json(silent=True) or {}
        num1 = data.get("num1")
        num2 = data.get("num2")
        operation = data.get("operation")
    else:
        num1 = request.args.get("num1")
        num2 = request.args.get("num2")
        operation = request.args.get("operation")

    if num1 is None or num2 is None or operation is None:
        return jsonify({
            "error": "Please provide num1, num2 and operation."
        }), 400

    try:
        num1 = float(num1)
        num2 = float(num2)
    except (TypeError, ValueError):
        return jsonify({
            "error": "num1 and num2 must be numeric."
        }), 400

    if operation == "add":
        result = num1 + num2

    elif operation == "subtract":
        result = num1 - num2

    elif operation == "multiply":
        result = num1 * num2

    elif operation == "divide":
        if num2 == 0:
            return jsonify({
                "error": "Division by zero is not allowed."
            }), 400
        result = num1 / num2

    else:
        return jsonify({
            "error": "Invalid operation."
        }), 400

    return jsonify({
        "num1": num1,
        "num2": num2,
        "operation": operation,
        "result": result
    })


if __name__ == "__main__":
    app.run(debug=True)