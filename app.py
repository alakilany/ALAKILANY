from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/booking')
def booking():
    return render_template('booking.html')

@app.route('/submit_booking', methods=['POST'])
def submit_booking():
    if request.method == 'POST':
        customer_name = request.form['customer_name']
        appointment_date = request.form['appointment_date']
        appointment_time = request.form['appointment_time']
        return render_template('submit_booking.html', customer_name=customer_name, appointment_date=appointment_date, appointment_time=appointment_time)
    else:
        return "حدث خطأ"


@app.route('/services')
def services():
    return render_template('services.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

if __name__ == '__main__':
    app.run(debug=True)
