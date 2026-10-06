from flask import Flask, render_template, request
import mysql.connector

app = Flask(__name__)

# Change this password to your MySQL password
DB = {
    "host": "localhost",
    "user": "root",
    "password": "YOUR_MYSQL_PASSWORD",
    "database": "cybershield"
}

def get_connection():
    return mysql.connector.connect(**DB)

def check_password(password):
    score = 0

    if len(password) >= 8:
        score += 1
    if any(c.isupper() for c in password):
        score += 1
    if any(c.islower() for c in password):
        score += 1
    if any(c.isdigit() for c in password):
        score += 1
    if any(not c.isalnum() for c in password):
        score += 1

    if score <= 2:
        return "Weak"
    elif score <= 4:
        return "Medium"
    else:
        return "Strong"

def check_message(message):
    words = [
        "urgent", "verify", "winner", "prize",
        "click", "password", "otp", "account"
    ]

    found = 0
    msg = message.lower()

    for word in words:
        if word in msg:
            found += 1

    if found >= 4:
        return "High"
    elif found >= 2:
        return "Medium"
    else:
        return "Low"

def save_result(scan_type, result):
    try:
        con = get_connection()
        cur = con.cursor()
        sql = "INSERT INTO scans (scan_type, result) VALUES (%s, %s)"
        cur.execute(sql, (scan_type, result))
        con.commit()
        cur.close()
        con.close()
    except Exception as e:
        print("Database error:", e)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/password", methods=["POST"])
def password_check():
    password = request.form["password"]
    result = check_password(password)
    save_result("Password Check", result)
    return render_template("result.html",
                           title="Password Check",
                           result=result)

@app.route("/phishing", methods=["POST"])
def phishing_check():
    message = request.form["message"]
    result = check_message(message)
    save_result("Phishing Check", result)
    return render_template("result.html",
                           title="Phishing Check",
                           result=result)

@app.route("/dashboard")
def dashboard():
    rows = []
    try:
        con = get_connection()
        cur = con.cursor()
        cur.execute(
            "SELECT scan_type, result, scan_time "
            "FROM scans ORDER BY scan_time DESC LIMIT 20"
        )
        rows = cur.fetchall()
        cur.close()
        con.close()
    except Exception as e:
        print("Database error:", e)

    return render_template("dashboard.html", rows=rows)

if __name__ == "__main__":
    app.run(debug=True)
