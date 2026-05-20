1. Classe Usuário
Representa quem acessa o sistema.
Atributos: nome, e-mail, senha e cargo.
Métodos: login(), logout() e verificarPermissao().
Objeto: usuarioAdministrador.

2. Classe Medicamento
Representa os remédios cadastrados na farmácia.
Atributos: nome, código, preço, quantidade e validade.
Métodos: cadastrar(), editar(), excluir() e verificarValidade().
Objeto: medicamentoDipirona.

3. Classe Estoque
Controla a entrada e saída dos medicamentos.
Atributos: lista de produtos e quantidade total.
Métodos: atualizarEstoque(), verificarEstoqueBaixo() e reporProduto().
Objeto: estoquePrincipal.

4. Classe Venda
Representa uma venda realizada no sistema.
Atributos: cliente, produtos, data, forma de pagamento e valor total.
Métodos: registrarVenda(), calcularTotal() e finalizarVenda().
Objeto: venda001.

5. Classe Cliente
Representa o comprador da farmácia.
Atributos: nome, CPF, telefone e histórico de compras.
Métodos: cadastrarCliente(), editarCliente() e buscarHistorico().
Objeto: clienteJoao.

6. Classe Relatório
Gera informações sobre vendas e estoque.
Atributos: tipo de relatório, data inicial, data final e dados.
Métodos: gerarPDF(), gerarRelatorioVendas() e gerarRelatorioEstoque().
Objeto: relatorioMensal.

Resumo:
As classes ajudam a separar cada parte do sistema.
Os atributos guardam os dados.
Os métodos representam as ações.
Os objetos são exemplos reais criados a partir das classes.
