#!/usr/bin/python


def gen_next(pat):
    m = len(pat);

    next_array = [0]*m;

    next_array[0] = 0;
    k = 0;
    
    for i in range(1, m):
        while k > 0 and pat[i] != pat[k]:
            k = next_array[k-1]

        if pat[i] == pat[k]:
            k += 1

        next_array[i] = k;

    print("next array is ", next_array);

    return next_array


def kmp(txt, pat):
    n = len(txt);
    m = len(pat);

    next_array = gen_next(pat);

    j = 0;

    for i in range(0, n):
        
        while j > 0 and txt[i] != pat[j]:
            j = next_array[j-1];

        if txt[i] == pat[j]:
            j += 1

        if j == m:
            print("found, offset = ", i - m + 1);
            break;


if __name__ == "__main__":
    txt = "aabcaabeaaba"
    pat = "aaba"

    kmp(txt, pat)


