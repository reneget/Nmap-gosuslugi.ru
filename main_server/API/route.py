from fastapi import APIRouter, status, HTTPException

server_router = APIRouter(
    '/server',
    tags=['server']
)

@server_router.post('/chek/password')
async def check_password():