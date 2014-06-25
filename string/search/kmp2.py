#!/usr/bin/python

def gen_next(pat):
    m = len(pat);

    next_array = [0]*(m+1);

    next_array[0] = -1;
    j = -1;
    i = 0;

    while i < m:

        print("i=", i, "j=", j);

        if j == -1 or pat[i] == pat[j]:
            i += 1;
            j += 1;
            next_array[i] = j
        else:
            j = next_array[j];


    print("next array is ", next_array);

    return next_array


def kmp(txt, pat):
    n = len(txt)
    m = len(pat)

    next_array = gen_next(pat)

    i = 0
    j = -1

    while i < n:

        if j == -1 or txt[i] == pat[j]:
            i += 1;
            j += 1;

        else:
            j = next_array[j]

        if j == m:
            print("found, offset = ", i - m );
            break;


if __name__ == "__main__":
    txt = "aabcaabeaaba"
    pat = "aaba"

    kmp(txt, pat)





