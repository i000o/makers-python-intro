# Video alternative: https://vimeo.com/954334103/0aed500d39#t=1295

from lib.helpers import check_that_these_are_equal

# Now it's your turn.

# Note that the exercise will be (a little) less challenging than the example.

# Write a function that takes a list of words and returns a report of all the
# words that are longer than 10 characters but don't contain a hyphen. If those
# words are longer than 15 characters, then they should be shortened to 15
# characters and have an ellipsis (...) added to the end.

# For example, if the input is:
# [
#   'hello',
#   'nonbiological',
#   'Kay',
#   'this-is-a-long-word',
#   'antidisestablishmentarianism'
# ]
# then the output should be:
# "These words are quite long: nonbiological, antidisestablis..."

# @TASK: Complete this exercise.

print("")
print("Function: report_long_words")

def report_long_words(words): # make a function called report_long_words which takes the parameter words 
  long_words = [] # make a list called long_words 
  for word in words: # iterate over each word in the words list 
    if len(word) > 10 and "-" not in word: # and if the length of the word is greater than 10 (characters) AND there is no hyphen in the word
      if len(word) > 15: # not only this, but if the length of the word is also greater than 15
        long_words.append(word[:15] + '...') # go into the long_words list, and add the word, but cut it at the 15th character and add an ellipse at the end 
      else: #otherwise, in the cases where the words are not so long that they need to be manipulated
        long_words.append(word) # just add them to the long_words list
  return "These words are quite long: " + ", " .join(long_words) # return me These words are quite long: and include a new string of all the words which are longer than 10 characters, with commas inbetween, and if they're longer than 15, cut them and add ellipse.

check_that_these_are_equal(
  report_long_words([
    'hello',
    'nonbiological',
    'Kay',
    'this-is-a-long-word',
    'antidisestablishmentarianism'
  ]),
  "These words are quite long: nonbiological, antidisestablis..."
)

check_that_these_are_equal(
  report_long_words([
    'cat',
    'dog',
    'rhinosaurus',
    'rhinosaurus-rex',
    'frog'
  ]),
  "These words are quite long: rhinosaurus"
)

check_that_these_are_equal(
  report_long_words([
    'cat'
  ]),
  "These words are quite long: "
)

# Once you're done, move on to 041_challenge_2_example.py
