import ping3


def ping_and_decode(host):
    result = ping3.ping(host, timeout=2, unit='ms')
    if result is not None:
        return str(result)
    else:
        return "Ping failed"


ping_result_yandex = ping_and_decode('yandex.ru')
ping_result_youtube = ping_and_decode('youtube.com')

print(ping_result_yandex)
print(ping_result_youtube)