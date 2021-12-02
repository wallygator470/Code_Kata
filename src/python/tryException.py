actor = {"name": "John Cleese", "rank": "awesome"}

#Function to modify, should return the last name of the actor - think back to previous lessons for how to get it
def get_last_name():
    return actor["name"].split()[1]

#Test code
get_last_name()
print("All exceptions caught! Good job!")
print("The actor's last name is %s" % get_last_name())