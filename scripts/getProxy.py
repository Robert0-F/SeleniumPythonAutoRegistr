def get_proxy():
    file = open('files/proxy.txt', 'r')
    proxies = file.read().split('\n')
    proxy = proxies[0]
    login, password, ip, port = proxy.split(":")
    file.close()
    file_proxy = open('files/proxy.txt', 'r')
    data = file_proxy.readlines()
    data[0] = ''
    file_proxy.close()
    with open('files/proxy.txt', 'w') as file_with_proxy:
        file_with_proxy.writelines(data)

    return login, password, ip, port






