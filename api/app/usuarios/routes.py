from fastapi import APIRouter, Form
from fastapi.responses import JSONResponse

router = APIRouter()

usuarios_cadastrados = []

@router.post("/cadastro")
async def cadastro_usuario(
    nome: str = Form(...),
    email: str = Form(...),
    senha: str = Form(...)
):
    for usuario in usuarios_cadastrados:
        if usuario["email"] == email:
            return JSONResponse(
                status_code=400,
                content={"erro": "Usuário com este e-mail já cadastrado."},
            )
    usuarios_cadastrados.append({"nome": nome, "email": email, "senha": senha})
    return {"mensagem": f"Usuário '{nome}' cadastrado com sucesso!"}

@router.post("/login")
async def login_usuario(
    email: str = Form(...),
    senha: str = Form(...)
):
    for usuario in usuarios_cadastrados:
        if usuario["email"] == email and usuario["senha"] == senha:
            return {"mensagem": f"Login bem-sucedido! Bem-vindo, {usuario['nome']}."}

    return JSONResponse(
        status_code=401,
        content={"erro": "Credenciais inválidas. Verifique e tente novamente."}
    )
