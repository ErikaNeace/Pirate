print "Arr, matey"

for i in range(99):
  print str(i) + " bottles of rum"

  with open('treasure.txt') as fh:
  for line in fh:
    print line