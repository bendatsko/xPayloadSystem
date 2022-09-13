import csv

with open('blue_bus_test.csv', 'r') as csv_file:
    csv_reader = csv.reader(csv_file)

    with open('blue_bus_test_fin.csv', 'w') as new_file:
        csv_writer = csv.writer(new_file, delimiter = ' ')

        next(csv_reader)

        for line in csv_reader:
            csv_writer.writerow(line[0])

