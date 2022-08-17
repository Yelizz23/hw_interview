class Stack:
    def __init__(self):
        self.stack = []

    # проверка стека на пустоту. Метод возвращает True или False
    def isEmpty(self):
        return self.stack or False

    # добавляет новый элемент на вершину стека. Метод ничего не возвращает
    def push(self, _item):
        self.stack.append(_item)

    # удаляет верхний элемент стека. Стек изменяется. Метод возвращает верхний элемент стека
    def pop(self):
        return self.stack.pop()

    # возвращает верхний элемент стека, но не удаляет его. Стек не меняется.
    def peek(self):
        if self.isEmpty():
            return self.stack[-1]

    # возвращает количество элементов в стеке
    def size(self):
        return len(self.stack)


def check_balance(string_):
    balance = True
    stack = Stack()
    for i in string_:
        if i in '({[':
            stack.push(i)
        else:
            if not stack.isEmpty():
                balance = False
                break
            elif stack.peek() == '(' and i == ')':
                stack.pop()
                continue
            elif stack.peek() == '{' and i == '}':
                stack.pop()
                continue
            elif stack.peek() == '[' and i == ']':
                stack.pop()
                continue
            else:
                balance = False
                break
    if balance is True:
        return 'Сбалансировано'
    else:
        return 'Несбалансировано'


if __name__ == '__main__':
    print(check_balance('[[([])((([[[]]])))]{()}'))
    print(check_balance('[[{())}]'))
