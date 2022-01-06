from typing import List;
from dataclasses import dataclass, field;

fileName = './Day8/input.txt';
testFileName = './Day8/testInput.txt';

segmentMap = {
  'abcefg': 0,
  'cf': 1,
  'acdeg': 2,
  'acdfg': 3,
  'bcdf': 4,
  'abdfg': 5,
  'abdefg': 6,
  'acf': 7,
  'abcdefg': 8,
  'abcdfg': 9,
};

nSegmentToNumberMap = {};

def generateNSegmentToNumberMap() -> None:
  global segmentMap;
  global nSegmentToNumberMap;

  for (key, value) in (segmentMap.items()):
    if len(key) not in nSegmentToNumberMap:
      nSegmentToNumberMap[len(key)] = [value];
    else:
      nSegmentToNumberMap[len(key)].append(value);

@dataclass
class Entry:
  input: List[str] = field(default_factory=list);
  output: List[str] = field(default_factory=list);

def parseFileIntoArray(fileName) -> List[int]:
  # reads into an array
  with open(fileName) as f:
    lines = f.readlines()
  
  return lines;

def buildEntries(inputs: List[str]) -> List[Entry]:
  signals = [];
  for input in inputs:
    entry = input.strip().split(' | ');
    signal = Entry(entry[0].split(' '), entry[1].split(' '));
    signals.append(signal);

  return signals;

def countSimpleOutputs(entries: List[Entry]) -> int:
  global nSegmentToNumberMap;
  count = 0;

  for entry in entries:
    for output in entry.output:
      nDigits = len(output);
      if (1 in nSegmentToNumberMap[nDigits] or
          4 in nSegmentToNumberMap[nDigits] or
          7 in nSegmentToNumberMap[nDigits] or
          8 in nSegmentToNumberMap[nDigits]):
        count = count + 1;

  return count;

def main():
  generateNSegmentToNumberMap();
  # inputs = parseFileIntoArray(testFileName);
  inputs = parseFileIntoArray(fileName);
  entries = buildEntries(inputs);
  nSimpleOutputs = countSimpleOutputs(entries);
  print(f'{nSimpleOutputs=}');

main();