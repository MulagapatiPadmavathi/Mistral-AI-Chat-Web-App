from flask import Flask, render_template, request, jsonify
import api_integration  # Ensure this file exists and is properly configured

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")  # Ensure templates/index.html exists

@app.route("/chat", methods=["POST"])
def chat():
    data = request.json
    user_message = data.get("message", "")

    if not user_message.strip():
        return jsonify({"response": "Error: Empty message received."})

    bot_response = api_integration.get_response(user_message)
    return jsonify({"response": bot_response})

if __name__ == "__main__":
    app.run(debug=True)
