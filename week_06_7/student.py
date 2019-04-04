class Student:

    def __init__(self, first_name="", last_name="", student_id=0):
        self.first_name = first_name
        self.last_name = last_name
        self.id = student_id
        self.subjects = set()

    def __str__(self):
        return "{} {} ({}); subjects: {}".format(self.first_name, self.last_name, self.id, self.subjects)

    def add_subject(self, subject):
        self.subjects.add(subject)
        # if subject not in self.subjects:
        #     self.subjects.append(subject)

    def is_doing_subject(self, subject):
        return subject in self.subjects


def main():
    # Simple example class usage (client code)
    first_name = "Lindsay"
    last_name = "Ward"
    student_id = 1
    # first_name = input("First name: ")
    # last_name = input("Last name: ")
    # student_id = int(input("ID: "))

    s1 = Student(first_name, last_name, student_id)
    print(s1.first_name, "has ID", s1.id)

    subject = input("Subject: ")
    while subject != "":
        s1.add_subject(subject)
        subject = input("Subject: ")

    # subject = "CP1404"
    # s1.add_subject(subject)
    # subject = "CP3402"
    # s1.add_subject(subject)
    print(s1.subjects)

    # print("CP1404" in s1.subjects)
    print(s1.is_doing_subject("CP1404"))

    print(s1)


main()
