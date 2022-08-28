from flask import Flask,render_template,request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
# app.config['SQLALCHEMY_DATABASE_URI'] = "mysql://root:1234@localhost/ultimate"
# sqldb = SQLAlchemy(app)
#
# class Contact(sqldb.Model):
#
#     sr_num = sqldb.Column(sqldb.Integer, primary_key = True)
#     name= sqldb.Column(sqldb.String(40))
#     email= sqldb.Column(sqldb.String(40))
#     phone = sqldb.Column(sqldb.String(40))
#     msg = sqldb.Column(sqldb.String(40))



@app.route('/')
def home():
    return  render_template('index.html')

# @app.route('/about')
# def about():
#     return render_template('about.html')
#
# @app.route('/contact', methods=['GET','POST'])
# def contact():
#     if request.method=='POST':
#         '''add entry to the database'''
#         name=request.form.get('name')
#         email = request.form.get('email')
#         phone = request.form.get('phone')
#         message = request.form.get('msg')
#         entry =Contact(name=name,email=email,phone=phone,msg=message)
#         sqldb.session.add(entry)
#         sqldb.session.commit()
#     return render_template('contact.html')




if __name__ == '__main__':
    app.run(debug=True)