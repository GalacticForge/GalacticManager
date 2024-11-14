import colorama, time

class Colors:
    @staticmethod
    def INFO():
        return f"{colorama.Fore.LIGHTBLACK_EX}[{time.strftime('%H:%M:%S')}][INFO]{colorama.Style.RESET_ALL}"
    
    @staticmethod
    def SUCCESS():
        return f"{colorama.Fore.GREEN}[{time.strftime('%H:%M:%S')}][SUCCESS]{colorama.Style.RESET_ALL}"
    
    @staticmethod
    def WARNING():
        return f"{colorama.Fore.YELLOW}[{time.strftime('%H:%M:%S')}][WARNING]{colorama.Style.RESET_ALL}"
    
    @staticmethod
    def ERROR():
        return f"{colorama.Fore.RED}[{time.strftime('%H:%M:%S')}][ERROR]{colorama.Style.RESET_ALL}"
    
    @staticmethod
    def DIVIDER():
        return f"{colorama.Fore.CYAN}{colorama.Style.RESET_ALL}"