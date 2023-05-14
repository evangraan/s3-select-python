import csv
import random
import string

# Function to generate random string of specific length


def random_string(length):
    return ''.join(random.choice(string.ascii_letters) for i in range(length))

# Function to generate random digit string of specific length


def random_digits(length):
    return ''.join(random.choice(string.digits) for i in range(length))

# Function to generate random category


def random_category():
    return random.randint(1, 100)


# Number of entries
num_entries = 78000000

# Filename
filename = "output.csv"

# Write to CSV
with open(filename, mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["id", "name", "surname", "phone number", "category"])
    for id in range(1, num_entries + 1):
        print(id)
        writer.writerow([id, random_string(20), random_string(
            20), random_digits(10), random_category()])

print(
    f"Data generation complete. {num_entries} entries were written to {filename}")
