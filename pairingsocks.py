def sockMerchant(n, ar):
  count = 0
  d = {}

  for i in ar:
    d[i] = d.get(i,0) + 1

  for i in d.keys():
    count+= d[i]//2
  return count

print(sockMerchant(9, [10,20,20, 10,10 ,30,50, 10 , 20]))

