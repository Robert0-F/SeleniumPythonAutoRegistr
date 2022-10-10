
def get_user_agent():
    file = open('files/agents.txt', 'r')
    proxies = file.read().split('\n')
    proxy = proxies[0]
    file.close()
    file_proxy = open('files/agents.txt', 'r')
    data = file_proxy.readlines()
    data[0] = ''
    file_proxy.close()
    with open('files/agents.txt', 'w') as file_with_proxy:
        file_with_proxy.writelines(data)

    return proxy






