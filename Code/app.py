from flask import Flask, render_template
import data  # Import data from the data.py file

app = Flask(__name__)

# Routes for each page
@app.route('/first-aid-guide')
def first_aid_guide():
    # Pass the list of first aid items to the HTML page
    return render_template('FirstAidGuide.html', first_aid_items=data.first_aid_items)

@app.route('/')
def home():
    return render_template('SymptomChecker.html')

@app.route('/symptom-checker')
def symptom_checker():
    return render_template('SymptomChecker.html')



@app.route('/courses')
def courses():
    return render_template('Courses.html')

@app.route('/doctor-consultation')
def doctor_consultation():
    return render_template('DoctorConsultation.html')

@app.route('/hospitals')
def hospitals():
    return render_template('Hospitals.html')

@app.route('/health-insurance')
def health_insurance():
    return render_template('HealthInsurance.html')

if __name__ == '__main__':
    app.run(debug=True)