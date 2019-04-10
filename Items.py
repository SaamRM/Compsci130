def get_valid_input():
    """
    Takes a number and only returns the number if its 1-10 inclusive
    """
    number = -1 #invalid
    while not 1 <= number <= 10:
        try:
            user_input = input("Enter a number between 1 and 10 inclusive: ")
            number = float(user_input)
        except:
            pass
    
    return number
    
 def letters(input):
    """
    Filters the non alpha characters out of a given string and keeps spaces
    """
    
    valid_letters = []
    
    for character in input:
        if character.isalpha() or character == " ":
            valid_letters.append(character)
            
    return ''.join(valid_letters)

print("Valid input: {}".format(get_valid_input()))

def get_largest_value(data):
    '''
    Finds the largest number in the dictionary and returns it's value
    '''
    greatest_val = 0

    for key, val in data.items():
        if val > greatest_val:  
            greatest_val = val
            
    return greatest_val
    
def ordered_keys(data, ordering, ascending):
    '''
    Takes a dictionary and sorts the keys based off ordering and ascending values
    
    >>> ordered_keys({'c' : 5, 'a' : 2, 'b' : 6}, 'key', True)
    ['a', 'b', 'c']
    >>> ordered_keys({'c' : 5, 'a' : 2, 'b' : 6}, 'key', False)
    ['c', 'b', 'a']
    
    '''
    
    sorted_list = []
    
    for key, val in data.items():
        if ordering == 'key':
            sorted_list.append((key,val))
        elif ordering == 'value':
            sorted_list.append((key,val))       
            
    if ordering == 'value':
        sorted_list.sort(key =lambda x : x[1])
        
    elif ordering == 'key':
        sorted_list.sort(key =lambda x : x[0])
        
    if ascending == False:
        sorted_list = list(reversed(sorted_list))
    
        
    return sorted_list
    
 (import string)

 def generate_frequency_table(filename):
    """
    Generates dictionary that has the frequency of each letter from a file
    """
    file = open(filename, 'r')
    original_text = file.read()
    letters = set(string.ascii_lowercase)
    text = list(original_text.lower())
    dictionary = {}
       
    for item in text:
        if item in letters:
            dictionary[item] = 0
    
    for item in text:
        if item in letters:
            dictionary[item] += 1
            
    return dictionary

def word_frequencies(sentence):
    """
    Letter frequncys from string and prints freq then letter
    """
    my_dict = {}
    my_dict2 = {}
    sentence = sentence.lower()
    word_list = sentence.split()
    
    for word in word_list:
        if word not in my_dict:
            my_dict[word] = 1
        else:
            my_dict[word] += 1
            
    for key in my_dict:
        value = my_dict[key]
        if value not in my_dict2:
            my_dict2[value] = [key]
        else:
            my_dict2[value].append(key)
            
    key_list = []
    for key in my_dict2: 
        key_list.append(key)
    
    for key in sorted(key_list, reverse = True):
        line = str(key) + ' ' + str(sorted(my_dict2[key]))
        print(line)
        
word_frequencies('a a a a a b b b b c c c d d e')

Class CLASSNAME():
    def __init__(self):
        pass
    def methodname(self):
        pass
    def __str__(self):
        pass
