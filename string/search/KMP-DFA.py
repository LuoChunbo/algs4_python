#!/usr/bin/python


def KMP(pat):
    m = len(pat)
    R = 256

    dfa = [[0 for col in range(m)] for row in range(R)]

    dfa[ord(pat[0])][0] = 1

    x = 0

    for j in range(1, m):

        for c in range(R):
            dfa[c][j] = dfa[c][x]

        dfa[ord(pat[j])][j] = j + 1

        x = dfa[ord(pat[j])][x]
        

    return dfa


def kmp_search(txt, pat):
    dfa = KMP(pat)

    n = len(txt)
    m = len(pat)

    j = 0;
    for i in range(0, n):
        j = dfa[ord(txt[i])][j]
        if j == m:
            break

    if j == m:
        return i - m +1 

    else:
        return n

if __name__ == "__main__":

    txt = "AABRAACADABRAACAADABRA"
    pattern = "AACAAk"

    offset = kmp_search(txt, pattern)
    print("offset = ", offset)

    print ("match pattern string", txt[offset:])
        
