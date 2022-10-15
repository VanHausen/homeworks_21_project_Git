class Request:
    def __init__(self, str):
        lst = self.get_info(str)

        self.from_ = lst[4]
        self.amount = int(lst[1])
        self.product = lst[2]

        if len(lst) > 6:
            self.to = lst[6]
        else:
            self.to = None

    def get_info(self, str):
        return str.split(" ")

    def __repr__(self):
        return f'Доставить** {self.amount} {self.product} **из** {self.from_} **в** {self.to}'
