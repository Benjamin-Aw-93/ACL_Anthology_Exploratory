import json
import glob
import pandas as pd
from os import walk
from tqdm.auto import tqdm

tqdm.pandas()

# Get all the files within Data/Base_JSON
# All files and directories ending with .json:

def get_file_dict(data_folder_path):
    
    dic_file = {"title": [],
               "file_path": []}
    
    f = []

    for (dirpath, dirnames, filenames) in walk(data_folder_path):
        f.extend([dirpath + '/' + filename for filename in filenames])

    for file_path in f:

        # Opening JSON file
        f = open(file_path)

        # returns JSON object as a dictionary
        data = json.load(f)
        title = data['title']

        # Getting the title
        dic_file['title'].append(title)
        dic_file['file_path'].append(file_path)

        # Closing file
        f.close()
        
    return pd.DataFrame.from_dict(dic_file)


def get_section(file_path, section_interest):
    
    # Dictionary keeping track of which section
    final_out = {i.lower().title(): "" for i in section_interest}
    
    # Opening JSON file
    f = open(file_path)

    # returns JSON object as a dictionary
    data = json.load(f)

    # Iterating through the json list
    for text_body in data['pdf_parse']['body_text']:
        if text_body["section"].lower() in section_interest:
            final_out[text_body["section"].lower().title()] += text_body["text"]

    # Closing file
    f.close()
    
    return final_out