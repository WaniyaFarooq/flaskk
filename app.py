from flask import Flask,render_template,request

app = Flask(__name__)
@app.route("/")
def student_profile():
    return render_template(
        "profile.html",name = "Waniya",
        is_Topper = True,
        subjects = {"Maths","Science","History"}
    )
@app.route("/chalchal")
def chalchal():
    return render_template("child.html")


@app.route("/feedback",methods=["POST","GET"])
def feedback():
    if request.method =="POST":
        name = request.form.get("username")
        message = request.form.get("message")

        return render_template("thankyou.html",user =name,message=message)
    
    return render_template("feedback.html")