from app import app
from flask import render_template, flash, redirect, request, url_for, jsonify
from app.forms import LoginForm
#routes - urls where flask app accepts requests
@app.route('/')
@app.route('/index')

# view function
def index():
    user = {'username':'Beau'}
    classes = [{'classInfo':{'code':'CSC324', 'title':'Dev Ops'}, 'instructor':'Baoqiang Yan'},
               {'classInfo':{'code':'CSC374', 'title':'Unix Admin'}, 'instructor':'Greg Lawson'},
               {'classInfo':{'code':'CSC294', 'title':'Networking'}, 'instructor':'Greg Lawson'},
               {'classInfo':{'code':'CSC452', 'title':'Sec+ Cert'}, 'instructor':'Baoqiang Yan'}]
    return render_template('index.html', title='Home', user=user, classes=classes)


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if request.method == 'POST':
        if form.validate_on_submit():
            flash('Welcome user {}! You opted for remember_me={}'.format(
                form.username.data, form.remember_me.data))
            return redirect(url_for('emcdowell'))
    else:
        if request.args:
            flash('GET method now allowed for login!')
        # else:​
        #     flash('No data in request!')​

    return render_template('login.html', title='Sign In', form=form)

@app.route('/emcdowell2')
def emcdowell():
    return render_template('emcdowell.html')

@app.route('/json')
def jsonTest():
    # return jsonify(list(range(5)))​
    instructor = {"username": "byan",
                  "role": "instructor",
                  "uid": 11,
                  "name":
                      {"firstname": "Baoqiang",
                       "lastname": "Yan"
                       }
                  }

    return jsonify(instructor)