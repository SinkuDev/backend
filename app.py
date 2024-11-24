from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return "Crack-In Backend is Running!"

@app.route('/login', methods=['POST'])
def login():
    data = request.json
    email = data.get('email')
    password = data.get('password')

    # For now, let's just return a placeholder response
    if email == 'test@example.com' and password == 'password123':
        return jsonify({"message": "Login successful!"}), 200
    else:
        return jsonify({"message": "Invalid credentials!"}), 401

if __name__ == '__main__':
    app.run(debug=True)
