from flask import Flask, render_template 

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/feedback')
def feedback():
    return render_template('feedback.index.html')

@app.route('/autor')
def autor():
    return render_template('autor.index.html')

@app.route('/about_site')
def aboute_site():
    return render_template('about_site.index.html')


app.run(debug=True)