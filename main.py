import os
import re

if __name__ == "__main__":
  def format_file(input_file, output_file):
    pattern = r'(?:\s+|^)(vs|itp|np|itd|a|i|że|o|u|w|z|też)(?=\s+|[,.:!?^&()%@#$*`"{[\\<\']|$)'
    
    with open(input_file, 'r', encoding='utf-8') as f_in, open(output_file, 'w', encoding='utf-8') as f_out:
        content = f_in.read()

        def replace_func(match):
            matched_text = match.group()
            return '~' + matched_text.lstrip()

        formatted_content = re.sub(pattern, lambda match: replace_func(match), content)
        f_out.write(formatted_content)

  def process_files(input_folder, output_folder):
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # Przetwarzamy pliki
    for filename in os.listdir(input_folder):
        input_file = os.path.join(input_folder, filename)
        output_file = os.path.join(output_folder, filename)
        format_file(input_file, output_file)
        
  folder_x = 'C:\\Users\\Daniel\\Desktop\\dyplomówka\\text-formatter\\input'
  folder_y = 'C:\\Users\\Daniel\\Desktop\\dyplomówka\\text-formatter\\output'

  process_files(folder_x, folder_y)
print("Przetwarzanie zakończone.")