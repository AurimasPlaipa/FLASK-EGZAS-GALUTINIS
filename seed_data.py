from app import db
from app.models.id import User, Amount, Description

db.create_all()


user1 = User('ID1', 'ID2')
user2 = User('ID3', 'ID4')

db.session.add_all([user1, user2])
db.session.commit()

amount1 = Amount('bill1', 'bill2')
amount2 = Amount('bill3', 'bill4')

db.session.add_all([amount1,amount2])
db.session.commit()

description1 = Description('description1', 'description2')
description2 = Description('description3', 'description4')

db.session.add_all([description1,description2])
db.session.commit()





