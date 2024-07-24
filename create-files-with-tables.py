"""code to create tables from 2 to 5 and save it to individual files"""

def write_tables():
    for i in range(2,5):
        table = f"Table of {i} is ::\n"
        for j in range(1,11):
            table = table + f"{i} * {j} = {i*j}\n"
        with open(f"table_of_{i}.txt", "w") as f:
            f.write(table)
        print(table)
write_tables()