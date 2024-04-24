from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///reservations.db'
db = SQLAlchemy(app)

class Reservation(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), nullable=False)
    phone = db.Column(db.String(20), nullable=False)
    check_in_date = db.Column(db.Date, nullable=False)

@app.route('/')
def welcome():
    return render_template('welcome.html')

@app.route('/reservation', methods=['GET', 'POST'])
def reservation():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        phone = request.form['phone']
        check_in_date = request.form['check_in_date']
        reservation = Reservation(name=name, email=email, phone=phone, check_in_date=check_in_date)
        db.session.add(reservation)
        db.session.commit()
        return redirect(url_for('confirmation'))
    return render_template('reservation.html')

@app.route('/confirmation')
def confirmation():
    return render_template('confirmation.html')

@app.route('/reservation_list')
def reservation_list():
    reservations = Reservation.query.all()
    return render_template('reservation_list.html', reservations=reservations)

if __name__ == '__main__':
    app.run(debug=True)
