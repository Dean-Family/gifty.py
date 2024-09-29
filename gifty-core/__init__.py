from gifty_core import Giftee, Gift, initialize_database, get_session

# Initialize the database
initialize_database()

# Create a new session
session = get_session()

# Create and add a new Giftee
new_giftee = Giftee(firstname="Jane", lastname="Doe")
session.add(new_giftee)
session.commit()

print(f"Added new giftee: {new_giftee.firstname} {new_giftee.lastname}")
