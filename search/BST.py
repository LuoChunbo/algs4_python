#/usr/bin/python


class Node:
    def __init__(self, key, val, N):
        self.key = key;
        self.val = val;
        self.N = N;
        self.left = None;
        self.right = None;



class BST:

    #root = None;

    def __init__(self):
        self.root = None;
        self.node_max = Node("",0, 0);

    def node_size(self, x):
        if not x:
            return 0;
        return x.N;

    def size(self):
        return self.node_size(self.root);

    def insert(self, x, key):
        if not x:
            return Node(key, 1, 1);
        
        if key < x.key:
            x.left = self.insert(x.left, key);
        elif key > x.key:
            x.right = self.insert(x.right, key);
        else:
            x.val += 1;

        x.N = self.node_size(x.left) + self.node_size(x.right) + 1;

        return x;

    def put(self, key):
        self.root = self.insert(self.root, key);

    def search(self, x, key):
        if not x:
            return None;

        if key < x.key:
            return self.get(x.left, key);
        elif key > x.key:
            return self.get(x.right, key);
        else:
            return x.val;

    def get(self, key):
        return self.search(self.root, key);

    def inorder_walk(self, x):
        if not x:
            return;
        self.inorder_walk(x.left);
        print("key =", x.key, "val=", x.val);
        self.inorder_walk(x.right);

    def traverse_tree(self):
        return self.inorder_walk(self.root);

    def get_node_max(self):
        return self.max_val(self.root);

    def max_val(self, x):
        if not x:
            return None;
        
        self.max_val(x.left);

        if x.val > self.node_max.val:
            self.node_max = x;

        self.max_val(x.right);

        return self.node_max;

    def node_min(self, x):
        if not x.left:
            return x;
        else:
            return self.node_min(x.left);

    def min(self):
        return self.node_min(self.root).key;

    def node_max(self, x):
        if not x.right:
            return x;
        else:
            return self.node_max(x.right);

    def max(self):
        return self.node_max(self.root).key;

    
    def node_floor(self, x, key):
        if not x:
            return None;
        
        if key == x.key:
            return x;

        if key < x.key:
            return self.node_floor(x.left, key);
        else:
            t = self.node_floor(x.right, key);
            if not t:
                return x;
            else:
                return t;

    def floor(self, key):
        x = self.node_floor(self.root, key);
        if not x:
            return None;

        return x.key;

    def node_ceiling(self, x, key):
        if not x:
            return None;

        if key == x.key:
            return x;

        if key > x.key:
            return self.node_ceiling(x.right, key);
        else:
            t = self.node_ceiling(x.left, key);
            if not t:
                return x;
            else:
                return t;


    def ceiling(self, key):
        x = self.node_ceiling(self.root, key);
        if not x:
            return None;

        return x.key;

    def node_select(self, x, k):
        if not x:
            return None;

        t = self.node_size(x.left);

        if t == k:
            return x.left;
        elif t > k:
            return self.node_select(x.left, k);
        else:
            return self.node_select(x.right, k - t -1);

    def select(self, k):
        x = self.node_select(self.root, k);
        if not x:
            return None;
        return x.key;


    def node_rank(self, x, key):
        if not x:
            return 0;

        if key < x.key:
            return self.node_rank(x.left, key);
        elif key > x.key:
            return 1 + self.node_size(x.left) + self.node_rank(x.right, key);
        else:
            return node_size(x.left);

    def rank(self, key):
        return self.node_rank(self.root, key);

    
    def node_deleteMin(self, x):
        if not x.left:
            return x.right;

        x.left = self.node_deleteMin(x.left);
        x.N = self.node_size(x.left) + self.node_size(x.right) + 1;

        return x;

    def deleteMin(self):
        self.root = self.node_deleteMin(self.root);


    def node_deleteMax(self, x):
        if not x.right:
            return x.left;

        x.right = self.node_deleteMax(x.right);
        x.N = self.node_size(x.left) + self.node_size(x.right) + 1;
        return x;

    def deleteMax(self):
        self.root = node_deleteMax(self.root);


    def node_delete(self, x, key):
        if not x:
            return None;

        if key < x.key:
            return self.node_delete(x.left, key);

        elif key > x.key:
            return self.node_delete(x.right, key);
        else:
            if x.right == None:
                return x.left;
            if x.left == None:
                return x.right;

            t = x;
            x = self.node_min(t.right);
            x.right = self.node_deleteMin(t.right);
            x.left = t.left;

        x.N = self.node_size(x.left) + self.node_size(x.right) + 1;

        return x;

    def delete(self, key):
        self.root = self.node_delete(self.root, key);




if __name__ == "__main__":

    minlen = 10;
    global root;
    f = open("tinyTale.txt");
    #f = open("tale.txt");
    #f = open("leipzig1M.txt");

    st = BST();

    words = 0;
    for line in f:
        for word in line.rstrip().split():
            words += len(word);
            if len(word) < minlen:
                continue;

            st.put(word);

    f.close()

    #st.traverse_tree();

    node = st.get_node_max();

    print("max node key = " + str(node.key) + " ,val = " + str(node.val));

    print("word size :", st.root.N);






