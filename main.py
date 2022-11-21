class Generator:
    def __init__(self):
        import random
        self.__random = random
        self.letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'ñ', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
        self.symbols = ['!', '@', '#', '$', '%', '&', '*', '-', '_', '=', '+', '?']
        self.numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    def classic_generator(self, lower, capital, numbers, symbols):
        _pass = []
        usr_numbers = round(numbers)
        usr_symbols = round(symbols)
        usr_capital = round (capital)
        usr_lower = round(lower)
        lenght = usr_capital + usr_lower + usr_numbers + usr_symbols
        for i in range(usr_capital):
            _pass.append(self.__random.choice(self.letters).upper())
        for i in range(usr_lower):
            _pass.append(self.__random.choice(self.letters).lower())
        for i in range(usr_numbers):
            _pass.append(self.__random.choice(self.numbers))
        for i in range(usr_symbols):
            _pass.append(self.__random.choice(self.symbols))
        for i in range(lenght):
            self.__random.shuffle(_pass)
        return "".join(_pass)
    def quetzal_generator(self, letters, numbers, symbols):
        usr_numbers = round(numbers)
        usr_letters = round(letters)
        usr_symbols = round(symbols)
        lenght = usr_letters + usr_numbers
        div = round(lenght / (usr_symbols + 1))
        _pass = []
        for i in range(usr_numbers):
            _pass.append(self.__random.choice(self.numbers))
        for i in range(round(usr_letters / 2)):
            _pass.append(self.__random.choice(self.letters).lower())
            _pass.append(self.__random.choice(self.letters).upper())
        for i in range(lenght):
            self.__random.shuffle(_pass)
        for i in range(usr_symbols):
            i = i + 1
            _pass.insert((i * div) + (i - 1), self.__random.choice(self.symbols)) 
        return "".join(_pass)


if __name__ == "__main__":
    import sys
    if '--help' in sys.argv:
        print("quezal-mode: python3", sys.argv[0], "--quetzal", "--letters [#]", "--numbers [#]", "--symbols [#]")
        print("classic-mode: python3", sys.argv[0], "--classic", "--upper [#]", "--lower [#]", "--numbers [#]", "--symbols [#]")
        sys.exit(0)
    if '--version' in sys.argv:
        print("Password-generator", "2.0.0", "'delta'")
        print("Pasa-san, (c) 2022")
        sys.exit(0)
    if '--quetzal' in sys.argv:
        try:
            letters = int(sys.argv[sys.argv.index("--letters") + 1])
            numbers = int(sys.argv[sys.argv.index("--numbers") + 1])
            symbols = int(sys.argv[sys.argv.index("--symbols") + 1])
            gen = Generator()
            print(gen.quetzal_generator(letters, numbers, symbols))
            sys.exit(0)
        except Exception as e:
            print(e)
    if '--classic' in sys.argv:
        try:
            upper = int(sys.argv[sys.argv.index("--upper") + 1])
            lower = int(sys.argv[sys.argv.index("--lower") + 1])
            numbers = int(sys.argv[sys.argv.index("--numbers") + 1])
            symbols = int(sys.argv[sys.argv.index("--symbols") + 1])
            gen = Generator()
            print(gen.classic_generator(lower, upper, numbers, symbols))
            sys.exit(0)
        except Exception as e:
            print(e)
    print("use '--help'")