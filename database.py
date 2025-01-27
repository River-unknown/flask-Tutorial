from sqlalchemy import create_engine,text
import os

db_conn_String = os.environ["DB_CONNECTION_STRING"]



engine = create_engine(db_conn_String
, connect_args={"ssl": {"ssl_ca": os.environ["CA_CERTIFICATE"]}}
)
def load_jobs_from_db():
  with engine.connect() as conn:
    result = conn.execute(text("select * from jobs"))


  jobs = []
  for row in result.all():
    jobs.append(row._mapping)

  return jobs