# Author: Zirou Qiu
# Program: Extract info from the dataset and save to a new file
# Created: 11/5/2018

import json

#-----------------------------read_json()----------------------------------
def read_json(file_name = "kindle_store.json") -> "[{obj_1}, {obj_2}, ... {obj_n}]":
    """
    # Description: Read the given json file(the default file name is kindle_store.json)
    and save json objects into a list of dicts. 

    # Return: the list of dicts where each dict consists of an json object
    """
    reviews = []
    with open(file_name) as f:
        for line in f:
            reviews.append(json.loads(line))
    return reviews

#---------------------------------write_file()-------------------------------
def write_file(reviews : "list of dicts where each dict consists of an json object", file_name = "clean.txt"):
    """
    # Description: Iterate the list of objects and write the following fields:
        1. reviewerID, 
        2. asin, 
        3. helpful, 
        4. overall, 
        5. reviewTime
      to the file.

    # Resulted file format:
        A17YHECC8H9NEY	B00M13FNSS	[0, 0]	5.0	07 23, 2014
        A20KO0BPMNREJL	B00M13FNSS	[1, 1]	5.0	07 23, 2014
        A1BQO66R6OLCCW	B00M13FNSS	[0, 0]	5.0	07 23, 2014
    """
    #write to file
    data_file = open("clean.txt", 'w+')
    for json_obj in reviews:
        #this is very sloppy, feel free to modify
        cleaned_data = json_obj["reviewerID"] + '\t' + json_obj["asin"] + '\t' + str(json_obj["helpful"]) +  '\t' + str(json_obj["overall"]) + '\t' + json_obj["reviewTime"] + '\n'
        data_file.write(cleaned_data)

    data_file.close()

#--------------------------------main()--------------------------------------
if __name__ == "__main__":
    #the list of dicts where each dict consists of an json object
    reviews = []

    reviews = read_json()
    write_file(reviews)