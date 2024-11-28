# import requests
# from openai import OpenAI
# client = OpenAI(api_key="g4a-R7lPsl3DlptnKbPQjYNfTHBMUc7uE9OqCad", base_url="https://api.gpt4-all.xyz/v1")
# token="7804862190:AAFm9kLfALUhpSe2jurdrcSwUfrzFZ6-Hfc"
# url=f"https://api.telegram.org/bot{token}/getUpdates"
# data=requests.get(url)
# print(data.text)
# print("json",data.json())
# receiver=[]
# updates=data.json()
# messages=len(updates["result"])
# print("\n",messages)
# # print(updates)
# for i in range(len(updates["result"])):
#   message_id=updates["result"][0]["message"]["message_id"]
#   ID=updates["result"][0]["message"]["from"]["id"]
#   firstname=updates["result"][i]["message"]["from"]["first_name"]
#   username=updates["result"][i]["message"]["from"]["username"]
#   text=updates["result"][i]["message"]["text"]
#   print(ID,firstname,username,text)
#   prompt =text

#   response2 = client.chat.completions.create(
#             model="gpt-4o-mini",
#             messages=[{"role": "user", "content":prompt}],
#             stream=False,
#         )
#   receiver.append(ID)


# for i in list(set(receiver)):
#   send_url=url=f"https://api.telegram.org/bot{token}/sendMessage"
#   chat_id=i
#   message="سلام به ربات ما خوش آمدید!"
#   response={"chat_id":chat_id,"text":response2.choices[0].message.content}
#   data=requests.post(send_url,response)


# seconone
# from openai import OpenAI
# from telegram import Update
# from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, ContextTypes
# import telegram.ext.filters as Filters


# import requests
# import openai
# openai.api_key = "g4a-R7lPsl3DlptnKbPQjYNfTHBMUc7uE9OqCad"
# openai.api_base = "https://api.gpt4-all.xyz/v1"
# async def hello(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None: 
#     await update.message.reply_text(f'Hello {update.effective_user.first_name}. How are you?')
# async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None: 
#     user_message = update.message.text
#     response2= openai.ChatCompletion.create(
#             model="gpt-4o-mini",
#             messages=[{"role": "user", "content":user_message}],
#             stream=False,
#         )
#     bot_reply = response2['choices'][0]['message']['content']
#     await update.message.reply_text(bot_reply)


# app = ApplicationBuilder().token("7804862190:AAFm9kLfALUhpSe2jurdrcSwUfrzFZ6-Hfc").build()
# app.add_handler(CommandHandler("start", hello))
# app.add_handler(MessageHandler(Filters.Text() & ~Filters.COMMAND, handle_message))
# app.run_polling()
# with python-telegram-bot
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, ContextTypes
import telegram.ext.filters as filters
import openai

# تنظیمات OpenAI
openai.api_key = "g4a-R7lPsl3DlptnKbPQjYNfTHBMUc7uE9OqCad"
openai.api_base = "https://api.gpt4-all.xyz/v1"

async def hello(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(f'Hello {update.effective_user.first_name}. How are you?')

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    user_message = update.message.text
    
    # ارسال پیام به API و دریافت پاسخ
    response2 = openai.ChatCompletion.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": user_message}],
        stream=False,
    )

    bot_reply = response2['choices'][0]['message']['content']

    # ارسال پاسخ به کاربر
    await update.message.reply_text(bot_reply)

app = ApplicationBuilder().token("7804862190:AAFm9kLfALUhpSe2jurdrcSwUfrzFZ6-Hfc").build()

app.add_handler(CommandHandler("start", hello))
app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))
app.run_polling()
