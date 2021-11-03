import os
import textfsm
from tabulate import tabulate

template = 'templates/cisco_ios/show_ip_bgp_neighbor,textfsm'
command_file = 'files/cisco_ios/show_ip_bgp_neighbor'
output_path = 'out/cisco_ios/show_ip_bgp_neighbor.out'

with open(template) as t, open(command_file) as c:
    with open(output_path, 'w') as o:
        re_table = textfsm.TextFSM(t)
        header = re_table.header
        p = c.read()
        result = re_table.ParseText(p)
        print(result, file=o)
        print(tabulate(result, headers=header))
