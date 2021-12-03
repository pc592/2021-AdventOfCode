from typing import List;
from dataclasses import dataclass;

fileName = './Day3/input.txt';

def parseFileIntoArray(fileName) -> List[str]:
  # reads into an array
  with open(fileName) as f:
    lines = f.readlines()
  
  # sanitize (using list comprehension)
  sanitizedLines = [line.strip() for line in lines];

  return sanitizedLines;

@dataclass
class Rates:
  gamma: str = '';
  epsilon: str = '';

def getRates(inputs: List[str]) -> Rates:
  rates = Rates();
  nBits = len(inputs[0]);

  for idx in range(0,nBits):
    zeroBits = 0;
    oneBits = 0;
    for input in inputs:
      if input[idx] == '0':
        zeroBits += 1;
      elif input[idx] == '1':
        oneBits += 1;
      else:
        print('How did you get here, something is wrong.')
    
    if oneBits > zeroBits:
      rates.gamma = rates.gamma + '1';
      rates.epsilon = rates.epsilon + '0';
    elif zeroBits > oneBits:
      rates.gamma = rates.gamma + '0';
      rates.epsilon = rates.epsilon + '1';
    else:
      print('Tie-breaker rules were not given.')

  return rates;

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
  rates = getRates(inputs);
  decGamma = convertBinaryToDecimal(rates.gamma);
  decEpislon = convertBinaryToDecimal(rates.epsilon);
  powerConsumption = decGamma * decEpislon;
  print(f'{rates=}');
  print(f'{powerConsumption=}');

main();