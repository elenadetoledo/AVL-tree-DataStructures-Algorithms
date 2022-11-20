from bst import BinarySearchTree
from bst import BinaryNode


class AVLTree(BinarySearchTree):

    # Override insert method from base class to keep it as AVL
    def insert(self, elem: object) -> None:
        """inserts a new node, with key and element elem"""
        self._root=self._insert(self._root,elem)

    def _insert(self, node: BinaryNode, elem: object) -> BinaryNode:
        """gets a node, searches the place to insert a new node with element e (using super()._insert),  and then,
        the function has to balance the node returned by the function super.()_insert"""
        node = super()._insert(node, elem)
        node = self._rebalance(node)
        return node

    # Override remove method from base class to keep it as AVL
    def remove(self, elem: object) -> None:
        self._root = self._remove(self._root, elem)

    def _remove(self, node: BinaryNode, elem: object) -> BinaryNode:
        """ gets a node, searches the node with element elem in the subtree that hangs down node , and
        then remove this node (using super()._remove). After this, the function has to balance the node returned by the function super()._remove"""
        node = super()._remove(node, elem)
        node = self._rebalance(node)
        return node

    def _rebalance(self, node: BinaryNode) -> BinaryNode:
        if node is not None:
                #First, we check if the node passed needs to be balanced or not
                if self.isnodebalanced(node) is False: #If it isn't balanced:
                    #Study which type of rotation should be applied and perform the rotation
                    type = self.idtype(node)
                    if type == 1:
                        self.simpleleftrot(node)
                    if type == 2:
                        self.simplerightrot(node)
                    if type == 3:
                        self.doubleleftrightrot(node)
                    if type == 4:
                        self.doublerightleftrot(node)
                    
                return node

    def isnodebalanced(self, node: BinaryNode):
        #This function checks wheter a node in a tree is balanced
        if node is self._root:
            #Empty tree is always balanced
            if node is None:
                return True

        if node is not None:
            #compute the height of its right and left subtrees
            lh = self._height(node.left)
            rh = self._height(node.right)
            if abs(lh - rh) <= 1: #check if the absolute value of the difference is less than 1
                return True
            else:
                return False

    def simpleleftrot(self, node: BinaryNode):
        if node is not None:
            # save references to the nodes who will be moved during this process: node is already saved as node
            newleft = node.right
            newright = node.right.right

            # now, we will save the subtrees : we won't need to save the subtrees of newright because they won't be altered
            nodesubt = node.left
            newleftsubt = newleft.left
            # we interchange nodes: for that we will change the element
            newelem = newleft.elem
            auxelem = node.elem
            node.elem = newelem
            newleft.elem = auxelem
            # we have to change the subtrees aswell
            node.left = newleftsubt
            newleft.left = nodesubt
            # now, we perform the rotation
            node.right= newright
            node.left = newleft
            newleft.right = newleftsubt

            return newleft

    def simplerightrot(self, node: BinaryNode):
        if node is not None:
            #save references to the nodes who will be moved during this process: node is already saved as node
            newright = node.left
            newleft = node.left.left

            #now, we will save the subtrees : we won't need to save the subtrees of newleft because they won't be altered
            nodesubt = node.right
            newrightsubt = newright.right
            #we interchange nodes: for that we will change the element
            newelem = newright.elem
            auxelem = node.elem
            node.elem = newelem
            newright.elem = auxelem
            #we have to change the subtrees aswell
            node.right = newrightsubt
            newright.right = nodesubt
            #now, we perform the rotation
            node.right = newright
            node.left = newleft
            newright.left = newrightsubt

            return newright

    def doubleleftrightrot(self, node: BinaryNode):
        if node is not None:
            if node.left is not None:
                #save the references of the nodes
                newmiddle = node.left.right
                newlast = node.left

                #break conections that will no longer be needed and create the ones we will use
                node.left = None
                newlast.right = newmiddle.left

                node.left = newmiddle
                newmiddle.left = newlast
                #newmiddle.right = None
                #once we have arrived to a situation needing simple right rotation, apply it
                self.simplerightrot(node)


        return node

    def doublerightleftrot(self, node: BinaryNode):
        if node is not None:
            if node.right is not None:
                # save the references of the nodes
                newmiddle = node.right.left
                newlast = node.right

                # break conections that will no longer be needed and create the ones we will use
                node.right = None
                newlast.left = newmiddle.right

                node.right = newmiddle
                newmiddle.right = newlast
                newmiddle.left = None

                # once we have arrived to a situation needing simple left rotation, apply it
                self.simpleleftrot(node)
                return node

    def idtype(self, node: BinaryNode) -> int:
        if node is not None:

            # see if it is a simple left rotation
            if node.right is not None:
                if node.right.right is not None:
                    return 1

            # see if it is a simple right rotation
            if node.left is not None:
                if node.left.left is not None:
                    return 2

            # see if it is a double left right rotation
            if node.left is not None:
                if node.left.right is not None:
                    return 3

            # see if it is a double right left rotation
            if node.right is not None:
                if node.right.left is not None:
                    return 4



















































