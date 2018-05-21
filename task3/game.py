from board import Board, OutTheBoard, InvalidMove, EndGame
from wood import BTree


class Bot:
    """
    Class for Bot representation
    """

    def __init__(self, pos):
        """
        Initialized an object
        :param pos:
        """
        self.tree = BTree(pos)
        self.tree.build_tree()

    def move(self, previous_moves):
        """

        :param previous_moves: all previous steps
        :return:
        """
        nodes = self.tree.root.children
        for i in range(1, len(previous_moves)):
            nodes = nodes[previous_moves[i]].children

        if len(nodes) == 0:
            raise EndGame
        mas = [(nodes[cell].data, cell) for cell in nodes]
        print(mas)
        out = max(mas, key=lambda x: x[0])[1]
        return out


class Player:
    """
    Class for Player representation
    """

    def __init__(self, name=None):
        self.name = self.registrate() if name is None else name

    def registrate(self):
        return input("Please, enter your name: ")

    def move(self, board):
        """

        :param board:
        :type board:Board
        :return:
        """
        while True:
            try:
                x, y = list(map(lambda x: int(x.strip()),
                                input("select cell (two numbers)").split()))
                board.move(x, y)
                break
            except OutTheBoard:
                print("your step is out the board")
            except InvalidMove:
                print("This cell is not free")
            except ValueError:
                print("please input two numbers")

        return x, y


def start_game():
    """
    This function start the game
    :return:
    """
    board = Board()

    p = Player()
    x_h, y_h = p.move(board)
    print(board, "\n******************************************")
    previous_moves = []
    previous_moves.append((x_h, y_h,))
    bot = Bot((x_h, y_h,))
    count = 1
    while True:
        try:
            if count % 2 == 1:
                x, y = bot.move(previous_moves)
                board.move(x, y)
                previous_moves.append((x, y,))
            else:
                x, y = p.move(board)
                previous_moves.append((x, y,))
            count += 1
            print(board, "\n******************************************")
        except EndGame:
            print(board, "\n******************************************")
            break


if __name__ == '__main__':
    start_game()
