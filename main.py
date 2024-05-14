korzina = []
destvie = input("1 В магазин 2 ненадо : ")
def skritiy():
    print("Все условия били выполнены!\nВы  зоходите на черный рынок\nОт сюда нет пути назад\n(Я конечно мог бы сделать но мне лень))")

def destvie_korzina():
    vibor_tovara = input("1.Banana\n2.Aplle\n3.Kivi\n")
    if vibor_tovara == "1":
        korzina.append("Banana")
        destvie_korzina()
    elif vibor_tovara == "2":
        korzina.append("Apple")
        destvie_korzina()
    elif vibor_tovara == "3":
        korzina.append("Kivi")
        destvie_korzina()
    elif vibor_tovara == "i":
        print(korzina)
        destvie_korzina()
    elif vibor_tovara == "0":
        print(f"Ваши товары : {korzina}")
    elif vibor_tovara == "x":
        print("Корзина очищенна")
        korzina.clear()
    else:
        print("Нет такого дейсвия")
        destvie_korzina()

if destvie == "1":
    print("Что-бы добавить в корзине предмет выберите цыфру под которой он стоит\nЕсли хотите узнать что есть в корзине не выходя из нее то введите 'i'\nЕсли вы заончили все действия с корзинкой и хотите выйти напишите '0'\nДля удаления корзинки напишите 'x'\n")
    destvie_korzina()
elif destvie == "2":
    print("Вы вышли из корзины")
elif destvie == "666":
    skritiy()
else:
    print("Нет такого дейсвия")
print(korzina)