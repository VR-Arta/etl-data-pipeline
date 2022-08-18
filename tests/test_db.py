import pytest
from scripts.db_postgres import engine

def test_db_connection():
    assert engine is not None
