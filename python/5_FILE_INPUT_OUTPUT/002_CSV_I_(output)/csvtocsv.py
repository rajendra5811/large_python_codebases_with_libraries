import csv
high_wages = []
desired_wage = 40000

with open('wages.csv', 'r') as infile:
    reader = csv.DictReader(infile)
    for elem in reader:
        print(elem)  # <= Each of these elements are `dict`s, not `list`s!
        if int(elem['annual_wage']) >= desired_wage:
            high_wages.append(elem)
            print(high_wages)

with open('high-wages-with-header.csv', 'w') as outfile:
    writer = csv.DictWriter(outfile, fieldnames=high_wages[0].keys())
    writer.writeheader()
    for elem in high_wages:
        writer.writerow(elem) 