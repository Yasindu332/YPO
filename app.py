from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        name = request.form['name']
        return render_template('index.html', name=name)
    return render_template('index.html', name=None)

if __name__ == '__main__':
    app.run(debug=True)
