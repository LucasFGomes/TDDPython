from leilao.dominio import Usuario, Lance, Leilao, Avaliador

usuario1 = Usuario('Lucas')
usuario2 = Usuario('João')

lance_usuario1 = Lance(usuario1, 100.0)
lance_usuario2 = Lance(usuario2, 150.0)

leilao = Leilao('Leilão de Celular')

leilao.lances.append(lance_usuario1)
leilao.lances.append(lance_usuario2)

avaliador = Avaliador()
avaliador.avalia(leilao)

print(f'O menor lance foi {avaliador.menor_lance} e o maior foi {avaliador.maior_lance}')
