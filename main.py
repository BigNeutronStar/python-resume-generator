from flask import Flask, render_template

import resume_manipulator
app = Flask(__name__, template_folder='templates')

@app.route("/")


def home():
    return render_template('index.html', data=resume_manipulator.generate_resume())

if (__name__ == '__main__'):
    resume_manipulator.generate_resume()
    app.run(host="0.0.0.0", port=5535, debug=True)