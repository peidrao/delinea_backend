# Delinea Backend

## Acessar o  [link](https://delinea.herokuapp.com/).

## Swagger

O usuário pode criar um novo usuário ou utilizar um usuário de teste.

Para a primeira opção basta acessar o edpoint 

[POST] /authentication/users

> username: test

> password: tecarch123


## Insomnia/Postman

Para fazer as requisições a partir do Insomnia ou Postman foi deixado dentro do projeto os arquivos com todas as requisições. 

**Postman**: Delinea.postman_collection.json

**Insomnia**: Insomnia_2021-12-12.json

## Requisições

**Usuário**

> [POST]: Login User

> [POST]: Create User


**Produtos**

> [POST]: Create Product

> [PATCH]: Update Product by ID

> [DELETE]: Destroy Product by ID

> [GET]: All Products

> [GET]: Product by ID

> [GET]: Product by Title [query-params]

> [GET]: Product by Price [query-params]

