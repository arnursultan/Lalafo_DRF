from django.shortcuts import render
from django.conf import settings
from aiogram import Bot, Dispatcher, types, executor
from asgiref.sync import sync_to_async
from logging import basicConfig, INFO

from apps.telegram.models import TelegramUser
from apps.telegram.keyboards import inline
from apps.posts.models import Post

# Create your views here.
bot = Bot(settings.TELEGRAM_BOT_TOKEN)
dp = Dispatcher(bot)
basicConfig(level=INFO)

@dp.message_handler(commands='start')
async def start(message:types.Message):
    user = await sync_to_async(TelegramUser.objects.get_or_create)(
        id_user=message.from_user.id,
        username=message.from_user.username,
        first_name=message.from_user.first_name,
        last_name=message.from_user.last_name,
        chat_id=message.chat.id
    )
    await message.answer(f"Привет {message.from_user.full_name}")

async def send_message(chat_id:int, message:str):
    await bot.send_message(chat_id, message, reply_markup=inline)

@dp.callback_query_handler(lambda call: call)
async def all_inline(call:types.Message):
    if call.data == "accept":
        await check_post(call, 'accept')
    elif call.data == "refuse":
        await check_post(call, 'refuse')

async def check_post(call:types.Message, type:str):
    post_id = call['message']['text'].split()[3]
    post = await sync_to_async(Post.objects.get)(id=int(post_id))
    await call.answer("OK")
    if type == "accept":
        print('accept')
        post.is_checked=True 
        await sync_to_async(post.save)()
    elif type == "refuse":
        print('delete')
        await sync_to_async(post.delete)()
    await bot.delete_message(call['message']['chat']['id'], call['message']['message_id'])