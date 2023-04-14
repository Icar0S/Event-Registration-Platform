# Event-Registration-Platform
projeto realizado pela pythonando na pystackweek 

### Conceitos
![Cliente_servidor](https://user-images.githubusercontent.com/39846852/232044613-fd83b8da-c9e8-435c-8983-7552c4169ab2.png)

Fluxo de dados no Django:
![diagrama_fluxo](https://user-images.githubusercontent.com/39846852/232044653-0bda3a30-cdb7-4288-9cdf-289f964ccba5.png)


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
```jsx
path('usuarios/', include('usuarios.urls')),
```
