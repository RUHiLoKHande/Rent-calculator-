from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        try:
            rent = int(request.form["rent"])
            food = int(request.form["food"])
            electricity = int(request.form["electricity"])
            water = int(request.form["water"])
            members = int(request.form["members"])

            total_bill = rent + food + electricity + water
            amount_per_member = total_bill / members
            return render_template("index.html", amount_per_member=amount_per_member)
        except ValueError:
            return render_template("index.html", error="Please enter valid numbers for all fields.")
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)
