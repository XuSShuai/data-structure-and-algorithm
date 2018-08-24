#  母牛每年生一只母牛，新出生的母牛三年后也能每年生出一只母牛，假设不会死，
#  求N年以后的母牛的数量。


def cow_number(years):
    if years == 1 or years == 2 or years == 3:
        return years
    return cow_number(years - 1) + cow_number(years - 3)

print(cow_number(6))