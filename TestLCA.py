from BinaryTree import BinaryTree
import unittest


class TestLCA(unittest.TestCase):

    def test_size(self):
        list = [5, 2, 7, 23, 74, -14, 845, -97, 42, 4, 68, -6, 73, 98, 10, 102, 25, -1, 0, 62, 81]
        bt = BinaryTree(list)
        self.assertEqual(bt.getSize(), 21) # Non-empty list with no duplicates

        list.append(2)
        list.append(-6)
        list.append(0)
        self.assertEqual(bt.getSize(), 21) # Non-empty list with duplicates

        bt = BinaryTree(None) 
        self.assertEqual(bt.getSize(), 0) # Null

        bt = BinaryTree([])
        self.assertEqual(bt.getSize(), 0) # Empty list

    def test_shape(self):
        list = [5, 2, 7, 23, 74, -14, 845, -97, 42, 4, 68, -6, 73, 98, 10, 102, 25, -1, 0, 62, 81]
        bt = BinaryTree(list)
        shape1 = "-5\n |-7\n | |-23\n | | |-74\n | | | |-845\n | | | | |-None\n | | | |  -98\n | | | |   |-102\n | | | |   | |-None\n | | | |   |  -None\n | | | |    -81\n | | | |     |-None\n | | | |      -None\n | | |  -42\n | | |   |-68\n | | |   | |-73\n | | |   | | |-None\n | | |   | |  -None\n | | |   |  -62\n | | |   |   |-None\n | | |   |    -None\n | | |    -25\n | | |     |-None\n | | |      -None\n | |  -10\n | |   |-None\n | |    -None\n |  -None\n  -2\n   |-4\n   | |-None\n   |  -None\n    --14\n     |--6\n     | |--1\n     | | |-0\n     | | | |-None\n     | | |  -None\n     | |  -None\n     |  -None\n      --97\n       |-None\n        -None\n"
        self.assertEqual(bt.shape(), shape1)

        list.append(2)
        list.append(-6)
        list.append(-14)
        bt = BinaryTree(list)
        self.assertEqual(bt.shape(), shape1)
		
        bt = BinaryTree(None)
        self.assertTrue(bt.shape(), "-None\n")
        bt = BinaryTree([])
        self.assertEqual(bt.shape(), "-None\n")
        bt = BinaryTree([1, 2, 3, None]);
        self.assertEqual(bt.shape(),
				"-1\n |-2\n | |-3\n | | |-None\n | |  -None\n |  -None\n  -None\n")

    def test_LCA(self):
        list = [5, 2, 7, 23, 74, -14, 845, -97, 42, 4, 68, -6, 73, 98, 10, 102, 25, -1, 0, 62, 81]
        bt = BinaryTree(list)
        self.assertEqual(5, bt.LCA(42, 0))
        self.assertEqual(74, bt.LCA(74, 74))
        self.assertEqual(5, bt.LCA(5, 7))
        self.assertEqual("None", bt.LCA(1000, -6))
        self.assertEqual("None", bt.LCA(None, 23))

if __name__ == '__main__':
    unittest.main()