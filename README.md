# Guia

1. Instale o seguinte pacote `python-dotenv`:

```bash
pip install python-dotenv
```

2. Crie um arquivo `.env` na raiz do projeto e coloque os seguintes dados:

```bash
NAME=SEU_PRIMEIRO_NOME
EMAIL=SEU_EMAIL
PASSWORD=SUA_SENHA
```
3. Adicione todos os nomes e emails dos receptores da seguinte forma no arquivo `data_contacts.csv`:

```
Name,name@domain.com
Name2,name2@domain.com
```

4. Enumere os arquivos de 1 até n, em que n é a quantidade de pessoas que receberão os emails.
Ex.:
```
attachs/
1.pdf ou 1.jpg ou 1.png
...
20.pdf ou 20.jpg ou 20.png
```

NOTA: renomeie a linha 52 com a extensão do arquivo a ser enviado.

5. Execute o programa com `python main.py` e aguarde até que todos os emails sejam enviados.

NOTA: você deve permitir no próprio GMAIL o login por "Fontes desconfiáveis".
