
from subprocess import PIPE,Popen
from prettytable import PrettyTable
from xlwt import Workbook

wb = Workbook()
sheet1 = wb.add_sheet("LIF Report1")
sheet2 = wb.add_sheet("LIF Report2")
sheet3 = wb.add_sheet("LIF Report3")
sheet4 = wb.add_sheet("LIF Report4")
sheet5 = wb.add_sheet("LIF Report5")
sheet6 = wb.add_sheet("LIF Report6")
sheet7 = wb.add_sheet("LIF Report7")
lif = PrettyTable(["VSERVER","LIF","PROTOCOL","Home-Node","Home-Port","IP Address"])
mylist =[]
lifshow = Popen("ssh cdot-sim net int show '-fields address,vserver,data-protocol,home-port,home-node'|sed \'1d;3d\'",shell=True,stdout=PIPE,stderr=PIPE)
stdout,stderr = lifshow.communicate()
output = stdout.strip().decode('utf-8').splitlines()
count = 0
for item in output:
    liflist = item.split()

    if not 'entries' in liflist:
        mylist.append(liflist)
        count = count + 1
        lif.add_row(liflist)
    else:
        continue

print("\n{}\n".format(lif))

for i in range(len(mylist)):
    for j in range(len(mylist[i])):

        sheet1.write(i,j,mylist[i][j])


wb.save("cDot-lif.xls")