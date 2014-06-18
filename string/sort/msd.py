#!/usr/bin/python

CUT_OFF = 15

R = 256

#aux = list()


def msd_sort(a):
    n = len(a)
    global aux
    aux = [[]]*n
    sort(a, 0, n-1, 0)

def sort(a, lo, hi, d):
    if hi <= lo + CUT_OFF:
        insertion_sort(a, lo, hi, d)
        return
    global aux

    count = [0]*(R+2)

    for i in range(lo, hi + 1):
        count[ord(a[i][d]) + 2] += 1

    for r in range(R+1):
        count[r+1] += count[r]

    for i in range(lo, hi+1):
        aux[count[ord(a[i][d]) + 1]]= a[i]

    for i in range(lo, hi+1):
        a[i] = aux[i-lo]

    for r in range(R):
        sort(a, lo + count[r], lo + count[r+1] - 1, d+1)


def insertion_sort(a, lo, hi, d):
    for i in range(lo, hi+1):
        for j in range(i, lo-1, -1):
            print("i=",i, ", j = ", j)
            print("a[j] = ", a[i])
            print("a[j-1j =", a[j-1])
            if a[j][d:] < a[j-1][d:]:
                tmp = a[j-1]
                a[j-1] = j
                a[j] = tmp



if __name__ == "__main__":
    f = open("shells.txt", "r")
    data = f.read().split()

    print(data)

    msd_sort(data)

    print(data)


