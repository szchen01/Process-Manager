#Setup
import sys
if "-v" in sys.argv:
    verbose = True
    sys.argv.remove("-v")
else:
    verbose = False
if len(sys.argv) != 3:
    print(f"Usage: {sys.argv[0]} <test case> <thread count> [-v]")
    print("Finds a solution for a given test case.")
    print("test case should be a file containing the data value")
    print("The starter code automatically parses the input file for you, and writes an answer in the appropriate format")
    print("You can save your answer by piping your output to a file (assuming you have no additional print statements)")
    print(f"ex: {sys.argv[0]} Test1.txt 2 > answer.out")
    print("An optional -v argument is included, but currently does nothing. You may want to use it as a verbose flag,")
    print("so that debugging data gets printed only when verbose is set to True.")
    exit()

#Parse input
def parsetestfile(testfile):
    data = testfile.readlines()[1:]
    result = []
    for i in data:
        element = [int(j) for j in i.strip().split(" ")]
        result.append({"TaskID":element[0], "runtime":element[1], "prerequisites":element[3:]})
    return result
testfile = open(sys.argv[1])
test = parsetestfile(testfile)
testfile.close()
threadcount = int(sys.argv[2])

#Return a list of length threadcount, where each list details what each thread does
def findsolution(test, threadcount):
    #YOUR SOLUTION HERE
    if verbose:
        print(test)
    finished = []
    returnlst = []
    work = []
    total_tasks = len(test)
    for _ in range(threadcount):
        returnlst += [[]]
        work.append(0)
    if verbose:
        print(f"work len: {len(work)}")
        print(f'returnlst len: {len(returnlst)}')
    while len(finished) < total_tasks:
        free = []
        for i in range(len(work)):
            if work[i] == 0:
                free.append(i)
        for i in free:
            found_work = False
            for task in test:
                if all(x in finished for x in task["prerequisites"]):
                    returnlst[i].append(task["TaskID"])
                    work[i] = task["runtime"]
                    test.remove(task)
                    free.pop(0)
                    found_work = True
                    break
            if not found_work:
                break

        for i in range(len(work)):
            if work[i] == 1:
                finished.append(returnlst[i][-1])
            if work[i] > 0:
                work[i] -= 1

                

    # return [list(range(len(test)))]+[[]]*(threadcount-1)
    print(returnlst)
    return returnlst



result = findsolution(test, threadcount)
val = ""
for i in result:
    for j in i:
        val+=str(j)+","
    val=val[:-1]+";"
f = open("solution.txt", "w")
f.write(val[:-1])
f.close()
# f = open("solution.txt", "r")
# print(f.read())
print(val[:-1])
