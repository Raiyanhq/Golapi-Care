import json

# 1. Read the JSON file
with open('input.json', 'r') as file:
    data = json.load(file)

# 2. Extract specific information
user_name = data['user']['name']
user_email = data['user']['email']

extracted_data = {
    'name': user_name,
    'email': user_email
}

# 3. Write the extracted data to a new file
with open('output.json', 'w') as file:
    json.dump(extracted_data, file, indent=4)

print("Data extracted and saved to output.json!")
