import pytest

@pytest.fixture()
def set_up():
    print("Start test session")
    yield
    print("Finish test session")
