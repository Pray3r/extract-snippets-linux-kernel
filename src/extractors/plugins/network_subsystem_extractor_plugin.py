from src.extractors.extractor_interface import ExtractorInterface

class NetworkSubsystemExtractor(ExtractorInterface):
    def extract_snippets(self, source_code):
        """
        Extract snippets related to the network subsystem such as protocols, sockets, etc.
        """
        snippets = []
        network_keywords = ["sock", "net_device", "netif_", "ethernet", "tcp_"]
        for keyword in network_keywords:
            start_pos = source_code.find(keyword)
            while start_pos != -1:
                end_pos = source_code.find("{", start_pos)
                snippet = source_code[start_pos:end_pos]
                if snippet:
                    snippets.append(snippet)
                start_pos = source_code.find(keyword, start_pos + 1)
        return snippets
