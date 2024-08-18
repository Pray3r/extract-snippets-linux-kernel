import unittest
from src.extractors.plugin_manager import PluginManager

class TestPluginManager(unittest.TestCase):
    def test_load_plugins(self):
        manager = PluginManager(plugins_dir='tests/mock_plugins')
        plugins = manager.load_plugins()
        self.assertGreater(len(plugins), 0)

    def test_execute_plugins(self):
        manager = PluginManager(plugins_dir='tests/mock_plugins')
        manager.load_plugins()
        snippets = manager.execute_plugins("int main() { return 0; }")
        self.assertGreater(len(snippets), 0)

if __name__ == '__main__':
    unittest.main()
