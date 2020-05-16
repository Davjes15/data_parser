from Parser import get_sorted_data
import json

"""
The objective is to parse the text file accompanying this script so that
it can be ingested into some higher level tool that will synthesize relationships
based on the dataset. 

"""

if __name__ == '__main__':
    input_filename = input('Enter the relative path of the file to parse: ')
    output_filename = input('Enter the relative path of the output file: ')

    # Sort the input data
    response = get_sorted_data(input_filename)

    # Now write a JSON file with the new data
    with open(output_filename, 'w') as f:
        json.dump(response, f)
