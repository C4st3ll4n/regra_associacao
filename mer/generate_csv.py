import pymysql

conexao = pymysql.connect(host='localhost', user='root', password='', db='mercado')

cursorVendas = conexao.cursor()
cursorVendaProduto = conexao.cursor()
cursorProduto = conexao.cursor()

cursorVendas.execute("select * from vendas")
transacoes = ''

for vendas in cursorVendas:
    quantidade = cursorVendaProduto.execute(f"select pd.nome from venda_produtos vp inner join produtos pd on vp.idproduto = "
                               f"pd.idproduto where idvenda like {vendas[0]}")
    produtos = ''

    i = 1
    for venda_produto in cursorVendaProduto:
        if i == quantidade:
            produtos = produtos + venda_produto[0]
        else:
            produtos = produtos + venda_produto[0] + ','

        i+=1

    transacoes = transacoes + produtos + '\n'


cursorVendas.close()
conexao.close()

print(transacoes)
with open('mercado.csv', 'w') as arquivo:
    arquivo.write(transacoes)
    arquivo.close()