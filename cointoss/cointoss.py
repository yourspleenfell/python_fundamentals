def coinToss(num, num1):
    import random
    heads = 0
    tails = 0
    for count in range(num, num1):
        val = round(random.random())
        if val%2 == 0:
            heads += 1
            print "Attempt #" + str(count) + ": Throwing a coin... It's a head! ... Got " + str(heads) + " head(s) so far and " + str(tails) + " tail(s) so far"
        elif val%2 != 0:
            tails += 1
            print "Attempt #" + str(count) + ": Throwing a coin... It's a tail! ... Got " + str(heads) + " head(s) so far and " + str(tails) + " tail(s) so far"

coinToss(1, 5001)