from src.extractors.extractor_interface import ExtractorInterface
import ast

class ASTExtractor(ExtractorInterface):
    def extract_snippets(self, source_code):
        """
        Extract code snippets using the Abstract Syntax Tree (AST) for Python code.
        """
        snippets = []
        try:
            tree = ast.parse(source_code)
            for node in ast.walk(tree):
                if isinstance(node, ast.FunctionDef):
                    snippets.append(ast.get_source_segment(source_code, node))
        except Exception as e:
            print(f"AST extraction failed: {e}")
        return snippets
