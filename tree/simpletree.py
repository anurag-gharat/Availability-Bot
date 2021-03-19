class TreeNode:
    def __init__(self, data):
        self.data = data
        self.children = []
        self.parent = None

    def add_child(self, child):
        # here self means
        child.parent = self
        self.children.append(child)

    def get_level(self):
        level = 0
        p = self.parent
        while p:
            level = level + 1
            p = p.parent
        return level

    def print_tree(self):
        spaces = "--" * self.get_level()
        print(spaces+self.data)
        for child in self.children:
            if self.children:
                child.print_tree()


def build_Tree():

    root = TreeNode("Mobiles")
    samsung = TreeNode("Samsung")
    root.add_child(samsung)
    samsung.add_child(TreeNode("Galaxy S20"))
    samsung.add_child(TreeNode("Galaxy S20 Plus"))
    samsung.add_child(TreeNode("Galaxy S20 Ultra"))

    oneplus = TreeNode("One Plus")
    root.add_child(oneplus)
    oneplus.add_child(TreeNode("One Plus 9"))
    oneplus.add_child(TreeNode("One Plus 9Pro"))
    oneplus.add_child(TreeNode("One Plus 9R"))

    redmi = TreeNode("Redmi")
    root.add_child(redmi)
    redmi.add_child(TreeNode("Note 8"))
    redmi.add_child(TreeNode("Note 8 Plus"))
    redmi.add_child(TreeNode("Note 8 Pro"))

    return root


if __name__ == '__main__':
    tree = build_Tree()

    tree.print_tree()
