import pytest
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import Session

from src.meuprojfastapi.meuapp import meuapp
from src.meuprojfastapi.models import table_registry


@pytest.fixture
def client():
    return TestClient(meuapp)


@pytest.fixture
def session():
    engine = create_engine('sqlite:///:memory:', echo=True)
    table_registry.metadata.create_all(engine)

    with Session(engine) as session:
        yield session

    table_registry.metadata.drop_all(engine)
