
def char_freq(text):
    dic = {}
    for ch in text:
        if ch not in dic:
            dic[ch] = 1
        else:
            dic[ch] += 1
    return sorted(dic.items(), key=lambda x: x[1])


class Node():
    """Class used for nodes in a Huffman binary tree. """

    def __init__(self, data):
        self.key = data[0]
        self.val = data[1]
        self.left = None
        self.right = None
        self.code = ""


class NodeQueue():
    """A queue containing nodes of a Huffman binary tree. """

    def __init__(self, data):
        q = []
        for node in data:
            q.append(Node(node))
        self.queue = q
        self.size = len(q)

    def add_nd(self, node):
        if self.size > 0:
            if node.val > self.queue[self.size-1].val:
                self.queue = self.queue + [node]
            else:
                for i in range(self.size):
                    if node.val <= self.queue[i].val:
                        self.queue = self.queue[:i] + [node] + self.queue[i:]
                        break
        else:
            self.queue = [node]
        self.size += 1

    def pop_nd(self):
        if self.size > 0:
            self.size -= 1
            return self.queue.pop(0)
        else:
            raise ValueError("Empty queue of nodes. Nothing to pop. ")


class TreeBuilder():
    """Class used for Huffman binary tree constructions. """

    def __init__(self, text: str):
        self.node_queue = NodeQueue(char_freq(text))

    def tree(self):
        nq = self.node_queue
        if nq.size < 1:
            raise ValueError("Empty queue of nodes. ")
        while nq.size > 1:
            node1 = nq.pop_nd()
            node2 = nq.pop_nd()
            r = Node((node1.key + node2.key, node1.val + node2.val))
            r.left = node1
            r.right = node2
            nq.add_nd(r)
        return nq.pop_nd()


class Codec():
    """Class used for encode and decode a Huffman tree. """

    def tree_complete(self, head, code):
        if head:
            self.tree_complete(head.left, code + '0')
            head.code += code
            if len(head.key) == 1:
                self.encoder[head.key] = head.code
                self.decoder[head.code] = head.key
            self.tree_complete(head.right, code + '1')

    def __init__(self, head):
        self.encoder = {}
        self.decoder = {}
        self.tree_complete(head, '')
        print(self.encoder)
        print(self.decoder)

    def encode(self, text):
        res = ""
        for ch in text:
            res += self.encoder[ch]
        return res

    def decode(self, b_text):
        res = ""
        temp = ""
        for ch in b_text:
            temp += ch
            if temp in self.decoder.keys():
                res += self.decoder[temp]
                temp = ""
        return res
