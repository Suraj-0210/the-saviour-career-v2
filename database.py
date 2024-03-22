from json import JSONDecoder

from flask import jsonify
from sqlalchemy import create_engine,text
import requests
import os

db_connection_string = os.environ['db_connection_string']

# Connect to the database
engine = create_engine(db_connection_string)


def load_jobs_from_db():
  jobs = []
  with engine.connect() as conn:
    result = conn.execute(text('select * from jobs'))
    for row in result.all():
      jobs.append(row._asdict())
  return jobs

def load_jobs_from_db_by_id(id):
  with engine.connect() as conn:
    result = conn.execute(
      text(f"select * from jobs where id = {id}")
    )
    row = result.all()
    if len(row) == 0:
      return None
    else:
      return row[0]._asdict()

def store_application_in_db(job_id, data):
  url_post = "http://suryakanta.pythonanywhere.com/post"

  data = jsonify(data)
  # A POST request to tthe API
  requests.post(url_post, json=data)

  
  # with engine.connect() as conn:
  #   conn.execute(text(f"INSERT INTO applications (job_id, full_name, email, linkedin_url, education, work_experience, resume_url) VALUES ({job_id}, '{data['full_name']}', '{data['email']}', '{data['linkedin_url']}', '{data['education']}', '{data['work_experience']}', '{data['resume_url']}')"))

# query = text(f"INSERT INTO applications (job_id, full_name, email, linkedin_url, education, work_experience, resume_url) VALUES (:job_id, :full_name, :email, :linkedin_url, :education, :work_experience, :resume_url)")
# conn.execute(query, 
#             job_id=job_id,
#             full_name=data['full_name'],
#             email=data['email'],
#             linkedin_url=data['linkedin_url'],
#             education=data['education'],
#             work_experience=data['work_experience'],
#             resume_url=data['resume_url'])

