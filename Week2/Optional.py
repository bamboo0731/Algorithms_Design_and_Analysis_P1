from math import log, floor, sqrt

"""
Q1:

much smaller than log_2(n)

for n > 1:
[log_2([log_2(n)])] + 2


"""
def Q1_count(n):
    predict = floor(log(floor(log(float(n), 2.0)),2.0)) + 2.0
    count = 1.0
    while(n>1.0):
        count += 1.0
        n = floor(sqrt(n))
    print int(count), int(predict)