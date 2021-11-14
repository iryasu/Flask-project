from flask.scaffold import F
from app import db, Puppy


## CREATE ##
my_puppy = Puppy('Goldie', 6)
db.session.add(my_puppy)
db.session.commit()

## READ ##
all_puppies = Puppy.query.all()  #all instances of Puppy
print(all_puppies)

## SELECT BY ID  ##
puppy_one = Puppy.query.get(1)
print(puppy_one)

## FILTERS  ##
puppy_frankie = Puppy.query.filter_by(name='Frankie')     #transforms this python code into SQL statements
print(puppy_frankie.all())

######### UPDATE
first_puppy = Puppy.query.get(1)
first_puppy.age = 10
db.session.add(first_puppy)
db.session.commit()

######## DELETE
second_puppy = Puppy.query.get(2)
db.session.delete(second_puppy)
db.session.commit()

#
all_puppies2 = Puppy.query.all()
print(all_puppies2)