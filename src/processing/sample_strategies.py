import random
import subprocess

def get_code_complexity(file_path):
    """Calculate the complexity of a code file using a static analysis tool."""
    try:
        result = subprocess.check_output(['lizard', file_path])
        return int(result.decode().split('\n')[-2].split()[-1])  # Extract complexity from the lizard output
    except Exception as e:
        return 0  # Fallback to 0 complexity if analysis fails

def smart_sample_files(files, min_complexity=10):
    """Sample files with a complexity above a certain threshold."""
    sampled_files = [f for f in files if get_code_complexity(f) >= min_complexity]
    return sampled_files

def sample_based_on_git_history(files):
    """Sample files based on their change frequency in Git history."""
    changed_files = []
    for file_path in files:
        try:
            changes = subprocess.check_output(['git', 'log', '--pretty=format:', '--name-only', file_path])
            change_count = len(changes.splitlines())
            if change_count > 5:  # Threshold for 'frequently changed'
                changed_files.append(file_path)
        except subprocess.CalledProcessError:
            continue
    return changed_files

def combined_advanced_sampling(files):
    """Combine smart sampling and git history based sampling."""
    complex_files = smart_sample_files(files)
    git_changed_files = sample_based_on_git_history(files)
    return list(set(complex_files + git_changed_files))
