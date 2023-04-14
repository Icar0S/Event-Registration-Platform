# Event-Registration-Platform
projeto realizado pela pythonando na pystackweek 

### Conceitos
![Cliente servidor.png](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/c6076cc0-2d69-4c17-9b9f-f2a51d2ddb24/Cliente_servidor.png)

Fluxo de dados no Django:
![Arquitetura.png](image.png)



### Configurações iniciais

Primeiro devemos criar o ambiente virtual:

```python
# Criar
	# Linux
		python3 -m venv venv
	# Windows
		python -m venv venv
```

Após a criação do venv vamos ativa-lo:

```python
#Ativar
	# Linux
		source venv/bin/activate
	# Windows
		venv\Scripts\Activate

# Caso algum comando retorne um erro de permissão execute o código e tente novamente:

Set-ExecutionPolicy -Scope CurrentUser -ExecutionPolicy RemoteSigned
```

Agora vamos fazer a instalação do Django e as demais bibliotecas:

```python
pip install django
pip install pillow
```

Vamos criar o nosso projeto Django:

```jsx
django-admin startproject type_event .
```

Crie o app usuarios:

## Instale o APP!

```jsx
python3 manage.py startapp usuarios
```

Crie uma URL para o APP usuarios: