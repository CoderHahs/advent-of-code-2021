import tools as t

data = t.read_file("d4_data.txt")

class Board:
  def __init__(self, n, board):
    self.n = n
    self.board = []
    self.populate_board(board)
  
  def populate_board(self, board):
    for row in board:
      bingo_row = []
      for n in row.split():
        bingo_row.append([n, False])
      self.board.append(bingo_row)

  def check_columns(self):
    for col in self.get_columns():
      check = True
      for i in range(self.n):
        if col[i][1] == False:
          check = False
      if check == True:
        return check
    return check
    
  def check_rows(self):
    for row in self.get_rows():
      check = True
      for i in range(self.n):
        if row[i][1] == False:
          check = False
      if check == True:
        return check
    return check

  def get_columns(self):
    cols = []
    for i in range(self.n):
      col = []
      for j in range(self.n):
        col.append(self.board[j][i])
      cols.append(col)
    return cols
  
  def get_rows(self):
    rows = []
    for row in self.board:
      rows.append(row)
    return rows

  def check_win(self):
    return self.check_columns() or self.check_rows()

  def check_number(self, number):
    # print(self.board, number)
    for i in range(self.n):
      for j in range(self.n):
        if self.board[i][j][0] == number:
          self.board[i][j][1] = True
  
  def get_sum_unmarked_nums(self):
    unmarked = 0
    for row in self.get_rows():
      for i in range(self.n):
        if row[i][1] == False:
          unmarked += int(row[i][0])
    return unmarked

  def __str__(self):
    return "Board: " + str(self.get_rows())

############### main

bingo_numbers = data[0].split(',')

bingo_boards = []

for i in range(1, len(data)-4, 5):
  board_data = [data[i], data[i+1], data[i+2], data[i+3], data[i+4]]
  bingo_boards.append(Board(5, board_data))


def get_last_board(bingo_boards, bingo_numbers):
  order_set = set()
  order = []
  for n in bingo_numbers:
    for i in range(len(bingo_boards)):
      bingo_boards[i].check_number(n)
      if (bingo_boards[i].check_win()):
        if i not in order_set:
          ans = bingo_boards[i].get_sum_unmarked_nums() * int(n)
          order.append([i,n, ans])
          order_set.add(i)
  print(order)
  return order[-1]


ans = get_last_board(bingo_boards, bingo_numbers)

print(ans[2])