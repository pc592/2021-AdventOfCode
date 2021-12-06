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

def getLanternfishByAge(school: List[int]):
  memo = {};

  # each fish denotes the age of the fish
  for fish in school:
    if fish in memo:
      memo[fish] += 1;
    else:
      memo[fish] = 1;

  return memo;

def getInitialTotal(lanternFishByAge: List[int], availableAges = List[int]):
  totalFish = 0;

  for age in availableAges:
    totalFish += lanternFishByAge[age];
  
  return totalFish;

def getNumberOfLanternfish(inputs: List[int], nDays: int) -> int:
  lanternfishByAge = getLanternfishByAge(inputs);
  availableAges = [k for k in lanternfishByAge.keys()];
  totalFish = getInitialTotal(lanternfishByAge, availableAges);

  for day in range(nDays):
    tempLanternfishByAge = {
      6: 0,
      8: 0,
    };

    for age in availableAges:
      if age in lanternfishByAge:
        nLanternFish = lanternfishByAge[age];
        if age == 0:
          tempLanternfishByAge[6] += nLanternFish;
          tempLanternfishByAge[8] += nLanternFish;
          totalFish += nLanternFish;
        else:
          if lanternfishByAge[age] != 0:
            tempLanternfishByAge[age-1] = nLanternFish;

    lanternfishByAge = tempLanternfishByAge;
    availableAges = [k for k in lanternfishByAge.keys()];
    # print(day+1, dict(sorted(lanternfishByAge.items())));
  
  return totalFish;

def main():
  # inputs = [3, 4, 3, 1, 2];
  inputs = parseFileIntoArray(fileName);
  nDays = 256;
  nLanternfish = getNumberOfLanternfish(inputs, nDays);
  print(f'{nLanternfish=}');

main();