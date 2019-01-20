import pytest
from colorthief import ColorThief


@pytest.fixture(scope='function')
def sunset():
    color_thief = ColorThief('images/sunset.jpg')
    yield color_thief
    color_thief.image.close()
