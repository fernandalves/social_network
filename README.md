# social_network
Projeto de web service, projeto com python 3.7 e django 2.1.
-------------------------------------------------------------------------------------------
# Como usar
para começar crie uma virtualenv

Exemplo:

```
virtualenv venv
```
ou
```
pipenv shell
```
caso a virtualenv não tenha sido iniciada automaticamente use;

```
source venv/bin/activate
```
ou
```
pipenv shell
```
agora digite o comando para baixar as dependências;

```
pip install -r requirements.txt
```
Caso queira iniciar o server faça um migrate e depois inicie o servidor como a seguir

```
python manage.py migrate

python manage.py runserver
```
abra o navegador e use o seguinte URL:


```
localhost:8000
```
ou
```
127.0.0.1:8000
```
