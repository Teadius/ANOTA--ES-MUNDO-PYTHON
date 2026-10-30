# Para acessar um banco de dados o usuario precisa passar por uma cadeia de permissoes

# usuario -> modulo sqlite3 por exemplo -> conexão -> cursor -> banco de dados

"""   Resumo do youtube
Esta aula aborda as **boas práticas para acessar bancos de dados SQLite** utilizando Python, focando em eficiência, segurança e organização. Abaixo estão os pontos principais da teoria:

**Fundamentos do Acesso a Dados (03:25 - 05:41):**

*   **Conexão (`connection`):** É o objeto que estabelece a ponte entre o seu código Python e o arquivo do banco de dados (ex: `meubanco.db`).
*   **Cursor (`cursor`):** É o objeto necessário para navegar, executar comandos SQL e recuperar os dados da tabela.

**Técnicas de Consulta e Memória (09:15 - 14:45):**

*   **`fetchall()`:** Busca todos os registros de uma vez e os carrega na memória RAM. É útil para tabelas pequenas, mas pode causar estouro de memória em bases grandes.
*   **`fetchone()` / `for`:** A técnica recomendada é percorrer o cursor com um laço `for` ou usar `fetchone()`. Isso garante que apenas um registro por vez ocupe a memória, otimizando o consumo de recursos.

**Organização com `sqlite3.Row` (17:09 - 18:38):**

*   Ao configurar o `row_factory` como `sqlite3.Row`, o acesso aos dados dentro da tupla deixa de depender apenas do índice numérico (ex: `amigo[0]`) e passa a ser feito pelos **nomes das colunas** (ex: `amigo['nome']`), tornando o código muito mais legível.

**Segurança e Boas Práticas (18:38 - 24:34):**

*   **Gerenciamento de Recursos (`with`):** A utilização do comando `with` garante que a conexão e o cursor sejam fechados automaticamente ao finalizar o bloco de código, evitando vazamento de memória.
*   **Tratamento de Erros (`try-except`):** Envolver as operações de banco em blocos `try` permite capturar falhas específicas, como erros de sintaxe SQL ou problemas no acesso ao arquivo, garantindo que o programa não pare inesperadamente.
*   **Prevenção contra SQL Injection (27:49 - 30:02):** Nunca concatene variáveis de busca diretamente na string SQL. Utilize **parâmetros** (representados por interrogações `?`) para separar o comando SQL dos dados do usuário, prevenindo ataques maliciosos.
"""