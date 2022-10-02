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

    def test_wrong_board_size_type(self):
        with pytest.raises(SystemExit) as test_exception_rows:
            wrong_settings = config.Settings(board_rows_number=1.1)

        with pytest.raises(SystemExit) as test_exception_cols:
            wrong_settings = config.Settings(board_columns_number="something")

        assert test_exception_rows.type == SystemExit
        assert test_exception_cols.type == SystemExit

    def test_wrong_window_title_type(self):
        with pytest.raises(SystemExit) as test_exception:
            wrong_settings = config.Settings(window_title=4)
        assert test_exception.type == SystemExit

    def test_wrong_window_color_type(self):
        with pytest.raises(SystemExit) as test_exception:
            wrong_settings = config.Settings(window_title=9)
        assert test_exception.type == SystemExit

    def test_wrong_token_colors_type(self):
        with pytest.raises(SystemExit) as test_exception:
            wrong_settings = config.Settings(token_colors="color")
        assert test_exception.type == SystemExit

    def test_wrong_board_color_type(self):
        with pytest.raises(SystemExit) as test_exception:
            wrong_settings = config.Settings(board_color=4)
        assert test_exception.type == SystemExit

    def test_wrong_board_border_thickness_type(self):
        with pytest.raises(SystemExit) as test_exception:
            wrong_settings = config.Settings(board_border_thickness="None")
        assert test_exception.type == SystemExit

    def test_wrong_font_family_type(self):
        with pytest.raises(SystemExit) as test_exception:
            wrong_settings = config.Settings(font_family=6)
        assert test_exception.type == SystemExit
