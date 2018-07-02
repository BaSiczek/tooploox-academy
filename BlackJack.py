class Player:
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance
        self.currentBet = 0

    def __str__(self):
        return('{} your current balance is: {}'.format(self.name, self.balance))

    def bet(self, bet_amount):
        if bet_amount in range(0, self.balance+1):
            self.currentBet = bet_amount
            self.balance -= bet_amount
            print('Great')
        else:
            print('Insufficient balance')



player_name = input("What is your name? ") #'Tom

try:
    player_balance = int(input("What is your balance? ")) #5000
except ValueError:
    print('Value should be an integer')

player = Player(player_name, player_balance)
#print(player)

#one play:

bet_amount = int(input("How much you bet? "))
player.bet(bet_amount)
