from typing import List;
from dataclasses import dataclass, field;

fileName = './Day8/input.txt';
testFileName = './Day8/testInput.txt';

segmentToDisplayMap = {
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
}

displayToSegmentMap = {
  0: 'abcefg',
  1: 'cf',
  2: 'acdeg',
  3: 'acdfg',
  4: 'bcdf',
  5: 'abdfg',
  6: 'abdefg',
  7: 'acf',
  8: 'abcdefg',
  9: 'abcdfg',
};

nSegmentMap = {
  6: {
    'display': [0, 6, 9],
    'segment': ['abcefg', 'abdefg', 'abcdfg'],
  },
  2: {
    'display': [1],
    'segment': ['cf'],
  },
  5: {
    'display': [2, 3, 5],
    'segment': ['acdeg', 'acdfg', 'abdfg'],
  },
  4: {
    'display': [4],
    'segment': ['bcdf'],
  },
  3: {
    'display': [7],
    'segment': ['acf'],
  },
  7: {
    'display': [8],
    'segment': ['abcdefg'],
  },
};

def generateMaps() -> None:
  global segmentToDisplayMap;
  global displayToSegmentMap;
  global nSegmentMap;

  for (segment, display) in (segmentToDisplayMap.items()):
    displayToSegmentMap[display] = segment;

    if len(segment) not in nSegmentMap:
      nSegmentMap[len(segment)] = {
      'display': [display],
      'segment': [segment],
    };
    else:
      nSegmentMap[len(segment)]['display'].append(display);
      nSegmentMap[len(segment)]['segment'].append(segment);

  print(displayToSegmentMap);
  print(nSegmentMap);

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
  global displayToSegmentMap;
  global nSegmentMap;
  
  uniqueDisplays = [1, 4, 7, 8];

  count = 0;

  for entry in entries:
    for output in entry.output:
      nDigits = len(output);
      for uniqueDisplay in uniqueDisplays:
        if (len(displayToSegmentMap[uniqueDisplay]) == nDigits):
          count = count + 1;

  return count;

def main():
  # generateMaps();
  # inputs = ['acedgfb cdfbe gcdfa fbcad dab cefabd cdfgeb eafb cagedb ab | cdfeb fcadb cdfeb cdbaf'];
  # inputs = parseFileIntoArray(testFileName);
  inputs = parseFileIntoArray(fileName);
  entries = buildEntries(inputs);
  nSimpleOutputs = countSimpleOutputs(entries);
  print(f'{nSimpleOutputs=}');

main();