from typing import List, Dict;
from dataclasses import dataclass, field;

fileName = './Day4/input.txt';

@dataclass
class Board:
  nRow: int = 0;
  nCol: int = 0;
  tiles: List[List[str]] = field(default_factory=list);
  markedTiles: List[List[str]] = field(default_factory=list);

@dataclass
class Bingo:
  drawnNumbers: List[str] = field(default_factory=list);
  boards: List[Board] = field(default_factory=list);

def parseFileIntoArray(fileName) -> Bingo:
  # reads into an array
  with open(fileName) as f:
    lines = f.readlines()
  
  return lines;

# initialize matrix with nRow and nCol to False values
def buildMarkedTiles(nRow: str, nCol: str) -> List[List[bool]]:
  return [
    [
      False for j in range(nCol)
    ] for i in range(nRow)
  ];

def buildBoards(lines: List[str]) -> List[Board]:
  boards = [];

  board = Board();
  for line in lines:
    if '\n' == line:
      # initialize markedTiles to false for board
      board.markedTiles = buildMarkedTiles(board.nRow, board.nCol);
      
      # save board
      boards.append(board);

      # start new board
      board = Board();
    else:
      row = line.strip().split();

      # update board row/col size (if needed)
      board.nRow = len(row) if board.nRow == 0 else board.nRow;
      board.nCol += 1;

      # update board tiles
      board.tiles.append(row);
  
  # initialize markedTiles to false for last board
  board.markedTiles = buildMarkedTiles(board.nRow, board.nCol);

  # save the last board
  boards.append(board);

  return boards;

def buildBingo(lines: List[str]) -> Bingo:
  bingo = Bingo();

  # the first line is the drawn numbers, in order
  bingo.drawnNumbers = lines[0].strip().split(',');

  # build bingo boards from the rest of the lines
  bingo.boards = buildBoards(lines[2:]);

  return bingo;

@dataclass
class MemoizeLocation:
  board: str;
  row: str;
  col: str;

def memoizeBoard(board: Board, boardNumber: str, memo: Dict) -> None:
  for row in range(board.nRow):
    for col in range(board.nCol):
      tile = board.tiles[row][col];
      if tile not in memo:
        memo[tile] = [];
      memo[tile].append(MemoizeLocation(boardNumber, row, col));

def memoizeBoards(boards: List[Board]) -> Dict:
  memo = {};
  for idx, board in enumerate(boards):
    memoizeBoard(board, idx, memo);
  return memo;

def markBoards(drawnNumber: str, memo: Dict, boards: List[Board]) -> List[Board]:
  locations = memo[drawnNumber];
  for location in locations:
    boards[location.board].markedTiles[location.row][location.col] = True;
  return boards;

def checkRows(tiles: List[List[str]]) -> bool:
  hasBingo = False;
  nRow = len(tiles);

  rowIdx = 0;
  while hasBingo == False and rowIdx < nRow:
    row = tiles[rowIdx];
    nCol = len(row);
    nFalses = nCol;
    for colIdx in range(nCol):
      if row[colIdx] == True:
        nFalses -= 1;
    hasBingo = nFalses == 0;
    rowIdx += 1;
  
  return hasBingo;

def checkCols(tiles: List[List[str]]) -> bool:
  hasBingo = False;
  nRow = len(tiles);
  nCol = len(tiles[0]);

  colIdx = 0;
  while hasBingo == False and colIdx < nCol:
    nFalses = nCol;
    for rowIdx in range(nRow):
      if tiles[rowIdx][colIdx] == True:
        nFalses -= 1;
    hasBingo = nFalses == 0;
    colIdx += 1;
  
  return hasBingo;

@dataclass
class Loser:
  board: Board;
  drawnNumber: str;

def checkBoards(unwonBoardsIdxList: List[str], boards: List[Board]) -> List[str]:
  hasWinningBoard = False;
  winningBoardIndexes = [];

  unwonBoardsIdx = 0;
  while unwonBoardsIdx < len(unwonBoardsIdxList):
    boardIdx = unwonBoardsIdxList[unwonBoardsIdx];
    board = boards[boardIdx];
    markedTiles = board.markedTiles;
    hasWinningBoard = checkRows(markedTiles) or checkCols(markedTiles);

    if hasWinningBoard == True:
      winningBoardIndexes.append(unwonBoardsIdxList[unwonBoardsIdx])

    unwonBoardsIdx += 1;

  if len(winningBoardIndexes) == 0:
    return None;
  else:
    return winningBoardIndexes;

def getLoser(bingo: Bingo) -> Loser:
  # memoize boards so we don't have to re-evaluate every board for every drawn number
  memo = memoizeBoards(bingo.boards);

  drawnNumbers = bingo.drawnNumbers;
  boards = bingo.boards;
  unwonBoardsIdxList = list(range(len(boards)));
  loser = None;

  drawnIdx = 0;
  while loser == None and drawnIdx < len(drawnNumbers):
    drawnNumber = drawnNumbers[drawnIdx];
    bingo.boards = markBoards(drawnNumber, memo, boards);
    winningBoardIndexes = checkBoards(unwonBoardsIdxList, bingo.boards);
    if winningBoardIndexes is not None:
      for winningBoardIdx in winningBoardIndexes:
        if winningBoardIdx in unwonBoardsIdxList:
          unwonBoardsIdxList.remove(winningBoardIdx);
          if len(unwonBoardsIdxList) == 0:
            loser = Loser(bingo.boards[winningBoardIdx], drawnNumber);

    drawnIdx += 1;

  return loser;

def calculateScore(loser: Loser):
  tiles = loser.board.tiles;
  markedTiles = loser.board.markedTiles;
  nRow = len(tiles);
  nCol = len(tiles[0]);

  unmarkedScore = 0;

  for row in range(nRow):
    for col in range(nCol):
      tile = tiles[row][col];
      markedTile = markedTiles[row][col];
      if markedTile == False:
        unmarkedScore += int(tile);
  
  return unmarkedScore * int(loser.drawnNumber);

def main():
  # inputs = ['7,4,9,5,11,17,23,2,0,14,21,24,10,16,13,6,15,25,12,22,18,20,8,19,3,26,1\n', '\n', '22 13 17 11  0\n', ' 8  2 23 4 24\n', '21  9 14 16  7\n', ' 6 10  3 18  5\n', ' 1 12 20 15 19\n', '\n', ' 3 15  0  2 22\n', ' 9 18 13 17  5\n', '19  8  7 25 23\n', '20 11 10 24  4\n', '14 21 16 12  6\n', '\n', '14 21 17 24  4\n', '10 16 15  9 19\n', '18 8 23 26 20\n', '22 11 13  6  5\n', ' 2  0 12  3  7'];
  inputs = parseFileIntoArray(fileName);

  bingo = buildBingo(inputs);
  loser = getLoser(bingo);
  score = calculateScore(loser);
  print(f'{loser=}');
  print(f'{score=}');

main();