import time
"""
timeLeft = 86100
while timeLeft > 0:
    print(timeLeft)
    time.sleep(1)
    timeLeft = timeLeft - 1
    """

def countdown(n):
    while n > 0:
        print (n)
        time.sleep(1)
        n = n-1
        if n == 0:
            print 'blast'
countdown(50)
