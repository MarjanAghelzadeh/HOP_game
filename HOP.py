
def game(n):
    for i in range(n):
        if i%3 == 0 and i%5 == 0:
            print('Ha')
        elif i % 3 == 0:
            print('Hop')
        elif i%5 == 0:
            print('Yo')
        else:
            print(i)
game(105)