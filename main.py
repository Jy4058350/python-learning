name = ""
while name == "":
    name = input("名前を入力してください: ").strip()
    if name == "":
        print("名前は必須です。もう一度入力してください。")


age = -1
while age < 0:
    age_text = input("年齢を入力してください（０以上の数字) : ").strip()
    if age_text.isdigit():
        age = int(age_text)
        if age < 0:
            print("0以上の数字を入力してください。")
    else:
        print("年齢は数字で入力してください")

print(f"こんにちは、{name}さん!")
      
if age >= 18:
    print("あなたは成人です。")
else:
    print("あなたは未成年です。")

