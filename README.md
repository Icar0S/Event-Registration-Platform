# Event-Registration-Platform
projeto realizado no curso da pythonando na pystackweek 

![tela1](https://user-images.githubusercontent.com/39846852/232151165-7a8308b1-efab-4d56-8b5f-bc7d0b2db235.png)
![tela2](https://user-images.githubusercontent.com/39846852/232151188-2c49b53e-f607-43b4-95b5-c4e344655cc6.png)
![tela3](https://user-images.githubusercontent.com/39846852/232151204-34c76d89-1fd5-408c-8ca3-2e56ac9e5597.png)
![tela4](https://user-images.githubusercontent.com/39846852/232151220-de563a96-961e-42e7-9ada-222ee4789e4a.png)
![tela5](https://user-images.githubusercontent.com/39846852/232151221-4e46adb6-c9b4-49a5-9869-a8c96699af6b.png)
![tela6](https://user-images.githubusercontent.com/39846852/232151224-f541a0af-5831-4912-8774-fefa04d62885.png)
![tela7](https://user-images.githubusercontent.com/39846852/232151228-f5547515-b1dd-4b0c-b7c9-7e83e585b592.png)


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
