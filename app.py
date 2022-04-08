from flask import Flask, render_template, url_for, redirect, flash
from forms import LoginForm, RegisterForm
from datetime import datetime

teacher = {
    'username': 'Oyaro Jared',
    'password': 'code',
    'email': 'oyarojared@nyabondomixed'
}

settings = {
    "term": 2,
    "week": 7,
    "term_length": 10,
    "date": datetime.now().date()
}

all_teachers = [
    {
        'name': 'Oyaro Jared',
        'tsc_no': 3238951,
        'phone': '0732637442'
    },
    {
        'name': 'Obadiah Nyandika',
        'tsc_no': 48832444,
        'phone': '0773293442'
    }
]

app = Flask(__name__)
app.config["SECRET_KEY"] = "2f33439e5bf223cad6ab1ff6248f453e"


@app.route("/", methods=['GET', 'POST'])
def index():
    form = LoginForm()
    if form.validate_on_submit(): # VALIDATE USER INPUTS @
        if form.username.data == 'oyarojared@nyabondomixed'\
           and form.password.data == 'code':
               return render_template("admin_general.html",\
                teacher=teacher, settings=settings)
        else:
            flash('Incorrect Username or Password!', 'danger')
            return redirect(url_for("index"))
    return render_template("index.html", form=form)


@app.route("/display_teachers")
def display_teachers():
    return render_template("display_teachers.html", settings=settings,\
    all_teachers=all_teachers, teacher=teacher)

@app.route("/register_teacher")
def register_teacher():
    form = RegisterForm()
    return render_template('register_teacher.html', form=form,\
     teacher=teacher, settings=settings)









if "__name__" == "__main__":
    app.run(debug=True)