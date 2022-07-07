import random

player_one_score = 0
player_two_score = 0

deck = []

def create_deck():
    for suit in('Hearts','Diamonds','Clubs','Spades'):
        for rank in range(2,15):
            deck.append((rank,suit))

def readable_card(card):
    if card[0] <= 11: rank = str( card[0])
    if card[0] == 11: rank = ' Jack'
    if card[0] == 12: rank = ' Queen'
    if card[0] == 13: rank = ' King'
    if card[0] == 14: rank = ' Ace'
    fullname = rank + 'of' + card[1]
    return fullname

def draw_card(player):
    card = deck[0]
    deck.remove(deck[0])
    print(player + ' drew the' + readable_card( card))
    return card

create_deck()

random.shuffle(deck)

while True:
    player_one_card = draw_card('Player one')
    player_two_card = draw_card('Player two')


    if player_one_card[0] > player_two_card[0]:
        winner = 'Player one'
        player_one_score += 2
    elif player_one_card[0] < player_two_card[0]:
        winner = 'Player two'
        player_two_score += 2
    else: winner = 'No one'

    print(winner + ' wins!')
    if len(deck) == 0:
        print('Game over. deck is empty')
        print('Player one:' + str(player_one_score))
        print('Player two:' + str(player_two_score))
    break