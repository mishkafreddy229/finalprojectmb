import telebot
import os
from dotenv import load_dotenv
from config import TOKEN
import random

load_dotenv()
bot = telebot.TeleBot(token=TOKEN)

FACTS = [
    "🌡️ Средняя температура Земли выросла на 1.1°C с доиндустриальной эпохи",
    "🧊 Арктический лед теряет около 13% площади каждое десятилетие",
    "🌊 Уровень моря поднимается на 3.6 мм в год из-за таяния ледников",
    "🔥 2020-2023 годы стали самыми теплыми за всю историю наблюдений",
    "🌪️ Глобальное потепление увеличивает частоту экстремальных погодных явлений",
    "🐻❄️ Таяние вечной мерзлоты высвобождает метан - мощный парниковый газ",
    "🌿 Океаны поглощают 30% CO2, что приводит к их закислению",
    "🏭 Сжигание ископаемого топлива - основной источник парниковых газов"
]

TIPS = [
    "💡 Замени лампочки на светодиодные - экономия до 80% энергии",
    "🚲 Пройдись пешком или поезжай на велосипеде вместо коротких поездок на авто",
    "🌱 Добавь в рацион больше растительной пищи",
    "♻️ Сортируй отходы и сдавай на переработку",
    "💧 Установи аэратор на кран - экономия воды до 50%",
    "🛒 Используй многоразовые сумки вместо пластиковых пакетов",
    "📱 Выключай зарядные устройства из розетки, когда не используешь",
    "🌳 Посади дерево - оно поглощает CO2 в течение жизни"
]

SOLUTIONS = [
    "⚡ **Переход на возобновляемую энергию:** Солнечные, ветровые, гидроэлектростанции",
    "🏠 **Энергоэффективность:** Утепление домов, умные системы отопления",
    "🚆 **Развитие общественного транспорта:** Электробусы, метро, электрички",
    "🌲 **Сохранение лесов:** Лесовосстановление, защита от вырубки",
    "🔋 **Электромобили:** Снижение выбросов в транспортном секторе",
    "🏭 **Зеленые технологии:** Улавливание CO2, переработка отходов",
    "🌾 **Устойчивое сельское хозяйство:** Органика, сохранение почв",
    "📚 **Экологическое образование:** Повышение осведомленности общества"
]

@bot.message_handler(commands=["start"])
def start_command(message):
    text = "🌍 Это бот \"Глобальное потепление\"\nЯ помогу тебе узнать больше об изменении климата и способах борьбы с ним.\n\nДоступные команды:\n/facts - Факты о глобальном потеплении\n/tips - Полезные эко-советы\n/solutions - Решения проблемы\n/quiz - Тест на экологическую грамотность\n/calculator - Расчет углеродного следа\n/news - Новости об изменении климата\n/help - Помощь по использованию бота"
    if message.text == "/start":
        text = f"Привет, {message.from_user.first_name}\n\n" + text
    
    bot.send_message(message.chat.id, text)

@bot.message_handler(commands=["help"])
def help_command(message):
    text = "Как пользоваться ботом:\n\n1. Выбери интересующую тему с помощью команд\n2. Используй кнопки для навигации\n3. Регулярно проверяй эко-советы (/tips)\n4. Пройди тест (/quiz) для проверки знаний\n5. Рассчитай свой углеродный след (/calculator)"    
    bot.send_message(message.chat.id, text)

@bot.message_handler(commands=["facts"])
def facts_command(message):
    fact = random.choice(FACTS)

    keyboard = telebot.types.InlineKeyboardMarkup()
    keyboard.add(telebot.types.InlineKeyboardButton(
        text="Еще факт",
        callback_data="more_facts"
    ))
    
    bot.send_message(
        message.chat.id,
        f"📊 *Факт о глобальном потеплении:*\n\n{fact}",
        parse_mode="Markdown",
        reply_markup=keyboard
    )

@bot.callback_query_handler(func=lambda call: call.data == "more_facts")
def more_facts_callback(call):
    fact = random.choice(FACTS)
    
    keyboard = telebot.types.InlineKeyboardMarkup()
    keyboard.add(telebot.types.InlineKeyboardButton(
        text="Еще факт",
        callback_data="more_facts"
    ))
    
    bot.edit_message_text(
        f"📊 *Факт о глобальном потеплении:*\n\n{fact}",
        chat_id=call.message.chat.id,
        message_id=call.message.message_id,
        parse_mode="Markdown",
        reply_markup=keyboard
    )

@bot.message_handler(commands=["tips"])
def tips_command(message):
    tip = random.choice(TIPS)
    
    keyboard = telebot.types.InlineKeyboardMarkup()
    keyboard.add(telebot.types.InlineKeyboardButton(
        text="Следующий совет",
        callback_data="more_tips"
    ))
    
    bot.send_message(
        message.chat.id,
        f"🌿 *Эко-совет дня:*\n\n{tip}",
        parse_mode="Markdown",
        reply_markup=keyboard
    )

@bot.callback_query_handler(func=lambda call: call.data == "more_tips")
def more_tips_callback(call):
    tip = random.choice(TIPS)
    
    keyboard = telebot.types.InlineKeyboardMarkup()
    keyboard.add(telebot.types.InlineKeyboardButton(
        text="Следующий совет",
        callback_data="more_tips"
    ))
    
    bot.edit_message_text(
        f"🌿 *Эко-совет дня:*\n\n{tip}",
        chat_id=call.message.chat.id,
        message_id=call.message.message_id,
        parse_mode="Markdown",
        reply_markup=keyboard
    )

@bot.message_handler(commands=["solutions"])
def solutions_command(message):
    solution = random.choice(SOLUTIONS)
    keyboard = telebot.types.InlineKeyboardMarkup()
    keyboard.add(telebot.types.InlineKeyboardButton(
        text="Другое решение",
        callback_data="more_solutions"
    ))
    bot.send_message(
        message.chat.id,
        f"🚀 *Решение проблемы:*\n\n{solution}",
        parse_mode="Markdown",
        reply_markup=keyboard
    )

@bot.callback_query_handler(func=lambda call: call.data == "more_solutions")
def more_solutions_callback(call):
    solution = random.choice(SOLUTIONS)
    keyboard = telebot.types.InlineKeyboardMarkup()
    keyboard.add(telebot.types.InlineKeyboardButton(
        text="Другое решение",
        callback_data="more_solutions"
    ))
    bot.edit_message_text(
        f"🚀 *Решение проблемы:*\n\n{solution}",
        chat_id=call.message.chat.id,
        message_id=call.message.message_id,
        parse_mode="Markdown",
        reply_markup=keyboard
    )

bot.infinity_polling()