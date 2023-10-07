import json
from resume_parser import resumeparse
import warnings

warnings.filterwarnings("ignore")
def return_data(path):
    return resumeparse.read_file(path)

def preprocess_data(data):
    data['total_exp'] = int(data['total_exp'])
    data['skills'] = [skill.strip() for skill in data['skills'] if skill.strip()]
    
    return data

def save_to_json(data, output_path):
    with open(output_path, 'w') as json_file:
        json.dump(data, json_file, indent=4)

input_resume_path = "/home/richard/Downloads/3.pdf"
output_json_path = "output.json"
save_to_json(preprocess_data(return_data(input_resume_path)), output_json_path)
