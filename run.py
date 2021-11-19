import os
import textfsm
from tabulate import tabulate

template = 'templates/cisco_xr/cisco_xr_show_ip_bgp_neighbors.textfsm'
command_file = 'files/cisco_xr/show_ip_bgp_neighbor'
output_path = 'out/cisco_xr/show_ip_bgp_neighbor.out'

with open(template) as t, open(command_file) as c:
    with open(output_path, 'w') as o:
        re_table = textfsm.TextFSM(t)
        header = re_table.header
        p = c.read()
        result = tabulate(re_table.ParseText(p), headers=header)
        print(result, file=o)
        print(result)