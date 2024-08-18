from src.extractors.extractor_interface import ExtractorInterface

class MemoryBarrierExtractor(ExtractorInterface):
    def extract_snippets(self, source_code):
        """
        Extract snippets related to memory barriers.
        """
        snippets = []
        barrier_keywords = ["smp_mb", "smp_rmb", "smp_wmb", "smp_store_release", "smp_load_acquire"]
        for keyword in barrier_keywords:
            start_pos = source_code.find(keyword)
            while start_pos != -1:
                end_pos = source_code.find(";", start_pos)
                snippet = source_code[start_pos:end_pos + 1]
                if snippet:
                    snippets.append(snippet)
                start_pos = source_code.find(keyword, start_pos + 1)
        return snippets