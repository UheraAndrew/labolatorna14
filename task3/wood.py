from board import Board


class BTNode:
    def __init__(self, pos):
        self.pos = pos
        self.children = {}
        self.data = 0


class BTree:
    def __init__(self, pos):
        self.root = BTNode(pos)

    def build_tree(self):
        def recursion(node, board, counter):
            """

            :param node:
            :param board:
            :param counter: represents whose step is
            :type counter: bool
            :return:
            """
            x, y = node.pos
            board.board[x][y] = "x" if counter else "o"
            # print("_______________________________________")
            # print(board)
            win = board.is_win()
            # print(win)
            if win[0] != 0:
                # print(1)
                node.data = 1 if win[0] == -1 else -50
                return

            if board.is_draw():
                # print(2)
                node.data = 15
                return

            for cell in board.free_cells():
                node.children[cell] = BTNode(cell)
                recursion(node.children[cell], board, not counter)
                x, y = cell
                board.board[x][y] = None

        board = Board()
        recursion(self.root, board, True)
        self.evaluate_the_steps()

    def evaluate_the_steps(self):
        """
        Put weight at the top of the graph
        :return:
        """

        def recursion(node, depth):
            if node.children == {}:
                return node.data
            coef = (1 + (9 - depth) * 0.1)
            for cell in node.children:
                node.data += recursion(node.children[cell], depth + 1) * coef
            return node.data

        for node in self.root.children:
            recursion(self.root.children[node], 1)
