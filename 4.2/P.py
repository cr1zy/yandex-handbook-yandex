def hello(username):
    print(f'Здравствуйте, {username}!')


def alert(username):
    print(f'!!! Попытка взлома аккаунта {username} !!!')
    print('Блокировка системы через...', 5, 4, 3, 2, 1, 'ТРЕВОГА!', sep='\n')

def login(name, password, sucess, error):
    true_password = hex(len(name) * sum([ord(i) for i in name]))[:1:-1]
    if true_password == password.lower():
        return sucess(name)
    else:
        return error(name)
    
    
login('оченьМаленькийРозовыйПони', 'EDE5A', hello, alert)




