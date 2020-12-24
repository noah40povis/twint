
import databases
import sqlalchemy


DATABASE_URL = "postgresql://noahchristian:7bear4u@localhost:5432/mydb"

database = databases.Database(DATABASE_URL)

metadata = sqlalchemy.MetaData()
