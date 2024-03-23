from flask import Flask, jsonify, render_template, request
from database import load_jobs_from_db, load_jobs_from_db_by_id, store_application_in_db

app = Flask(__name__)


@app.route('/careers')
def helloWorld():
  jobs = load_jobs_from_db()
  return render_template('home.html', jobs=jobs)


@app.route('/api/jobs')
def list_jobs():
  jobs = load_jobs_from_db()
  return jsonify(jobs)

@app.route('/jobs/<id>')
def show_jobs(id):
  job = load_jobs_from_db_by_id(id)
  if not job:
    return 'Not Found', 404
  else:
    return render_template('jobpage.html',job=job)


@app.route('/job/<id>/apply', methods=['post'])
def apply_to_job(id):
  data = request.form
  job = load_jobs_from_db_by_id(id)

  store_application_in_db(id, data)

  return render_template('application_submittd.html', application=data, job=job)


if __name__ == '__main__':
  app.run(host='0.0.0.0', debug=True, port=8080)
