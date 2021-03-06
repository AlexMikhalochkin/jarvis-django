import requests


def get_port_status(port):
    response = requests.get('http://192.168.100.14/sec/?cmd=all').text
    return response.split(';')[port] == 'ON'


def turn_on(port):
    change_status(port, 1)


def turn_off(port):
    change_status(port, 0)


def change_status(port, status):
    endpoint = 'http://192.168.100.14/sec/?pt={pt}&cmd={pt}:{status}'
    requests.get(endpoint.format(pt=port, status=status))
