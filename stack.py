class Stack:
    def __init__(self, max_size=None):
        # Добавляем возможность задавать максимальный размер стека
        self.items = []
        self.max_size = max_size

    def is_empty(self):
        return self.items == []

    def is_full(self):
        # Проверяем, достиг ли стек максимального размера
        if self.max_size is None:
            return False
        return len(self.items) >= self.max_size

    def push(self, item):
        # Добавляем проверку на заполненность стека
        if self.is_full():
            print("Ошибка: Стек переполнен!")
        else:
            self.items.append(item)
            print(f"Элемент '{item}' добавлен в стек.")

    def pop(self):
        if self.is_empty():
            print("Ошибка: Стек пуст!")
            return None
        else:
            item = self.items.pop()
            print(f"Элемент '{item}' удалён из стека.")
            return item

    def peek(self):
        if self.is_empty():
            print("Ошибка: Стек пуст!")
            return None
        return self.items[-1]

    def size(self):
        return len(self.items)

# Пример использования
stack = Stack(max_size=3)  # Создаём стек с максимальным размером 3
stack.push(10)             # Элемент '10' добавлен в стек.
stack.push(20)             # Элемент '20' добавлен в стек.
stack.push(30)             # Элемент '30' добавлен в стек.
stack.push(40)             # Ошибка: Стек переполнен!

stack.pop()                # Элемент '30' удалён из стека.
stack.pop()                # Элемент '20' удалён из стека.
stack.pop()                # Элемент '10' удалён из стека.
stack.pop()                # Ошибка: Стек пуст!
