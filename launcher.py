import subprocess


server_script = 'server.py'
client_script = 'client.py'
server_address = '127.0.0.1'
server_port = '7777'
PROCESS = []

while True:
    ANSWER = input('Выберите действие: q - выход, '
                   's - запустить сервер и клиенты, x - закрыть все окна: ')

    if ANSWER == 'q':
        break
    elif ANSWER == 's':
        PROCESS.append(subprocess.Popen(['python', server_script, server_port],
                                        creationflags=subprocess.CREATE_NEW_CONSOLE))
        for i in range(5):
            PROCESS.append(subprocess.Popen(['python', client_script, server_address, server_port],
                                            creationflags=subprocess.CREATE_NEW_CONSOLE))
    elif ANSWER == 'x':
        while PROCESS:
            VICTIM = PROCESS.pop()
            VICTIM.kill()