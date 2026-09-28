def coin_change(amount, coin):
    
    coin.sort(reverse=True)

    change = []
    largest = 0

    while amount > 0:

        if amount < coin[largest]:
            largest += 1

        else:
            change.append(coin[largest])
            amount -= coin[largest]

    print(change)


coi = [300, 400, 50, 10, 500]

coin_change(800, coi)