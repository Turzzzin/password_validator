# Password Validator  
A simple API to validate passwords based on predefined security rules.  

## Rodar o programa local
### Pré-requisitos
1. Ter o `Python` instalado e configurado
2. Ter o `git` instalado e configurado

### 1. Clone ou Baixe o Repositório  
Se você ainda não clonou o repositório, execute:  

```powershell
git clone https://github.com/Turzzzin/password_validator.git
```  
Ou faça o download do código-fonte manualmente e extraia os arquivos.  

### 2. Acesse o Diretório do Projeto  
Abra o terminal e navegue até a pasta do projeto:  

```powershell
cd password_validator
```  

### 3. Crie e Ative um Ambiente Virtual  

Crie um ambiente virtual para isolar as dependências do projeto:  

```powershell
python -m venv venv
```  

Ative o ambiente virtual (Windows):  

```powershell
./venv/Scripts/activate
```  

Para macOS/Linux:  

```bash
source venv/bin/activate
```  

### 4. Instale as Dependências  
Instale os pacotes necessários:  

```powershell
pip install -r requirements.txt
```  

### 5. Inicie o Servidor  
Execute o Uvicorn para iniciar a API:  

```powershell
uvicorn main:app --reload
```  

### 6. Teste a API  
Abra seu navegador e acesse a interface interativa da API:  

[http://localhost:8000/docs](http://localhost:8000/docs)  

- Encontre a rota `/validate-password`  
- Clique em **"Try it out"**  
- Insira diferentes valores para testar a validação de senha  

📌 **Dica:** Modifique o valor do campo `"string"` e veja se sua senha atende às regras!  
