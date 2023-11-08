```python
class WordWrap:
  def __init__(self):
    self.defaultLineWidth = 80
    self.defaultSpaceWidth = 1

  def minNumLinesWrap(self, text, lineWidth=None):
    if lineWidth is None:
      lineWidth = self.defaultLineWidth
      
    spaceLeft = lineWidth
    spaceWidth = self.defaultSpaceWidth
    words = text.split()
    result = ""
    
    for word in words:
      if len(word) + spaceWidth > spaceLeft:
        result += "\n" + word + " "
        spaceLeft = lineWidth - len(word)
      else:
        result += word + " "
        spaceLeft -= (len(word) + spaceWidth)
        
    print(result)

def main():
  now = WordWrap()
  wodehouse = "Old Mr MacFarland (_said Henry_) started the place fifteen years ago..."
  
  print("DEFAULT:")
  now.minNumLinesWrap(wodehouse)
  print("\n\nLINEWIDTH=120")
  now.minNumLinesWrap(wodehouse, 120)

if __name__ == "__main__":
  main()
```