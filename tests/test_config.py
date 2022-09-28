from src import config


class TestConfig:
    @classmethod
    def setup_class(cls):
        cls.default_settings = config.Settings()
        cls.wrong_settings = config.Settings(1.1, 1.2, (1,), "toto")

    def test_board_size(self):
        assert isinstance(self.default_settings.board_rows_number, int)
        assert isinstance(self.default_settings.board_columns_number, int)

    def test_boxes_number(self):
        assert isinstance(self.default_settings.get_number_of_boxes, int)

    def test_window_title(self):
        assert isinstance(self.default_settings.window_title, str)
