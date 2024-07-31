import random
import yaml
import ast
from tqdm import tqdm
import random

def drop_fraction_randomly(lst, drop_fraction):
    l = []
    for item in lst:
        random_float = random.random()
        if random_float < 1 - drop_fraction:
            l.append(item)
    return l

def read_file(filename):
    with open(filename, 'r') as file:
        return [line.strip() for line in file.readlines()]

def read(file_name):
        # Open the file in read mode
    with open(file_name, 'r') as file:
        # Read the entire contents of the file as a single string
        contents = file.read()

    # Split the string by comma and create a list
    room_list = [room.strip(' ') for room in contents.split(',')]
    return room_list

def lower_(l):
    return [a.lower() for a in l]

# Read all files
sentences_raw = read_file('sentences_2.txt')
sentences = ast.literal_eval(''.join(sentences_raw))  # Safely evaluate the string as a Python expression

actions = lower_(read('actions.txt')) # Skip the first line which is a variable declaration
places = lower_(read('places.txt'))    # Skip the first line which is a variable declaration
things = lower_(read('things.txt'))    # Skip the first line which is a variable declaration
times = lower_(read('times.txt'))
amounts = lower_(read('amounts.txt'))
numbers = lower_(read('numbers.txt'))


gen_sentences = []
for sen in tqdm(sentences):
    for act in actions:
        for pl in places:
            for th in things:
                for ti in times:
                    for am in amounts:
                        for nu in numbers:
                            s = sen
                            if '<time>' in s:
                                s = s.replace('<time>', ti)
                            if '<place>' in s:
                                s = s.replace('<place>', pl)
                            if '<amount>' in s:
                                s = s.replace('<amount>', am)
                            if '<number>' in s:
                                s = s.replace('<number>', nu)

                            s = s.replace('<action>', act)
                            s = s.replace('<thing>', th)
                            gen_sentences.append(s)

gen_sentences = list(set(gen_sentences))
print(len(gen_sentences))
final_list = drop_fraction_randomly(gen_sentences, drop_fraction=0.95)
print(len(final_list))
with open('synt_sentences_2.yaml', 'w') as file:
    yaml.dump(final_list, file)
