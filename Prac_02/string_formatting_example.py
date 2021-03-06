"""
CP1404 - Prac
"""

name = "Gibson L-5 CES"
year = 1922
cost = 16035.40

#better way
print("My guitar: {}, first made in {}".format(name, year))
print("My guitar: {0}, first made in {1}".format(name, year))
print("My {0} was first made in {1} (that's right, {1}!)".format(name, year))

#currency
print("My {} would cost ${:,.2f}".format(name, cost))

#aligning columns
numbers = [1, 19, 123, 456, -25]
for i in range(len(numbers)):
    print("number {0} is {1:>15}".format(i + 1, numbers[i]))