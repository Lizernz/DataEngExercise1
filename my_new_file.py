with open("my_new_file.txt", "w") as outfile:
    outfile.write("Hello World! \n")
    outfile.write("This is a text file")

with open("my_new_file.txt", "r+") as file:
    for new_line in file:
        print(new_line.strip())

with open("my_new_file.txt", "a") as file:
    file.write("\nThis line was appended using python")



