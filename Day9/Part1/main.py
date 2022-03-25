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

def findLowPoints(heightmap: List[str]) -> List[int]:
  lowPoints = [];
  nRow = len(heightmap);
  nCol = len(heightmap[0]) if nRow else 0;

  for rowIdx in range(0,nRow):
    for colIdx in range(0,nCol):
      isLowPoint = getIsLowPoint(heightmap, nRow, nCol, rowIdx, colIdx);
      if (isLowPoint):
        lowPoints.append(int(heightmap[rowIdx][colIdx]));
  return lowPoints;

def calculateRiskLevel(lowPoints: List[int]) -> int:
  riskLevel = 0;

  for lowPoint in lowPoints:
    riskLevel += lowPoint+1;

  return riskLevel;

def main():
  # inputs = parseFileIntoArray(testFileName);
  inputs = parseFileIntoArray(fileName);
  lowPoints = findLowPoints(inputs);
  riskLevel = calculateRiskLevel(lowPoints);
  print(f'{riskLevel=}');

main();