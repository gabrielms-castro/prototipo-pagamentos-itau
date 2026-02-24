# Itaú Use Rede

Prototipação de uma SDK para a API e.Rede do Itaú.

Foi utilizado o repositório [original](https://github.com/DevelopersRede/erede-python/tree/master) como inspiração.

Este protótipo é basicamente uma refatoração/atualização com uma versão mais atual do Python e de novas funcionalidades do e.Rede (por exemplo, OAUTH2.0 para autenticação)

## Sandbox
 * [Cartões](https://developer.userede.com.br/e-rede#tutorial-sandbox-cartoes)


### [Autenticação](https://developer.userede.com.br/e-rede#autenticacao-autorizacao-rede-apis)

### [Captura](https://developer.userede.com.br/e-rede#documentacao-captura)
Ao realizar uma autorização, é necessária a confirmação desta transação (captura). Nesse momento é gerada a cobrança na fatura do portador do cartão.
```sh
PUT: /v2/transactions/{tid}
```
