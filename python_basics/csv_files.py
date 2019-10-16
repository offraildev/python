import csv

# read from the csv file
with open('data_files/names.csv', 'r') as csv_file:
    csv_reader = csv.reader(csv_file)

    print(csv_reader)  # csv_reader varible is just an object

    next(csv_reader) # skip over the column names, the pointer gets adjusted to the next items

    # iterate through the items
    for line in csv_reader:
        print(line)

# write into a csv file
with open('data_files/names.csv', 'r') as csv_file:
    csv_reader = csv.reader(csv_file)
    
    with open('data_files/new_names.csv', 'w') as new_csv_file:
        csv_writer = csv.writer(new_csv_file, delimiter='\t')

        for line in csv_reader:
            csv_writer.writerow(line)

# using dict reader and writer, more simple to handle the data
with open('data_files/names.csv', 'r') as csv_file:
    csv_reader = csv.DictReader(csv_file)

    with open('data_files/new_names.csv', 'w') as new_csv_file:
        fieldnames = ['first_name', 'last_name'] # in case of dict writer need to pass in field names
        csv_writer = csv.DictWriter(new_csv_file, fieldnames=fieldnames, delimiter='\t')
        
        # write out the header first if header is needed
        csv_writer.writeheader() 

        # loop through the lines and write it 
        for line in csv_reader:
            del line['email'] # can delete a key if needed
            csv_writer.writerow(line)
