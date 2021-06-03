from unittest import TestCase

from leilao.dominio import Usuario, Lance, Leilao
from leilao.excecoes import LanceInvalido


class TestLeilao(TestCase):

    def setUp(self) -> None:
        self.usuario1 = Usuario('Lucas', 500.0)
        self.lance_usuario1 = Lance(self.usuario1, 100.0)
        self.leilao = Leilao('Leilão de Celular')


    def test_deve_retornar_o_maior_e_o_menor_valor_de_um_lance_quando_adicionados_em_ordem_crescente(self):
        usuario2 = Usuario('João', 500.0)

        lance_usuario2 = Lance(usuario2, 150.0)

        self.leilao.propoe(self.lance_usuario1)
        self.leilao.propoe(lance_usuario2)

        self.assertEqual(100.0, self.leilao.menor_lance)
        self.assertEqual(150.0, self.leilao.maior_lance)


    def test_nao_deve_permitir_propor_um_lance_em_ordem_decrescente(self):

        with self.assertRaises(LanceInvalido):
            usuario2 = Usuario('João', 500.0)

            lance_usuario2 = Lance(usuario2, 150.0)

            self.leilao.propoe(lance_usuario2)
            self.leilao.propoe(self.lance_usuario1)


    def test_deve_retornar_o_mesmo_valor_quando_o_leilao_tiver_um_lance(self):
        lance_usuario1 = Lance(self.usuario1, 100.0)

        self.leilao.propoe(lance_usuario1)

        self.assertEqual(100.0, self.leilao.menor_lance)
        self.assertEqual(100.0, self.leilao.maior_lance)


    def test_deve_retornar_o_maior_e_o_menor_valor_quando_o_leilao_tiver_tres_lances(self):
        usuario2 = Usuario('João', 500.0)
        usuario3 = Usuario('Maria', 500.0)

        lance_usuario2 = Lance(usuario2, 50.0)
        lance_usuario3 = Lance(usuario3, 250.0)

        self.leilao.propoe(lance_usuario2)
        self.leilao.propoe(self.lance_usuario1)
        self.leilao.propoe(lance_usuario3)

        self.assertEqual(50.0, self.leilao.menor_lance)
        self.assertEqual(250.0, self.leilao.maior_lance)


    def test_deve_permitir_propor_um_lance_caso_o_leilao_nao_tenha_um_lance(self):
        self.leilao.propoe(self.lance_usuario1)

        self.assertEqual(1, len(self.leilao.lances))


    def test_deve_permitir_propor_um_lance_caso_o_ultimo_usuario_seja_diferente(self):
        usuario2 = Usuario("Maria", 500.0)
        lance_usuario2 = Lance(usuario2, 300.0)

        self.leilao.propoe(self.lance_usuario1)
        self.leilao.propoe(lance_usuario2)

        self.assertEqual(2, len(self.leilao.lances))


    def test_nao_deve_permitir_propor_lance_caso_o_ultimo_usuario_seja_o_mesmo(self):
        novo_lance_usuario1 = Lance(self.usuario1, 500.0)

        with self.assertRaises(LanceInvalido):
            self.leilao.propoe(self.lance_usuario1)
            self.leilao.propoe(novo_lance_usuario1)

