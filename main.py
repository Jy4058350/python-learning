# name = input("Enter your name: ").strip()
# age = int(input("Enter your age: ").strip())
# height_m = float(input("Enter your height (m): ").strip())

# answer = input("Are you a student? (y/n):").strip().lower()
# is_student = answer == "y"

# print("\n--- Values ---")
# print(name, age, height_m, is_student)

# print("\n--- Types ---")
# print(type(name), type(age), type(height_m), type(is_student))

# if is_student:
#     print("Student mode ON")
# else:
#     print("Student mode OFF")


fruits = []

for i in range(3):
    fruit = input(f"Fruit {i+1}: ").strip()
    fruits.append(fruit)

print("\nYour fruits:")
for fruit in fruits:
    print("-", fruit)

print(f"Total: {len(fruits)} items")