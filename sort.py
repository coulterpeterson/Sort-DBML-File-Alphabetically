# Requires Python 3.7 or higher
import re

dbmlFileNameInput = "ProdData.dbml"
dbmlFileNameInputOutput = "ProdDataSorted.dbml"

regexTableTitle = r"Table \"(.*)\" {"
allTables = {}
allRefs = {}
currentItem = []

# DEBUG: for just testing with the first 20 lines
#with open("DSProdData.dbml", "r") as file:
#    head = [next(file) for x in range(20)]

file = open(dbmlFileName, "r")

# This will print every line one by one in the file
for line in file:
    # DEBUG printing each line to console
    #print ("* " + line)
  
    currentItem.append(line)
    if len(str(line).strip()) < 1:
        # DEBUG announcing when the end of a stanza has been found
        # print ("Found empty line!")

        # Item should now be a complete Table or Ref object, so we can parse it
        itemName = ""
        matches = re.findall(regexTableTitle, currentItem[0])
        
        # TODO: Expand this for more cases than Tables and Refs
        try:
            itemName = matches[0]
            allTables[itemName] = currentItem
        except:
            # This is a ref line
            itemName = currentItem[0]
            allRefs[itemName] = currentItem

        currentItem = []
allTablesSorted = dict(sorted(allTables.items()))
allRefsSorted = dict(sorted(allRefs.items()))

#DEBUG print sorted dictionaries
#print (allTablesSorted)
#print (allRefsSorted)

# Time to write the new file
newFile = open(dbmlFileNameInputOutput,'w')
for key, value in allTablesSorted.items():
    output = ''.join(str(x) for x in value)
    newFile.write('%s\n' % (output))
for key, value in allRefsSorted.items():
    output = ''.join(str(x) for x in value)
    newFile.write('%s\n' % (output))

