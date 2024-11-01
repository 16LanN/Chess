from random import randint

class Piece:
    def __init__(self, color):
        self.name = None
        self.color = color
    def __str__(self):
        return self.symbol
    def is_valid_move(self, board, start_pos, end_pos):
        raise NotImplementedError("Метод должен быть определен в подклассе")

class King(Piece):
    def __init__(self, color):
        super().__init__(color)
        self.name = 'King'
        self.symbol = '♔' if color == 'black' else '♚'
        self.virgin = True
        self.alive = True

    def is_valid_move(self, board, start_pos, end_pos):
        start_row, start_col = start_pos
        end_row, end_col = end_pos
        final_col = abs(start_col - end_col)
        final_row = abs(start_row - end_row)
        if final_col <= 1 and final_row <= 1 and (final_col != 0 or final_row != 0):
            if board[end_row][end_col] and board[end_row][end_col].color != self.color:
                self.virgin = False
                return True
            elif board[end_row][end_col] and board[end_row][end_col].color == self.color:
                return False
            self.virgin = False
            return True
        elif start_col - end_col == -2 and not board[end_row][end_col] and not board[end_row][end_col-1] and self.virgin == True and board[end_row][end_col+1].virgin == True and board[end_row][end_col+1].color == self.color:
            return True, 1
        elif start_col - end_col == 2 and not board[end_row][end_col] and not board[end_row][end_col+1] and not board[end_row][end_col-1] and self.virgin == True and board[end_row][end_col-2].virgin == True and board[end_row][end_col-2].color == self.color:
            print('work')
            return True, 2
        else:
            return False

class Queen(Piece):
    def __init__(self, color):
        super().__init__(color)
        self.name = 'Queen'
        self.symbol = '♕' if color == 'black' else '♛'

    def is_valid_move(self, board, start_pos, end_pos):
        start_row, start_col = start_pos
        end_row, end_col = end_pos
        if abs(start_row - end_row) == abs(start_col - end_col):
            step_col = 1 if end_col > start_col else -1
            step_row = 1 if end_row > start_row else -1
            col, row = start_col + step_col, start_row + step_row
            while (col, row) != (end_col, end_row):
                if board[row][col]:
                    return False
                col += step_col
                row += step_row
            if board[end_row][end_col] and board[end_row][end_col].color != self.color:
                return True
            elif board[end_row][end_col] and board[end_row][end_col].color == self.color:
                return False
            return True
        if start_row == end_row:
            step = 1 if start_col < end_col else -1
            for col in range(start_col + step, end_col, step):
                if board[start_row][col] is not None:
                    return False
        elif start_col == end_col:
            step = 1 if start_row < end_row else -1
            for row in range(start_row + step, end_row, step):
                if board[row][start_col] is not None:
                    return False
        if start_row != end_row and start_col != end_col:
            return False
        if board[end_row][end_col] and board[end_row][end_col].color != self.color:
            return True
        elif board[end_row][end_col] and board[end_row][end_col].color == self.color:
            return False
        return True

class Rook(Piece):
    def __init__(self, color):
        super().__init__(color)
        self.name = 'Rook'
        self.symbol = '♖' if color == 'black' else '♜'
        self.virgin = True

    def is_valid_move(self, board, start_pos, end_pos):
        start_row, start_col = start_pos
        end_row, end_col = end_pos
        if start_row != end_row and start_col != end_col:
            return False
        if start_row == end_row:
            step = 1 if start_col < end_col else -1
            for col in range(start_col + step, end_col, step):
                if board[start_row][col] is not None:
                    return False
        else:
            step = 1 if start_row < end_row else -1
            for row in range(start_row + step, end_row, step):
                if board[row][start_col] is not None:
                    return False
        if board[end_row][end_col] and board[end_row][end_col].color != self.color:
            self.virgin = False
            return True
        elif board[end_row][end_col] and board[end_row][end_col].color == self.color:
            return False
        self.virgin = False
        return True

class Bishop(Piece):
    def __init__(self, color):
        super().__init__(color)
        self.name = 'Bishop'
        self.symbol = '♗' if color == 'black' else '♝'

    def is_valid_move(self, board, start_pos, end_pos):
        start_row, start_col = start_pos
        end_row, end_col = end_pos
        if abs(start_row - end_row) != abs(start_col - end_col):
            return False
        if board[end_row][end_col] and board[end_row][end_col].color != self.color:
            return True
        elif board[end_row][end_col] and board[end_row][end_col].color == self.color:
            return False
        step_col = 1 if end_col > start_col else -1
        step_row = 1 if end_row > start_row else -1
        col, row = start_col + step_col, start_row + step_row
        while (col, row) != (end_col, end_row):
            if board[row][col]:
                return False
            col += step_col
            row += step_row
        return True

