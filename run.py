import sys
import textfsm
from tabulate import tabulate
template = './templates/show_bgp_ipv4_all_neighbors_performance-statistics.textfsm'
output_file = './files/show_bgp_ipv4_all_neighbors_performance-statistics.txt'
with open(template) as f, open(output_file) as output:
    re_table = textfsm.TextFSM(f)
    header = re_table.header
    p = output.read()
    result = re_table.ParseText(p)
    print(result)
    print(tabulate(result, headers=header))