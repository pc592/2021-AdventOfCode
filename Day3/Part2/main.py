from typing import List;
from dataclasses import dataclass, field;

fileName = './Day3/input.txt';
nBits = 0;

def parseFileIntoArray(fileName) -> List[str]:
  # reads into an array
  with open(fileName) as f:
    lines = f.readlines()
  
  # sanitize (using list comprehension)
  sanitizedLines = [line.strip() for line in lines];

  return sanitizedLines;

@dataclass
class Ratings:
  oxygenGenerator: str = '';
  CO2Scrubber: str = '';

@dataclass
class BitsArrays:
  zeroBitArray: List[str] = field(default_factory=list);
  oneBitArray: List[str] = field(default_factory=list);

def getBitsArrays(inputs: List[str], idx: int) -> BitsArrays:
  zeroBitArray = [];
  oneBitArray = [];

  for input in inputs:
    if input[idx] == '0':
      zeroBitArray.append(input);
    elif input[idx] == '1':
      oneBitArray.append(input);
    else:
      print('How did you get here, something is wrong.')
  
  bitsArrays = BitsArrays(zeroBitArray, oneBitArray);
  return bitsArrays;

def getOxygenGeneratorArray(inputs: List[str], idx: int) -> List[str]:
  global nBits;
  if len(inputs) == 1 or idx >= nBits:
    return inputs;
  else:
    bitsArray = getBitsArrays(inputs, idx);

    zeroBitArray = bitsArray.zeroBitArray;
    oneBitArray = bitsArray.oneBitArray;
    zeroBits = len(zeroBitArray);
    oneBits = len(oneBitArray);

    if oneBits >= zeroBits:
      return getOxygenGeneratorArray(oneBitArray, idx+1);
    elif zeroBits > oneBits:
      return getOxygenGeneratorArray(zeroBitArray, idx+1);
    else:
      print('How did you get here, something is wrong.')
    
    return [];

def getCO2ScrubberArray(inputs: List[str], idx: int) -> List[str]:
  global nBits;
  if len(inputs) == 1 or idx >= nBits:
    return inputs;
  else:
    bitsArray = getBitsArrays(inputs, idx);

    zeroBitArray = bitsArray.zeroBitArray;
    oneBitArray = bitsArray.oneBitArray;
    zeroBits = len(zeroBitArray);
    oneBits = len(oneBitArray);

    if oneBits >= zeroBits:
      return getCO2ScrubberArray(zeroBitArray, idx+1);
    elif zeroBits > oneBits:
      return getCO2ScrubberArray(oneBitArray, idx+1);
    else:
      print('How did you get here, something is wrong.')
    
    return [];

def getRatings(inputs: List[str]) -> Ratings:
  global nBits;
  nBits = len(inputs[0]);

  oxygenGeneratorArray = getOxygenGeneratorArray(inputs, 0);
  CO2ScrubberArray = getCO2ScrubberArray(inputs, 0);

  ratings = Ratings(oxygenGeneratorArray[0], CO2ScrubberArray[0]);
  return ratings;

def convertBinaryToDecimal(binary: str) -> int:
  reverseBinary = binary[::-1];
  decimal = 0;

  for idx in range(0,len(binary)):
    if reverseBinary[idx] == '1':
      decimal += 2**idx;

  return decimal;

def main():
  # inputs = ['00100', '11110', '10110', '10111', '10101', '01111', '00111', '11100', '10000', '11001', '00010', '01010'];
  inputs = parseFileIntoArray(fileName);
  ratings = getRatings(inputs);
  decOxygenGenerator = convertBinaryToDecimal(ratings.oxygenGenerator);
  decCO2Scrubber = convertBinaryToDecimal(ratings.CO2Scrubber);
  lifeSupportRating = decOxygenGenerator * decCO2Scrubber;
  print(f'{ratings=}');
  print(f'{lifeSupportRating=}');

main();