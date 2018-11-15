

def one_in_another (question,word):
    isit = word in question
    print(isit)


the_question = input('Enter your question:')
the_word = input('Enter your word: ')
one_in_another(the_question,the_word)