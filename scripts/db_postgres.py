from sqlalchemy import create_engine

engine = create_engine('postgresql://user:password@localhost:5432/mydatabase')
print('Connected to PostgreSQL')
