
#shiraz yeshayahu
#209086768

#A
def reverse(sentence, reverse_word):
    if type(sentence)==str and type(reverse_word)== str:
        if reverse_word in sentence:
            new_sentence= sentence.replace(reverse_word, reverse_word[::-1], 1)
            return new_sentence
        else:
            return "The word was not found"
    else:
        return "invalid input"
                       

