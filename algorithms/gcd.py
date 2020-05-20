def greatest_common_denom(a, b):
  while b != 0:
    temp = a
    a = b
    b = temp % b

  print(a)
  return a

greatest_common_denom(20, 4)
greatest_common_denom(50, 15)
greatest_common_denom(200, 60)
greatest_common_denom(60, 96)