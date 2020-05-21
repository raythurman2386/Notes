def palindromeIndex(s):
  if s == s[::-1]:
    return -1
  a = list(s)
  b=list(s)
  
  for i in range(len(a)//2):
    if a[i] != a[len(a)-1-i]:
      b=b[:len(a)-1-i]+b[len(a)-i:]
      a.pop(i) 
      if a == a[::-1]:
        return i 
      elif(b==b[::-1]):
        return(len(a)-i)
      else: 
        return(-1)

print(palindromeIndex('aayush'))
print(palindromeIndex('aaab'))
print(palindromeIndex('baa'))
print(palindromeIndex('aaa'))