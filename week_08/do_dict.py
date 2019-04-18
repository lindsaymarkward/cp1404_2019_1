def find_younger_names(name_to_age, threshold):
    names = []

    for name, age in name_to_age.items():
        if age <= threshold:
            names.append(name)

    return names
    # or
    # return [name for name, age in name_to_age.items() if age <= threshold]
