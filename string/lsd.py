#/usr/bin/python


from __future__ import print_function

def lsd_sort(a, w):
    n = len(a)
    r = 256


    aux = [[]]*n
    for d in range(w-1, -1, -1):
        count = [0]*(r+1)
        for i in range(n):
            
            count[ord(a[i][d]) + 1] += 1;

        for i in range(r):
            count[i+1] += count[i]


        for i in range(n):
            aux[count[ord(a[i][d])]] = a[i]
            count[ord(a[i][d])] += 1

        for i in range(n):
            a[i] = aux[i]





if __name__ =="__main__":
    f = open('words3.txt','r')
    ss = f.read().split()

    print(ss)
    lsd_sort(ss, 3)

    print(ss)


