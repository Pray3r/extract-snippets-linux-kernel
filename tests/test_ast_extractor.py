import unittest
from src.extractors.plugins.ast_extractor_plugin import ASTExtractor

class TestASTExtractor(unittest.TestCase):

    def setUp(self):
        """Set up the test case environment."""
        # 初始化一个 ASTExtractor 实例
        config = {
            'custom_patterns': 'path/to/custom_patterns.yaml'
        }
        self.extractor = ASTExtractor(config=config)

    def test_extract_simple_function(self):
        """Test extracting a simple C function."""
        source_code = """
        int add(int a, int b) {
            return a + b;
        }
        """
        snippets = self.extractor.extract_snippets(source_code)
        self.assertEqual(len(snippets), 1)
        self.assertIn('add', snippets[0])
    
    def test_extract_with_macro(self):
        """Test extracting a function with macros."""
        source_code = """
        #define SQUARE(x) ((x) * (x))
        int square(int n) {
            return SQUARE(n);
        }
        """
        snippets = self.extractor.extract_snippets(source_code)
        self.assertEqual(len(snippets), 1)
        self.assertIn('square', snippets[0])

    def test_extract_struct(self):
        """Test extracting a C struct."""
        source_code = """
        struct Point {
            int x;
            int y;
        };
        """
        snippets = self.extractor.extract_snippets(source_code)
        self.assertEqual(len(snippets), 1)
        self.assertIn('Point', snippets[0])
    
    def test_extract_conditional_compilation(self):
        """Test extracting code with conditional compilation."""
        source_code = """
        #ifdef DEBUG
        void debug_log(const char *msg) {
            printf("DEBUG: %s\\n", msg);
        }
        #endif
        """
        snippets = self.extractor.extract_snippets(source_code)
        self.assertTrue(any('#ifdef' in snippet for snippet in snippets))

    def test_handle_extraction_error(self):
        """Test the extractor's error handling."""
        source_code = "int main( { return 0; }"  # Syntax error
        snippets = self.extractor.extract_snippets(source_code)
        self.assertEqual(snippets, [])  # Expecting no valid snippets due to syntax error

if __name__ == '__main__':
    unittest.main()
