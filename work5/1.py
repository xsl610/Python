def calc_sum(*args):
    def sum():
        ax = 0
        for n in args:
            ax = ax + n
        return ax

    return sum


sum1 = calc_sum(1, 3, 5, 7, 9)
print(sum1)
print(sum1())
