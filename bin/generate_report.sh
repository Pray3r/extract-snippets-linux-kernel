#!/bin/bash

# 设置脚本在出错时退出
set -e

# 定义默认的输出目录和报告文件路径
SNIPPETS_DIR="output/snippets"
REPORT_FILE="output/report/snippets_report.txt"

# 日志文件
LOG_FILE="output/logs/report.log"

# 帮助信息
usage() {
    echo "Usage: $0 [-d snippets_directory] [-r report_file]"
    exit 1
}

# 解析命令行参数
while getopts ":d:r:h" opt; do
    case ${opt} in
        d )
            SNIPPETS_DIR=$OPTARG
            ;;
        r )
            REPORT_FILE=$OPTARG
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

# 确保报告目录存在
mkdir -p $(dirname "$REPORT_FILE")
mkdir -p $(dirname "$LOG_FILE")

# 生成报告
echo "Generating report from snippets in $SNIPPETS_DIR" | tee "$LOG_FILE"
find "$SNIPPETS_DIR" -type f -name '*.txt' -exec cat {} + > "$REPORT_FILE"
echo "Report generated at $REPORT_FILE" | tee -a "$LOG_FILE"
