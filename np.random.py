'''
import numpy as np

# ১. ০ থেকে ১ এর মধ্যে একটি এলোমেলো দশমিক সংখ্যা (Float) তৈরি করা
random_float = np.random.uniform(0,1)
print("Random Float (0 to 1):", random_float)

# ২. ১০ থেকে ৫০ এর মধ্যে ৫টি এলোমেলো পূর্ণসংখ্যা (Integer) তৈরি করা
random_integers = np.random.randint(10, 50, size=5)
print("5 Random Integers (10 to 50):", random_integers)

# ৩. একটি নির্দিষ্ট লিস্ট থেকে এলোমেলোভাবে ১টি উপাদান বেছে নেওয়া
fruits = ['apple', 'banana', 'cherry', 'orange']
random_choice = np.random.choice(fruits)
print("Random Choice from list:", random_choice)

'''


import numpy as np

fruits=['apple','banana','kola']
choice=np.random.choice(fruits)
print(choice)