from fastapi import FastAPI, Request, Response, Form, Depends, HTTPException, status
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.staticfiles import StaticFiles
from fastapi.routing import APIRouter
import jwt
import logging

from .pydantic import UserProperties
from functions import Password, Database

server_router = APIRouter(
    prefix='/server',
    tags=['server']
)
templates = Jinja2Templates(directory="front")

server_logger = logging.getLogger(__name__)

# Секретный ключ для JWT (замените на свой безопасный ключ в продакшене)
SECRET_KEY = "your_secret_key_here"  # Используйте os.environ для безопасности
ALGORITHM = "HS256"

# Хардкод credentials для примера (в реальности используйте БД или хэшированные пароли)
ADMIN_USERNAME = "admin"
ADMIN_PASSWORD = "password"  # В реальности хэшируйте с bcrypt или аналогом


@server_router.post('/chek/password')
async def operation_emulation(user_properties: UserProperties):
    try:
        server_logger.info('Password verification request')

        # params
        user_id = user_properties.user_id
        unique_key = user_properties.key
        entropy = user_properties.entropy

        server_logger.info('Getting parameters for generation')
        properties = Database.get_user_key_properties(user_id)
        secret_key, is_active = properties['secret_key'], properties['is_active']

        if is_active is None:
            return False

        server_logger.info('Parameters received')

        gen_key = Password.generated_new_key(secret_key, entropy)
        server_logger.info('Generate a key to check against the reader key')

        check_keys = Password.key_verification(unique_key, gen_key[0])
        server_logger.info(f'status={check_keys}')

        return check_keys
    except Exception:
        server_logger.error('Error checking key', exc_info=True)


# Ваш существующий код (с исправлением имени функции для /admin)
@server_router.get('/admin/login', response_class=HTMLResponse)
async def login_page(request: Request):
    return templates.TemplateResponse("admin_login.html", {"request": request})


@server_router.get('/admin', response_class=HTMLResponse)
async def admin_panel(request: Request):
    token = request.cookies.get("access_token")
    if not token:
        return RedirectResponse(url="/admin/login", status_code=status.HTTP_303_SEE_OTHER)

    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username: str = payload.get("sub")
        if username != ADMIN_USERNAME:
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid authentication")
    except jwt.PyJWTError:
        return RedirectResponse(url="/admin/login", status_code=status.HTTP_303_SEE_OTHER)

    return templates.TemplateResponse("admin_panel.html", {"request": request})


# # Новый POST-роут для обработки формы логина
# @server_router.post('/admin/login')
# async def login(response: Response, username: str = Form(...), password: str = Form(...)):
#     if username != ADMIN_USERNAME or password != ADMIN_PASSWORD:
#         raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Incorrect username or password")
#
#     # Создаем JWT токен
#     access_token = jwt.encode({"sub": username}, SECRET_KEY, algorithm=ALGORITHM)
#
#     # Устанавливаем куки (httponly для безопасности, чтобы JS не имел доступа)
#     response.set_cookie(
#         key="access_token",
#         value=access_token,
#         httponly=True,
#         secure=False,  # В продакшене True для HTTPS
#         samesite="lax",
#         max_age=3600  # 1 час, настройте по нужде
#     )
#
#     return RedirectResponse(url="/admin", status_code=status.HTTP_303_SEE_OTHER)

@server_router.get("/admin/login", response_class=HTMLResponse)
async def admin_login(request: Request):
    return templates.TemplateResponse("admin_login.html", {"request": request})