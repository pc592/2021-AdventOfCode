from typing import List;
from dataclasses import dataclass;

fileName = './Day5/input.txt';
maxDomain = 0;
maxRange = 0;

def parseFileIntoArray(fileName) -> List[str]:
  # reads into an array
  with open(fileName) as f:
    lines = f.readlines()
  
  # sanitize (using list comprehension)
  sanitizedLines = [line.strip() for line in lines];

  return sanitizedLines;

@dataclass
class Point:
  x: int;
  y: int;

@dataclass
class Line:
  start: Point;
  end: Point;

def createPoint(postion: str) -> Point:
  point = postion.strip().split(',');
  
  x = int(point[0]);
  y = int(point[1]);

  global maxDomain;
  if x > maxDomain:
    maxDomain = x;
  global maxRange;
  if y > maxRange:
    maxRange = y;

  return Point(x, y);

def parseInput(input: str) -> Line:
  splitInput = input.split('->');

  startPoint = createPoint(splitInput[0]);
  endPoint = createPoint(splitInput[1]);

  return Line(startPoint, endPoint);

def getVentLines(inputs: List[str]) -> List[Line]:
  return [parseInput(input) for input in inputs];

def isHorizontalVerticalLine(line: Line) -> bool:
  return line.start.x == line.end.x or line.start.y == line.end.y;

def buildEmptyVentMap() -> List[List[int]]:
  global maxDomain, maxRange;

  return [
    [
      0 for j in range(maxDomain+1)
    ] for i in range(maxRange+1)
  ];

@dataclass
class DirectedLine:
  x1: int = 0;
  y1: int = 0;
  x2: int = 0;
  y2: int = 0;
  delta: int = 0;

def buildHorizontalXY(startPoint: Point, endPoint: Point) -> DirectedLine:
  minX = min(startPoint.x, endPoint.x);
  maxX = max(startPoint.x, endPoint.x);
  minY = min(startPoint.y, endPoint.y);
  maxY = max(startPoint.y, endPoint.y);

  return DirectedLine(x1=minX, y1=minY, x2=maxX, y2=maxY);

def buildDiagonalXY(startPoint: Point, endPoint: Point) -> DirectedLine:
  directedLine = None;

  if startPoint.y <= endPoint.y:
    directedLine = DirectedLine(x1=startPoint.x, y1=startPoint.y, x2=endPoint.x, y2=endPoint.y);
  else:
    directedLine = DirectedLine(x1=endPoint.x, y1=endPoint.y, x2=startPoint.x, y2=startPoint.y);
  
  if directedLine.x1 > directedLine.x2:
    directedLine.delta = -1;
  elif directedLine.x1 < directedLine.x2:
    directedLine.delta = 1;
  else:
    print('How did you get here, something is wrong.')

  return directedLine;

def getNumOfOverlaps(ventLines: List[Line]) -> int:
  ventMap = buildEmptyVentMap();
  countedPositions = buildEmptyVentMap();
  nOverlaps = 0;
  
  # fill out vent map
  for ventLine in ventLines:
    startPoint = ventLine.start;
    endPoint = ventLine.end;

    if isHorizontalVerticalLine(ventLine):
      horizontalXY = buildHorizontalXY(startPoint, endPoint);

      for row in range(horizontalXY.y1, horizontalXY.y2+1):
        for col in range(horizontalXY.x1, horizontalXY.x2+1):
          ventMap[row][col] += 1;
          if (ventMap[row][col]) > 1 and countedPositions[row][col] == 0:
            countedPositions[row][col] = 1;
            nOverlaps += 1;
    else:
      # diagonal line
      diagonalXY = buildDiagonalXY(startPoint, endPoint);
      deltaCol = diagonalXY.delta;

      col = diagonalXY.x1;
      for row in range(diagonalXY.y1, diagonalXY.y2+1):
        ventMap[row][col] += 1;
        if (ventMap[row][col]) > 1 and countedPositions[row][col] == 0:
            countedPositions[row][col] = 1;
            nOverlaps += 1;
        
        col += deltaCol;

  # print(f'{countedPositions=}');
  # print(f'{ventMap=}');

  return nOverlaps;

def main():
  # inputs = ['0,9 -> 5,9', '8,0 -> 0,8', '9,4 -> 3,4', '2,2 -> 2,1', '7,0 -> 7,4', '6,4 -> 2,0', '0,9 -> 2,9', '3,4 -> 1,4', '0,0 -> 8,8', '5,5 -> 8,2'];
  inputs = parseFileIntoArray(fileName);
  ventLines = getVentLines(inputs);
  nOverlaps = getNumOfOverlaps(ventLines);
  print(f'{nOverlaps=}');

main();