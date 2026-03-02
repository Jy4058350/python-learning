name = input("名前を入力してください: ").strip()

if name == "":
	print("名前が未入力です。")
else:
	age_text = input("年齢を入力してください: ").strip()

	if age_text.isdigit():
		age = int(age_text)
		print(f"こんにちは、{name} さん！")

		if age >= 18:
			print("あなたは成人です。")
		else:
			print("あなたは未成年です。")
	else:
		print("年齢は数字で入力してください。")