# Author RTS 12/9/21

def tp(freethrow, twopoint, threepoint):
    tp = 0
    tp = (1 * freethrow) + (2 * twopoint) + (3 * threepoint)
    return tp

freethrow = int(input("Enter the number of free throws: "))
twopoint = int(input("Enter the number of points beyond three point line: "))
threepoint = int(input("Enter the amount of points inside the three point line: "))

print(int(tp))
