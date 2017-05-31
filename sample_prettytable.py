
from subprocess import PIPE, Popen
from prettytable import PrettyTable
x = PrettyTable(["FileType","Links","User","Group","Bytes","Month","Day","Time","Dir/File"])
#x.padding_width = 1

host = "192.168.0.18"
mymac = Popen("ls -ltr",shell=True, stdout=PIPE, stderr=PIPE)
stdout,stderr = mymac.communicate()
output = stdout.strip().decode('utf-8').splitlines()
for line in output:
    print(line)
    if not "total" in line:
        y = line.strip().split()


        x.add_row(y)
    else:
        continue
print ("\n{}\n".format(x))








