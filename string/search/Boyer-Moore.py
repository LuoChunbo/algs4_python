#!/usr/bin/python

def BoyerMoore(pat):
    m = len(pat)
    R = 256

    right = [-1] * R

    for i in range(m):
        right[ord(pat[i])] = i;

    return right;

def search(txt, pat):
    n = len(txt)
    m = len(pat)


    right = BoyerMoore(pat)

    i = 0

    while i < n - m:
        skip = 0
        for j in range(m-1, -1, -1):
            if pat[j] != txt[i+j]:
                skip = j - right[ord(txt[i+j])]
                if skip < 1:
                    skip = 1
                break

        if skip == 0:
            return i
        else:
            i += skip

    return n


if __name__ == "__main__":

    txt = "AABRAACADABRAACAADABRA"
    pattern = "AACAA"

    offset = search(txt, pattern)
    print("offset = ", offset)

    print ("match pattern string", txt[offset:])








