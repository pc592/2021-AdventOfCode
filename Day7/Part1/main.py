from typing import List;
import math;

fileName = './Day7/input.txt';

def parseFileIntoArray(fileName) -> List[int]:
  # reads into an array
  with open(fileName) as f:
    lines = f.readlines()
  
  # sanitize (using list comprehension)
  # there is only one relevant line, containing an array
  sanitizedLines = [int(num.strip()) for num in lines[0].split(',')];

  return sanitizedLines;

def getMedian(inputs: List[int]) -> int:
  nLen = len(inputs);
  sortedInputs = sorted(inputs);

  medianPosition = nLen/2;

  if medianPosition.is_integer():
    return sortedInputs[int(medianPosition)];
  else:
    medianLeftPosition = int(math.floor(medianPosition));
    medianRightPosition = int(math.ceil(medianPosition));
    medianLeft = sortedInputs[medianLeftPosition];
    medianRight = sortedInputs[medianRightPosition];
    return int(round((medianLeft + medianRight) / 2), 0);

def getFuel(inputs: List[int], position: int) -> int:
  fuelConsumed = 0;

  for input in inputs:
    fuelConsumed += abs(input - position);
  
  return fuelConsumed;

def main():
  # inputs = [16, 1, 2, 0, 4, 2, 7, 1, 2, 14];
  inputs = parseFileIntoArray(fileName);
  position = getMedian(inputs);
  fuelConsumed = getFuel(inputs, position);
  print(f'{position=}');
  print(f'{fuelConsumed=}');

main();