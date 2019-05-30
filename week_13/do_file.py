"""
Write a program that swaps the content of a file,
"switch.txt" between "out" and "in"
every time it runs.

open
contents = read
close

if contents == 'out'
    new_contents = 'in'

open
write new_contents
close
"""
FILENAME = "switch.txt"

in_file = open(FILENAME, 'r')
contents = in_file.read()
in_file.close()

if contents == 'out':
    new_contents = 'in'
else:
    new_contents = 'out'

out_file = open(FILENAME, 'w')
out_file.write(new_contents)
out_file.close()
