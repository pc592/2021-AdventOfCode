from typing import List;
from dataclasses import dataclass;

fileName = './Day9/input.txt';
testFileName = './Day9/testInput.txt';

@dataclass
class Point:
  rowIdx: int;
  colIdx: int;

def parseFileIntoArray(fileName) -> List[str]:
  # reads into an array
  with open(fileName) as f:
    lines = f.readlines()
  
  sanitizedLines = [line.strip() for line in lines];

  return sanitizedLines;

def getPointsToCheck(nRow: int, nCol: int, rowIdx: int, colIdx: int) -> List[Point]:
  pointsToCheck = [];

  if not (rowIdx-1 < 0):
    pointsToCheck.append(Point(rowIdx-1, colIdx)); # up

  if not (rowIdx+1 == nRow):
    pointsToCheck.append(Point(rowIdx+1, colIdx)); # down

  if not (colIdx-1 < 0):
    pointsToCheck.append(Point(rowIdx, colIdx-1)); # left

  if not (colIdx+1 == nCol):
    pointsToCheck.append(Point(rowIdx, colIdx+1)); # right

  return pointsToCheck;

def getIsLowPoint(heightmap: List[str], nRow: int, nCol: int, rowIdx: int, colIdx: int) -> bool:
  point = heightmap[rowIdx][colIdx];

  pointsToCheck = getPointsToCheck(nRow, nCol, rowIdx, colIdx);

  isLowPoint = True;

  for checkPoint in pointsToCheck:
    adjacentPoint = heightmap[checkPoint.rowIdx][checkPoint.colIdx]
    if (adjacentPoint <= point):
      isLowPoint = False;

  return isLowPoint;

def findLowPoints(heightmap: List[str]) -> List[Point]:
  lowPoints = [];
  nRow = len(heightmap);
  nCol = len(heightmap[0]) if nRow else 0;

  for rowIdx in range(0,nRow):
    for colIdx in range(0,nCol):
      isLowPoint = getIsLowPoint(heightmap, nRow, nCol, rowIdx, colIdx);
      if (isLowPoint):
        lowPoints.append(Point(rowIdx, colIdx));

  return lowPoints;

def dfsForBasinSize(heightmap: List[str], visitedNodes: List[List[bool]], nodesToVisit: List[Point]) -> int:
  nRow = len(heightmap);
  nCol = len(heightmap[0]) if nRow else 0;

  basinSize = 1;

  while len(nodesToVisit) != 0:
    nodeToVisit = nodesToVisit.pop();
    rowIdx = nodeToVisit.rowIdx;
    colIdx = nodeToVisit.colIdx;
    if (visitedNodes[rowIdx][colIdx] != True):
      visitedNodes[rowIdx][colIdx] = True;

      if heightmap[rowIdx][colIdx] != '9':
        basinSize += 1;
        
        newNodes = getPointsToCheck(nRow, nCol, rowIdx, colIdx);
        for newNode in newNodes:
          newNodeRowIdx = newNode.rowIdx;
          newNodeColIdx = newNode.colIdx;
          if visitedNodes[newNodeRowIdx][newNodeColIdx] == False:
            nodesToVisit.append(newNode);

  return basinSize;

def calculateBasinSize(heightmap: List[str], lowPoint: Point) -> int:
  nRow = len(heightmap);
  nCol = len(heightmap[0]) if nRow else 0;

  rowIdx = lowPoint.rowIdx;
  colIdx = lowPoint.colIdx;
  
  # do a DFS for 9's?
  visitedNodes = [
    [
      False for j in range(nCol)
    ] for i in range(nRow)
  ];
  visitedNodes[rowIdx][colIdx] = True;

  nodesToVisit = getPointsToCheck(nRow, nCol, rowIdx, colIdx);

  return dfsForBasinSize(heightmap, visitedNodes, nodesToVisit);

# there's probably a more efficient way, by calculating the basin size
#   after or while determining a low point, but this is cleaner
def calculateBasinSizes(heightmap: List[str], lowPoints: List[Point]) -> List[int]:
  basinSizes = [];

  for lowPoint in lowPoints:
    basinSizes.append(calculateBasinSize(heightmap, lowPoint));

  return basinSizes;

def getThreeLargestBasins(basinSizes: List[int]) -> int:
  sortedBasinSizes = sorted(basinSizes, reverse=True);
  return sortedBasinSizes[0] * sortedBasinSizes[1] * sortedBasinSizes[2];

def main():
  # inputs = parseFileIntoArray(testFileName);
  inputs = parseFileIntoArray(fileName);
  lowPoints = findLowPoints(inputs);
  basinSizes = calculateBasinSizes(inputs, lowPoints);
  result = getThreeLargestBasins(basinSizes);
  print(f'{result=}');

main();