
defence = 20000
level_dif = 4
u = 0


while not u == "c":
    u = input("C = break loop").lower()
    inc = 0

    inc = input("int: ")

    if len(inc) > 0:
        defence += int(inc)

    mult = 1-(defence/(defence+4000+1500*level_dif))


    print()
    print(defence,"defence.")

    print()
    print(f"raw: {mult}")
    print("-")
    print(f"Damage reduction: {int((1-mult) * 100)}%")
    print()
