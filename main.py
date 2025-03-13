from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from fastapi.exceptions import RequestValidationError
from pydantic import BaseModel, field_validator
import re
from typing import Dict, List, Any

app = FastAPI()


class PasswordRequest(BaseModel):
    password: str
    
    @field_validator('password')
    def password_must_be_string(cls, v):
        if v is None or v == "":
            raise ValueError("A senha não pode ser vazia")
        if not isinstance(v, str):
            raise ValueError("A senha deve ser uma string")
        if len(v) > 1000: 
            raise ValueError("A senha não pode exceder 1000 caracteres")
        return v

def validate_password(password: str) -> Dict[str, Any]:
    """
    Validates a password against security rules
    
    Args:
        password: The password string to validate
        
    Returns:
        Dictionary containing validation results
    """
    rules = {
        "A senha deve ter pelo menos 8 caracteres.": len(password) >= 8,
        "A senha deve conter pelo menos uma letra maiúscula.": bool(re.search(r'[A-Z]', password)),
        "A senha deve conter pelo menos uma letra minúscula.": bool(re.search(r'[a-z]', password)),
        "A senha deve conter pelo menos um número.": bool(re.search(r'\d', password)),
        "A senha deve conter pelo menos um símbolo.": bool(re.search(r'[!@#$%^&*(),.?":{}|<>]', password))
    }
    
    regras_validas = []
    regras_invalidas = []
    
    for rule, passed in rules.items():
        if passed:
            regras_validas.append(rule)
        else:
            regras_invalidas.append(rule)
    
    senha_valida = len(regras_invalidas) == 0
    
    return {
        "senha_valida": senha_valida,
        "regras_validas": regras_validas,
        "regras_invalidas": regras_invalidas
    }


@app.exception_handler(RequestValidationError)
async def validation_exception_handler(request: Request, exc: RequestValidationError):
    # Extract the error details
    error = exc.errors()[0]
    
    return JSONResponse(
        status_code=400,
        content={
            "status_code": 400,
            "error_type": error["type"],
            "message": error["msg"]
        }
    )


@app.post("/validate-password")
async def validate_password_endpoint(request: PasswordRequest):
    return validate_password(request.password)