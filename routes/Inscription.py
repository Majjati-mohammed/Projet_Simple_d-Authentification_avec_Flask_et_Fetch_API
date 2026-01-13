from flask import Flask, request, jsonify, Blueprint, render_template
import database


inscrire_bp = Blueprint("inscrire", __name__)

@inscrire_bp.route("/")
def index():
    return render_template("index.html")

@inscrire_bp.route("/inscription")
def inscription():
    return render_template("Inscription.html")


@inscrire_bp.route('/inscrire', methods=["POST"])
def add_user():
    data = request.get_json()
    name = data.get("name")
    email = data.get("email")
    password = data.get("password")

    conn = database.get_db_connection()
    conn.execute(
        "INSERT INTO users (name, email, password) VALUES (?, ?, ?)",
        (name, email, password)
    )
    conn.commit()
    conn.close()
    return jsonify(message = f"Utilisateur {name} ajouté")