# Charlie Miller
# AVL Tree Testing
# Written 11/26/2020
import unittest,sys
from AVLTree import AVLTree
from TreePrinter import TreePrinter

class AVLTestCase(unittest.TestCase):
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

    def verify_tree(self,tree):
        is_bst = self.verify_bst(tree.root,float("-inf"),float("inf"))
        is_balanced = self.verify_balanced(tree)
        self.assertTrue(is_bst,"Not A Binary Search Tree")
        self.assertTrue(is_balanced,"Not balanced")

    def verify_and_catch(self,tree,insert_delete,big_i,small_j):
        """
        Perform the test. If it fails, catch, print out tree structure,
        then reraise. Show what number the test failed on
        """
        insert_delete = list(insert_delete)
        try:
            self.verify_tree(tree)
        except AssertionError as e:
            cur_arr = insert_delete[:big_i]
            cur_arr.append(insert_delete[big_i][:small_j+1])
            print(tree,file=sys.stderr)
            print(cur_arr,file=sys.stderr)
            raise e

    def run_test(self,*insert_deletes):
        """
        Run a series of insertions and deletes. After
        each operation, check if the tree follows AVL tree
        properties (is a Binary Search Tree, and height for
        each of the children differ no more than 1)
        """
        #instantiate a printer for debugging
        tp = TreePrinter()
        avl = AVLTree(tp)

        #switch between inserting and deletion state
        state = "insert"
        for i,sequence in enumerate(insert_deletes):
            if state == "insert":
                for j,value in enumerate(sequence):
                    avl.insert(value)
                    self.verify_and_catch(avl,insert_deletes,i,j)
                state = "delete"
            elif state == "delete":
                for j,value in enumerate(sequence):
                    avl.delete(value)
                    self.verify_and_catch(avl,insert_deletes,i,j)
                state = "insert"
            else:
                print("invalid testing state!!")
                state = "insert"


    def test_nominal(self):
        self.run_test([1,5,3])

    def test_insert_remove_full(self):
        self.run_test([1,5,3],[1,5,3])

    def test_full_increase(self):
        self.run_test([1,2,3,4,5,6,7,8,9])

    def test_insert_full_decrease(self):
        self.run_test([9,8,7,6,5,4,3,2,1])

    def test_weaving_right(self):
        self.run_test([1,9,2,8,3,7,4,6,5])

    def test_weaving_left(self):
        self.run_test([9,1,8,2,7,3,6,4,5])

    def test_wing_pattern(self):
        self.run_test([5,4,6,3,7,2,8,1,9])

    def test_delete_roots(self):
        self.run_test([5,4,6,3,7,2,8,1,9],
                      [5,6,7,3,4,8,2,9,1],
                      [8,3,2,6,0,-9,-8])

    def test_delete_non_roots(self):
        self.run_test([1,2,3,4,5,6,7,8,9,0],[6,7,8,2,1])

    def test_delete_one_child_roots(self):
        self.run_test([1,2,3,4,5,6,7,8,9,0],[1,0,2,7,8])

    def test_delete_leaves(self):
        self.run_test([1,2,3,4,5,6,7,8,9,0],[0,7,9,1,8,3,5,6,2,4])

    def test_build_up_and_down(self):
        self.run_test([1,2,3,4,5,6,7,8,9,0],[1,2,3,4,5,6,7,8,9,0],[1,2,3,4,5,6,7,8,9,0],[1,2,3,4,5,6,7,8,9,0])

    def test_delete_same_multiple(self):
        self.run_test([1,2,3,4,5,6,7,8,9,0],[1,1,1,1,1,1,2,2,2,2,2,2,5,5,5,5,5])

    def test_insert_same_multiple(self):
        self.run_test([1,2,3,4,5,6,7,8,9,0,1,1,1,1,1,0,0,0,0,0,0,6,6,6,6,6,6])


if __name__ == "__main__":
    unittest.main()