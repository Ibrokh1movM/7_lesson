import json
import matplotlib.pyplot as plt


class Fibonacci:
    def __init__(self, max_terms=None, include_negative=False, step=1):
        self.max_terms = max_terms
        self.include_negative = include_negative
        self.step = step
        self.current = 0
        self.next = 1
        self.count = 0
        self.direction = 1
        self.cache = {0: 0, 1: 1}

    def __iter__(self):
        return self

    def __next__(self):
        if self.max_terms is not None and self.count >= self.max_terms:
            raise StopIteration

        if self.direction == -1:
            current = self.current
            self.current, self.next = self.next, self.current - self.next
        else:
            current = self.current
            self.current, self.next = self.next, self.current + self.next

        for _ in range(self.step - 1):
            self.current, self.next = self.next, self.current + self.next

        self.count += 1
        return current

    def toggle_direction(self):
        """
        this function toggles the direction of the fibonacci sequence
        :return:
        """
        if self.include_negative:
            self.direction *= -1

    def calculate(self, n):
        """
        this function calculates nth term of the Fibonacci sequence.
        :param n:
        :return:
        """
        if n in self.cache:
            return self.cache[n]
        if n > 0:
            self.cache[n] = self.calculate(n - 1) + self.calculate(n - 2)
        else:
            self.cache[n] = self.calculate(n + 2) - self.calculate(n + 1)
        return self.cache[n]


# *** Fibonacci qatori bilan ishlash ***
# 1. 10 ta Fibonacci sonlarini chiqarish
print("10 ta Fibonacci sonlari:")
fib = Fibonacci(max_terms=10)
for num in fib:
    print(num, end=" ")

# 2. Manfiy Fibonacci qatorini chiqarish
print("\n\nManfiy Fibonacci sonlari:")
fib_negative = Fibonacci(max_terms=10, include_negative=True)
fib_negative.toggle_direction()
for num in fib_negative:
    print(num, end=" ")

# 3. Har 2-sonni chiqarish
print("\n\nHar 2-son:")
fib_step = Fibonacci(max_terms=10, step=2)
for num in fib_step:
    print(num, end=" ")

# 4. Muayyan Fibonacci sonlarini hisoblash
print("\n\nMuayyan sonlarni hisoblash:")
fib_calc = Fibonacci()
print(f"F(20): {fib_calc.calculate(20)}")
print(f"F(-5): {fib_calc.calculate(-5)}")

# 5. Fibonacci qatorini grafikda tasvirlash
fib_graph = Fibonacci(max_terms=20)
values = [num for num in fib_graph]
plt.plot(values, marker="o")
plt.title("Fibonacci Sequence")
plt.xlabel("Index")
plt.ylabel("Value")
plt.grid()
plt.show()

# 6. JSON faylga saqlash
fib_json = Fibonacci(max_terms=10)
values = [num for num in fib_json]
with open("fibonacci.json", "w") as file:
    json.dump(values, file)
print("\nFibonacci qatori JSON faylga saqlandi.")

# 7. Statistik tahlil
print("\nStatistik tahlil:")
fib_stats = Fibonacci(max_terms=10)
values = [num for num in fib_stats]
print(f"Fibonacci qatori: {values}")
print(f"Eng katta son: {max(values)}")
print(f"O'rtacha qiymat: {sum(values) / len(values)}")
