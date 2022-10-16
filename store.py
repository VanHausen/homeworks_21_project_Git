from storage import Storage


class Store(Storage):
    def __init__(self):
        self.items = {}
        self.capacity = 100


    def add(self, name, count):
        if self.get_free_space() > count:
            if name in self.items:
                self.items[name] += count
            else:
                self.items[name] = count
            print("Товар добавлен")
        else:
            print(f"Товар не может быть добавлен, так как есть место только на {self.get_free_space()} товаров")

    def remove(self, name, count):
                if self.items[name] - count >= 0:
                    self.items[name] = self.items[name] - count
                elif self.items[name] - count <= 0:
                    print(f"Слишком мало {name}")
                else:
                    print(f"{name.title()} - нет на складе")

    def get_free_space(self):
        return self.capacity - sum(self.items.values())

    def get_item(self):
        return self.items

    def get_unique_items_count(self):
        return len(self.items.keys())