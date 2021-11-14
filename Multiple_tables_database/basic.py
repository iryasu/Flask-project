# CREATING ENTRIES INTO THE DB
from app import db, Puppy, Toy, Owner


# CREATING 2 PUPPIES
rufus = Puppy('Rufus')
fido = Puppy('Fido')

# ADD PUPPIES TO DB
db.session.add_all([rufus, fido])
db.session.commit()


# check
print(Puppy.query.all())

rufus = Puppy.query.filter_by(name='Rufus').first()
print(rufus)

# CREATE OWNER
mark = Owner('Mark', rufus.id)

# ADD TOYS
toy1 = Toy('Chew Toy', rufus.id)
toy2 = Toy('Ball', rufus.id)

db.session.add_all([mark, toy1, toy2])
db.session.commit()

rufus = Puppy.query.filter_by(name='Rufus').first()
print(rufus)

# db.session.delete(Puppy.query.all)
# db.session.delete(Toy.query.all)
# db.session.delete(Owner.query.all)