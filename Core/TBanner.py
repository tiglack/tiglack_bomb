from colorama import Fore



_banner = '''
 ▄▄    ▄▄     ▄▄        ▄▄▄▄   ▄▄   ▄▄▄            @TIGLACK_ARXIV
 ██    ██    ████     ██▀▀▀▀█  ██  ██▀             @TIGLACK_ARXIV
 ██    ██    ████    ██▀       ██▄██               @TIGLACK_ARXIV
 ████████   ██  ██   ██        █████               @TIGLACK_ARXIV
 ██    ██   ██████   ██▄       ██  ██▄             @TIGLACK_ARXIV
 ██    ██  ▄██  ██▄   ██▄▄▄▄█  ██   ██▄            @TIGLACK_ARXIV
 ▀▀    ▀▀  ▀▀    ▀▀     ▀▀▀▀   ▀▀    ▀▀            @TIGLACK_ARXIV
'''

def banner(host, port):
    '''Вывод баннера с ссылкой'''

    print(Fore.GREEN + _banner)
    print(f'Перейдите по http://{host}:{port}')