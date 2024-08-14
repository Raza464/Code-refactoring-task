from flask import Flask, render_template, request, redirect

app = Flask(__name__)

notes = []
# added get method in home route.
# changed request.args to request.form for post method.
@app.route('/', methods=["GET", "POST"])
def index():
    if request.method == "POST":
        note = request.form.get("note")
        if note:
            notes.append(note)
        return redirect('/') # Redirected to homepage to prevent from adding the same note again on reload.
    return render_template("home.html", notes=notes)


if __name__ == '__main__':
    app.run(debug=True, host = "0.0.0.0")





# All list of changes made:
#   1) added get method in home route.
#   2) changed request.args to request.form for post method.
#   3) Redirected to homepage to prevent from adding the same note again on reload.
#   4) added action and method in form.