from http import HTTPStatus

from fastapi.testclient import TestClient

from src.meuprojfastapi.meuapp import meuapp

client = TestClient(meuapp)


def test_read_root_deve_reotornar_ok_e_hello_world():
    client = TestClient(meuapp)  # arrange (organizacao)
    reponse = client.get('/')  # act (acao)
    assert reponse.status_code == HTTPStatus.OK  # assert (afirmacao)
    assert reponse.json() == {
        'message': 'Hello World of FastAPI'
    }  # assert (afirmacao)
