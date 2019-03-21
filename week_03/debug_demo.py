def is_valid_label(label):
    """Determine if the input label matches the requirements:
    labels must start with a capital, have at least 5 characters
    and at least one number"""
    label = label.upper()
    if len(label) < 5:
        return False
    if not label[0].isupper():
        return False
    for char in label:
        if not char.isnumeric():
            return False
    return True


# This code doesn't look too bad, but does it work?
# We can run it with some tests, e.g.
print(is_valid_label("demo"))
print(is_valid_label("Demo."))
print(is_valid_label("Demo 7"))
