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

def getMean(inputs: List[int]) -> List[int]:
  nLen = len(inputs);
  inputSum = 0;

  for input in inputs:
    inputSum += input;
  
  mean = inputSum/nLen;

  return [int(math.floor(mean)), int(math.ceil(mean))];

def calculateTriangularNumber(n: int) -> int:
  return int((pow(n, 2) + n)/2);

def getFuel(inputs: List[int], positions: List[int]) -> int:
  leastFuelConsumed = -1;

  for position in positions:
    fuelConsumed = 0;

    for input in inputs:
      fuelConsumed += calculateTriangularNumber(abs(input - position));
  
    if leastFuelConsumed == -1 or fuelConsumed < leastFuelConsumed:
      leastFuelConsumed = fuelConsumed;
  
  return leastFuelConsumed;

def main():
  # inputs = [16, 1, 2, 0, 4, 2, 7, 1, 2, 14];
  inputs = parseFileIntoArray(fileName);
  positions = getMean(inputs);
  fuelConsumed = getFuel(inputs, positions);
  print(f'{positions=}');
  print(f'{fuelConsumed=}');

main();