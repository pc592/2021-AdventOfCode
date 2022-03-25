from typing import List;
from dataclasses import dataclass;
from enum import Enum;

fileName = './Day10/input.txt';
testFileName = './Day10/testInput.txt';

@dataclass
class InvalidType(Enum):
  IS_CORRUPTED: str = 'IS_CORRUPTED';
  IS_INCOMPLETE: str = 'IS_INCOMPLETE';

@dataclass
class InvalidInfo:
  error: InvalidType;
  firstIllegalChar: str | None;
  unmatchedChars: str | None;
  line: str;

@dataclass
class Lines:
  corruptedLines: List[InvalidInfo];
  incompleteLines: List[InvalidInfo];
  validLines: List[InvalidInfo];

corruptedScoreTable = {
  ')': 3,
  ']': 57,
  '}': 1197,
  '>': 25137,
}

incompleteScoreTable = {
  '(': 1,
  '[': 2,
  '{': 3,
  '<': 4,
}

getClosingCharFromOpeningChar = {
  '(': ')',
  '[': ']',
  '{': '}',
  '<': '>',
}

def parseFileIntoArray(fileName) -> List[str]:
  # reads into an array
  with open(fileName) as f:
    lines = f.readlines()
  
  sanitizedLines = [line.strip() for line in lines];

  return sanitizedLines;

def isOpeningChar(char: str) -> bool:
  if (char == '(' or char == '[' or char == '{' or char == '<'):
    return True;
  else:
    return False;

# Returns None if valid.
def getInvalidInfo(line: str) -> InvalidInfo | None:
  unmatchedChars = [];

  for char in line:
    if (isOpeningChar(char)):
      unmatchedChars.append(char);
    else:
      if len(unmatchedChars) == 0:
        return InvalidInfo(InvalidType.IS_CORRUPTED, char, None, line);
      else:
        unmatchedChar = unmatchedChars.pop();
        closingChar = getClosingCharFromOpeningChar[unmatchedChar];
        if (char != closingChar):
          return InvalidInfo(InvalidType.IS_CORRUPTED, char, None, line);
  
  if len(unmatchedChars) == 0:
    return None;
  else:
    return InvalidInfo(InvalidType.IS_INCOMPLETE, None, unmatchedChars, line);

def sortLines(inputs: List[str]) -> Lines:
  corruptedLines = [];
  incompleteLines = [];
  validLines = [];
  
  for input in inputs:
    invalidInfo = getInvalidInfo(input);
    if invalidInfo is None:
      validLines.append(invalidInfo);
    elif invalidInfo.error is InvalidType.IS_CORRUPTED:
      corruptedLines.append(invalidInfo);
    elif invalidInfo.error is InvalidType.IS_INCOMPLETE:
      incompleteLines.append(invalidInfo);
    else:
      print('Unhandled error case. Must be one of corrupted or incomplete.')

  return Lines(corruptedLines, incompleteLines, validLines);

def getSyntaxErrorScore(corruptedLines: List[InvalidInfo]) -> int:
  score = 0;
  for line in corruptedLines:
    invalidChar = line.firstIllegalChar;
    score += corruptedScoreTable[invalidChar];

  return score;

def getCompletionScore(incompleteLines: List[InvalidInfo]) -> int:
  scoreList = [];
  for line in incompleteLines:
    score = 0;
    unmatchedChars = line.unmatchedChars;
    for unmatchedChar in reversed(unmatchedChars):
      score = score*5 + incompleteScoreTable[unmatchedChar];
    scoreList.append(score);

  sortedScoreList = sorted(scoreList);
  median = int((len(sortedScoreList) - 1) / 2);

  return sortedScoreList[median];

def main():
  # inputs = parseFileIntoArray(testFileName);
  inputs = parseFileIntoArray(fileName);
  lines = sortLines(inputs);
  syntaxErrorScore = getSyntaxErrorScore(lines.corruptedLines);
  completionScore = getCompletionScore(lines.incompleteLines);
  print(f'{completionScore=}');

main();