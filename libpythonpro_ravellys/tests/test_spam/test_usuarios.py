from libpythonpro_ravellys.spam.modelos import Usuario


def test_salvar_usuario(sessao):
    usuario = Usuario(nome='renzo', email='renzo@pythopro.br')
    sessao.salvar(usuario)
    assert isinstance(usuario.id, int)


def test_listar_usuarios(sessao):
    usuarios = [Usuario(nome='renzo', email='renzo@pythopro.br'),
                Usuario(nome='luciano', email='luciano@pythopro.br')]
    for usuario in usuarios:
        sessao.salvar(usuario)
    assert sessao.listar() == usuarios
