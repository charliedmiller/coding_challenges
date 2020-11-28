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

    def verify_and_catch(self,tree,sequence,big_i,small_j):
        try:
            self.verify_tree(tree)
        except AssertionError as e:
            cur_arr = sequence[:big_i]
            cur_arr.append(sequence[big_i][:small_j+1])
            print(tree,file=sys.stderr)
            print(cur_arr,file=sys.stderr)
            raise e

    def run_test(self,*insert_deletes):
        tp = TreePrinter()
        avl = AVLTree(tp)
        state = "insert"
        for i,sequence in enumerate(insert_deletes):
            if state == "insert":
                for j,value in enumerate(sequence):
                    avl.insert(value)
                    self.verify_and_catch(avl,sequence,i,j)
                state = "delete"
            elif state == "delete":
                for j,value in enumerate(sequence):
                    avl.delete(value)
                    self.verify_and_catch(avl,sequence,i,j)
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



if __name__ == "__main__":
    unittest.main()
    # do_test([1,4,7,5,2])
    # do_test([9,8,7,6,5,4,3,2,1])
    # do_test([1,904565,44])
    # do_test([1])
    # do_test([1,4])