from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes




async def start(update: Update, contex: ContextTypes.DEFAULT_TYPE) -> None:
    """Send a message when the command /start is issued"""
    response_message = 'Olá, equipe! Sou o Bot EECAC!\nFui criado pela equipe de Tecnologia da EECAC\
    da Universidade Federal Rural de Pernambuco (UFRPE) para o auxílio nas atividades da equipe Técnica de Campo.\n\
    Você pode começar listando meus comandos disponíveis com o /hello.'

    await update.message.reply_text(response_message)

async def hello(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    # await update.message.reply_text(f'Hello {update.effective_user.first_name}')
    await update.message.reply_text('Hello, Equipe da EECAC')


app = ApplicationBuilder().token("7003829563:AAGhXisgAVYQgsIQmsm5rPoKvGvYkG7dFM8").build()

app.add_handler(CommandHandler("hello", hello))
app.add_handler(CommandHandler("start", start))

app.run_polling()

