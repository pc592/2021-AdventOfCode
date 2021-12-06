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

# filter out lines that are not horizontal/vertical
def filterVentLines(lines: List[Line]) -> List[Line]:
  return [line for line in lines if line.start.x == line.end.x or line.start.y == line.end.y];

def buildEmptyVentMap() -> List[List[int]]:
  global maxDomain, maxRange;

  return [
    [
      0 for j in range(maxDomain+1)
    ] for i in range(maxRange+1)
  ];

def getNumOfOverlaps(ventLines: List[Line]) -> int:
  ventMap = buildEmptyVentMap();
  countedPositions = {};
  nOverlaps = 0;
  
  # fill out vent map
  for ventLine in ventLines:
    startPoint = ventLine.start;
    endPoint = ventLine.end;

    minX = min(startPoint.x, endPoint.x);
    maxX = max(startPoint.x, endPoint.x);
    minY = min(startPoint.y, endPoint.y);
    maxY = max(startPoint.y, endPoint.y);
    for row in range(minY, maxY+1):
      for col in range(minX, maxX+1):
        ventMap[row][col] += 1;
        if (ventMap[row][col]) > 1:
          if row not in countedPositions:
            countedPositions[row] = { col: True };
            nOverlaps += 1;
          else:
            if col not in countedPositions[row]:
              countedPositions[row][col] = True;
              nOverlaps += 1;

  # print(f'{countedPositions=}');
  # print(f'{ventMap=}');

  return nOverlaps;

def main():
  # inputs = ['0,9 -> 5,9', '8,0 -> 0,8', '9,4 -> 3,4', '2,2 -> 2,1', '7,0 -> 7,4', '6,4 -> 2,0', '0,9 -> 2,9', '3,4 -> 1,4', '0,0 -> 8,8', '5,5 -> 8,2'];
  inputs = parseFileIntoArray(fileName);
  ventLines = getVentLines(inputs);
  filteredVentLines = filterVentLines(ventLines);
  nOverlaps = getNumOfOverlaps(filteredVentLines);
  print(f'{nOverlaps=}');

main();