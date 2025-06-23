class PrintPretty:
    _ANSI_RESET = "\u001B[0m"
    _ANSI_GREEN = "\u001B[32m"
    _ANSI_RED = "\u001B[31m"
    _ANSI_YELLOW = "\u001B[33m"

    def green(self, text: str):
        print(self._ANSI_GREEN + text + self._ANSI_RESET)

    def yellow(self, text: str):
        print(self._ANSI_YELLOW + text + self._ANSI_RESET)

    def red(self, text: str):
        print(self._ANSI_RED + text + self._ANSI_RESET)

    def green(self, text: str):
        print(self._ANSI_GREEN + text + self._ANSI_RESET)