from fastapi import FastAPI, Path
from typing import Annotated

#Создайте приложение(объект) FastAPI предварительно импортировав класс для него.
app = FastAPI()

#Создайте маршрут к главной странице - "/". По нему должно выводиться сообщение "Главная страница".
@app.get("/")
async def home():
    return "Главная страница"

#Создайте маршрут к странице администратора - "/user/admin". По нему должно выводиться сообщение "Вы вошли как администратор".
@app.get("/user/admin")
async def admin():
    return "Вы вошли как администратор"

#Создайте маршрут к страницам пользователей используя параметр в пути - "/user/{user_id}". По нему должно выводиться сообщение "Вы вошли как пользователь № <user_id>".
@app.get("/user/{user_id}")
async def users(
        user_id: Annotated[int, Path(..., ge=1,le=100, description="Enter User ID", example='1')]
):
    return f"Вы вошли как пользователь № {user_id}"

#Создайте маршрут к страницам пользователей передавая данные в адресной строке - "/user". По нему должно выводиться сообщение "Информация о пользователе. Имя: <username>, Возраст: <age>".
@app.get("/user/{username}/{age}'")
async def us_message(
        username: Annotated[str, Path(..., min_length=5, max_length=20, description="Enter username", example='UrbanUser')],
        age: Annotated[int, Path(..., ge=18, le=120, description="Enter age", example='24')]
):
    return f"Информация о пользователе. Имя: {username}, Возраст: {age}"


#uvicorn module_16_1:app --reload