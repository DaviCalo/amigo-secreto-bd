class PrintPretty:
    _ANSI_RESET = "\033[0m"
    _ANSI_GREEN = "\033[32m"
    _ANSI_RED = "\033[31m"
    _ANSI_YELLOW = "\033[33m"

    def green(self, text: str):
        print(self._ANSI_GREEN + text + self._ANSI_RESET)

    def yellow(self, text: str):
        print(self._ANSI_YELLOW + text + self._ANSI_RESET)

    def red(self, text: str):
        print(self._ANSI_RED + text + self._ANSI_RESET)

    def green(self, text: str):
        print(self._ANSI_GREEN + text + self._ANSI_RESET)