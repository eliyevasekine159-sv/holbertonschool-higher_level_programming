#!/usr/bin/python3
"""
Flask API demonstrating Basic Authentication and JWT Token-based Authentication
with Role-based Access Control (RBAC).
"""
from flask import Flask, jsonify, request
from flask_httpauth import HTTPBasicAuth
from flask_jwt_extended import (
    JWTManager, create_access_token, jwt_required, get_jwt, get_jwt_identity
)
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)

# JWT Konfiqurasiyası üçün təhlükəsiz açar
app.config["JWT_SECRET_KEY"] = "super-secret-key-change-in-production"
jwt = JWTManager(app)
auth = HTTPBasicAuth()

# Rəsmi sənəddə tələb olunan istifadəçi məlumatları strukturu
users = {
    "user1": {
        "username": "user1",
        "password": generate_password_hash("password"),
        "role": "user"
    },
    "admin1": {
        "username": "admin1",
        "password": generate_password_hash("password"),
        "role": "admin"
    }
}


# --- Basic Authentication Hissəsi ---
@auth.verify_password
def verify_password(username, password):
    """Verifies user credentials for Basic HTTP Authentication"""
    if username in users and check_password_hash(users[username]["password"], password):
        return username
    return None


@app.route("/basic-protected")
@auth.login_required
def basic_protected():
    """Route protected by Basic HTTP Authentication"""
    return "Basic Auth: Access Granted"


# --- JWT Authentication Login Hissəsi ---
@app.route("/login", methods=["POST"])
def login():
    """Authenticates user and returns a JWT Access Token containing user role"""
    data = request.get_json(silent=True)
    if not data:
        return jsonify({"error": "Invalid JSON"}), 400

    username = data.get("username")
    password = data.get("password")

    if not username or not password:
        return jsonify({"error": "Missing username or password"}), 400

    user = users.get(username)
    if not user or not check_password_hash(user["password"], password):
        return jsonify({"error": "Invalid credentials"}), 401

    # Rol məlumatını token payload-na (claims) əlavə edirik
    additional_claims = {"role": user["role"]}
    access_token = create_access_token(
        identity=username,
        additional_claims=additional_claims
    )
    return jsonify(access_token=access_token), 200


@app.route("/jwt-protected")
@jwt_required()
def jwt_protected():
    """Route protected by standard JWT Authentication"""
    return "JWT Auth: Access Granted"


# --- Role-based Access Control (RBAC) Hissəsi ---
@app.route("/admin-only")
@jwt_required()
def admin_only():
    """Route restricted to users with 'admin' role only"""
    claims = get_jwt()
    if claims.get("role") != "admin":
        return jsonify({"error": "Admin access required"}), 403
    return "Admin Access: Granted"


# --- Custom JWT Error Handlers (Tələb olunan 401 Loader-lər) ---
@jwt.unauthorized_loader
def handle_unauthorized_error(err):
    """Handles missing token errors"""
    return jsonify({"error": "Missing or invalid token"}), 401


@jwt.invalid_token_loader
def handle_invalid_token_error(err):
    """Handles malformed or invalid token errors"""
    return jsonify({"error": "Invalid token"}), 401


@jwt.expired_token_loader
def handle_expired_token_error(err):
    """Handles expired token errors"""
    return jsonify({"error": "Token has expired"}), 401


@jwt.revoked_token_loader
def handle_revoked_token_error(err):
    """Handles revoked token errors"""
    return jsonify({"error": "Token has been revoked"}), 401


@jwt.needs_fresh_token_loader
def handle_needs_fresh_token_error(err):
    """Handles fresh token required errors"""
    return jsonify({"error": "Fresh token required"}), 401


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
