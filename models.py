from peewee import Model, CharField, ForeignKeyField
from peewee_async import PooledPostgresqlDatabase

db = PooledPostgresqlDatabase(
    'iot_db',
    user='postgres',
    password='postgres',
    host='localhost',
    port=5432
)

class ApiUser(Model):
    name = CharField()
    email = CharField(unique=True)
    password = CharField()

    class Meta:
        database = db

class Location(Model):
    name = CharField()

    class Meta:
        database = db

class Device(Model):
    name = CharField()
    type = CharField()
    login = CharField()
    password = CharField()
    location = ForeignKeyField(Location, backref='devices')
    api_user = ForeignKeyField(ApiUser, backref='devices')

    class Meta:
        database = db

db.connect()
db.create_tables([ApiUser, Location, Device])