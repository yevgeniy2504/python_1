import csv
import random


def generate_csv_file(filename, num_rows):
    with open(filename, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        for i in range(num_rows):
            row = [random.randint(1, 1000) for j in range(3)]
            writer.writerow(row)


if __name__ == '__main__':
    generate_csv_file("new_csv.csv", 50)
