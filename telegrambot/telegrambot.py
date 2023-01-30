from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes


async def hi_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(f'Hello {update.effective_user.first_name}')

async def sum_command (update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    mess = update.message.text
    items = mess.split()
    a = int(items[1])
    b = int(items[2])
    await update.message.reply_text(a+b)

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(f'/hello\n/help\n/sum')


app = ApplicationBuilder().token("token").build()
print("Server start")

app.add_handler(CommandHandler("hello", hi_command))

app.add_handler(CommandHandler("sum", sum_command))

app.add_handler(CommandHandler("help", help_command))

app.run_polling()

print("Server stop")
