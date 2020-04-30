import vk_api, random
import sqlite3
import os

from vk_api.longpoll import VkLongPoll, VkEventType
 
TOKEN = os.environ.get('TOKEN_BOT')
vk_session = vk_api.VkApi(token = TOKEN_BT)

longpoll = VkLongPoll(vk_session)

vk = vk_session.get_api()

conn = sqlite3.connect("db.db")
c = conn.cursor()

global Random


def random_id():
    Random = 0
    Random += random.randint(0, 1000000000);
    return Random


def check_if_exists(user_id):
    c.execute("SELECT * FROM users WHERE user_id = %d" % user_id)
    result = c.fetchone()
    if result is None:
        return False
    return True


def register_new_user(user_id):
    c.execute("INSERT INTO users(user_id, state) VALUES (%d, '')" % user_id)
    conn.commit()
    c.execute("INSERT INTO user_info(user_id, user_wish) VALUES (%d, 0)" % user_id)
    conn.commit()


def get_user_state(user_id):
    c.execute("SELECT state FROM users WHERE user_id = %d" % user_id)
    result = c.fetchone()
    return result[0]


def get_user_wish(user_id):
    c.execute("SELECT user_wish FROM user_info WHERE user_id = %d" % user_id)
    result = c.fetchone()
    return result[0]


def set_user_wish(user_id, user_wish):
    c.execute("UPDATE user_info SET user_wish = %d WHERE user_id = %d" % (user_wish, user_id))
    conn.commit()


while True:
    for event in longpoll.listen():
        if event.type == VkEventType.MESSAGE_NEW and event.to_me:

            if not check_if_exists(event.user_id):
                register_new_user(event.user_id)

            if event.text.lower() == "начать":
                vk.messages.send(
                    user_id=event.user_id,
                    message="Приветик!\nНа связли Jim из технической поддержки.\nМогу я Вам чем-то помочь?",
                    keyboard=open("keyboard.json", "r", encoding="UTF-8").read(),
                    random_id=random_id()
                )

            elif event.text.lower() == "🎯 купить":
                if get_user_wish(event.user_id) == 1:
                    vk.messages.send(
                        user_id=event.user_id,
                        message="🎯 Что-нибудь купить можно тут: https://modshanshop.ru",
                        keyboard=open("keyboard.json", "r", encoding="UTF-8").read(),
                        random_id=random_id()
                    )
            
            elif event.text.lower() == "🌚 о нас":
                if get_user_wish(event.user_id) == 1:
                    vk.messages.send(
                        user_id=event.user_id,
                        message="🌚 Мы команда хакеров которые могут взломать любой пиратский сервер майнкрафт без смс и регистрации.\nВы можете присылать нам IP адреса серверов которые обманывают на команды или донат\n\nВид обращения: ! [IP]",
                        keyboard=open("keyboard.json", "r", encoding="UTF-8").read(),
                        random_id=random_id()
                    )
            elif event.text.lower() == "🌏 пользовательское соглашение":
                if get_user_wish(event.user_id) == 1:
                    vk.messages.send(
                        user_id=event.user_id,
                        message="🌏 Пользовательское соглашение: https://vk.com/topic-183789286_39359574",
                        keyboard=open("keyboard.json", "r", encoding="UTF-8").read(),
                        random_id=random_id()
                    )
            elif event.text.lower() == "💥 faq":
                if get_user_wish(event.user_id) == 1:
                    vk.messages.send(
                        user_id=event.user_id,
                        message="💥 Q: Кто мы такие?\nМы команда хакеров которые могут взломать любой пиратский сервер майнкрафт без смс и регистрации.\nВы можете присылать нам IP адреса серверов которые обманывают на команды или донат.\n\n💥Q: Где базируется команда разработчиков?\nБольшинство разработчиков из Санкт-Петербурга.",
                        keyboard=open("keyboard.json", "r", encoding="UTF-8").read(),
                        random_id=random_id()
                    )

            elif event.text.lower() == "хуй соси":
                if get_user_wish(event.user_id) == 1:
                    vk.messages.send(
                        user_id=event.user_id,
                        message="Сам соси",
                        keyboard=open("keyboard.json", "r", encoding="UTF-8").read(),
                        random_id=random_id()
                    )

            elif event.text.lower() == "пидарас":
                if get_user_wish(event.user_id) == 1:
                    vk.messages.send(
                        user_id=event.user_id,
                        message="Сам гандон",
                        keyboard=open("keyboard.json", "r", encoding="UTF-8").read(),
                        random_id=random_id()
                    )

            elif event.text.lower() == "гандон":
                if get_user_wish(event.user_id) == 1:
                    vk.messages.send(
                        user_id=event.user_id,
                        message="Пасть закрой, пёс",
                        keyboard=open("keyboard.json", "r", encoding="UTF-8").read(),
                        random_id=random_id()
                    )            

            elif event.text.lower() == "сука":
                if get_user_wish(event.user_id) == 1:
                    vk.messages.send(
                        user_id=event.user_id,
                        message="Сам сука",
                        keyboard=open("keyboard.json", "r", encoding="UTF-8").read(),
                        random_id=random_id()
                    )                 

            elif event.text.lower() == "блять":
                if get_user_wish(event.user_id) == 1:
                    vk.messages.send(
                        user_id=event.user_id,
                        message="Сам блять",
                        keyboard=open("keyboard.json", "r", encoding="UTF-8").read(),
                        random_id=random_id()
                    )                 

            elif event.text.lower() == "блядь":
                if get_user_wish(event.user_id) == 1:
                    vk.messages.send(
                        user_id=event.user_id,
                        message="Сам блядь",
                        keyboard=open("keyboard.json", "r", encoding="UTF-8").read(),
                        random_id=random_id()
                    )

            elif event.text.lower() == "пидрила":
                if get_user_wish(event.user_id) == 1:
                    vk.messages.send(
                        user_id=event.user_id,
                        message="А ты пёс",
                        keyboard=open("keyboard.json", "r", encoding="UTF-8").read(),
                        random_id=random_id()
                    )        

            elif event.text.lower() == "питух":
                if get_user_wish(event.user_id) == 1:
                    vk.messages.send(
                        user_id=event.user_id,
                        message="Шмара ёбаная",
                        keyboard=open("keyboard.json", "r", encoding="UTF-8").read(),
                        random_id=random_id()
                    )      

            elif event.text.lower() == "шмара":
                if get_user_wish(event.user_id) == 1:
                    vk.messages.send(
                        user_id=event.user_id,
                        message="Шмара ёбаная",
                        keyboard=open("keyboard.json", "r", encoding="UTF-8").read(),
                        random_id=random_id()
                    )    

            elif event.text.lower().startswith("!"):
                if get_user_wish(event.user_id) == 1:
                    vk.messages.send(
                        user_id=event.user_id,
                        message="Понял, принял. Переключаем ваш диалог на оператора. Мы уже занимаемся вашим вопросом, ответим в ближайшее время",
                        keyboard=open("keyboard.json", "r", encoding="UTF-8").read(),
                        random_id=random_id()
                    )


            else:
                vk.messages.send(
                    user_id=event.user_id,
                    message="Если хотите задать вопрос администратору - перед вашим вопросом напишите '!' ",
                    keyboard=open("keyboard.json", "r", encoding="UTF-8").read(),
                    random_id=random_id()
                )
