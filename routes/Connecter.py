from flask import Flask, request, jsonify, Blueprint, session, render_template
import database

connecter_bp = Blueprint("connexion", __name__)

@connecter_bp.route("/profile")
def compte():
    return render_template("profile.html")


@connecter_bp.route("/CONNECTER", methods=["POST"])
def get_users():
    data = request.get_json()
    uname = data.get("name")
    upassword = data.get("password")
    conn = database.get_db_connection()
    user = conn.execute("SELECT * FROM users WHERE name=? AND password=?", (uname, upassword)).fetchone()
    conn.close()
    if user:
        session["user_id"] = user[0]
        session["user_name"] = user[1]
        session["user_email"] = user[2]
        session["created_at"] = user[4]
        return jsonify({"success" : True})
    else:
        return jsonify({"success": False, "message" : f"Utilisateur introuvable"})

@connecter_bp.route("/api/profile",methods=["GET"])
def me():
    if "user_name" not in session:
        return jsonify({"login": False})
    return jsonify({"login":True, "name": session["user_name"], "mail": session["user_email"],  "created_at": session["created_at"]})