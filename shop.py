from store import Store


class Shop(Store):
    def __init__(self, limit=5):
        super().__init__()
        self.capacity = 30
        self._limit = limit
        self.items = {}

    @property
    def get_item_limit(self):
        return self._limit

    def add(self, name, count):
        if self.get_unique_items_count() < self._limit:
            super().add(name, count)
        else:
            print(f"Товар не может быть добавлен")

    def get_unique_items_count(self):
        return len(self.items.keys())