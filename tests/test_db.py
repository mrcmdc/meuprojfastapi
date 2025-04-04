from sqlalchemy import select

from meuprojfastapi.models import User


def test_create_user(session):
    user = User(username='jose', email='jose@me.com', password='12345678')
    session.add(user)
    session.commit()

    result = session.scalar(select(User).where(User.email == 'jose@me.com'))

    assert result.username == 'jose'
