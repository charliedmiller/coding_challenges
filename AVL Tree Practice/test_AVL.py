# Charlie Miller
# AVL Tree Testing
# Written 11/26/2020
import unittest
from AVLTree import AVLTree
from TreePrinter import TreePrinter

class AVLTestCase(unittest.TestCase):
    def do_test(self,*insert_deletes):
        tp = TreePrinter()
        avl = AVLTree(tp)
        state = "insert"
        for sequence in insert_deletes:
            if state == "insert":
                for value in sequence:
                    avl.insert(value)
                state = "delete"
            elif state == "delete":
                for value in sequence:
                    avl.delete(value)
                state = "insert"
            else:
                print("invalid testing state!!")
                state = "insert"

        print("\n")
        print(avl)
        is_bst = self.verify_bst(avl.root,float("-inf"),float("inf"))
        is_balanced = self.verify_balanced(avl)
        self.assertTrue(is_bst,"Not A Binary Search Tree")
        self.assertTrue(is_balanced,"Not balanced")

    def verify_bst(self,root,min_val,max_val):
        if not root:
            return True

        if root.val < min_val or root.val > max_val:
            return False

        if not self.verify_bst(root.left,min_val,root.val):
            return False

        if not self.verify_bst(root.right,root.val,max_val):
            return False

        return True

    def verify_balanced(self,tree):
        bias = tree.get_bias(tree.root)
        return abs(bias) < 2

    def test_nominal(self):
        self.do_test([1,5,3])

    def test_insert_remove_full(self):
        self.do_test([1,5,3],[1,5,3])

    def test_full_increase(self):
        self.do_test([1,2,3,4,5,6,7,8,9])

    def test_insert_full_decrease(self):
        self.do_test([9,8,7,6,5,4,3,2,1])

    def test_weaving_right(self):
        self.do_test([1,9,2,8,3,7,4,6,5])



if __name__ == "__main__":
    unittest.main()
    # do_test([1,4,7,5,2])
    # do_test([9,8,7,6,5,4,3,2,1])
    # do_test([1,904565,44])
    # do_test([1])
    # do_test([1,4])