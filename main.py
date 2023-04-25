import string


class SyntaxAnalyzer:
    """
    МЛиТА-2023 ИДЗ№2
    Группа 1305, студент Димитрий Перчаткин, вариант №12

        Правильная скобочная запись арифметических выражений с одной операцией - операцией
    умножения и двумя видами скобок. Причем знак умножения не пишется и обозначается
    отсутствием знака. Выражение в скобках, если есть, то не может начинаться с квадратной
    скобки. Могут быть “лишние” скобки, но одна буква не может браться в скобки.

    Пример          Правильная запись: [a((bcd))(((ac)d[ab](aaa)))]
                    Неправильная запись: [(ccc)a([ab]([cd](abc)(b)))]

    Press ctrl+c to exit...
    """

    def __init__(self, input_string):
        self.__index = -1
        self.__string = input_string
        self.ch = ''
        self.read()

    def read(self):
        if self.__index + 1 < len(self.__string):
            self.__index += 1
            self.ch = self.__string[self.__index]
        else:
            self.ch = "success"
        
    def language(self):
        if self.ch in string.ascii_lowercase:
            self.content()
        elif self.ch == '(':
            self.content()
        elif self.ch == '[':
            self.content()

    def content(self):
        if self.ch in string.ascii_lowercase:
            self.letter()
            self.language()
        elif self.ch == '(':
            self.read()
            self.expression()
            if self.ch == ')':
                self.read()
                self.language()
            else:
                raise ValueError
        elif self.ch == '[':
            self.read()
            self.expression()
            if self.ch == ']':
                self.read()
                self.language()
            else:
                raise ValueError
        else:
            raise ValueError

    def expression(self):
        if self.ch in string.ascii_letters:
            self.letter()
            self.content()
            self.language()
        elif self.ch == '(':
            self.read()
            self.expression()
            if self.ch == ')':
                self.read()
                self.language()
            else:
                raise ValueError
        else:
            raise ValueError

    def letter(self):
        if self.ch in string.ascii_letters:
            self.read()
        else:
            raise ValueError
        
    def main(self):
        try:
            self.language()
        except ValueError:
            print(f"Result: ERROR")
        else:
            if self.ch == "success":
                print(f"Result: OK")


if __name__ == "__main__":
    print(SyntaxAnalyzer.__doc__)
    while True:
        try:
            syntax_analyzer = SyntaxAnalyzer(input("Insert string: "))
            syntax_analyzer.main()
        except KeyboardInterrupt:
            break
