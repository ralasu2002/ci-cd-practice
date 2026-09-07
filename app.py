from flask import Flask, request, jsonify

from calculator import add, subtract, multiply, divide

app = Flask(__name__)


def get_operands():
    a = float(request.args.get("a"))
    b = float(request.args.get("b"))
    return a, b


@app.route("/add")
def add_route():
    a, b = get_operands()
    return jsonify(result=add(a, b))


@app.route("/subtract")
def subtract_route():
    a, b = get_operands()
    return jsonify(result=subtract(a, b))


@app.route("/multiply")
def multiply_route():
    a, b = get_operands()
    return jsonify(result=multiply(a, b))


@app.route("/divide")
def divide_route():
    a, b = get_operands()
    try:
        return jsonify(result=divide(a, b))
    except ValueError as e:
        return jsonify(error=str(e)), 400


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
