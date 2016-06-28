def is_anagram(test_word=None, words_list=None):
    """ Small function that takes a string and a list
    as an input and returns a list of all the anagrams
    of the word present in the list.
    :param test_word  -> input string word
    :param words_list -> input list of strings
    :return list of anagrams of test_word in word_list
    """
    # In case of None value arguments Return None
    if not all([test_word, words_list]):
        return None
    # First let's eliminate case issues and turn this string
    # into a sorted list of characters.
    word_l = sorted(test_word.lower())
    # Now let's iterate over words_list, remove case issues
    # and generate a new list made from each elements from
    # words_list that is an anagram of word_l
    return [word for word in words_list if word_l == sorted(word.lower())]

if __name__ == '__main__':
    print "Rest : [tesr,sseer,setr,toss] -> {}".format(is_anagram("Rest", ["tesr", "sseer", "setr", "toss"]))
    print "Rest : (tesr,sseer,setr,toss) -> {}".format(is_anagram("Rest", ("tesr", "sseer", "setr", "toss")))
    print "Rose : [tesr,sseer,setr,toss] -> {}".format(is_anagram("Rose", ["tesr", "sseer", "setr", "toss"]))
    print "Rambo: []                     -> {}".format(is_anagram("Rambo"))
    print " " " : []                     ----> {}".format(is_anagram())
