from gb_chat.task_2 import host_range_ping
from tabulate import tabulate

def host_range_ping_tab(start_ip, end_ip):
    response_tab = host_range_ping(start_ip, end_ip)
    print()
    print(tabulate([response_tab], headers='keys', tablefmt="pipe", stralign="center"))


if __name__ == "__main__":
    start_ip = '192.168.0.250'
    end_ip = '192.168.0.254'
    host_range_ping_tab(start_ip, end_ip)
