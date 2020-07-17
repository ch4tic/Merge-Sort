#!/usr/bin/python3 

# merge sorting function 
def sorting(numbers):
  if len(numbers) == 1:
    return numbers # returning the list if there is only one number 
  elif len(numbers) == 2:
    if numbers[0] > numbers[1]: # comparing the first and second number 
      return [numbers[1], numbers[0]] # returning the sorted list 
    else:
      return numbers 

  middle = len(numbers) // 2 # finding the middle 
  sub1 = sorting(numbers[:middle]) # sublist 1 
  sub2 = sorting(numbers[middle:]) # sublist 2 
  sort = [] # list of sorted numbers

  # comparing the two sublists 
  while True:
    # determining the length of sublists 
    if len(sub1) > 0 and len(sub2) > 0:
      if sub1[0] <= sub2[0]: # comparing the first elements of sublists 
        sort.append(sub1[0]) # appending the first element of the sublist 1 
        sub1 = sub1[1:] # slicing the sublist 1 
      else:
        sort.append(sub2[0]) # appending the first element of the sublist 2 
        sub2 = sub2[1:] # slicing the sublist 2 
    # checking the length of sublist 1 
    elif len(sub1) > 0:
      sort += sub1
      sub1 = [] # reseting the sublist 1 
    # checking the length of sublist 2 
    elif len(sub2) > 0:
      sort += sub2
      sub2 = [] # reseting the sublist 2 
    else:
      break # breaking the loop 
  return sort # returning the sorted numbers 

def main(): 
  numbers = ['3', '2', '6', '5', '1'] # numbers to sort 
  print(sorting(numbers)) # calling the function and printing the output 

# calling the main function at the start of the program 
if __name__ == '__main__': 
  main() 