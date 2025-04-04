from http import HTTPStatus


def test_read_root_deve_reotornar_ok_e_hello_world(client):
    # client = TestClient(meuapp)  # arrange (organizacao)
    reponse = client.get('/')  # act (acao)
    assert reponse.status_code == HTTPStatus.OK  # assert (afirmacao)
    assert reponse.json() == {
        'message': 'Hello World of FastAPI'
    }  # assert (afirmacao)


def test_create_user(client):
    # client = TestClient(meuapp)
    reponse = client.post(
        '/users/',
        json={
            'username': 'jose',
            'email': 'jose@me.com',
            'password': '12345678',
        },
    )
    assert reponse.status_code == HTTPStatus.CREATED
    assert reponse.json() == {
        'id': 1,
        'username': 'jose',
        'email': 'jose@me.com',
    }

    def test_read_users(client):
        reponse = client.get('/users/')
        assert reponse.status_code == HTTPStatus.OK
        assert reponse.json() == {
            'users': [
                {
                    'id': 1,
                    'username': 'jose',
                    'email': 'jose@me.com',
                }
            ]
        }
