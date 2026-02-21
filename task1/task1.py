# Завдання 1

from pathlib import Path

def total_salary(path):
    path = Path(path)

    # add raise if file doesn't exist
    if not path.exists():
       raise FileNotFoundError("File does not exist.")

    total = 0
    count = 0

    with path.open("r", encoding="utf-8") as file:
        for line in file:
            name, salary = line.strip().split(",")
            total += float(salary)
            count += 1
    # calculate total and average  
    return total, total / count if count else 0

# use try and except to display proper error format
try:
    total, average = total_salary("goit-pycore-hw-04/task1/salary.txt")
    print(f"Total salary: {total}, Average salary: {average}")
except FileNotFoundError as e:
    print(e)


