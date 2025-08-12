from st7789 import ST7789 as Screen, BG_SPI_CS_FRONT

screen = Screen(
    height=240,
    rotation=180,
    port=1,
    cs=0,
    dc=19,
    spi_speed_hz=40 * 1000 * 1000,
    offset_left=0,
    offset_top=0,
)