#/usr/bin/python

def quick3string_sort(a):
	sort(a, 0, len(a) - 1, 0)

def swap(a, i, j):
	tmp = a[i]
	a[i] = a[j]
	a[j] = tmp

def sort(a, lo, hi ,d):
	if lo >= hi:
		return

	left = lo
	right = hi

	if len(a[lo]) <= d:
		return
	
	v = a[lo][d]
	i = lo + 1

	while i <= right:
		if len(a[i]) <= d:
			t = -1
		else:
			t = a[i][d]

		if t < v:
			swap(a, left, i)
			left += 1
			i += 1
		elif t > v:
			swap(a, right, i)
			right -= 1
		else:
			i += 1
	
	sort(a, lo, left-1, d)
	sort(a, left, right, d+1)
	sort(a, right+1, hi, d)



if __name__ == "__main__":
    f = open("shells.txt", "r")
    data = f.read().split()

    print(data)

    quick3string_sort(data)

    print(data)



