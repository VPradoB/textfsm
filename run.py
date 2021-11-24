import textfsm
from tabulate import tabulate

template = "templates/cisco_xr/show_processes_cpu.textfsm"
command_file = "files/cisco_xr/show_processes_cpu"
output_path = "out/cisco_xr/show_processes_cpu.out"

with open(template) as t, open(command_file) as c:
    with open(output_path, "w") as o:
        re_table = textfsm.TextFSM(t)
        header = re_table.header
        p = c.read()
        raw_result = re_table.ParseText(p)
        result = tabulate(raw_result, headers=header)
        print(result, file=o)
        print(result)
