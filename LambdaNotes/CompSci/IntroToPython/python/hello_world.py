hello = "Hello World!"

print(f"{hello} {hello}")
print("{} {}".format(hello, hello), 'test')

arr = [1, 2, 3, 4]

dict = {
  "name": "Ray",
  "age": 31,
  "sex": "male"
}

dict['hobby'] = ['computers', 'games']

spouse = dict.get('spouse', 'No spouse assigned')
print(spouse)

for key, value in dict.items():
  if key == 'hobby':
    for i in dict['hobby']:
      print(f"{key}: {i}")
  else:
    print(f"{key}: {value}")

# for i in dict:
#   if i != 'hobby':
#     print(f"{i}: {dict[i]}")
#   else:
#     for j in dict[i]:
#       print(f"{i}: {j}")



nested_arr = [[1, 2, 3], [4, 5], [6, 7]]

nested_arr.append([8, 9, 0])
print(nested_arr[1:3])
print(nested_arr[-1])
nested_arr.insert(0, ['testing', 'insert'])

nested_arr.remove([4, 5])

arr.sort(reverse=True)
print(arr)

print(len(nested_arr))

for i in nested_arr:
  for j in i:
    print(j)

print("*******")

nums = list(range(2, 10, 2))

print(sum(nums), 'sum\n')

for num in nums:
  if num in range(2, 7):
    print(num)

squares = [value**2 for value in range(1, 11)]

print(squares)

copied_arr = nested_arr[:]

for arr in copied_arr[:3]:
  print(arr)

dimensions = (200, 50)

for item in dimensions:
  print(item)

print([4, 5] in copied_arr)

prompt = "If you tell us your age, we can let you know how much a ticket is."
prompt += "\nHow old are you? "

age = int(input(prompt))

if age < 4:
  price = 0
elif age < 18:
  price = 25
else:
  price = 40

print(f"Your admission cost is ${price}.")

available_toppings = ['mushrooms', 'olives', 'green peppers', 'pepperoni']

requested_toppings = ['mushrooms', 'pepperoni', 'banana peppers']

for requested_topping in requested_toppings:
  if requested_topping in available_toppings:
    print(f"Adding {requested_topping}")
  else:
    print(f"Sorry, we do not have {requested_topping}")

print("\nYour Pizza is complete!".title())

next_prompt = "\nTell me something, and I will repeat it back to you:"
next_prompt += "\nEnter 'quit' to end the program. "

message = ""
active = True

while active:
  message = input(next_prompt)

  if message == 'quit':
    active = False
  else:
    print(message)