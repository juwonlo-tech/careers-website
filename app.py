from flask import Flask, jsonify, render_template

app = Flask(__name__)

JOBS = [{
    'id': 1,
    'title': 'Data Analyst',
    'location': 'New York',
    'salary': 80000
}, {
    'id': 2,
    'title': 'Data Analyst',
    'location': 'Calgary',
    'salary': 65000
}, {
    'id': 3,
    'title': 'Cloud Engineer',
    'location': 'New Delhi',
    'salary': 120000
}, {
    'id': 4,
    'title': 'UI/UX Developer',
    'location': 'Remote'
}]


@app.route('/')
def hello_world():
  return render_template('home.html', jobs=JOBS)
  
@app.route('/api/jobs')
def list_jobs():
  return jsonify(JOBS)

if __name__ == '__main__':
  app.run(host='0.0.0.0', debug=True)
