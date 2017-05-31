
from prettytable import PrettyTable



lif = PrettyTable(["VSERVER","LIF","PROTOCOL","Home-Node","Home-Port","IP Address"])
myargs = ['ssh cdot-sim net int show \'-fields address,vserver,data-protocol,home-port,home-node\'|sed 1,3d','-user','admin']
print(myargs)
lifshow = Popen(myargs,shell=True,stdout=PIPE,stderr=PIPE)
lifshow.stdin.write('Muppala143\n')
lifshow.stdin.flush()
stdout,stderr = lifshow.communicate()
output = stdout.strip().splitlines()
for item in output:
    liflist = item.split()
    if not 'entries' in liflist:
        lif.add_row(liflist)
    else:
        continue
print("\n{}\n".format(lif))