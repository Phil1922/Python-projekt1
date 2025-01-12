"""
projekt_1.py: první projekt do Engeto Online Python Akademie

author: Filip Eliáš
email:  elias.filip@gmail.com
"""


TEXTS = ['''
Situated about 10 miles west of Kemmerer,
Fossil Butte is a ruggedly impressive
topographic feature that rises sharply
some 1000 feet above Twin Creek Valley
to an elevation of more than 7500 feet
above sea level. The butte is located just
north of US 30N and the Union Pacific Railroad,
which traverse the valley. ''',
'''At the base of Fossil Butte are the bright
red, purple, yellow and gray beds of the Wasatch
Formation. Eroded portions of these horizontal
beds slope gradually upward from the valley floor
and steepen abruptly. Overlying them and extending
to the top of the butte are the much steeper
buff-to-white beds of the Green River Formation,
which are about 300 feet thick.''',
'''The monument contains 8198 acres and protects
a portion of the largest deposit of freshwater fish
fossils in the world. The richest fossil fish deposits
are found in multiple limestone layers, which lie some
100 feet below the top of the butte. The fossils
represent several varieties of perch, as well as
other freshwater genera and herring similar to those
in modern oceans. Other fish such as paddlefish,
garpike and stingray are also present.'''
]

users = {
    "bob":"123",
    "ann":"pass123",
    "mike":"password123",
    "liz":"pass123",
}
min_value = 1
max_value = len(TEXTS)
separator = "-" * 30

username = input("username:")
password = input("password:")

if (
    users.get(username)
    and users[username] == password
):
    print(separator)
    print("Welcome to the app,", username)
    print("We have", max_value, "texts to by analyzed.")
    print(separator)
    number_of_text = input(
        f"Please enter an integer between {min_value} and {max_value} to select text:"
    )
    if number_of_text not in map(str, range(min_value, max_value + 1)):
        print(separator)
        print("An invalid symbol was entered.")
        print(f"Please enter an integer between {min_value} to {max_value}")
        print("Terminating the program")
        print(separator)
        exit()
    else:
        print(separator)
        selected_text = int(number_of_text)
        words = TEXTS[selected_text - 1].split()
        total_number_of_words = len(words)
        
        titlecase_number_of_words = list()
        uppercase_number_of_words = list()
        lowercase_number_of_words = list()
        number_of_numeric_strings = list()
        sum_of_numeric_strings = 0

        for word in words:
            if word.istitle():
                titlecase_number_of_words.append(word)

            elif word.isupper() and word.isalpha():
                uppercase_number_of_words.append(word)

            elif word.islower():
                lowercase_number_of_words.append(word)
        
            elif word.isdigit():
                number_of_numeric_strings.append(word)
                sum_of_numeric_strings += int(word)
                
        print(f"There are {total_number_of_words} words in the selected text.")
        print(f"There are {len(titlecase_number_of_words)} titlecase words.")
        print(f"There are {len(uppercase_number_of_words)} uppercase words.")
        print(f"There are {len(lowercase_number_of_words)} lowercase words.")
        print(f"There are {len(number_of_numeric_strings)} numeric strings.")
        print(f"The sum of all the numbers is {sum_of_numeric_strings}.")
        
        print(separator)

        length_counts = {}
        
        for word in words:
            word_length = len(word.strip(".,!?;:"))
            length_counts[word_length] = length_counts.get(word_length, 0) + 1

        print(f"LEN|{"OCCERENCES":^16}|NR.")
        print(separator)
        
        for word_length in sorted(length_counts):
            count = length_counts[word_length]
            print(f"{word_length:>3}|{'*' * count:<16}|{count:<3}")
            
        print(separator)
else:
    print("Unregistered user or wrong password. Terminating the program.")
    exit()