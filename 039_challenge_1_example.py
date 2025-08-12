# Video alternative: https://vimeo.com/954334103/0aed500d39#t=0

# Congratulations! You've covered all of the key syntax, concepts, and ideas
# necessary to succeed in your assessment. You can take it now if you like,
# though you might be a little stronger if you do these extra challenges.

# Each challenge focuses on a new technique or approach. It starts with an
# example, and then leads into an exercise.

# We'll start with combining filtering, mapping, and summarising into one
# super-brilliant pipeline.

# I'll demonstrate for you a function that:
#
# * Gets rid of junk data
# * Converts negative integers to positive numbers
# * Creates a graph of how frequently each number shows up
#
# If you've not used the videos so far, you might want to do so for this one. It
# will show you how I build up the program piece by piece.

example_numbers = [1, 2, 3, -2, -2, 2, None, -3, 4, 4, None, 3, 3, 2, 2, 1]

# Desired output:
# 1: xx
# 2: xxxxxx
# 3: xxxx
# 4: xx

# First I'll show you the function that will combine all the other functions
# together to create the graph. This will give you an idea of the flow of the
# program.
def generate_frequency_graph(numbers): # write a function called generate_frequency_graph and it'll take the parameter numbers 
  integers = get_only_integers(numbers) # make a variable called integers which will store a function called get_only_integers which takes the parameter numbers 
  positive_integers = convert_negatives_to_positives(integers) # make a a variable called number_frequency which will store a function called convert_negatives_to_positives which takes the paramter positive_integers
  number_frequency = calc_frequency_of_numbers(positive_integers) # make a variable called number_frequency which will store a function called calc_frequency_of_numbers which takes the parameter number_frequency
  graph = format_graph(number_frequency) # make a variable called graph which will store a function called format_graph which takes the parameter number_frequency
  return graph # return the graph to me 

# Here we'll use filtering to get rid of the None values
def get_only_integers(numbers): # write a function called get_only_integers which takes the parameter numbers 
  integers = [] # create a list called integers for storing 
  for number in numbers: # iterate over each number in numbers
    if number != None: # if the number is not None
      integers.append(number) # go to the integers list and add the number to it 
  return integers # return the list of integers to me 

# Here we'll use mapping to convert negative numbers to positive numbers
def convert_negatives_to_positives(numbers): # make a function called convert_negatives_to_positives which takes the parameter numbers 
  positive_integers = [] # create a list for storing 
  for number in numbers: # iterate over each number in nunmbers 
    if number < 0: # and if the number is less than 0 
      # Note that a negative number multiplied by -1
      # will be its positive equivalent
      positive_integers.append(number * -1) # go into the positive_integers list and add the number (which was less than 0) and multiply it by -1 to give us its positive equivalent 
    else: # otherwise, i.e. if it's already positive/greater than 0 
      positive_integers.append(number) # go into the positive_integers list and add the number as it is 
  return positive_integers # return to me the list of positive_integers

# Here we'll use dictionary summarising to create a graph of how frequently each
# number shows up
def calc_frequency_of_numbers(numbers): # write a function called calc_frequency_of_numbers which takes the parameter numbers 
  number_frequency = {} # create a dictionary called number_frequency to store key/value pairs of the numbers and how frequently they appear 
  for number in numbers: # iterate over each number 
    if number not in number_frequency: # if the number has not already appeared in the number_frequency dictionary
      number_frequency[number] = 1 # go into the dictionary, go into the key for number and assign that key the value of 1. This means that if we haven't seen the number before, we mark its first instance of appearance 
    else: # otherwise, i.e. if we have come across it before in the iteration
      number_frequency[number] += 1 # go into the dictionary, go into the key number and add another 1 to the existing value. E.g. if the value is 5, make it 6. 
  return number_frequency # return me the dictionary number_frequency 

# Here we'll use summarising and mapping in the same loop to format the graph.
def format_graph(number_frequency): # write a function called format_graph which takes the parameter of our dictionary number_frequency
  graph = "" # make a variable called graph for storing and initially, have it be empty 
  for number in number_frequency: # iterate over the the key number in the number_frequency dictionary 
    # Note the cool use of 'string multiplication' here!
    # 'x' * 3 will give you 'xxx'
    graph += f"{number}: {'x' * number_frequency[number]}\n" # and go into the variable graph, and add to it, the number: and the string 'x', but print 'x' the number of times the number appears in the number_frequency dictionary (i.e. the value) and make a new line
  return graph # return the graph to me when the loop is complete 

# Now let's use it!
print(generate_frequency_graph(example_numbers))

# @TASK Run this file to see the result.

# Once you're done, move on to 040_challenge_1_exercise.py
