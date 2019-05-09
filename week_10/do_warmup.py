"""
Write a function definition to take in a filename and return
the longest line of that file. 
It should return a tuple of both:
(line number, length in characters)

Write a function call to show how this would be used
"""


def find_longest_line(filename):
    line_number = 0
    max_length = 0

    in_file = open(filename)
    for i, line in enumerate(in_file, 1):
        if len(line) > max_length:
            max_length = len(line)
            line_number = i
    in_file.close()
    return line_number, max_length

def main():
    line_number, length = find_longest_line("os_demos.py")
    print("line {} is the longest line with {} characters".format(line_number, length))

main()