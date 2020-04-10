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
            print('stack is empty')
        else:
            return self.buffer[len(self.buffer)-1]

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
        for symbol_stack in list(in_string):
            current_stack.push(symbol_stack)

        if current_stack.is_empty():
            print('Нет данных')
        else:
            while current_stack.size():
                current_symbol_pair = key_dict.get(current_stack.peek())
                if not current_symbol_pair:
                    ad_stack.push(current_stack.pop())
                else:
                    if ad_stack.peek() == current_symbol_pair:
                        current_stack.pop()
                        ad_stack.pop()
                    else:
                        print('Несбалансированно')
                        break

            if not current_stack.size() and not ad_stack.size():
                print('Сбалансировано')
        # print(ad_stack.buffer)
        # print(current_stack.buffer)
        if not input('Попробуем еще раз?(y)').upper() == 'Y':
            break
