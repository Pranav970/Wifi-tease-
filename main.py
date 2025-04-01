from flask import Flask, request, jsonify from flask_bcrypt import Bcrypt from flask_jwt_extended import JWTManager, create_access_token, jwt_required, get_jwt_identity from datetime import timedelta

app = Flask(name) app.config['JWT_SECRET_KEY'] = 'your_secret_key'  # Change this to a strong secret app.config['JWT_ACCESS_TOKEN_EXPIRES'] = timedelta(hours=1)

bcrypt = Bcrypt(app) jwt = JWTManager(app)

Simulated user database

users_db = {}

@app.route('/register', methods=['POST']) def register(): data = request.json username = data.get('username') password = data.get('password')

if username in users_db:
    return jsonify({'message': 'User already exists'}), 400

hashed_pw = bcrypt.generate_password_hash(password).decode('utf-8')
users_db[username] = hashed_pw
return jsonify({'message': 'User registered successfully'})

@app.route('/login', methods=['POST']) def login(): data = request.json username = data.get('username') password = data.get('password')

stored_password = users_db.get(username)
if not stored_password or not bcrypt.check_password_hash(stored_password, password):
    return jsonify({'message': 'Invalid credentials'}), 401

access_token = create_access_token(identity=username)
return jsonify({'access_token': access_token})

@app.route('/protected', methods=['GET']) @jwt_required() def protected(): current_user = get_jwt_identity() return jsonify({'message': f'Hello, {current_user}! You have access to this route.'})

if name == 'main': app.run(debug=True)

