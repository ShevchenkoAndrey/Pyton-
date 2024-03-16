import random
players = []
questions = [
    "Какое самое смешное кино, которое ты когда-либо видел, и почему?",
    "Если бы у тебя была возможность пожить в любой стране мира в течение года, куда бы ты отправился и почему?",
    "Расскажи о самом странном сне, который тебе когда-либо снился.",
    "Какая самая смешная ситуация произошла с тобой в общественном месте?",
    "Если бы у тебя была возможность встретиться с любым известным человеком (живым или мёртвым), кто бы это был и что бы ты ему сказал?",
    "Какой самый дикий спортивный вид ты бы хотел попробовать и почему?",
    "Расскажи о самом странном или смешном путешествии, которое ты когда-либо совершал.",
    "Какой самый странный предмет ты когда-либо находил в своей сумке или кармане?",
    "Если бы ты мог стать профессиональным актёром, в каком фильме ты бы хотел сыграть главную роль и почему?",
    "Какое самое экстремальное испытание ты бы хотел пройти в своей жизни, и почему?"
]
actions = [
    "Попробуйте нарисовать портрет кого-то в комнате, держа карандаш во рту.  ",
    "Попробуйте пройти через всю комнату, держа на голове книгу.",
    "Имитируйте звук любого животного, которое выберет другой игрок.",
    "Попробуйте угадать, что пишут на вашей ладони, пока глаза закрыты.  ",
    "Поставьте свой наиболее громкий смех в течение 30 секунд.",
    "Попробуйте повторить пословицу или поговорку задом наперёд."
]
while True:
    ask = input("Додати гравця? - ")
    if ask.lower() == "так":
        player = input("Додати гравця - ")
        players.append(player)
    elif ask.lower() == "ні":
        break
    else:
        print("Неправильна відповідь")
while True:
    cur_player = random.choice(players)
    print(cur_player)
    choice = input("правда чи дія? - ")
    if choice.lower() == "правда":
        question_index = random.randint(0, len(questions) - 1)
        question = questions.pop(question_index)
        print(question)
    elif choice.lower() == "дія":
        action_index = random.randint(0, len(actions) - 1)
        action = actions.pop(action_index)
        print(action)
    else:
        print("Неверный выбор. Повторите попытку.")
    continue_game = input("Продовжити? - ")
    if continue_game.lower() != "так" or continue_game.lower() != "т":
        print("                ")