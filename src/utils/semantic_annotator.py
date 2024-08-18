class SemanticAnnotator:
    @staticmethod
    def annotate_function_role(snippet, role):
        """Annotate a function snippet with its identified role."""
        annotation = f"// Function role: {role}\n"
        return annotation + snippet

    @staticmethod
    def generate_context_description(snippet, context):
        """Generate a context description for the given snippet."""
        context_info = f"// Context: {context}\n"
        return context_info + snippet

    @staticmethod
    def auto_generate_comments(snippet):
        """Automatically generate comments for the code snippet."""
        comments = "// This function performs critical operations related to memory management.\n"
        return comments + snippet
