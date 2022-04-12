from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String

# engine = create_engine('sqlite:///college.db', echo=True)
engine = create_engine("mysql://root:raghu@localhost/college", echo=True)

# mysql+pymysql://<username>:<password>@<host>/<dbname>

meta = MetaData()

students = Table(
    'students', meta,
    Column('id', Integer, primary_key=True),
    Column('name', String(16)),
    Column('lastname', String(16)),
)
meta.create_all(engine)
