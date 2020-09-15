
class ColorConsole(object):
    BLACK = '\033[30m'
    RED = '\033[31m'
    YELLOW = '\033[33m'
    BLUE = '\033[34m'
    MAGENTA = '\033[35m'
    CYAN = '\033[36m'
    WHITE = '\033[37m'
    UNDERLINE = '\033[4m'
    RESET = '\033[0m'
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

    @staticmethod
    def out(message: str, *args):
        prefix = "".join(args)
        print(f'{prefix}{message}{ColorConsole.ENDC}')


if __name__ == "__main__":
    ColorConsole.out('This is a test Message',
                     ColorConsole.RED, ColorConsole.BOLD)
