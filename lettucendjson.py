
import json

def json_to_ndjson(input_file, output_file):
    # Open input JSON file
    with open(input_file, 'r') as infile:
        # Load JSON data
        data = json.load(infile)

    # Open output file for writing
    with open(output_file, 'w') as outfile:
        # Write each JSON object as newline-delimited JSON
        for obj in data:
            json.dump(obj, outfile)
            outfile.write('\n')

# Example usage:
json_to_ndjson('/Users/pkalyanakumar/Downloads/archive2/fixed_lettuce_dataset1.json', '/Users/pkalyanakumar/Downloads/archive2/final_lettuce.ndjson')