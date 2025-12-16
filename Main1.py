numbers=[1,6,56,38,74.9,64,77]
strings=["tables","books","apples","house"]
mix=["bike20",89,"polar",True,False]
print(f"The first number in the number list is: {numbers[0]}")
print(f"The second number in the number list is: {numbers[1]}")
print(f"The third number in the number list is: {numbers[2]}")
print(f"The last number in the number list is: {numbers[-1]}")
mix[0]=20
mix[4]=15
print(f"The updated list for mix is : {mix}")
added=numbers+mix
print (f"The added list is: {added}")
print(f"The length if mix list is: {len(mix)}")
print(f"The length if numbers list is: {len(numbers)}")