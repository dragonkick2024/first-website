from flask import Flask, render_template, jsonify

app = Flask(__name__)

JOBS = [
  {
    'id': 1,
    'title': 'Data Analyst',
    'location': 'Cupertino, Califonia',
    'salary': '$100,000'
  },
  {
    'id': 2,
    'title': 'Computer Scientist',
    'location': 'Cupertino, Califonia',
    'salary': '$125,000'
  },
  {
    'id': 3,
    'title': 'Frontend Computer Scientist',
    'location': 'Cupertino, Califonia',
    'salary': '$150,000'
  },
  {
    'id': 4,
    'title': 'Backend Computer Scientist',
    'location': 'Cupertino, Califonia',
    'salary': '$200,000'
  }
]
@app.route('/')
def helloworld():
  return render_template('home.html', jobs=JOBS, company_name='Apple')

@app.route('/api/jobs')
def list_jobs():
  return jsonify(JOBS)

if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)
