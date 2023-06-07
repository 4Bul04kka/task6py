from flask import Flask, render_template, request
import re

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html', output='')

@app.route('/debug', methods=['POST'])
def debug():
    regex = request.form['regex']
    text = request.form['text']
    output = ', '.join(re.findall(regex, text))
    return render_template('index.html', regex=regex, text=text, output=output)

if __name__ == '__main__':
    app.run(debug=True)
