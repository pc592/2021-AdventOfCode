from typing import List;

fileName = './Day6/input.txt';

def parseFileIntoArray(fileName) -> List[int]:
  # reads into an array
  with open(fileName) as f:
    lines = f.readlines()
  
  # sanitize (using list comprehension)
  # there is only one relevant line, containing an array
  sanitizedLines = [int(num.strip()) for num in lines[0].split(',')];

  return sanitizedLines;

def getLanternfish(currSchool: List[int], nDays: int) -> int:
  if nDays == 0:
    return currSchool;
  else:
    newSchool = [];
    for fish in currSchool:
      if fish == 0:
        newSchool.append(6);
        newSchool.append(8);
      else:
        newSchool.append(fish-1);
  
    # print(18-nDays+1, newSchool);
    return getLanternfish(newSchool, nDays-1);

def main():
  # inputs = [3, 4, 3, 1, 2];
  inputs = parseFileIntoArray(fileName);
  nDays = 80;
  lanternfish = getLanternfish(inputs, nDays);
  print(f'nLanternfish: {len(lanternfish)}');

main();