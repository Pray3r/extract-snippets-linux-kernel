#!/bin/bash

# 设置脚本在出错时退出
set -e

# 定义默认的配置文件路径
CONFIG_FILE="config/default_config.yaml"

# 定义源代码目录
SOURCE_DIR="path/to/linux/kernel/source"

# 输出目录
OUTPUT_DIR="output/snippets"

# 日志文件
LOG_FILE="output/logs/extract.log"

# 帮助信息
usage() {
    echo "Usage: $0 [-c config_file] [-s source_directory] [-o output_directory]"
    exit 1
}

# 解析命令行参数
while getopts ":c:s:o:h" opt; do
    case ${opt} in
        c )
            CONFIG_FILE=$OPTARG
            ;;
        s )
            SOURCE_DIR=$OPTARG
            ;;
        o )
            OUTPUT_DIR=$OPTARG
            ;;
        h )
            usage
            ;;
        \? )
            echo "Invalid option: $OPTARG" 1>&2
            usage
            ;;
        : )
            echo "Invalid option: $OPTARG requires an argument" 1>&2
            usage
            ;;
    esac
done

# 确保日志目录存在
mkdir -p $(dirname "$LOG_FILE")
mkdir -p "$OUTPUT_DIR"

# 运行Python提取脚本
python3 src/main.py --config "$CONFIG_FILE" --source "$SOURCE_DIR" --output "$OUTPUT_DIR" | tee "$LOG_FILE"

echo "Extraction completed. Snippets saved to $OUTPUT_DIR"
