from sqlalchemy import create_engine,text

# Connect to the database
engine = create_engine("mysql+pymysql://sql6692084:kkUpAyP9Hc@sql6.freemysqlhosting.net/sql6692084?charset=utf8mb4")


def load_jobs_from_db():
  jobs = []
  with engine.connect() as conn:
    result = conn.execute(text('select * from jobs'))
    for row in result.all():
      jobs.append(row._asdict())
  return jobs


