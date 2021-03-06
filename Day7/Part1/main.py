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

def getMedian(inputs: List[int]) -> List[int]:
  nLen = len(inputs);
  sortedInputs = sorted(inputs);

  medianPosition = nLen/2;

  if medianPosition.is_integer():
    return [sortedInputs[int(medianPosition)]];
  else:
    medianLeftPosition = int(math.floor(medianPosition));
    medianRightPosition = int(math.ceil(medianPosition));
    medianLeft = sortedInputs[medianLeftPosition];
    medianRight = sortedInputs[medianRightPosition];

    return [medianLeft, medianRight];

def getFuel(inputs: List[int], positions: List[int]) -> int:
  leastFuelConsumed = -1;

  for position in positions:
    fuelConsumed = 0;

    for input in inputs:
      fuelConsumed += abs(input - position);
    
    if leastFuelConsumed == -1 or fuelConsumed < leastFuelConsumed:
      leastFuelConsumed = fuelConsumed;
    
  return fuelConsumed;

def main():
  # inputs = [16, 1, 2, 0, 4, 2, 7, 1, 2, 14];
  inputs = parseFileIntoArray(fileName);
  positions = getMedian(inputs);
  fuelConsumed = getFuel(inputs, positions);
  print(f'{positions=}');
  print(f'{fuelConsumed=}');

main();