import argparse
import sys
import os
from src.extraction_pipeline import ExtractionPipeline
from src.cross_extractor_validation import CrossExtractorValidator
from src.utils.config_manager import ConfigManager

def main():
    parser = argparse.ArgumentParser(description="Linux Kernel Code Snippets Extractor")
    parser.add_argument('-v', '--version', action='version', version='1.0.0', help="Show the version of the tool")

    subparsers = parser.add_subparsers(dest='command', help="Available commands")

    # Subcommand: Extract
    extract_parser = subparsers.add_parser('extract', help="Extract code snippets from source files")
    extract_parser.add_argument("-c", "--config", type=str, default=os.getenv("CONFIG_PATH", "config/default_config.yaml"), help="Path to the configuration file (default: config/default_config.yaml).")
    extract_parser.add_argument("-o", "--output", type=str, default=os.getenv("OUTPUT_DIR", "output/snippets"), help="Path to the output directory (default: output/snippets).")
    extract_parser.add_argument("-p", "--parallel", action="store_true", help="Enable parallel processing")
    extract_parser.add_argument("-f", "--format", choices=["json", "yaml", "text"], default="text", help="Specify the output format (default: text).")

    # Subcommand: Validate
    validate_parser = subparsers.add_parser('validate', help="Validate the extracted snippets for consistency")
    validate_parser.add_argument("-c", "--config", type=str, default=os.getenv("CONFIG_PATH", "config/default_config.yaml"), help="Path to the configuration file (default: config/default_config.yaml).")
    validate_parser.add_argument("-i", "--input", type=str, help="Path to the input directory containing snippets.")
    validate_parser.add_argument("-o", "--output", type=str, default=os.getenv("OUTPUT_DIR", "output/validation"), help="Path to the output directory for validation results (default: output/validation).")

    # Subcommand: Report
    report_parser = subparsers.add_parser('report', help="Generate a report based on extracted snippets")
    report_parser.add_argument("-i", "--input", type=str, help="Path to the input directory containing snippets.")
    report_parser.add_argument("-o", "--output", type=str, default=os.getenv("OUTPUT_DIR", "output/report"), help="Path to the output directory for reports (default: output/report).")

    # Subcommand: Batch Processing
    batch_parser = subparsers.add_parser('batch', help="Run multiple commands in sequence")
    batch_parser.add_argument("-c", "--config", type=str, help="Path to the configuration file.")
    batch_parser.add_argument("-o", "--output", type=str, help="Path to the output directory.")
    batch_parser.add_argument("--commands", nargs='+', choices=['extract', 'validate', 'report'], help="Commands to run in sequence.")

    if len(sys.argv) < 2:
        parser.print_help()
        sys.exit(1)

    args = parser.parse_args()

    if args.command == 'extract':
        try:
            pipeline = ExtractionPipeline(config_path=args.config, output_dir=args.output)
            if args.parallel:
                pipeline.enable_parallel_processing()
            pipeline.run()
        except Exception as e:
            print(f"Error: {e}")
            print("Please check your configuration or input files and try again.")
            sys.exit(1)

    elif args.command == 'validate':
        try:
            config_manager = ConfigManager(args.config)
            validator = CrossExtractorValidator()
            source_files = config_manager.config['source_files']['directories']
            extensions = config_manager.config['source_files']['extensions']

            for directory in source_files:
                print(f"Validating snippets in {directory}")
                # Additional logic for validation can be added here
        except Exception as e:
            print(f"Error: {e}")
            print("Please check your configuration or input files and try again.")
            sys.exit(1)

    elif args.command == 'report':
        try:
            print(f"Generating report from {args.input}")
            # Logic for generating the report
        except Exception as e:
            print(f"Error: {e}")
            print("Please check your configuration or input files and try again.")
            sys.exit(1)

    elif args.command == 'batch':
        try:
            for command in args.commands:
                if command == 'extract':
                    pipeline = ExtractionPipeline(config_path=args.config, output_dir=args.output)
                    pipeline.run()
                elif command == 'validate':
                    config_manager = ConfigManager(args.config)
                    validator = CrossExtractorValidator()
                    source_files = config_manager.config['source_files']['directories']
                    extensions = config_manager.config['source_files']['extensions']
                    for directory in source_files:
                        print(f"Validating snippets in {directory}")
                        # Additional validation logic here
                elif command == 'report':
                    print(f"Generating report from {args.input}")
                    # Additional report generation logic here
        except Exception as e:
            print(f"Error: {e}")
            print("Please check your configuration or input files and try again.")
            sys.exit(1)
    
    else:
        parser.print_help()

if __name__ == "__main__":
    main()