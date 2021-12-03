from typing import List;
from dataclasses import dataclass;

fileName = './Day2/input.txt';

def parseFileIntoArray(fileName) -> List[str]:
  # reads into an array
  with open(fileName) as f:
    lines = f.readlines()
  
  # sanitize (using list comprehension)
  sanitizedLines = [line.strip() for line in lines];

  return sanitizedLines;

@dataclass
class Position:
  x: int = 0;
  y: int = 0;

@dataclass
class Instruction:
  direction: str;
  unit: str;

def parseInput(input: str) -> Instruction:
  splitInput = input.split();
  return Instruction(splitInput[0], splitInput[1]);

def getFinalPosition(inputs: List[str]) -> Position:
  position = Position();

  for input in inputs:
    instruction = parseInput(input);
    match instruction.direction:
      case 'forward':
        position.x += int(instruction.unit);
      case 'down':
        position.y += int(instruction.unit);
      case 'up':
        position.y -= int(instruction.unit);

  return position;

def main():
  # inputs = ['forward 5', 'down 5', 'forward 8', 'up 3', 'down 8', 'forward 2'];
  inputs = parseFileIntoArray(fileName);
  finalPostion = getFinalPosition(inputs);
  result = finalPostion.x * finalPostion.y;
  print(f'{finalPostion=}');
  print(f'multiplied: {result}');

main();