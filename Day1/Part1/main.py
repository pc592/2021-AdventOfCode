from typing import List;

fileName = './Day1/input.txt';

def parseFileIntoArray(fileName) -> List[int]:
  # reads into an array
  with open(fileName) as f:
    lines = f.readlines()
  
  # sanitize (using list comprehension)
  sanitizedLines = [int(line.strip()) for line in lines];

  return sanitizedLines;

def getNumberOfIncreases(inputs: List[int]) -> int:
  nIncreases = 0;

  # loop starting at the second element (and keeping the correct index)
  for idx, input in enumerate(inputs[1:], start=1):
    prevInput = inputs[idx-1];
    if input > prevInput:
      nIncreases+=1;

  return nIncreases;

def main():
  # inputs = [199, 200, 208, 210, 200, 207, 240, 269, 260, 263];
  inputs = parseFileIntoArray(fileName);
  result = getNumberOfIncreases(inputs);
  print(f'nIncreases: {result}');

main();