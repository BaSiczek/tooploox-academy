class Player:
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance
    def __str__(self):
        return('{} your current balance is: {}'.format(self.name, self.balance))
    def bet(self, bet_amount):
        pass

player_name = input("What is your name? ")
player_balance = input("What is your balance? ")

player = Player(player_name, player_balance)
print(player)

#one play:

bet_amount = input("How much you bet?")
