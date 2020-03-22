
def main():
    income_num = []
    months = int(input("How many months?: "))

    for month in range(1, months + 1):
        income = float(
            input("Enter income for month {}: ". format(month)))
        income_num.append(income)

    print_sum(income_num)

#calculate total income
def print_sum(income_num):
    total = 0
    for month, income in enumerate(income_num):
        total += income
        print("Month {} - Income: ${} Total:$ {}".format(month+1, income, total))

main()