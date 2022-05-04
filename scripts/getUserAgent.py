
def get_user_agent():
    file = open('files/userAgents.txt', 'r')
    proxies = file.read().split('\n')
    proxy = proxies[0]
    file.close()
    file_proxy = open('files/userAgents.txt', 'r')
    data = file_proxy.readlines()
    data[0] = ''
    file_proxy.close()
    with open('files/userAgents.txt', 'w') as file_with_proxy:
        file_with_proxy.writelines(data)

    return proxy






