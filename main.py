class Stack:
    def __init__(self):
        self.buffer = []

    # - проверка стека на пустоту. Метод возвращает True или False.
    def is_empty(self):
        return False if self.buffer else True

    # push - добавляет новый элемент на вершину стека.Метод ничего не возвращает.
    def push(self, argument):
        self.buffer.append(argument)

    # pop - удаляет верхний элемент стека.Стек изменяется.Метод возвращает
    # верхний элемент стека
    def pop(self):
        if self.is_empty():
            print('stack is empty')
        else:
            return self.buffer.pop()

    # peek - возвращает верхний элемент стека, но не удаляет его.Стек не меняется.
    def peek(self):
        if self.is_empty():
            return False
        else:
            return self.buffer[-1]

    # size - возвращает количество элементов в стеке.
    def size(self):
        return len(self.buffer)

    def clear_buffer(self):
        self.buffer = []


if __name__ == '__main__':
    key_dict = {'[': ']', '(': ')', '{': '}'}
    current_stack = Stack()
    ad_stack = Stack()
    while True:
        current_stack.clear_buffer()
        ad_stack.clear_buffer()
        in_string = input('Эта программа позволяет определить корректность расставленых скобок\n'
                          'Введите строку для опреледения нормализации, например ({}[](())): ')
        balance_flag = True
        for symbol_stack in list(in_string):
            if symbol_stack not in '[({})]':
                # print('Некорректные данные')
                # break
                continue
            elif symbol_stack in '[({':
                current_stack.push(symbol_stack)
            else:  # '})]'
                if current_stack.is_empty() and key_dict.get(current_stack.peek()) != symbol_stack:
                    balance_flag = False
                    break
                else:
                    current_stack.pop()
        if current_stack.is_empty() and balance_flag:
            print('Сбалансировано')
        else:
            print('Несбалансировано')

        if not input('Попробуем еще раз?(y)').upper() == 'Y':
            break
