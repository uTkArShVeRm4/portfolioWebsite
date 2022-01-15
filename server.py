from flask import Flask, render_template, request
import csv

app = Flask(__name__)

@app.route("/", methods=["POST"])
def home_page():
    if request.method == "POST":
        return render_template('index.html')
    return render_template('index.html')

def writeToFile(data):
    with open('database.txt', mode='a') as database:
        name = data['name']
        email = data['email']
        subject = data['subject']
        message = data['message']
        file = database.write(f'\n{name} from {email} said {subject}. {message}')

def writeToCSV(data):
    with open('database.csv', mode='a', newline='') as database:
        name = data['name']
        email = data['email']
        subject = data['subject']
        message = data['message']
        
        csv_writer = csv.writer(database, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow([name,email,subject,message])

@app.route("/submit_form", methods = ['POST', 'GET'])
def submit_form():
    if request.method == "POST":
        data = request.form.to_dict()
        writeToCSV(data)
        return render_template('FormSubmitted.html')


