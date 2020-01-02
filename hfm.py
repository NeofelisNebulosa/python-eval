import numpy as np

text = "a dead dad ceded a bad babe a beaded abaca bed"


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
            i = 0
            while(node.val > self.queue[i].val and i < self.size):
                i += 1
            self.queue = self.queue[:i] + [node] + self.queue[i:]
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
        self.head = self.node_queue.queue[0]

    def tree(self):
        nq = self.node_queue
        if nq.size < 1:
            raise ValueError("Empty queue of nodes. ")
        while nq.size > 1:
            node1 = nq.pop_nd()
            # node2 = nq.pop_nd()
            print(node1.key, node1.val)


class Codec():
    """Class used for encode and decode a Huffman tree. """

    def __init__(self, tree):
        pass

    def encode(self):
        pass

    def decode(self):
        pass


# print(char_freq(text)[:])
# nq = NodeQueue(char_freq(text))
# nd = Node(('sd', 8))
# for x in nq.queue:
#     print(x.key, x.val)
# nq.add_nd(nd)
# for x in nq.queue:
#     print(x.key, x.val)
# print(nq.pop_nd().val)

hfmt = TreeBuilder(text)
hfmt.tree()
