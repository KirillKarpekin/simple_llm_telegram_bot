import os
import re
from html import escape
from dotenv import load_dotenv
from aiogram import Bot, Dispatcher, types
from aiogram.types import Message
from aiogram.utils.chat_action import ChatActionSender
from aiogram.filters import Command
from aiogram.enums import ParseMode

from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate

load_dotenv()


llm = ChatOpenAI(
    model="tngtech/deepseek-r1t2-chimera:free",
    api_key=os.getenv("OPENROUTER_API_KEY"),
    base_url="https://openrouter.ai/api/v1",
    temperature=0.7
)

prompt = ChatPromptTemplate.from_messages([
    ("system",
     "You are a helpful and polite assistant.\n"
     "Always respond in the same language as the user.\n"
     "Your answers must NOT contain any Markdown, formatting symbols or special characters.\n"
     "Write in clean, plain text only.\n"
     "\n"
     "Despite not using Markdown, your responses should be clear, well-structured and pleasant to read:\n"
     "- use short paragraphs\n"
     "- keep sentences concise\n"
     "- keep a friendly and warm tone\n"
     "- explain complex ideas simply\n"
     "- highlight important points with good phrasing instead of formatting\n"
     "\n"
     "Avoid emojis unless the user uses them first.\n"
     "Avoid any characters that could interfere with Telegram MarkdownV2.\n"
     "Your goal is to return beautiful, readable, human-friendly plain text messages."
    ),
    ("user", "{text}")
])


chain = prompt | llm


bot = Bot(token=os.getenv("TELEGRAM_BOT_TOKEN"))
dp = Dispatcher()


@dp.message(Command("start"))
async def start_cmd(message: Message):
    async with ChatActionSender.typing(bot=bot, chat_id=message.chat.id):
        await message.answer("Hi! message text!")

TELEGRAM_MD_V2_SPECIAL = r'_*\[\]()~`>#+\-=|{}.!'

def escape_markdown_v2(text: str):
    return re.sub(
        f'([{re.escape(TELEGRAM_MD_V2_SPECIAL)}])',
        r'\\\1',
        text
    )

@dp.message()
async def handle_message(message: Message):
    user_text = message.text

    async with ChatActionSender.typing(bot=bot, chat_id=message.chat.id):
        await asyncio.sleep(1)

        # Получаем ответ модели
        response = chain.invoke({"text": user_text})
        raw_reply = response.content

        # Полностью экранируем для MarkdownV2
        safe_reply = escape_markdown_v2(raw_reply)

        # Отправляем безопасный ответ
        await message.answer(
            safe_reply,
            parse_mode=ParseMode.MARKDOWN_V2
        )



async def main():
    print("Bot is running (aiogram)...")
    await dp.start_polling(bot)


if __name__ == "__main__":
    import asyncio
    asyncio.run(main())
