import random

# Create a deck of 52 cards
def initialize_deck():
    type_of_card = ['♤', '♢', '♧', '♡']
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K', 'A']
    deck = []

    for i in numbers:
        for j in type_of_card:
            deck.append(str(i) + j)

    random.shuffle(deck)
    return deck

def print_cards(deck):
    # Take out 3 cards from the deck then remove them from the deck
    a = [deck.pop(), deck.pop(), deck.pop()]
    # Print out the player's cards
    for i in range(len(a)):
        print(a[i], end=' ')
    print("\t|\t",end='')

    # Perform scoring work
    for i in range(len(a)):
        a[i] = a[i].replace('♤', '').replace(
            '♢', '').replace('♧', '').replace('♡', '')

    not_number = ['J', 'Q', 'K']
    result = ''
    if a[0] == 'A' and a[1] == 'A' and a[2] == 'A':
        print("Three A \t|")
        return 11
    elif a[0] in not_number and a[1] in not_number and a[2] in not_number:
        print("Three Western cards\t|")
        return 10
    else:
        for i in range(len(a)):
            if a[i] == "A":
                a[i] = a[i].replace('A', '1')
            elif a[i] == 'J' or a[i] == 'Q' or a[i] == 'K':
                a[i] = '10'
        sum = (int(a[0]) + int(a[1]) + int(a[2])) % 10
        result = sum

        print('Sum: {}'.format(result),end= '\t|\t')
        return sum

#Run game
while True:
    n = int(input("Number of players: "))
    deck = initialize_deck()
    list_point = []
    for i in range(n):
        print("Player",i+1,end='\t|\t ')
        temp = print_cards(deck)
        list_point.append(temp)
        print()
    highest_point = max(list_point)
    if list_point.count(highest_point) == 1 :
      print("The winning player is the player",list_point.index(max(list_point))+1)
    else:
      index_win = []
      for i in range(len(list_point)):
        if list_point[i] == highest_point :
          index_win.append(str(i+1))
      print("The winning players are the players",', '.join(index_win))

    play_again = input("Do you want to play again? (yes/no): ").lower()
    if play_again != 'yes':
        break