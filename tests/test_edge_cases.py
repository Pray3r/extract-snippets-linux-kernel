import unittest
from src.extractors.plugin_manager import PluginManager

class TestEdgeCases(unittest.TestCase):
    def setUp(self):
        self.manager = PluginManager(plugins_dir='tests/mock_plugins')
        self.manager.load_plugins()

    def test_empty_source_code(self):
        source_code = ""
        snippets = self.manager.execute_plugins(source_code)
        self.assertEqual(len(snippets), 0, "No snippets should be extracted from empty source code.")

    def test_malformed_source_code(self):
        source_code = "int main( { return 0; }"
        snippets = self.manager.execute_plugins(source_code)
        self.assertEqual(len(snippets), 0, "Malformed source code should not produce snippets.")

if __name__ == '__main__':
    unittest.main()
