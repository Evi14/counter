from flask import Flask, render_template, request, redirect, session

app = Flask(__name__)
app.secret_key = 'yfufo8thyfurutcd'

@app.route('/')
def index():
    if "count" in session:
        print('key exists!')
        session["count"] += 1
    elif "count" in session and "fake" in session:
        session["count"] += 1
    else:    
        session["count"] = 1
        session["fake"] = 0
        print("key 'count' does NOT exist")
    session["real"] = session["count"] - session["fake"]
    return render_template("index.html")    

@app.route("/count", methods=["POST"])
def view_count():
    if request.form["chngCounter"]=="click":
        session["count"] += 1
    elif request.form["chngCounter"]=="reset":
        session["count"] = 0
        session["fake"] = 0
        session["real"] = 1
    elif request.form["chngCounter"]=="inputCounter":
        session["count"] += (int(request.form["addNum"])-1)
        session["fake"] += (int(request.form["addNum"]))
        
    return redirect("/")

@app.route("/destroy_session")
def destroy():
    session.clear()
    # session.pop('count')
    return redirect("/")
    
if __name__ == "__main__":
    app.run(debug=True)
