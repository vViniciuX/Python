x = [1,5,10,8]

hasher = {}

def Sum(target, x):
  for index, i in enumerate(x):
    if hasher.get(i) is not None:
      return [hasher.get(i), index]
    hasher[target-i] = index
    
print(Sum(9, x))