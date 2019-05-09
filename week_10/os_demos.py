"""CP1404 In-class demo of os module with file handling.
find_in_files comes from the chapter 14 lecture notes.
The example uses the "Lyrics" files/folders from prac 9.
Note the use of exception handling as some of these files have unreadable characters.
"""

import os


def main():
    print(os.getcwd())
    os.chdir('..')
    print(os.getcwd())


def find_in_files(search_string, file_extension, files_found):
    """Find files of type file_extension that contain search_string."""
    count = 0
    for directory_name, directories, filenames in os.walk(
            "."):
        for filename in filenames:
            if os.path.splitext(filename)[1] == file_extension:
                count += 1
                current_file = open(os.path.join(directory_name, filename), 'r')
                try:
                    text = current_file.read()
                except UnicodeDecodeError:
                    print("Problem reading", os.path.join(directory_name, filename))
                    continue
                if search_string in text:
                    full_filename = os.path.join(directory_name, filename)
                    files_found.append(full_filename)
                current_file.close()
    return count


def test_find():
    filenames = []
    os.chdir('Lyrics')
    file_extension = ".txt"
    search_string = ".i"
    count = find_in_files(search_string, file_extension, filenames)
    print("Examined {} {} files and found '{}' in:\n{}".format(count, file_extension, search_string, filenames))


if __name__ == '__main__':
    # main()
    test_find()
