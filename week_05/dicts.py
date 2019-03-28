name_to_age = {"Bill": 21, "Jane": 34, "Sven": 56}

# name_to_age[name] = age
for name, age in name_to_age.items():
    print("{:12} - {:8}".format(name, age))
