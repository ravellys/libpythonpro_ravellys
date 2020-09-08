import pytest

from libpythonpro_ravellys.spam.enviador_email import Enviar, EmailInvalido


def test_criar_enviador_de_email():
    enviador = Enviar()
    assert enviador is not None


@pytest.mark.parametrize(
    'remetente',
    ['lucas.ravellys@ufpe.br', 'ravellyspyrrho@gmail.com']
)
def test_remetente(remetente):
    enviador = Enviar()
    resultado = enviador.enviar(
        remetente=remetente,
        destinatario='ravellyspyrrho@gmail.com',
        assunto='novo email',
        corpo='corpo do novo email'
    )
    assert remetente in resultado


@pytest.mark.parametrize(
    'remetente',
    ['lucas.ravellys', ' ']
)
def test_remetente_invalido(remetente):
    enviador = Enviar()
    with pytest.raises(EmailInvalido):
        enviador.enviar(
            remetente=remetente,
            destinatario='ravellyspyrrho@gmail.com',
            assunto='novo email',
            corpo='corpo do novo email'
        )
