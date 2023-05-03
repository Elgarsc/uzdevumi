#zem class customer
def save_customers_to_csv(customers, filename):
    with open(filename, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['Name', 'Surname', 'ID', 'Email', 'Date Created'])
        for customer in customers:
            writer.writerow([customer.name, customer.surname, customer.id, customer.email, customer.datetime_created])
