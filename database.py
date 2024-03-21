from sqlalchemy import create_engine,text
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
  with engine.connect() as conn:
    query = text(f"insert into applications (job_id, full_name, email, linkedin_url, education, work_experience, resume_url) values ({str(job_id)}, {str(data['full_name'])}, {str(data['email'])}, {str(data['linkedin_url'])}, {str(data['education'])}, {str(data['work_experience'])}, {str(data['resume_url'])});")
    conn.execute(query)
