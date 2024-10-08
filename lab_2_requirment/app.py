from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/')
def form():
    return render_template('form.html')

@app.route('/submit', methods=['POST'])
def submit():
    name = request.form['name']
    email = request.form['email']
    age = request.form['age']
    return render_template('result.html', name=name, email=email, age=age)

if __name__ == '__main__':

    app.run(debug=True)

