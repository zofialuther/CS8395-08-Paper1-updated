def isNumeric(inputData):
  formatter = NumberFormat.getInstance()
  pos = ParsePosition(0)
  formatter.parse(inputData, pos)
  return len(inputData) == pos.getIndex()