

def printBlankLines(numberOfLines):
  for number in range(numberOfLines):
    print('')


def printHeader():
  print("**********************************************")

def printMiddle():
  print("*                                            *")

def printLineheading(heading,numberOfLines):
  printHeader()
  for number in range(numberOfLines):
    printMiddle()
  print(heading)
  for number in range(numberOfLines):
    printMiddle()
  printHeader()
