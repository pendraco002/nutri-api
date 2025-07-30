from flask import Flask, request, jsonify
from planner import create_meal_plan

app = Flask(__name__)

@app.route('/')
def index():
    return "API do Plano Alimentar está funcionando!"

@app.route('/create_plan', methods=['POST'])
def handle_create_plan():
    data = request.json

    if not data or "goals" not in data:
        return jsonify({"error": "Dados de metas ausentes"}), 400

    try:
        plan = create_meal_plan(data["goals"])
        return jsonify({
            "function_name": "CreateMealPlan",
            "result": plan
        })
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
