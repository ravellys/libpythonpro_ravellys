from unittest.mock import Mock
import pytest
from libpythonpro_ravellys.spam.main import EnviadorDeSpam
from libpythonpro_ravellys.spam.modelos import Usuario


@pytest.mark.parametrize(
    'usuarios',
    [
        [Usuario(nome='renzo', email='renzo@pythopro.br'),
         Usuario(nome='luciano', email='luciano@pythopro.br')],
        [Usuario(nome='renzo', email='renzo@pythopro.br')]
    ])
def test_qtd_de_spam(sessao, usuarios):
    for usuario in usuarios:
        sessao.salvar(usuario)
    enviador = Mock()
    enviador_de_spam = EnviadorDeSpam(sessao, enviador)
    enviador_de_spam.enviar_spam(
        remetente='lucas.ravellys@ufpe.br',
        assunto="envio de spam",
        corpo="envio de spam"
    )
    assert len(usuarios) == enviador.enviar.call_count


def test_parametros_de_spam(sessao):
    usuario = Usuario(nome='renzo', email='renzo@pythopro.br')
    sessao.salvar(usuario)
    enviador = Mock()
    enviador_de_spam = EnviadorDeSpam(sessao, enviador)
    enviador_de_spam.enviar_spam(
        remetente='lucas.ravellys@ufpe.br',
        assunto="envio de spam",
        corpo="envio de spam"
    )
    enviador.enviar.assert_called_once_with(
        'lucas.ravellys@ufpe.br',
        'renzo@pythopro.br',
        "envio de spam",
        "envio de spam"
    )
