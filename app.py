from flask import Flask, g, render_template, jsonify, url_for, flash
from flask import request, redirect, make_response
from flask import session as login_session
import random
import string
import json
import datetime

app = Flask(__name__)

@app.route('/login', methods=['GET', 'POST'])
def login():

	if request.method == 'GET':
		state = ''.join(random.choice(
				string.ascii_uppercase + string.digits) for x in range(32))
		# store it in session for later use
		login_session['state'] = state
		return render_template('login.html', STATE = state)
	else:
		if request.method == 'POST':
			print ("dentro de POST login")
			
			user = session.query(User).filter_by(
				username = request.form['username'],
				password = request.form['password']).first()

			if not user:
				error = "Usuario no registrado!!!"
				return render_template('login.html', error = error)
			else:
				print ("dentro de user")
				login_session['username'] = request.form['username']
				return render_template('public.html', username=login_session['username'])
				


@app.route('/logout')
def logout():
		
		del login_session['username']

		return render_template('public.html')

# Crear usuario
@app.route('/registrar', methods=['GET', 'POST'])
def registrar():

	if request.method == 'GET':
		return render_template('add-user.html')
	else:
		if request.method == 'POST':
			nuevoUsuario = User(
					username = request.form['username'],
					password=request.form['password'],
					email = request.form['email']) 
			session.add(nuevoUsuario)
			session.commit()
			login_session['username'] = request.form['username']
			return redirect(url_for('showMain'))

# Delete post
# /blog/eliminar/2
@app.route('/blog/eliminar/<int:id>', methods=['GET', 'POST'])
def eliminarItem(id):

	post = session.query(Blog).filter_by(id = id).one()
	# select * from blog where id=2
	if request.method == 'GET':
		return render_template('delete-post.html', post = post)
	else:
		if request.method == 'POST':
			session.delete(post)
			# delete blog set id=2
			session.commit()
			return redirect(url_for('showMain'))
					 

# Crear Post
@app.route('/agregarPost', methods=['GET', 'POST'])
def agregarPost():

	if request.method == 'GET':
		return render_template('add-post.html')
	else:
		if request.method == 'POST':
			post = Blog(
					titulo = request.form['titulo'],
					contenido=request.form['contenido'],
					fecha_creacion = datetime.datetime.now())
			session.add(post)
			session.commit()
			return redirect(url_for('showMain'))


# Show all
@app.route('/', methods=['GET'])
@app.route('/public/', methods=['GET'])
def showMain():
	
	return render_template('public.html')

if __name__ == '__main__':
	app.secret_key = "secret key"
	app.debug = True
	app.run(host = '0.0.0.0', port = 5000)
