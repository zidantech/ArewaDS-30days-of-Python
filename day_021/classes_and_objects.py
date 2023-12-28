
# # Day 21 - Classes and objects


# Python has the module called statistics and we can use this module to do all the statistical calculations. However, to learn how to make function and reuse function let us try to develop a program, which calculates the measure of central tendency of a sample (mean, median, mode) and measure of variability (range, variance, standard deviation). In addition to those measures, find the min, max, count, percentile, and frequency distribution of the sample. You can create a class called Statistics and create all the functions that do statistical calculations as methods for the Statistics class. Check the output below.
class Statistics:
    def __init__(self, data):
        self.data = data

    def count(self):
        return len(self.data)

    def sum(self):
        return sum(self.data)

    def min(self):
        return min(self.data)

    def max(self):
        return max(self.data)

    def range(self):
        return max(self.data) - min(self.data)

    def mean(self):
        return sum(self.data) / len(self.data)

    def median(self):
        sorted_data = sorted(self.data)
        n = len(sorted_data)
        if n % 2 == 0:
            mid1 = sorted_data[n // 2 - 1]
            mid2 = sorted_data[n // 2]
            return (mid1 + mid2) / 2
        else:
            return sorted_data[n // 2]

    def mode(self):
        frequency = {}
        for value in self.data:
            frequency[value] = frequency.get(value, 0) + 1
        max_count = max(frequency.values())
        mode_value = [key for key, count in frequency.items() if count == max_count]
        return {'mode': mode_value[0], 'count': max_count}

    def std(self):
        mean = self.mean()
        squared_diff = sum((x - mean) ** 2 for x in self.data)
        variance = squared_diff / len(self.data)
        return variance ** 0.5

    def var(self):
        mean = self.mean()
        squared_diff = sum((x - mean) ** 2 for x in self.data)
        return squared_diff / len(self.data)

    def freq_dist(self):
        frequency = {}
        for value in self.data:
            frequency[value] = frequency.get(value, 0) + 1
        return sorted([(count, value) for value, count in frequency.items()], reverse=True)

    def describe(self):
        result = f"Count: {self.count()}\n"
        result += f"Sum: {self.sum()}\n"
        result += f"Min: {self.min()}\n"
        result += f"Max: {self.max()}\n"
        result += f"Range: {self.range()}\n"
        result += f"Mean: {self.mean()}\n"
        result += f"Median: {self.median()}\n"
        result += f"Mode: {self.mode()}\n"
        result += f"Variance: {self.var()}\n"
        result += f"Standard Deviation: {self.std()}\n"
        result += f"Frequency Distribution: {self.freq_dist()}"
        return result

# Example usage:
ages = [31, 26, 34, 37, 27, 26, 32, 32, 26, 27, 27, 24, 32, 33, 27, 25, 26, 38, 37, 31, 34, 24, 33, 29, 26]
data = Statistics(ages)

# Print the statistics
print(data.describe())



# Create a class called PersonAccount. It has firstname, lastname, incomes, expenses properties and it has total_income, total_expense, account_info, add_income, add_expense and account_balance methods. Incomes is a set of incomes and its description. The same goes for expenses.
class PersonAccount:
    def __init__(self, firstname, lastname):
        self.firstname = firstname
        self.lastname = lastname
        self.incomes = {}
        self.expenses = {}

    def add_income(self, amount, description):
        self.incomes[description] = amount

    def add_expense(self, amount, description):
        self.expenses[description] = amount

    def total_income(self):
        return sum(self.incomes.values())

    def total_expense(self):
        return sum(self.expenses.values())

    def account_balance(self):
        return self.total_income() - self.total_expense()

    def account_info(self):
        info = f"Account Information for {self.firstname} {self.lastname}:\n"
        info += f"Total Income: {self.total_income()}\n"
        info += f"Total Expense: {self.total_expense()}\n"
        info += f"Account Balance: {self.account_balance()}\n"
        info += "\nIncome Details:\n"
        for desc, amount in self.incomes.items():
            info += f"{desc}: {amount}\n"
        info += "\nExpense Details:\n"
        for desc, amount in self.expenses.items():
            info += f"{desc}: {amount}\n"
        return info

# Example usage:
person = PersonAccount("Zidan", "Musa")

# Adding income and expenses
person.add_income(150000, "Salary")
person.add_income(50000, "Freelance Work")
person.add_expense(50000, "Rent")
person.add_expense(30000, "Utilities")
person.add_expense(20000, "Groceries")

# Displaying account information
print(person.account_info())



