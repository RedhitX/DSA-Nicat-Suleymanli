class BSTNode:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None


class BST:
    def __init__(self):
        self.root = None
        self.size = 0

    def __len__(self):
        return self.size

    def _find(self, key):
        parent, node = None, self.root
        while node is not None and node.key != key:
            parent = node
            node = node.left if key < node.key else node.right
        return parent, node

    def insert(self, key):
        parent, node = self._find(key)
        if node is not None:
            return False
        new_node = BSTNode(key)
        if parent is None:
            self.root = new_node
        elif key < parent.key:
            parent.left = new_node
        else:
            parent.right = new_node
        self.size += 1
        return True

    def search(self, key):
        _, node = self._find(key)
        return node is not None

    def delete(self, key):
        parent, node = self._find(key)
        if node is None:
            return False
        # İki övladı varsa, sağ alt ağacın ən kiçik açarını götür.
        if node.left is not None and node.right is not None:
            target = node
            parent, node = node, node.right
            while node.left is not None:
                parent, node = node, node.left
            target.key = node.key
        child = node.left or node.right
        if parent is None:
            self.root = child
        elif parent.left is node:
            parent.left = child
        else:
            parent.right = child
        self.size -= 1
        return True

    def height(self):
        if self.root is None:
            return 0
        deepest = 0
        pending = [(self.root, 1)]
        while pending:
            node, depth = pending.pop()
            deepest = max(deepest, depth)
            if node.left is not None:
                pending.append((node.left, depth + 1))
            if node.right is not None:
                pending.append((node.right, depth + 1))
        return deepest

    def inorder(self):
        values, pending = [], []
        node = self.root
        while pending or node is not None:
            while node is not None:
                pending.append(node)
                node = node.left
            node = pending.pop()
            values.append(node.key)
            node = node.right
        return values

    def display(self):
        if self.root is None:
            print("  (boş ağac)")
            return
        pending = [(self.root, 0)]
        while pending:
            node, depth = pending.pop()
            print(f"  {'  ' * depth}{node.key}")
            if node.right is not None:
                pending.append((node.right, depth + 1))
            if node.left is not None:
                pending.append((node.left, depth + 1))
