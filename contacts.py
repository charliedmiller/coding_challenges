# Charlie Miller
# Hackerrank - Contacts
# https://www.hackerrank.com/challenges/contacts/problem

import os
import sys

"""
Maintain a Trie where each node keeps track of how many words has passed thru it
when a node just starts out, it's guaranteed to have one child: itself
Though we don't increment the children count unless another contact is added
For finding, traverse the Trie and return the children count if it exists
"""


class TrieNode:
    def __init__(self,char,origin):
        self.char = char
        self.origin = origin
        self.children_count = 1
        self.children = {}

    def get_children_count(self):
        return self.children_count

    def has_child(self,char):
        return char in self.children

    def get_child(self,char):
        if not self.has_child(char):
            return None

        return self.children[char]

    def increment_children_count(self):
        self.children_count += 1

    def add_child(self,char,word):
        #Do not increment if we're still building the original contact
        if word != self.origin:
            self.increment_children_count()

        if not self.has_child(char):
            self.children[char] = TrieNode(char,word)

class Contacts:
    def __init__(self):
        self.root = TrieNode("#","#")
        self.root.children_count = 0
        self.results = []

    #Add the contact by traversing the Trie
    #The trie will take care of duplicates and mainting children count
    def add(self,contact):
        cur_node = self.root
        for char in contact:
            cur_node.add_child(char,contact)
            cur_node = cur_node.get_child(char)

    #Traverse the Trie. If any node doesn't have what we're looking for,
    # we just add 0 to our results, otherwise return children count for
    #for the Trie node we traversed to
    def find(self,contact):
        cur_node = self.root
        found = True
        for char in contact:
            if not cur_node.has_child(char):
                self.results.append(0)
                found = False
                break
            cur_node = cur_node.get_child(char)
    
        if found:
            self.results.append(cur_node.get_children_count())

def contacts(queries):
    #Start the trie with a root, build a results array for the problem
    results = []

    #Init application
    contacts_app = Contacts()

    #parse the queries, and execute the operations with the provided operands
    for query in queries:
        operation = query[0]
        operand = query[1]

        if operation == "add":
            contacts_app.add(operand)

        elif operation == "find":
            contacts_app.find(operand)

        else:
            raise RuntimeError("Illegal Operation")

    return contacts_app.results

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    queries_rows = int(input())

    queries = []

    for _ in range(queries_rows):
        queries.append(input().rstrip().split())

    result = contacts(queries)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
