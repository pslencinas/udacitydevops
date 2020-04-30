from flask import Flask, render_template

app = Flask(__name__)


# Show all
@app.route('/', methods=['GET'])
@app.route('/public/', methods=['GET'])
def showMain():
	
	return render_template('public.html')

if __name__ == '__main__':
	app.secret_key = "secret key"
	app.debug = True
	app.run(host = '0.0.0.0', port = 5000)