class Star(Piece):
    def __init__(self, color):
        super().__init__(color)
        self.name = 'Star'
        self.symbol = '★' if color == 'white' else '☆'

    def piece_taking(self, board, end_pos):
        end_row, end_col = end_pos
        if board[end_row][end_col] and board[end_row][end_col].color != self.color:
            return True
        elif board[end_row][end_col] and board[end_row][end_col].color == self.color:
            return False
        else:
            return True

    def is_valid_move(self, board, start_pos, end_pos):
        start_row, start_col = start_pos
        end_row, end_col = end_pos
        final_col = abs(start_col - end_col)
        final_row = abs(start_row - end_row)
        if final_col <= 1 and final_row <= 1 and (final_col != 0 or final_row != 0):
            if board[end_row][end_col] and board[end_row][end_col].color != self.color:
                return self.piece_taking(board, end_pos), True, 1
            elif board[end_row][end_col] and board[end_row][end_col].color == self.color:
                return False
            return True
        else:
            return False
        
    
class Goose(Piece):
    def __init__(self, color):
        super().__init__(color)
        self.name = 'Goose'
        self.symbol = '▽' if color == 'black' else '▼'

    def piece_taking(self, board, end_pos):
        end_row, end_col = end_pos
        if board[end_row][end_col] and board[end_row][end_col].color != self.color:
            return True
        elif board[end_row][end_col] and board[end_row][end_col].color == self.color:
            return False
        else:
            return True

    def is_valid_move(self, board, start_pos, end_pos):
        start_row, start_col = start_pos
        end_row, end_col = end_pos
        direction_col = 2 if start_col < end_col else -2
        direction_row = -2 if self.color == 'white' else 2
        final_row = abs(start_row - end_row)
        final_col = abs(start_col - end_col)

        if final_col == final_row and (final_row + final_col) == 2:
            if start_row < end_row and start_col < end_col and self.color == 'white':
                return False
            elif start_row > end_row and start_col > end_col and self.color == 'black':
                return False
            else: 
                return self.piece_taking(board, end_pos)

        if start_col == end_col and end_row == start_row + direction_row:
            if board[end_row+1][end_col] and board[end_row+1][end_col].color == self.color and self.color == 'white':
                dice = randint(1, 6)
                row = end_row + 1
                if dice % 2 == 0:
                    return self.piece_taking(board, end_pos), True, row, end_col, dice
                else:
                    return self.piece_taking(board, end_pos), False, 0, 1, dice
            elif board[end_row-1][end_col] and board[end_row-1][end_col].color == self.color and self.color == 'black':
                dice = randint(1, 6)
                row = end_row -1 
                if dice % 2 == 0:
                    return self.piece_taking(board, end_pos), True, row, end_col, dice
                else:
                    return self.piece_taking(board, end_pos), False, 0, 1, dice
            return self.piece_taking(board, end_pos)

        if start_row == end_row and end_col == start_col + direction_col:
            if start_col > end_col:
                if board[end_row][end_col+1] and board[end_row][end_col+1].color == self.color:
                    dice = randint(1, 6)
                    col = end_col + 1
                    if dice % 2 == 0:
                        return self.piece_taking(board, end_pos), True, end_row, col, dice
                    else:
                        return self.piece_taking(board, end_pos), False, 0, 1, dice
            elif start_col < end_col:
                if board[end_row][end_col-1] and board[end_row][end_col-1].color == self.color:
                    dice = randint(1, 6)
                    col = end_col - 1
                    if dice % 2 == 0:
                        return self.piece_taking(board, end_pos), True, end_row, col, dice
                    else:
                        return self.piece_taking(board, end_pos), False, 0, 1, dice
            return self.piece_taking(board, end_pos)
        return False


class Knight(Piece):
    def __init__(self, color):
        super().__init__(color)
        self.name = 'Knight'
        self.symbol = '♘' if color == 'black' else '♞'

    def is_valid_move(self, board, start_pos, end_pos):
        start_row, start_col = start_pos
        end_row, end_col = end_pos
        final_row = abs(end_row - start_row)
        final_col = abs(end_col - start_col)
        if final_row == 2 and final_col == 1 or final_col == 2 and final_row == 1:
            if board[end_row][end_col] and board[end_row][end_col].color != self.color:
                return True
            elif board[end_row][end_col] and board[end_row][end_col].color == self.color:
                return False
            else:
                return True
        else:
            return False

class Pawn(Piece):
    def __init__(self, color):
        super().__init__(color)
        self.name = 'Pawn'
        self.symbol = '♙' if color == 'black' else '♟'

    def is_valid_move(self, board, start_pos, end_pos):
        direction = -1 if self.color == 'white' else 1
        start_row, start_col = start_pos
        end_row, end_col = end_pos
        if start_col == end_col and end_row == start_row + direction and board[end_row][end_col]:
            return False
        if start_col == end_col and end_row == start_row + direction:
            return True
        if start_col == end_col and end_row == start_row + direction*2:
            if start_row == 1:
                return True
            elif start_row == 6:
                return True
            else:
                return False
        if abs(start_col - end_col) == 1 and end_row == start_row + direction:
            target_piece = board[end_row][end_col]
            if target_piece and target_piece.color != self.color:
                return True
        return False
        

