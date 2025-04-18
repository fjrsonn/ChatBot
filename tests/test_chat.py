from core.chat import get_response

def test_get_response():
    resposta = get_response("oi")
    assert isinstance(resposta, str)
    assert len(resposta) > 0
