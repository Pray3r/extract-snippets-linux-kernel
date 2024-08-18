from src.extractors.extractor_interface import ExtractorInterface

class HotplugSupportExtractor(ExtractorInterface):
    def extract_snippets(self, source_code):
        """
        Extract snippets related to hotplug support in the kernel.
        """
        snippets = []
        hotplug_keywords = ["register_hotplug", "unregister_hotplug", "cpu_hotplug", "memory_hotplug"]
        for keyword in hotplug_keywords:
            start_pos = source_code.find(keyword)
            while start_pos != -1:
                end_pos = source_code.find(";", start_pos)
                snippet = source_code[start_pos:end_pos + 1]
                if snippet:
                    snippets.append(snippet)
                start_pos = source_code.find(keyword, start_pos + 1)
        return snippets
