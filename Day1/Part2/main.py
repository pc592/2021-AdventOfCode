from typing import List;

fileName = './Day1/Part2/input.txt';

def parseFileIntoArray(fileName) -> List[int]:
  # reads into an array
  with open(fileName) as f:
    lines = f.readlines()
  
  # sanitize (using list comprehension)
  sanitizedLines = [int(line.strip()) for line in lines];

  return sanitizedLines;

# using a sliding window
def getNumberOfIncreases(inputs: List[int]) -> int:
  nIncreases = 0;

  prevSum = inputs[0] + inputs[1] + inputs[2];
  # loop starting at the third element (and keeping the correct index)
  for idx, input in enumerate(inputs[2:-1], start=2):
    prevInput = inputs[idx-1];
    nextInput = inputs[idx+1];
    currSum = prevInput + input + nextInput;
    if currSum > prevSum:
      nIncreases+=1;
    prevSum = currSum;

  return nIncreases;

def main():
  # inputs = [199, 200, 208, 210, 200, 207, 240, 269, 260, 263];
  inputs = parseFileIntoArray(fileName);
  result = getNumberOfIncreases(inputs);
  print(f'nIncreases: {result}');

main();