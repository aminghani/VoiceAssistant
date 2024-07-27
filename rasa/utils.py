import re

def merge_lines(yaml_file):
    with open(yaml_file, 'r') as file:
        lines = file.readlines()

    merged_lines = []
    temp_line = ""
    for line in lines:
        line = line.strip()
        if line.startswith("-"):
            if temp_line:
                merged_lines.append(temp_line)
            temp_line = line
        else:
            temp_line += " " + line

    if temp_line:
        merged_lines.append(temp_line)

    with open("merged_" + yaml_file, 'w') as file:
        for line in merged_lines:
            file.write(line + "\n")

# Specify your YAML file name here
yaml_file = 'synt_sentences.yaml'
merge_lines(yaml_file)