import random
import yaml
import ast
from tqdm import tqdm

def read_file(filename):
    with open(filename, 'r') as file:
        return [line.strip() for line in file.readlines()]

def replace_tag(sentence, tag, options):
    if f"[{tag}]" in sentence:
        return sentence.replace(f"[{tag}]", f"[{random.choice(options)}]({tag})")
    return sentence

# Read all files
sentences_raw = read_file('sentences.txt')
sentences = ast.literal_eval(''.join(sentences_raw))  # Safely evaluate the string as a Python expression

actions = read_file('actions.txt')[1:]  # Skip the first line which is a variable declaration
places = read_file('places.txt')[1:]    # Skip the first line which is a variable declaration
things = read_file('things.txt')[1:]    # Skip the first line which is a variable declaration
times = read_file('times.txt')[1:] 

print(things)
"""
new_sentences = []
for sentence in tqdm(sentences):
    for action in actions:
        for thing in things:
            for place in places:
                for time in times:
                    new_sentence = sentence
                    new_sentence = replace_tag(new_sentence, "action", action)
                    new_sentence = replace_tag(new_sentence, "thing", thing)
                    if "[place]" in new_sentence:
                        new_sentence = replace_tag(new_sentence, "place", place)
                    if "[time]" in new_sentence:
                        new_sentence = replace_tag(new_sentence, "time", time)
                    new_sentences.append(new_sentence)

# Write to YAML file
with open('synt_sentences.yaml', 'w') as file:
    yaml.dump(new_sentences, file)

print(f"Generated {len(new_sentences)} sentences and saved to synt_sentences.yaml")
"""