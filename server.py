from flask import Flask , render_template, request
import csv
app = Flask(__name__)
print (__name__)

@app.route('/')
def home():
	return render_template('index.html')


@app.route('/<string:page_name>')
def links(page_name):
	return render_template(page_name)

def write_to_file(data):
	with open('./database.txt', 'a') as database:
		email = data['email']
		subject = data['subject']
		message = data['message']
		file=database.write(f'\n{email},{subject},{message}')

def write_to_csv_file(data):
	with open('./database.csv', 'a', newline='') as file:
		email = data['email']
		subject = data['subject']
		message = data['message']        
		csv_writer = csv.writer(file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
		csv_writer.writerow([email,subject,message])
		

@app.route('/submit_form', methods=['POST', 'GET'])
def submit():
	if request.method=='POST':
		data = request.form.to_dict()
		write_to_csv_file(data)
		return render_template('submit.html')