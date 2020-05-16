from Parser import get_sorted_data
import json

"""
The data is now parsed as a JSON file that can be ingested
by a higher level entity. This issue now, however, is that we
wish to decrease the amount of data we are sending to reduce traffic. One method is
to apply a moving average filter. 


If `num_samples` is given a value of '3' then a moving average filter
of length 3 will be applied to the "value" fields under Z1 and Z2 seperately

* The file handle edge cases. For example, if `num_samples` is too high. It's up to you how you handle them.
"""

if __name__ == '__main__':
    input_filename = input('Enter the relative path of the file to parse: ')
    output_filename = input('Enter the relative path of the output file: ')
    num_samples= input('Enter the number of samples ')
    # Sort the input data
    response = get_sorted_data(input_filename, num_samples=num_samples)

    # Now write a JSON file with the new data
    with open(output_filename, 'w') as f:
        json.dump(response, f, indent=4)
