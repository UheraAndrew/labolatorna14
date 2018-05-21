class OutTheBoard(Exception):
    pass


class InvalidMove(Exception):
    pass


class EndGame(Exception):
    pass


class Board:

    def __init__(self):
        self.board = [[None for i in range(3)] for j in range(3)]
        self.your_move = True
        self.end_game = False

    def current_state(self):
        """

        :return: 1 if winner present, 0 if draw,-1 game continues
        """
        win = self.is_win()
        if win[0] != 0:
            print("Winner present")
            return win
        if self.is_draw():
            print("draw")
            return 0, None
        return None

    def is_win(self):
        counter1 = 0
        counter2 = 0

        for i in range(3):
            if self.board[i][i] is not None:
                counter1 += 1 if self.board[i][i] == "x" else -1
            if self.board[i][2 - i] is not None:
                counter2 += 1 if self.board[i][2 - i] == "x" else -1

        if abs(counter1) == 3:
            return (1, "x",) if counter1 == 3 else (-1, "o",)
        if abs(counter2) == 3:
            return (1, "x",) if counter2 == 3 else (-1, "o",)

        for i in range(3):
            counter1 = 0
            counter2 = 0
            for j in range(3):
                if self.board[i][j] is not None:
                    counter1 += 1 if self.board[i][j] == "x" else -1
                if self.board[j][i] is not None:
                    counter2 += 1 if self.board[j][i] == "x" else -1

            if abs(counter1) == 3:
                return (1, "x",) if counter1 == 3 else (-1, "o",)
            if abs(counter2) == 3:
                return (1, "x",) if counter2 == 3 else (-1, "o",)

        return (0, None,)

    def is_draw(self):
        for i in range(3):
            for j in range(3):
                if self.board[i][j] is None:
                    return False
        return True

    def free_cells(self):
        out = []
        for i in range(3):
            for j in range(3):
                if self.board[i][j] is None:
                    out.append((i, j,))
        return out

    def __str__(self):
        out = ""
        for i in self.board:
            for j in i:
                if j is None:
                    out += " "
                else:
                    out += j
            out += "\n"
        return out

    def move(self, x, y):

        if not (0 <= x <= 2) or not (0 <= y <= 2):
            raise OutTheBoard()
        if (x, y,) not in self.free_cells():
            if self.end_game:
                raise EndGame
            raise InvalidMove()

        self.your_move = not self.your_move
        self.board[x][y] = "x" if (self.your_move is True) else "o"

        if self.is_win()[0] != 0 \
                or self.is_draw() or self.free_cells() == None:
            raise EndGame
