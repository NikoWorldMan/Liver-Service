
defence = 20000
level_dif = 21
u = 0

damage = 100



while not u == "c":
    u = input("C = break loop").lower()
    inc = 0

    inc = input("int: ")

    if len(inc) > 0:
        defence = int(inc)

    mult = 1 - ((1 + defence) / (defence + 500 + (2 ** level_dif) + 66 * level_dif ))


    print()
    print(defence,"defence.")

    print()
    print(f"raw: {mult}")
    print("-")
    print(f"Damage reduction: {int((1-mult) * 100)}%")
    print()

    print(f'Took {int(damage*mult)} damage')










































