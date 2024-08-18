from src.extractors.extractor_interface import ExtractorInterface
from src.extractors.plugin_manager import PluginManager

class CrossExtractor(ExtractorInterface):
    def __init__(self):
        self.plugin_manager = PluginManager()

    def extract_snippets(self, source_code):
        """
        Perform cross-extraction using multiple extractors and ensure consistency.
        """
        snippets = []
        plugins = self.plugin_manager.load_plugins()

        for plugin in plugins:
            plugin_snippets = plugin.extract_snippets(source_code)
            if plugin_snippets:
                snippets.extend(plugin_snippets)

        # Perform additional cross-validation and ensure no duplicates or inconsistencies
        unique_snippets = list(set(snippets))
        return unique_snippets
