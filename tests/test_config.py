import pytest

from src import config


class TestSettings:
    @classmethod
    def setup_class(cls):
        cls.default_settings = config.Settings()

    def test_default_board_size_type(self):
        assert isinstance(self.default_settings.board_rows_number, int)
        assert isinstance(self.default_settings.board_columns_number, int)

    def test_default_boxes_number_type(self):
        assert isinstance(self.default_settings.get_number_of_boxes, int)

    def test_default_window_title_type(self):
        assert isinstance(self.default_settings.window_title, str)

    def test_default_window_color_type(self):
        assert isinstance(self.default_settings.window_color, str)

    def test_default_token_colors_type(self):
        assert isinstance(self.default_settings.token_colors, tuple)

    def test_default_board_color_type(self):
        assert isinstance(self.default_settings.board_color, str)

    def test_default_board_border_thickness(self):
        assert isinstance(self.default_settings.board_border_thickness, int)

    def test_default_font_family_type(self):
        assert isinstance(self.default_settings.font_family, str)

    def test_get_number_of_boxes(self):
        assert self.default_settings.get_number_of_boxes == \
               self.default_settings.board_columns_number * self.default_settings.board_rows_number

    def test_wrong_board_rows_number_type(self):
        wrong_settings = config.Settings(board_rows_number=1.1)
        assert wrong_settings != self.default_settings
        assert self.default_settings == wrong_settings.save(log=False)

    def test_wrong_board_columns_number_type(self):
        wrong_settings = config.Settings(board_columns_number="something")
        assert wrong_settings != self.default_settings
        assert self.default_settings == wrong_settings.save(log=False)

    def test_wrong_window_title_type(self):
        wrong_settings = config.Settings(window_title=4)
        assert wrong_settings != self.default_settings
        assert self.default_settings == wrong_settings.save(log=False)

    def test_wrong_window_color_type(self):
        wrong_settings = config.Settings(window_title=9)
        assert wrong_settings != self.default_settings
        assert self.default_settings == wrong_settings.save(log=False)

    def test_wrong_token_colors_type(self):
        wrong_settings = config.Settings(token_colors="color")
        assert wrong_settings != self.default_settings
        assert self.default_settings == wrong_settings.save(log=False)

    def test_wrong_board_color_type(self):
        wrong_settings = config.Settings(board_color=4)
        assert wrong_settings != self.default_settings
        assert self.default_settings == wrong_settings.save(log=False)

    def test_wrong_board_border_thickness_type(self):
        wrong_settings = config.Settings(board_border_thickness="None")
        assert wrong_settings != self.default_settings
        assert self.default_settings == wrong_settings.save(log=False)

    def test_wrong_font_family_type(self):
        wrong_settings = config.Settings(font_family=6)
        assert wrong_settings != self.default_settings
        assert self.default_settings == wrong_settings.save(log=False)
