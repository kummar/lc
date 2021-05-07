total = 0
months = 0

while total - 2 * 50000000 < 0 and months / 12.0 < 10:
    total = total * 1.01 + 5000
    months += 1
    print("You have {inverse} YUAN now!".format(inverse=str(total)))
    print("You have during {m} months, it's about {y} years!".format(m=months, y=float(months)/12.0))