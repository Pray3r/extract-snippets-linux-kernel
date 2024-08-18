_extract_snippets_linux_kernel() {
    local cur prev opts
    COMPREPLY=()
    cur="${COMP_WORDS[COMP_CWORD]}"
    prev="${COMP_WORDS[COMP_CWORD-1]}"
    opts=$(python3 src/main.py -h | awk '/optional arguments:/ {getline; while ($1 != "") {print $1; getline}}')

    COMPREPLY=( $(compgen -W "${opts}" -- ${cur}) )
    return 0
}
complete -F _extract_snippets_linux_kernel extract-snippets-linux-kernel
