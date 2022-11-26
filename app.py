from collections import namedtuple
from flask import Flask, request, render_template
from forms import LoginForm, EmaiPasswordForm

app = Flask(__name__)
app.config["SECRET_KEY"] = 'no_access'

User = namedtuple('User', field_names=['email', 'password'])
user = User(email='john@john.john', password='black')

@app.route('/login/', methods=['GET', 'POST'])
def login():
    form = EmaiPasswordForm()
    error = ''
    if request.method == 'POST':
        if form.validate_on_submit():
            if (
                form.email.data == user.email and
                form.password.data == user.password
            ):
                return "You're inn"
            else:
                return "Wrong credentials!!!"
        else:
            error = form.errors

    return render_template('login.html', form=form, error=error)

if __name__== "__main__":
    app.debug(debug=False)