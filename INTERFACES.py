class Pattern(object):

    class Adapter(object):
        __item = None

        def __init__(self, item):
            self.__item = item

        def getItem(self):
            return self.__item

    class Container(object):
        __content = []

        def append(self, item):
            self.__content.append(item)

        def remove(self, item):
            self.__content.remove(item)

        def getContent(self):
            return self.__content

        def getAttrInContent(self, itemMethod="name()"):
            """
            This method can return any 'content' within the 'item', within the 'container'

            If: content = [Adapter, Adapter, Adapter, Adapter, Adapter]
            And: list = wh.getAttrInContent("getItem()")
            Then: list = [PyNode, PyNode, PyNode, PyNode, PyNode]

            Its smart if you contain objects that hold strings and want these returned, or want any other deeper information
            """

            result = []
            for item in self.__content:
                exec ("result.append(item.{0})".format(itemMethod))

            return result

    class Warehouse(Container):

        def append(self, container):
            if isinstance(container, Pattern.Container):
                self.__content.append(container)
            else:
                raise AttributeError("Warehouse only takes 'Container' type objects, not {0}".format(type(container)))

    class Factory(object):

        def create(self, target):
            pass

        def complete(self, target):
            pass

        def reset(self):
            pass


class Method(object):

    class GetRoot(object):

        def getRoot(self, node, method="getParent()"):
            result = node
            exec ("if node.{0}: result = self.getRoot(node.{0}, method=method)".format(method))

            return result

    class GetTree(object):

        def getTree(self, node, method="listRelatives(ad=True)"):
            result = node
            exec ("result.append(node.{0})".format(method))

            return result

    class GetHierarchy(GetRoot, GetTree):
        """Interface behavior for returning a full list of """

        def getHierarchy(self, node, rootMethod="getParent()", treeMethod="listRelatives(ad=True)"):
            root = self.getRoot(node, method=rootMethod)
            hierarchy = self.getTree(root, method=treeMethod)

            return hierarchy

