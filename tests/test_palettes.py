import pytest
from colorthief import ColorThief


@pytest.mark.sunsetimage
def test_get_palette_sunset_quality_10_count_5():
    imgpath = 'images/sunset.jpg'
    color_thief = ColorThief(imgpath)
    palette = color_thief.get_palette(quality=10, color_count=5)
    expected = [
        (163, 143, 178),
        (9, 6, 5),
        (99, 36, 32),
        (246, 222, 171),
        (153, 83, 63)
    ]
    assert palette == expected

def test_get_palette_sunset_quality_10_count_4():
    imgpath = 'images/sunset.jpg'
    color_thief = ColorThief(imgpath)
    palette = color_thief.get_palette(quality=10, color_count=4)
    expected = [
        (164, 144, 178),
        (9, 6, 5),
        (99, 35, 32),
        (153, 83, 63),
    ]
    assert palette == expected


def test_get_palette_sunset_quality_10_count_3(sunset):
    palette = sunset.get_palette(quality=10, color_count=3)
    expected = [
        (164, 144, 178),
        (9, 6, 5),
        (99, 36, 32),
    ]
    assert palette == expected


def test_get_palette_sunset_quality_10_count_2(sunset):
    imgpath = 'images/sunset.jpg'
    color_thief = ColorThief(imgpath)
    palette = color_thief.get_palette(quality=10, color_count=2)
    expected = [
        (164, 144, 177),
        (9, 6, 5),
    ]
    assert palette == expected


def test_get_palette_sunset_quality_10_count_1():
    imgpath = 'images/sunset.jpg'
    color_thief = ColorThief(imgpath)
    palette = color_thief.get_palette(quality=10, color_count=1)
    expected = [
        (163, 143, 178),
    ]
    assert palette == expected


@pytest.mark.xfail()
def test_get_palette_count_10():
    imgpath = 'images/sunset.jpg'
    color_thief = ColorThief(imgpath)
    palette = color_thief.get_palette(quality=10, color_count=10)
    assert len(palette) == 10


@pytest.mark.sunsetimage
@pytest.mark.parametrize(('quality', 'expected_count'), [
    (1, 5),
    (2, 5),
    (3, 5),
    (4, 5),
    (5, 5),
    (6, 5),
    (7, 5),
    (8, 5),
    (9, 5),
    (10, 5),
])
def test_get_palette_count(quality, expected_count):
    imgpath = 'images/sunset.jpg'
    color_thief = ColorThief(imgpath)
    palette = color_thief.get_palette(quality=quality, color_count=5)
    assert len(palette) == expected_count