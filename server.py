from flask import Flask, render_template, redirect, request, session, flash
app = Flask(__name__)
app.secret_key = 'KeepItSecretKeepItSafe'

@app.route('/') #This is the root
def landing_page():

  if not ('name' in session):
    session['name'] = 0
  if not ('comment' in session):
    session['comment'] = 0

  return render_template('index.html')  

@app.route('/result', methods=['POST']) 
def result():
    session['name'] = str(request.form['name'])
    location = str(request.form['location'])
    language = str(request.form['language'])
    session['comment'] = str(request.form['comment'])
    survey = str(request.form['survey'])
    
    if len(session['name']) <= 0 or len(session['comment']) <= 0:
      flash("Name or Comment cannot be empty!")
      print session['name']
      print session['comment']
      return redirect('/')
    elif len(session['comment']) > 121:
       flash("Characters should be 120 only")
       print len(session['comment'])
       return redirect('/')
    else:
      return render_template('result.html',name = session['name'], location = location, language = language, comment = session['comment'], survey = survey)
#session for name is not working before dumping values

@app.route('/back')
def restart():
  session.pop('name')
  session.pop('comment')
  return redirect('/')
app.run(debug=True) 