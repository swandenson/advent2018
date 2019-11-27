myfile = open("day1_input.txt", "r")
contents = myfile.read()

contents = contents.replace('+', '')

contents = contents.split("\n")

contents = [int(i) for i in contents]

listSum = sum(contents)

print(listSum)

myfile.close()