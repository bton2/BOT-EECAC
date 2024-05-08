from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
from time import sleep
from datetime import datetime
import pandas as pd

data_hora_atuais = datetime.now()

async def start(update: Update, contex: ContextTypes.DEFAULT_TYPE) -> None:
    """Send a message when the command /start is issued"""
    response_message = 'Olá, equipe! Sou o Bot EECAC!\nFui criado pela equipe de Tecnologia da EECAC\
    da Universidade Federal Rural de Pernambuco (UFRPE) para o auxílio nas atividades da equipe Técnica de Campo.\n\
    Você pode começar listando meus comandos disponíveis com o /hello.'

    await update.message.reply_text(response_message)

async def hello(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    # await update.message.reply_text(f'Hello {update.effective_user.first_name}')
    await update.message.reply_text('Hello, Equipe da EECAC')

# Dados da planiha
async def dia(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    df = pd.read_excel("colheita_completa_2022.23.xlsx", sheet_name="Planilha1", skiprows= range(0, 1))
    tecnicos = df["Técnico responsável"]
    tecnico_responsavel = tecnicos.dropna(how="any", axis=0)
    lista = tecnico_responsavel.index.tolist()
    resultado = df.loc[lista[0]][1:16]
    await update.message.reply_text(f"Bom dia, Equipe EECAC! Os dados do dia: {resultado}")
    data_hora_br = data_hora_atuais.strftime("%d/%m/%Y %H:%M")
    await update.message.reply_text(f"Consulta realizada em: {data_hora_br}")


app = ApplicationBuilder().token("").build()

app.add_handler(CommandHandler("start", start))
app.add_handler(CommandHandler("hello", hello))
app.add_handler(CommandHandler("dia", dia))


app.run_polling()

