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

import os
import math

def partition_yaml(input_file, num_partitions):
    # Read the input file
    with open(input_file, 'r') as f:
        lines = f.readlines()

    total_lines = len(lines)
    lines_per_partition = math.ceil(total_lines / num_partitions)

    # Create output directory
    output_dir = './nlu2/partitioned_yaml'
    os.makedirs(output_dir, exist_ok=True)

    # Partition the file
    for i in range(num_partitions):
        start = i * lines_per_partition
        end = min((i + 1) * lines_per_partition, total_lines)
        
        output_file = os.path.join(output_dir, f'part_{i+1}.yaml')
        
        with open(output_file, 'w') as f:
            f.writelines(lines[start:end])

    print(f"Partitioned {input_file} into {num_partitions} files in the '{output_dir}' directory.")


input_file = 'merged_synt_sentences_2.yaml'
num_partitions = 8

partition_yaml(input_file, num_partitions)

"""
yaml_file = 'synt_sentences.yaml'
merge_lines(yaml_file)
"""