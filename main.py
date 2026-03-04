def get_name():
  while True:
    name = input("what is your name?").strip()
    if name != "":
      return name
    print("Name is required. Please try again.")

name = get_name()
print(f"Hello, {name}!")


def get_age():
  while True:
    age_text = input("How old are you?").strip()
    if age_text.isdigit():
      age = int(age_text)
      if age >= 0:
        return age
    print("Age must be a number 0 or higher. Please try again.")

age = get_age()

if age >= 18:
    print("You are an adult.")
else:
    print("You are a minor.")