from ygka.utils import YGKAConfigManager


def test_init_without_path():
    config_manager = YGKAConfigManager()
    assert config_manager.config_path == YGKAConfigManager.DEFAULT_CONFIG_PATH


def test_with_path():
    config_manager = YGKAConfigManager(config_path='test_path')
    assert config_manager.config_path == 'test_path'
