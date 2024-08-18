import os
import yaml
from src.utils.config_manager import ConfigManager
from src.cross_extractor_validation import CrossExtractorValidator
from src.utils.logging.logger_manager import LoggerManager

class ExtractionPipeline:
    def __init__(self, config_path, output_dir):
        self.config_manager = ConfigManager(config_path)
        self.output_dir = output_dir
        self.logger = LoggerManager("extraction_pipeline", os.path.join(output_dir, "pipeline.log")).logger
        self.validator = CrossExtractorValidator()

    def run(self):
        """
        Run the entire extraction pipeline: load configuration, process files,
        perform extraction, validate results, and save output.
        """
        self.logger.info("Starting the extraction pipeline.")
        
        # Load source files configuration
        source_directories = self.config_manager.config['source_files']['directories']
        extensions = self.config_manager.config['source_files']['extensions']
        
        # Collect all source files
        source_files = self.collect_source_files(source_directories, extensions)
        
        # Process each file
        for file_path in source_files:
            self.process_file(file_path)
        
        self.logger.info("Extraction pipeline completed.")

    def collect_source_files(self, directories, extensions):
        """
        Collect all source files from the specified directories with the given extensions.
        """
        source_files = []
        for directory in directories:
            for root, _, files in os.walk(directory):
                for file in files:
                    if any(file.endswith(ext) for ext in extensions):
                        source_files.append(os.path.join(root, file))
        
        self.logger.info(f"Collected {len(source_files)} source files.")
        return source_files

    def process_file(self, file_path):
        """
        Process a single file: read its content, perform extraction, validate, and save results.
        """
        self.logger.info(f"Processing file: {file_path}")
        
        with open(file_path, 'r') as file:
            source_code = file.read()
        
        snippets, consistency_issues = self.validator.validate_extraction(source_code)
        
        self.save_snippets(file_path, snippets)
        self.save_consistency_issues(file_path, consistency_issues)

    def save_snippets(self, file_path, snippets):
        """
        Save extracted snippets to the output directory.
        """
        base_name = os.path.basename(file_path)
        output_file = os.path.join(self.output_dir, f"{base_name}_snippets.yaml")
        
        with open(output_file, 'w') as file:
            yaml.safe_dump(snippets, file)
        
        self.logger.info(f"Saved snippets to {output_file}")

    def save_consistency_issues(self, file_path, issues):
        """
        Save consistency issues found during cross-validation to the output directory.
        """
        if issues:
            base_name = os.path.basename(file_path)
            issues_file = os.path.join(self.output_dir, f"{base_name}_issues.yaml")
            
            with open(issues_file, 'w') as file:
                yaml.safe_dump(issues, file)
            
            self.logger.warning(f"Found consistency issues in {file_path}, saved to {issues_file}")
        else:
            self.logger.info(f"No consistency issues found in {file_path}")
