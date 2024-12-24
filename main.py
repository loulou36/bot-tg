print("Hello, World!")

# Basic mathematical operations

# Addition
a = 10
b = 5
print("Addition: {} + {} = {}".format(a, b, a + b))

# Subtraction
print("Subtraction: {} - {} = {}".format(a, b, a - b))

# Multiplication
print("Multiplication: {} * {} = {}".format(a, b, a * b))

# Division
print("Division: {} / {} = {:.2f}".format(a, b, a / b))

# Modulus
print("Modulus: {} % {} = {}".format(a, b, a % b))

# Exponentiation
print("Exponentiation: {} ** {} = {}".format(a, b, a ** b))

# Floor Division
print("Floor Division: {} // {} = {}".format(a, b, a // b))


#creqte a bot 
#pip install python-telegram-bot
#pip3 install python-telegram-bot


#sudo apt update
#sudo apt install python3 python3-pip
#


#script for the bot 
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters

# Command handler for /start
async def start(update: Update, context):
    await update.message.reply_text("Hello! I'm your locally hosted bot. How can I help you?")

# Echo handler for text messages
async def echo(update: Update, context):
    user_message = update.message.text
    await update.message.reply_text(f"You said: {user_message}")

# Main function
def main():
    bot_token = "YOUR_BOT_TOKEN"  # Replace with your BotFather token
    app = ApplicationBuilder().token(bot_token).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, echo))

    print("Bot is running...")
    app.run_polling()

if __name__ == "__main__":
    main()
    main()
    
    
    
    
    
    
    
    
    
    
    
    
    ###########################################################################################################
    
    from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters
import logging

# Enable logging
logging.basicConfig(level=logging.INFO)

# Store user IDs (in memory for simplicity; use a database for production)
user_ids = set()

# Command to collect users from a group
async def collect_users(update: Update, context):
    chat_id = update.effective_chat.id
    user_id = update.effective_user.id

    # Check if the bot is in a group
    if update.effective_chat.type in ["group", "supergroup"]:
        user_ids.add(user_id)  # Add the user ID to the set
        logging.info(f"Added user {user_id} from group {chat_id}")
        await update.message.reply_text(f"User {user_id} has been recorded for private broadcasts.")
    else:
        await update.message.reply_text("This command works only in a group!")

# Command to broadcast a message to collected users
async def broadcast(update: Update, context):
    if not context.args:
        await update.message.reply_text("Usage: /broadcast <message>")
        return

    message = " ".join(context.args)

    # Send the message to each user in the list
    for user_id in user_ids:
        try:
            await context.bot.send_message(chat_id=user_id, text=message)
            logging.info(f"Message sent to user {user_id}")
        except Exception as e:
            logging.error(f"Failed to send message to {user_id}: {e}")

    await update.message.reply_text("Broadcast message sent!")

# Command to list stored user IDs (for admin use)
async def list_users(update: Update, context):
    if user_ids:
        await update.message.reply_text(f"Collected User IDs: {', '.join(map(str, user_ids))}")
    else:
        await update.message.reply_text("No users have been collected yet.")

# Main function
def main():
    bot_token = "YOUR_BOT_TOKEN"  # Replace with your BotFather token
    app = ApplicationBuilder().token(bot_token).build()

    # Handlers
    app.add_handler(CommandHandler("collect_users", collect_users))
    app.add_handler(CommandHandler("broadcast", broadcast))
    app.add_handler(CommandHandler("list_users", list_users))

    print("Bot is running...")
    app.run_polling()

if __name__ == "__main__":
    main()
    ########################################################################################