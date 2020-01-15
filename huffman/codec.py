def char_freq(text):
    """Counting frequency of letter in a text. """
    dic = {}
    for ch in text:
        if ch not in dic:
            dic[ch] = 1
        else:
            dic[ch] += 1
    # Results will be sorted
    return sorted(dic.items(), key=lambda x: x[1])


class Node():
    """Class used for nodes in a Huffman binary tree. """

    def __init__(self, data):
        """Initialization of a node. """
        self.key = data[0]  # Saved letter
        self.val = data[1]  # Frequency of this letter
        self.left = None  # Left child node
        self.right = None  # Right child node
        self.code = ""  # Storage of binary code


class NodeQueue():
    """A queue containing nodes of a Huffman binary tree. """

    def __init__(self, data):
        """Initialization of a queue of nodes. """
        q = []
        # Put the informations into the queue
        for node in data:
            q.append(Node(node))
        self.queue = q  # Save the nodes in a queue
        self.size = len(q)

    def add_nd(self, node):
        """Add a node to the existing queue. """
        if self.size > 0:  # Queue is not empty
            if node.val > self.queue[self.size-1].val:
                # Put the most frequent one at the end of queue
                self.queue = self.queue + [node]
            else:
                for i in range(self.size):
                    # Sorting when input
                    if node.val <= self.queue[i].val:
                        self.queue = self.queue[:i] + [node] + self.queue[i:]
                        break
        else:  # Queue is empty
            self.queue = [node]
        self.size += 1

    def pop_nd(self):
        """"Pop out the first node of the queue. """
        if self.size > 0:
            self.size -= 1
            return self.queue.pop(0)
        else:  # When the queue is empty
            raise ValueError("Empty queue of nodes. Nothing to pop. ")


class TreeBuilder():
    """Class used for Huffman binary tree constructions. """

    def __init__(self, text: str):
        self.node_queue = NodeQueue(char_freq(text))

    def tree(self):
        """Construct the Huffman tree from a node queue. """
        nq = self.node_queue
        if nq.size < 1:
            raise ValueError("Empty queue of nodes. ")
        while nq.size > 1:
            node1 = nq.pop_nd()
            node2 = nq.pop_nd()  # Get the first 2 nodes out
            r = Node((node1.key + node2.key, node1.val + node2.val))
            r.left = node1
            r.right = node2
            nq.add_nd(r)  # Put the new constructed node in
        return nq.pop_nd()  # Return the head node of the tree


class Codec():
    """Class used for encode and decode a Huffman tree. """

    def tree_complete(self, head, code):
        """Construct dictionaries for encoding and decoding. """
        if head:  # Node exists
            # Add an '0' to a leftchild's code
            self.tree_complete(head.left, code + '0')
            head.code += code
            if len(head.key) == 1:  # Node contains a letter
                # Add it into the dictionaries
                self.encoder[head.key] = head.code
                self.decoder[head.code] = head.key
            # Add an '1' to a leftchild's code
            self.tree_complete(head.right, code + '1')

    def __init__(self, head):
        self.encoder = {}
        self.decoder = {}
        self.tree_complete(head, '')

    def encode(self, text):
        # Use the encoder dictionary to encode
        res = ""
        for ch in text:
            res += self.encoder[ch]
        return res

    def decode(self, b_text):
        # Use the decoder dictionary to decode
        res = ""
        temp = ""
        for ch in b_text:
            temp += ch
            if temp in self.decoder.keys():
                res += self.decoder[temp]
                temp = ""
        return res
