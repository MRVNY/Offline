fp = open('echo-request.txt', 'r')

tab = []
line = fp.readline()
while line:
    tab.append(line)
    line = fp.readline()

for line in tab:
    print(line)

fp.close()