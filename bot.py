
import logging
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

TOKEN = "7842707470:AAFDSyElrjfrHLq6gmfOh4LByMJu9Bbrfh0"

logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
)

WELCOME_TEXT = (
    "Привет 👋\n"
    "Я — Татьяна, архитектор и GSR-специалист.\n\n"
    "Ты здесь, потому что чувствуешь, что с пространством — что-то не то.\n\n"
    "Если ты ловишь себя на раздражении дома — скорее всего, дело не в тебе, а в среде. "
    "Вот чеклист, с которым работают мои клиенты ⬇️"
)

FOLLOWUP_TEXT = (
    "Хочешь больше таких материалов и неожиданных откровений?\n\n"
    "🔗 Подписывайся на канал: @tm_ad_gsr\n\n"
    "Это не интерьерный блог и не психология.\n"
    "Это — другое. Загляни."
)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(WELCOME_TEXT)
    await context.bot.send_document(
        chat_id=update.effective_chat.id,
        document=open("5_errors_interior_state_detailed.pdf", "rb")
    )
    await update.message.reply_text(FOLLOWUP_TEXT)

if __name__ == "__main__":
    app = ApplicationBuilder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.run_polling()
