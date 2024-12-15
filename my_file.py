with open("my_file.txt", "w") as outfile:
    outfile.write("This is a text file")

with open("my_file.txt", "r") as infile:
    lines = infile.readlines()
    line_count = len(lines)
    print(f"{line_count}")
