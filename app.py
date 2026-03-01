from flask import Flask, render_template, request, redirect, url_for
import os

app = Flask(__name__)

def get_contacts():
    contacts = []
    if os.path.exists("contacts.txt"):
        with open("contacts.txt", "r") as file:
            for line in file:
                if line.strip():
                    parts = line.strip().split(",")
                    if len(parts) == 3:
                        contacts.append({
                            "name": parts[0],
                            "phone": parts[1],
                            "email": parts[2]
                        })
    return contacts

@app.route("/")
def index():
    contacts = get_contacts()
    return render_template("index.html", contacts=contacts)

@app.route("/add", methods=["POST"])
def add_contact():
    name = request.form.get("name")
    phone = request.form.get("phone")
    email = request.form.get("email")
    
    if name and phone and email:
        with open("contacts.txt", "a") as file:
            file.write(f"{name},{phone},{email}\n")
    
    return redirect(url_for("index"))

if __name__ == "__main__":
    app.run(debug=True, port=5000)
