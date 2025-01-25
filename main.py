from telegram.ext import Application, CommandHandler, MessageHandler
from telegram.ext import filters
from instaloader import Instaloader, Post

# Bot tokenini joylashtiring
BOT_TOKEN = '7792357047:AAGHkjG9RG7QnRpYyWSWX_29b350M10mS4E'

# Instagram videolarini yuklash funksiyasi
def download_instagram_video(url):
    loader = Instaloader()
    post = Post.from_shortcode(loader.context, url.split("/")[-2])
    video_url = post.video_url
    return video_url

# /start komandasi
async def start(update, context):
    await update.message.reply_text("Salom! Men Instagram videolarini yuklab beruvchi botman. Videoning havolasini yuboring!")

# Havolani qayta ishlash
async def handle_message(update, context):
    url = update.message.text
    if "instagram.com" in url:
        await update.message.reply_text("Videoni yuklab olish uchun ishlov berilmoqda...")
        try:
            video_url = download_instagram_video(url)
            await context.bot.send_video(chat_id=update.effective_chat.id, video=video_url)
        except Exception as e:
            await update.message.reply_text("Xatolik yuz berdi! Havolani qayta tekshiring yoki boshqa havola yuboring.")
    else:
        await update.message.reply_text("Iltimos, Instagram video havolasini yuboring.")

# Botni ishga tushirish
def main():
    # Botni sozlash
    application = Application.builder().token(BOT_TOKEN).build()

    # Handlers qo‘shish
    application.add_handler(CommandHandler("start", start))
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

    # Ishga tushirish
    application.run_polling()

if __name__ == '__main__':
    main()
