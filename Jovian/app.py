from flask import Flask, render_template, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
db = SQLAlchemy(app)


# class Job(db.Model):
#     id = db.Column(db.Integer(), primary_key=True)
#     title = db.Column(db.String(20), nullable=False)
#     location = db.Column(db.String(30), nullable=False)
#     salary = db.Column(db.String(30), nullable=False)

jobs = [
    {
        'id': 1,
        'title': 'Data Analyst',
        'location': 'Remote',
        'salary': 'Rs. 1,200,000'
    }
]


@app.route('/')
def home_page():
    # jobs = Job.query.all()
    return render_template('home.html', jobs=jobs, company_name='Jovian')


@app.route('/api/jobs')
def list_jobs():
    return jsonify(jobs)


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
