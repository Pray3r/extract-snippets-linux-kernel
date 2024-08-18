import importlib
import os

class PluginManager:
    def __init__(self, plugins_dir='src/extractors/plugins'):
        self.plugins_dir = plugins_dir
        self.plugins = []

    def load_plugins(self):
        """Load all extractor plugins dynamically."""
        for filename in os.listdir(self.plugins_dir):
            if filename.endswith(".py"):
                module_name = filename[:-3]
                module = importlib.import_module(f'src.extractors.plugins.{module_name}')
                if hasattr(module, 'Extractor'):
                    self.plugins.append(module.Extractor())
        return self.plugins

    def execute_plugins(self, source_code):
        """Execute all loaded plugins on the source code."""
        snippets = []
        for plugin in self.plugins:
            snippets.extend(plugin.extract_snippets(source_code))
        return snippets
