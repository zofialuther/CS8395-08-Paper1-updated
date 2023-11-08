```python
from typing import List, Tuple

acesHigh = [Ace, Ten, Jack, Queen, King]

def isSucc(lst: List[Rank]) -> bool:
  if len(lst) == 0 or len(lst) == 1:
    return True
  else:
    for i in range(len(lst) - 1):
      if lst[i] != max(lst) and lst[i+1] == lst[i] + 1:
        continue
      else:
        return False
    return True

def nameHand(cards: List[Card]) -> str:
  if len(cards) == 0:
    return "Invalid Input"
  
  sortedRank = sorted([card.rank for card in cards])
  rankCounts = [(k, len(list(g))) for k, g in groupby(sortedRank)]
  uniqRanks = len(rankCounts)

  def ofKind(n: int) -> bool:
    return any(count == n for _, count in rankCounts)

  straight = isSucc(sortedRank) or sortedRank == acesHigh
  flush = len(set([card.suit for card in cards])) == 1
  invalidHand = len(set(cards)) != 5

  if invalidHand:
    return "Invalid hand"
  elif straight and flush:
    return "Straight flush"
  elif ofKind(4):
    return "Four of a kind"
  elif ofKind(3) and ofKind(2):
    return "Full house"
  elif flush:
    return "Flush"
  elif straight:
    return "Straight"
  elif ofKind(3):
    return "Three of a kind"
  elif uniqRanks == 3:
    return "Two pair"
  elif uniqRanks == 4:
    return "One pair"
  else:
    return "High card"

def readHand(s: str) -> Tuple[str, List[Card]]:
  result = s.split()
  return result[0], [Card(suit=c[1], rank=r[0]) for c, r in result]

testHands = [
  "2♥ 2♦ 2♣ k♣ q♦",
  "2♥ 5♥ 7♦ 8♣ 9♠",
  "a♥ 2♦ 3♣ 4♣ 5♦",
  "2♥ 3♥ 2♦ 3♣ 3♦",
  "2♥ 7♥ 2♦ 3♣ 3♦",
  "2♥ 7♥ 7♦ 7♣ 7♠",
  "10♥ j♥ q♥ k♥ a♥",
  "4♥ 4♠ k♠ 5♦ 10♠",
  "q♣ 10♣ 7♣ 6♣ 4♣",
  "q♣ 10♣ 7♣ 6♣ 7♣",
  "Bad input"
]

def main() -> None:
  for hand in testHands:
    name = nameHand(hand[1])
    print(f"{hand[0]}: {name}")

if __name__ == "__main__":
  main()
```