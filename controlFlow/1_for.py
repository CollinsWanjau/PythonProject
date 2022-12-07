#!/usr/bin/python3
# Create a sample collection

# modifying code while iterating it can be tricky
# it is usually more straight-forward to loop over a
# copy of the collection or to create a new collection

# items() - used to return the list with all the dictionary
# keys with values.It takes no parameter

# del - used to delete a key a key that does exist
# indexing notattion is used to retrieve the item from the
# dictionary we want to use
users = {'Hans': 'active', 'Éléonore': 'inactive', '景太郎': 'active'}

# Strategy: Iterate over a copy
for user, status in users.copy().items():
    if status == 'inactive':
        del users[user]
        print(users)

# Strategy: Create a new collection
active_users = {}
for user, status in users.items():
    if status == 'active':
        active_users[user] = status
        print(active_users)
