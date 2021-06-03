import pytest
from leilao.dominio import Usuario, Leilao
from leilao.excecoes import LanceInvalido


@pytest.fixture
def usuario():
    return Usuario("Roberto", 100.0)


@pytest.fixture
def leilao():
    return Leilao("Leilão de Carros")


def test_deve_subtrair_valor_da_carteira_do_usuario_quando_este_propor_um_lance(usuario, leilao):
    usuario.propoe_lance(leilao, 50.0)

    assert usuario.carteira == 50.0

def test_deve_permitir_propor_lance_quando_o_valor_eh_menor_que_o_valor_da_carteira(usuario, leilao):
    usuario.propoe_lance(leilao, 50.0)

    assert usuario.carteira == 50.0

def test_deve_permitir_propor_lance_quando_o_valor_eh_igual_ao_da_carteira(usuario, leilao):
    usuario.propoe_lance(leilao, 100.0)

    assert usuario.carteira == 0.0

def test_nao_deve_permitir_propor_um_lance_quando_o_valor_eh_maior_que_o_da_carteira(usuario, leilao):

    with pytest.raises(LanceInvalido):
        usuario.propoe_lance(leilao, 200.0)
