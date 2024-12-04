#reads entire info on data.txt
file = open("doro.txt", "r")
print(file.read())

#writes a modified version to a new file
file1 = open("write.txt", "w")
file1.write("I love nature and adventure. ")
file1 = open("write.txt", "a")
file1.write("I see you")
file1 = open("write.txt", "r")

#merging data.txt into new file1
for data in file:
    file1.write(data)
print(file1.read())