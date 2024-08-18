from src.extractors.extractor_interface import ExtractorInterface

class EventNotificationExtractor(ExtractorInterface):
    def extract_snippets(self, source_code):
        """
        Extract snippets related to event notification mechanisms.
        """
        snippets = []
        event_keywords = ["notify", "notifier", "event", "signal", "wake_up"]
        for keyword in event_keywords:
            start_pos = source_code.find(keyword)
            while start_pos != -1:
                end_pos = source_code.find(";", start_pos)
                snippet = source_code[start_pos:end_pos + 1]
                if snippet:
                    snippets.append(snippet)
                start_pos = source_code.find(keyword, start_pos + 1)
        return snippets
