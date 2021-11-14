from app import db, Puppy


# Create all the tables of the model
db.create_all()

sam = Puppy('Sammy', 3)
frank = Puppy('Frankie', 4)

print(sam.id)
print(frank.id)

db.session.add_all([sam, frank])

# Or one by one : db.session.add(sam)

db.session.commit()

print(sam.id)
print(frank.id)