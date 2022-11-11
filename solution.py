file = open('test.txt', 'r')
Lines = file.readlines()
allValid = True
errorCodes = []
for record in Lines:
    recordList = record.split(" ")
    res = []
    for record in recordList:
        res.append(record.replace("\n", ""))
    allValid = res[1]
    if 'true' not in res[1]:
        errorCodes.append(res[2])

if "ture" in allValid:
    print ("Yes")
else:
    print ("No")
    print(" ".join(errorCodes))