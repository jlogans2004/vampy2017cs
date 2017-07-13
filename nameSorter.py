import Sorting
rFilename = "/home/vampy/data/test3"
wFilename = "/home/vampy/data/test4"
fp = open(rFilename, "r")

N = int(fp.readline())
names = []

for i in range(N):
	names.append(fp.readline().strip())

fp.close()

Sorting.mergeSort(names)
fp = open(wFilename, "w")
fp.write("First: "+ "{0}\n".format(names[0]))
fp.write("Third: "+ "{0}\n".format(names[2]))
fp.write("Last: "+ "{0}\n".format(names[N-1]))
fp.close()
