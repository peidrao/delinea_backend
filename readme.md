# :books: Delinea Backend

## [Link da aplicação](https://delinea.herokuapp.com/)

## :ledger: Swagger

O usuário pode criar um novo usuário ou utilizar um usuário de teste.

Para a primeira opção basta acessar o edpoint 

[POST] /authentication/users

> username: test

> password: tecarch123


## :mag_right: Insomnia/Postman

Para fazer as requisições a partir do Insomnia ou Postman foi deixado dentro do projeto os arquivos com todas as requisições. 

Ao utilizar as requisições de produtos é necessário ter o token, na qual é obito no **access_token**, através do login

```
{
  "access_token": "Wp9r80LrRtSYaX838w6xF4nFaLUnYo",
  "expires_in": 36000,
  "token_type": "Bearer",
  "scope": "read write groups",
  "refresh_token": "xQV5tQyKwmxOdZeidY84cvUKdKuDUc"
}
```


**Postman**: Delinea.postman_collection.json

**Insomnia**: Insomnia_2021-12-12.json


## :round_pushpin: Requisições

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



## :ballot_box_with_check: O que foi feito?

### Requisitos funcionais

- [x] RF001: Ser capaz de criar um produto

- [x] RF002: Ser capaz de editar um produto

- [x] RF004: Ser capaz de listar um ou mais produtos


### Requisitos não funcionais

- [x] RN001: Somente o owner deve poder editar/deletar/listar seus produtos.

- [x] RN002: Não deve ser possível alterar os campos owner e created_datetime depois que o produto estiver criado.

- [x] RN003: Implementar filtros via query-param para que seja possível refinar a busca (GET) utilizando os campos title e price.

- [x] RN004: Documentar a API de forma que alguém consiga utilizá-la sem mais instruções. (readme ou swagger)

- [x] RN005: Implementar testes para os serviços desenvolvidos.

- [x] RN006: Fazer o deploy do seu código em um servidor (Heroku, AWS) para que seja testável.