from ipaddress import ip_address
from subprocess import Popen, PIPE


def host_range_ping(start_ip, end_ip):
    results = {'Доступные узлы': "", 'Недоступные узлы': ""}
    start = ip_address(start_ip)
    end = ip_address(end_ip)
    ip_addresses = []
    while start <= end:
        ip_addresses.append(start)
        start += 1
    for address in ip_addresses:
        try:
            address = ip_address(address)
        except ValueError:
            pass
        timeout = 500
        requests = 1
        proc = Popen(f"ping {address} -w {timeout} -n {requests}", shell=False, stdout=PIPE)
        proc.wait()
        if proc.returncode == 0:
            results['Доступные узлы'] += f"{str(address)}\n"
            res_string = f'{address} - Узел доступен'
        else:
            results['Недоступные узлы'] += f"{str(address)}\n"
            res_string = f'{address} - Узел недоступен'
        print(res_string)
    return results


if __name__ == "__main__":
    start_ip = '192.168.0.250'
    end_ip = '192.168.0.254'
    host_range_ping(start_ip, end_ip)
