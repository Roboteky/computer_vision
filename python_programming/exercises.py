def word_frequency(text):
    
    words = text.lower().split()
    
    freq = {}
    
    for word in words:
        
        if word in freq:
            
            freq[word] = freq.get(word, 0) + 1
            
        return freq
    
text = "Hello world hello Python hello World"

print(word_frequency(text))


####################################################################


Person_One = {'first_name': 'Kingstone',
              
              'last_name': 'kamau',
              
              'age' : '30',
              
              'city' : 'LAS VEGAS'
              
              }

print(Person_One)



fav_number = {'peter': '1',
              
              'kamau': '11',
              
              'john' : '2',
              
              'zuku' : '5'
            
              }

print(fav_number)



glossary = {'jump' : ' hop from one point to another',
            
            'run' : ' push one leg after the other at a higher frequency',
            
            'cook' : ' burn some palatable food to consume'
            }

for term, meaning in glossary.items():
    
    print(f"{term.title()}:\n  {meaning}\n") 