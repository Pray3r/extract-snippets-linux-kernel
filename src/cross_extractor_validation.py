from src.extractors.plugin_manager import PluginManager

class CrossExtractorValidator:
    def __init__(self):
        self.plugin_manager = PluginManager()

    def validate_extraction(self, source_code):
        """
        Perform cross-validation using multiple extractors and ensure consistency
        in extracted snippets.
        """
        snippets = {}
        plugins = self.plugin_manager.load_plugins()

        for plugin in plugins:
            plugin_name = plugin.__class__.__name__
            plugin_snippets = plugin.extract_snippets(source_code)
            if plugin_snippets:
                snippets[plugin_name] = plugin_snippets

        # Validate consistency across different extractors
        consistency_issues = self.cross_validate(snippets)
        return snippets, consistency_issues

    def cross_validate(self, snippets):
        """
        Cross-validate extracted snippets from different extractors to ensure
        there are no conflicting or overlapping extractions.
        """
        consistency_issues = []
        keys = list(snippets.keys())

        for i in range(len(keys)):
            for j in range(i + 1, len(keys)):
                extractor_1_snippets = set(snippets[keys[i]])
                extractor_2_snippets = set(snippets[keys[j]])

                intersection = extractor_1_snippets & extractor_2_snippets
                if intersection:
                    consistency_issues.append({
                        'extractor_1': keys[i],
                        'extractor_2': keys[j],
                        'conflicting_snippets': list(intersection)
                    })

        return consistency_issues
