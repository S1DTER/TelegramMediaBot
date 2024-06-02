from aiogram import Router, F
from aiogram.filters import CommandStart
from aiogram.types import Message
from app.keyboards import kb, film_kb, seral_kb, starwars_kb

router = Router()


@router.message(CommandStart())
async def cmd_start(massage: Message):
    await massage.answer("Пошла работа", reply_markup=kb)


@router.message(F.text == 'Фильмы')
async def film(message: Message):
    await message.answer("Выбери фильм", reply_markup=film_kb)

@router.message(F.text == 'Звездные войны')
async def film(message: Message):
    await message.answer_photo(photo="AgACAgIAAxkBAAIB9WZcV2Zkuz4LwzILvZ6ZOknu3GVvAAJm3TEbo9PgSiI23TQbWStzAQADAgADeQADNQQ",
                               caption='Выбирай',
                               reply_markup=starwars_kb)

@router.message(F.text == 'Звездные Войны. Эпизод I')
async def video(message: Message):
    await message.answer_video(video='BAACAgIAAxkBAAIBu2ZcTIQLOT-d6MjdF-0WgBcDxszhAAJDRgACo9PgSk0AAUzDd2DIIjUE')
    await message.answer_video(video='BAACAgIAAxkBAAIBxWZcTfnX7W8oQTxeAX4DfraeTiwRAAKPRgACo9PgSuiy9beSmUVyNQQ',
                               caption='Звездные Войны. Эпизод I: Скрытая угроза')


@router.message(F.text == 'Сериалы')
async def serial(massage: Message):
    await massage.answer("Выбери сериал", reply_markup=seral_kb)


@router.message(F.video)
async def get_video(message: Message):
    await message.answer(f'ID VIDEO: {message.video.file_id}')

@router.message(F.photo)
async def get_photo(message: Message):
    await message.answer(f'ID PHOTO: {message.photo[-1].file_id}')