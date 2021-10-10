from flask import Flask, render_template
from loginForm import LoginForm
from flask_bootstrap import Bootstrap

app = Flask(__name__)
app.secret_key = "hjsadkf23478612"
Bootstrap(app)


@app.route("/")
def home():
    return render_template('index.html')


@app.route("/login", methods=["GET", "POST"])
def login():
    login_form = LoginForm()
    page = 'denied.html'
    if login_form.validate_on_submit():
        print(login_form.email.data)
        print(login_form.password.data)
        if login_form.email.data == 'admin@email.com' and login_form.password.data == '12345678':
            page = 'success.html'
        print(page)
        return render_template(page)
    return render_template('login.html', this_form=login_form)


if __name__ == '__main__':
    app.run(debug=True)