class ChessBoard:
    def __init__(self):
        self.board = self.create_board()

    def create_board(self):
        board = [[None] * 8 for _ in range(8)]
        board[0] = [Rook('black'), Star('black'), Goose('black'), Queen('black'), King('black'), Goose('black'), Knight('black'), Rook('black')]
        board[1] = [Pawn('black') for _ in range(8)]
        board[6] = [Pawn('white') for _ in range(8)]
        board[7] = [Rook('white'), Star('white'), Goose('white'), Queen('white'), King('white'), Goose('white'), Knight('white'), Rook('white')]
        
        # board[0] = [Rook('white'), King('black'), None, None, None, None, None, None]
        # board[7] = [None, King('white'), None, None, None, None, None, None]

        # board[0] = [King('black'), Star('white'), Rook('black'), None, None, None, None, None]
        # board[7] = [Star('black'), King('white'), Rook('white'), None, None, None, None, None]
        return board

    def display(self):
        for row in self.board:
            print(" ".join([str(piece) if piece else '▢' for piece in row]))


class ChessGame:
    def __init__(self):
        self.board = ChessBoard()
        self.turn = 'white'

    def kingsexistance(self, board):
        king_counter = 0
        pieces = 0
        for i in range(8):
            for j in range(8):
                if board[i][j] == None:
                    pass
                elif board[i][j].name == 'King':
                    king_counter += 1
                if board[i][j]:
                    pieces += 1
        if king_counter == 2:
            if pieces == 2:
                print('Ничья')
                return False
            return True
        elif king_counter != 2:
            print(f'{self.turn} проиграли')
            return False



    def play(self):
        while True:
            self.board.display()
            if not self.kingsexistance(self.board.board):
                print("Игра завершена.")
                break

            move = input(f"{self.turn}'s move (формат: начальная позиция конечная позиция): ")
            print('''-------------------------------------------------------------------------
                  
                  
                  ''')
            if move.lower() == 'exit':
                print("Игра завершена.")
                break
            start_pos, end_pos = move.split()
            start_pos = self.parse_position(start_pos)
            end_pos = self.parse_position(end_pos)
            if self.move_piece(start_pos, end_pos):
                self.turn = 'black' if self.turn == 'white' else 'white'
            else:
                print('Недопустимый ход. Попробуйте снова.')

    def parse_position(self, pos):
        column, row = pos
        return 8 - int(row), ord(column) - ord('a')

    def move_piece(self, start_pos, end_pos):
        piece = self.board.board[start_pos[0]][start_pos[1]]
        if piece and piece.color == self.turn:
            if piece.is_valid_move(self.board.board, start_pos, end_pos):

                if len(str(piece.is_valid_move(self.board.board, start_pos, end_pos)).split()) == 5:
                    valid_move, death_or_life, row, col, dice = piece.is_valid_move(self.board.board, start_pos, end_pos)
                    if death_or_life:
                        print(f'Шестигранная кость показала - {dice}. Пешка умирает.')
                        self.board.board[end_pos[0]][end_pos[1]] = piece
                        self.board.board[start_pos[0]][start_pos[1]] = None
                        self.board.board[row][col] = None
                        return True
                    else:
                        print(f'Шестигранная кость показала - {dice}. Пешка выживает')
                        self.board.board[end_pos[0]][end_pos[1]] = piece
                        self.board.board[start_pos[0]][start_pos[1]] = None
                        return True

                elif len(str(piece.is_valid_move(self.board.board, start_pos, end_pos)).split()) == 2:
                    valid_move, rand = piece.is_valid_move(self.board.board, start_pos, end_pos)
                    print('Рокировка')
                    self.board.board[end_pos[0]][end_pos[1]] = piece
                    if rand == 1:
                        self.board.board[end_pos[0]][end_pos[1]-1] = self.board.board[end_pos[0]][end_pos[1]+1]
                        self.board.board[end_pos[0]][end_pos[1]+1] = None
                    elif rand == 2:
                        self.board.board[end_pos[0]][end_pos[1]+1] = self.board.board[end_pos[0]][end_pos[1]-2]
                        self.board.board[end_pos[0]][end_pos[1]-2] = None
                    self.board.board[start_pos[0]][start_pos[1]] = None
                    return True

                elif len(str(piece.is_valid_move(self.board.board, start_pos, end_pos)).split()) == 3:
                    self.board.board[end_pos[0]][end_pos[1]] = piece
                    self.board.board[start_pos[0]][start_pos[1]] = None
                    pieces = [None, Knight(piece.color), None, Bishop(piece.color), None, Goose(piece.color), None, Rook(piece.color), Star(piece.color), None, Pawn(piece.color), None]
                    random = randint(0, 11)
                    if pieces[random] == None:
                        print('Не повезло. Фигуру воскресить не получилось...')
                    else:
                        print('Воскрешение!')
                    self.board.board[start_pos[0]][start_pos[1]] = pieces[random]
                    return True
                
                else:
                    self.board.board[end_pos[0]][end_pos[1]] = piece
                    self.board.board[start_pos[0]][start_pos[1]] = None
                    return True


            else:
                print('Недопустимый ход фигуры.')
        return False


if __name__ == "__main__":
    game = ChessGame()
    game.play()
