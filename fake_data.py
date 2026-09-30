from faker import Faker
from faker.providers import internet
import csv

def generate_user_data(num_of_users):
    fake = Faker()
    
    fake.add_provider(internet)
    
    user_data = []
    
    for _ in range(num_of_users):
        user = {
            'Name': fake.name(),
            'Email': fake.free_email(),
            'Phone Number': fake.phone_number(),
            'Birthdate': fake.date_of_birth(),
            'Address': fake.address(),
            'City': fake.city(),
            'ZIP Code': fake.country(),
            'Job Title': fake.zipcode(),
            'Company': fake.company(),
            'IP Address': fake.ipv4_private(),
            'Credit Card Number': fake.credit_card_number(),
            'Username': fake.user_name(),
            'Website': fake.url(),
            'SSN': fake.ssn()
            }
        
        user_data.append(user)
        
        return user_data
        

def save_to_csv(data, filename):
    keys = data[0].keys()
    
    with open(filename, 'w', newline='') as output_file:
        writer = csv.DictWriter(output_file, fieldnames=keys)
        writer.writeheader()
        for user in data:
            writer.writerow(user)
    
    print(f'[+] Data saved to {filename} successfully.')

def save_to_text(data, filename):
    with open(filename, 'w') as output_file:
        for user in data:
            for key, value in user.items():
                output_file.write(f"{key}: {value}\n")
            
            output_file.write('\n')
    print(f'[+] Data saved to {filename} successfully.')
    

def print_data_vertically(data):
    for user in data:
        for key, value in user.items():
            print(f"{key}: {value}")
            
        print()
        

number_of_users = int(input("[!] Enter the number of users to generate: "))

user_data = generate_user_data(number_of_users)

save_option = input("[?] Do you want to save the data to a file? (yes/no): ")

if save_option == 'yes':
    file_type = input("[!] Enter file type (csv/txt/both): ").lower()
    if file_type == 'csv' or file_type == 'both':
        custom_filename_csv = input("[!] Enter the CSV filename (without
