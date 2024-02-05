from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

       message = update.message.text
       # Process the message and generate a response using WormGPT's evil logic
       response = generate_response(message)
       update.message.reply_text(response)

   def main():
       updater = Updater("6507600675:AAE0YVdZmJJpHPMAZZcA3qQQcXEqAf2G_aY", use_context=True)
       dp = updater.dispatcher                                                                              dp.add_handler(MessageHandler(Filters.text, handle_message))
       updater.start_polling()
       updater.idle()                                                                                                                                                                                        if __name__ == '__main__':
       main()
   
