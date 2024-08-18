from src.extractors.extractor_interface import ExtractorInterface

class NetworkProtocolStackExtractor(ExtractorInterface):
    def extract_snippets(self, source_code):
        """
        Extract snippets related to network protocol stack implementations.
        """
        snippets = []
        protocol_keywords = ["tcp_", "udp_", "ip_", "skb_", "net_"]
        for keyword in protocol_keywords:
            start_pos = source_code.find(keyword)
            while start_pos != -1:
                end_pos = source_code.find("{", start_pos)
                snippet = source_code[start_pos:end_pos]
                if snippet:
                    snippets.append(snippet)
                start_pos = source_code.find(keyword, start_pos + 1)
        return snippets
