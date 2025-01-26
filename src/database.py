from peewee import *
from datetime import datetime

db = SqliteDatabase('./db/control_stock.db')

class BaseModel(Model):
    class Meta:
        database = db

# def model
class Product(BaseModel):
    id = AutoField()
    name = TextField(null=False)
    category = CharField(null=True)
    price = FloatField(null=False)
    current_stock = IntegerField(default=0)

class Movements(BaseModel):
    id = AutoField()
    product = ForeignKeyField(Product, backref='movements')
    type = CharField(constraints=[Check("type IN ('in', 'out')")], null=False)
    amount = IntegerField(null=False)
    date = DateTimeField(default=datetime.now)

# Crear tablas si no existen
def init_db():
    db.connect()
    db.create_tables([Product,Movements])
