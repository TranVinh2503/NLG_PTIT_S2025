import os
import json

def merge_jsonl_files(input_folder, output_file):
    with open(output_file, 'w', encoding='utf-8') as outfile:
        for filename in os.listdir(input_folder):
            if filename.endswith('.jsonl'):
                filepath = os.path.join(input_folder, filename)
                with open(filepath, 'r', encoding='utf-8') as infile:
                    for line in infile:
                        outfile.write(line)

# Thay đổi đường dẫn thư mục đầu vào và tên file đầu ra theo nhu cầu của bạn
input_folder = 'fine_tuning'
output_file = 'data_total.jsonl'

merge_jsonl_files(input_folder, output_file)
print("Gộp file JSONL thành công!")
