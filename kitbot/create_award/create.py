import asyncio
from PIL import Image, ImageDraw, ImageFont


async def main(user_name: str, user_id: int) -> str:
    image = Image.open("kitbot/create_award/sample.jpg")

    font = ImageFont.truetype(font="kitbot/create_award/NotoSans-Light.ttf", size=100, encoding="UTF-8")
    drawer = ImageDraw.Draw(image)
    drawer.text((1404, 1166), user_name, font=font, fill='black', anchor="mm")

    file_name = 'kitbot/create_award/' + str(user_id) + '.jpg'

    image.save(file_name)

    return file_name
