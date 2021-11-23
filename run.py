import textfsm
from tabulate import tabulate

template = "templates/cisco_ios_xe/sh_ip_route_summary.textfsm"
command_file = "files/cisco_ios_xe/sh_ip_route_summary"
output_path = "out/cisco_ios_xe/sh_ip_route_summary.out"

with open(template) as t, open(command_file) as c:
    with open(output_path, "w") as o:
        re_table = textfsm.TextFSM(t)
        header = re_table.header
        p = c.read()
        raw_result = re_table.ParseText(p)
        result = tabulate(re_table.ParseText(p), headers=header)
        print(result, file=o)
        print(result)
