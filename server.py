from flask import Flask, render_template, request, redirect, session

app = Flask(__name__)
app.secret_key = "secret"

# Make a route if you want to go to a particular HTML file, ie index for home and result for output of something

# Make a route for every action I take in my app ie submit data, update data, delete data

@app.route("/")
def display_home():
    return render_template("index.html")

@app.route("/process", methods = ['POST'])
def go_to_result():
    if request.form.get("fun") and request.form.get("notrobot"):
        session['new_dict'] = {
            "name": request.form["name"],
            "dojo_location": request.form["dojo_location"],
            "fav_language": request.form["fav_language"],
            "comment": request.form["comment"],
            "notrobot": request.form["notrobot"],
            "fun": request.form["fun"]
        }
    elif request.form.get("fun"):
        session['new_dict'] = {
            "name": request.form["name"],
            "dojo_location": request.form["dojo_location"],
            "fav_language": request.form["fav_language"],
            "comment": request.form["comment"],
            "notrobot": "Bleep bloop",
            "fun": request.form["fun"]
    }
    elif request.form.get("notrobot"):
        session['new_dict'] = {
            "name": request.form["name"],
            "dojo_location": request.form["dojo_location"],
            "fav_language": request.form["fav_language"],
            "comment": request.form["comment"],
            "notrobot": request.form["notrobot"],
            "fun": "Yesiree!"
    }
    else:
        session['new_dict'] = {
            "name": request.form["name"],
            "dojo_location": request.form["dojo_location"],
            "fav_language": request.form["fav_language"],
            "comment": request.form["comment"],
            "notrobot": "Bleep bloop",
            "fun": "I am not having fun"
    }
    return redirect("/result")

@app.route("/result")
def display_result():
    return render_template("result.html")

@app.route("/result", methods = ['POST'])
def go_to_home():
    return redirect("/")


if __name__ == "__main__":
    app.run(debug = True)