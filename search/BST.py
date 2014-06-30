#/usr/bin/python


class Node:
    def __init__(self, key, val, N):
        self.key = key;
        self.val = val;
        self.N = N;
        self.left = None;
        self.right = None;


root = None;

"""def size():
        return size(root);
"""
def size(x):
    if not x:
        return 0;

    return x.N;

"""def get(key):
    return get(root, key);
"""
def get(x, key):
    if not x:
        return None;

    if key < x.key:
        return get(x.left, key);
    elif key > x.key:
        return get(x.right, key);
    else:
        return x.val;


"""def put(key, val):
    root = put(root, key, val)
"""
def put(x, key, val):
    if not x:
        return Node(key, val, 1);

    if key < x.key:
        x.left = put(x.left, key, val);
    elif key > x.key:
        x.right = put(x.right, key, val);
    else:
        x.val = val;
    
    x.N = size(x.left) + size(x.right) + 1;

    return x;


def min():
    return min(root).key;

def min(x):
    if not x.left:
        return x;
    else:
        return min(x.left);

def max():
    return max(root).key;

def max(x):
    if not x.right:
        return x;
    else:
        return max(x.right);


def floor(key):
    x = floor(root, key);
    if not x:
        return None;
    return x.key;

def floor(x, key):
    if not x:
        return None;

    if x.key == key:
        return x;

    elif key < x.key:
        return floor(x.left, key);
    else:
        t = floor(x.right, key);
        if not t:
            return x;
        else:
            return t;

def ceiling(key):
    x = ceiling(root, key);
    if not x:
        return None;
    return x.key

def ceiling(x, key):
    if not x:
        return None;

    if key == x.key:
        return x;

    elif key > x.key:
        return ceiling(x.right, key)
    else:
        t = ceiling(x.left, key);
        if not t:
            return x;
        else:
            return t;


def select(k):
    return select(root, k).key;

def select(x, k):
    if not x:
        return None;

    t = size(x.left);
    if t < k:
        return select(x.right, k - t - 1);
    elif t > k:
        return select(x.left, k);
    else:
        return x;

def rank(key):
    return rank(root, key);

def rank(x, key):
    if not x:
        return 0;

    if key < x.key:
        return rank(x.left, key);
    elif key > x.key:
        return  1 + size(x.left) + rank(x.right, key);
    else:
        return size(x.left);


def deleteMin():
    root = deleteMin(root);


def deleteMin(x):
    if not x.left:
        return x.right;

    x.left = deleteMin(x.left);
    x.N = size(x.left) + size(x.right) + 1;
    return x;

def deleteMax(x):
    root = deleteMax(root);

def deleteMax(x):
    if not x.right:
        return x.left;

    x.right = deletcMax(x.right);
    x.N = size(x.left) + size(x.right) + 1;
    return x;

def delete(key):
    root = delete(root, key);

def delete(x, key):
    if not x:
        return None;

    if key < x.key:
        x.left = delete(x.left, key);
    elif key > x.key:
        x.right = delecte(x.right, key);
    else:
        if x.right == None:
            return x.left;
        if x.left == None:
            return x.right;

        t = x;
        x = min(t.right);
        x.right = deleteMin(t.right);
        x.left = t.left;

    x. N = size(x.left) + size(x.right) + 1;

    return x;

def contains(key):
    return get(root, key) != None

def iterator_node(x):
    if not x:
        return;
    iterator_node(x.left);
    print("key = ", x.key , "value = ", x.val);
    iterator_node(x.right)

max_key=""
max_val=0

def find_max_node(x):
    if not x:
        return;

    global max_key;
    global max_val;

    find_max_node(x.left);
    find_max_node(x.right);
    if x.val > max_val:
        max_val = x.val;
        max_key = x.key;


if __name__ == "__main__":

    minlen = 8;
    global root;
    #f = open("tinyTale.txt");
    #f = open("tale.txt");
    f = open("leipzig1M.txt");

    words = 0;
    for line in f:
        for word in line.rstrip().split():
            words += len(word);
            if len(word) < minlen:
                continue;
            #print(word)
            if not contains(word):
                root = put(root, word, 1);
            else:
                root = put(root, word, get(root, word) + 1);
    f.close()

    #iterator_node(root)

    find_max_node(root)

    print("all words = ", words);

    print("max node key: ", max_key, "max node val :", max_val);

    print("word size: ", root.N);




