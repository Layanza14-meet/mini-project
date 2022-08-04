from flask import Flask, render_template, request, redirect, url_for, flash
from flask import session as login_session
import pyrebase
config={
    
  "apiKey": "AIzaSyCeM92vdtvp-XPDiITvz4tMg45SJ_HeOSc",
  "authDomain": "layan-zahrawi.firebaseapp.com",
  "projectId": "layan-zahrawi",
  "storageBucket": "layan-zahrawi.appspot.com",
  "messagingSenderId": "819872730920",
  "appId": "1:819872730920:web:d569fcb1d4c3abe0eb0a1d",
  "measurementId": "G-1BQHYQJ52W",
  "databaseURL": "https://cs-mini-project-e9aa2-default-rtdb.firebaseio.com/"

}
firebase=pyrebase.initialize_app(config)
auth=firebase.auth()
db = firebase.database()
app=Flask(__name__)




app = Flask(__name__, template_folder='templates', static_folder='static')
app.config['SECRET_KEY'] = 'super-secret-key'

@app.route('/')

def home():
    return render_template("home.html")










@app.route('/signin', methods=['GET', 'POST'])
def signin():
    error = ""
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        try:
            login_session['user'] = auth.sign_in_with_email_and_password(email, password)
            return redirect(url_for('every'))
        except:
           error = "Authentication failed"
        return render_template("signin.html")
    else:
        if request.method == 'GET':
            return render_template("signin.html")


    


@app.route('/signup', methods=['GET', 'POST'])
def signup():

    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        bio = request.form['bio']
        fullname = request.form['fullname']
        username = request.form['username']
        
        try:
            login_session['user'] = auth.create_user_with_email_and_password(email, password)
            user = {"bio":bio,"fullname":fullname,"username":username,"password":password,"email":email}
            db.child("users").child(login_session['user']['localId'] ).set(user)




            return redirect(url_for('every'))

        except:
           error = "Authentication failed"
           return error

 
    else:
         if request.method == 'GET':
            return render_template("signup.html")

    



@app.route('/cart')
def add_cart():
    return render_template("carth.html")
@app.route('/all_photos', methods=['GET', 'POST'])
def open_link():
    if request.method == 'POST':
        link = request.form['link']
        return render_template("all_photos.html", link=link)
        



        









                

@app.route('/every')
def every():
    username=db.child("users").child(login_session["user"]["localId"]).get().val()
    print(username)
    return render_template("every.html",username=username['username'])


if __name__ == '__main__':
    app.run(debug=True)