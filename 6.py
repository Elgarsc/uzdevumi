def rewards(self,amount):
        amount = random.randint(1, 100)
        if Account(self.datetime_created) == (2022, 4, 1):
            self.transactions.append(Transaction(amount))
