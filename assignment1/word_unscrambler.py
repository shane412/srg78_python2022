user_input = input("Please enter a word!\n")
#user_input = "cardiothorasic"

words = open('words.txt', 'r')

wordlist = words.readlines()

wordclean = [word.strip().lower() for word in wordlist]

user_input_sorted = sorted(user_input) # list of characters in user input

matches = []

for word in wordclean:
    word_sorted = sorted(word)
    if all(elem in user_input_sorted  for elem in word_sorted):
        matches.append(word)


matches.sort(key=len)

if len(matches) == 3 or 4 or 5 or 6:
   #  print(matches)

   # matches.sort(key=len) 
    print (matches)

