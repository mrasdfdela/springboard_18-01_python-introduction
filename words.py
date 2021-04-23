def print_upper_words(words,must_start_with):
  for word in words:
    for eval_letter in must_start_with:
      if word[0].lower() == eval_letter.lower():
        print(word.upper())

test_list = ["Homer", "Marge", "Bart", "Lisa", "Maggie",]

print_upper_words(test_list, {"h","l"})
print_upper_words(["hello", "hey", "goodbye", "yo", "yes"],
                   must_start_with={"h", "y"})