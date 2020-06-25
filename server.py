from flask import Flask, render_template, url_for, request, redirect
import csv

app = Flask(__name__)


@app.route('/')  # Anytime we hit /(aka root) define the hello_world function
def myHome():
    return render_template('index.html')


@app.route('/<string:page_name>')
def html_page(page_name):
    return render_template(page_name)


def writeToFile(data):
    with open('database.txt', mode='a') as database:
        email = data["email"]
        subject = data["subject"]
        message = data["message"]
        file = database.write(f'\n{email},{subject},{message}')


def writeToCsv(data):
    with open('database.csv', mode='a', newline='') as db:
        email = data["email"]
        subject = data["subject"]
        message = data["message"]
        file = csv.writer(db, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        file.writerow([email, subject, message])


@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method == 'POST':
        try:
            data = request.form.to_dict()
            # writeToFile(data)
            writeToCsv(data)
            return redirect('/thanks.html')
        except:
            return 'Did not save to database'
    else:
        return 'Something went wrong try again now'

# @app.route('/thanks/<email>')
# def thanks(email=None):
#     return render_template('thanks.html', email=email)
