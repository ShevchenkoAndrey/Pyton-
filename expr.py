def vow_c():
    text = input("Введіть рядок - ")
    vows = "уУеЕїЇіІаАоОєЄяЯиИюЮ"
    num = 0
    for i in text:
        if i in vows:
            num +=1
    print("Число голосних -", num)
vow_c()