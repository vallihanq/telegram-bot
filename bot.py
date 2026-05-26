from telegram import Update, ReplyKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters, ContextTypes

TOKEN = 8243850753:AAEO3qma1C7-WscpYNg0fCSoJJVClGRRpgU  

keyboard = [
    ["📦 Заказать", "📋 Меню"],
    ["📞 Связаться"]
]

reply_markup = ReplyKeyboardMarkup(keyboard, resize_keyboard=True)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "Привет! 👋 Добро пожаловать в Marmelad Jelly World 🍬",
        reply_markup=reply_markup
    )

async def handle(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text

    if text == "📦 Заказать":
        await update.message.reply_text("Напишите заказ 🍬")
    elif text == "📋 Меню":
        await update.message.reply_text("У нас разные мармеладки 😋")
    elif text == "📞 Связаться":
        await update.message.reply_text("Мы скоро ответим 👌")
    else:
        await update.message.reply_text("Спасибо! Мы получили сообщение 👍")

app = ApplicationBuilder().token(TOKEN).build()

app.add_handler(CommandHandler("start", start))
app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle))

app.run_polling()
