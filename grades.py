f = open("Grades.txt", "w")

name = input("What is your name?")

grade = 0
testCount = 0
testSum = 0

while grade != -1:
	grade = float(input("Enter your test Grades."))
	testCount += 1
	testSum = testSum + grade
f.write(str(name) + "\n============\nAverage: " + str(testSum/testCount))
