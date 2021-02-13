from flask import Flask,session,render_template,redirect,request,url_for
import db as api
import credential
import mailing as mail
from itsdangerous import URLSafeTimedSerializer,SignatureExpired

app = Flask(__name__)
app.secret_key=credential.secret_key
# app.config.from_pyfile('config.cfg')
# mail = Mail(app)
# mail['MAIL_PORT']
s = URLSafeTimedSerializer(credential.secret_key)


@app.route('/')
def home():
    return render_template('untitled.html')



@app.route('/doc_signup',methods=['POST','GET'])
def doc_signup():
    if request.method=='POST':
        form_details=request.form
        email=form_details['doc_email']
        # print(email,"hehehehehheheheh")
        token = s.dumps(email,salt='email-confirm')
        link = url_for('confirm_email',token=token,_external=True)
        msg = 'This link will disable in 10 Minutes.\n Confirmation Link: '+str(link)
        mail.send(email,msg)
        session['doc_username']=request.form['doc_username']
        api.doc_signup(form_details['doc_id'],form_details['doc_username'],form_details['doc_password'],form_details['doc_name'],form_details['qualification'],form_details['specialization'],form_details['doc_email'],"1")
        return render_template('index.html')
    return render_template('temp.html')    


@app.route('/login',methods=['POST','GET'])
def login():
    if request.method=='POST':
        form_details = request.form
        # if api.check_confirmation()
        data=api.doc_login(form_details['email'],form_details['pass'])
        if(data=='correct_password'):
            session['email']=form_details['email']
            return redirect('/')
        elif data=='wrong_password':
            return render_template('login.html')
        elif data == 'username_dosenot_exist':
            return  render_template('login.html')
    return render_template('login.html')


@app.route('/doc_logout',methods=['POST','GET'])
def doc_logout():
    session.pop('doc_username',None)
    return redirect('/doc_login')


@app.route('/confirm_email/<token>')
def confirm_email(token):
    try:
        email=s.loads(token,salt='email-confirm',max_age=600)
        api.doc_update(email)
        return render_template('index.html')
    except SignatureExpired:
        return '<h1>Token expired</h1>'   

if __name__=='__main__':
    app.run(debug=True)


