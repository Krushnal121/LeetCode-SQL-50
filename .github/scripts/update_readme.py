import os
import re
from github import Github

def get_problem_info(directory):
    match = re.match(r'(\d+)\.LeetCode@(\d+)_(.+)', directory)
    if match:
        day, problem_id, problem_name = match.groups()
        problem_name = problem_name.replace('_', ' ')
        return int(day), problem_id, problem_name
    return None

def generate_table_row(day, problem_id, problem_name, directory):
    problem_link = f"{directory}/{directory}.md"
    solution_link = f"{directory}/{directory}.sql"
    return f"| {day} | [{problem_name}]({problem_link}) | [Solution]({solution_link}) |\n"

def update_readme(repo):
    readme_path = "README.md"
    readme_content = repo.get_contents(readme_path).decoded_content.decode("utf-8")

    table_pattern = r'\| Day \| Problem Title.*?\n(.*?)\n\n'
    table_match = re.search(table_pattern, readme_content, re.DOTALL)

    if not table_match:
        print("Table not found in README.md")
        return

    directories = [d for d in os.listdir('.') if os.path.isdir(d) and d.startswith(tuple(str(i) for i in range(10)))]
    table_rows = []

    for directory in sorted(directories, key=lambda x: int(x.split('.')[0])):
        problem_info = get_problem_info(directory)
        if problem_info:
            day, problem_id, problem_name = problem_info
            table_rows.append(generate_table_row(day, problem_id, problem_name, directory))

    new_table = "| Day | Problem Title | Solution Link |\n|-----|---------------|---------------|\n" + "".join(table_rows)
    updated_content = re.sub(table_pattern, f"| Day | Problem Title | Solution Link |\n{new_table}\n\n", readme_content, flags=re.DOTALL)

    if updated_content != readme_content:
        repo.update_file(readme_path, "Update README.md", updated_content, repo.get_contents(readme_path).sha)
        print("README.md updated successfully")
    else:
        print("No changes needed in README.md")

if __name__ == "__main__":
    github_token = os.environ["GITHUB_TOKEN"]
    repo_name = os.environ["GITHUB_REPOSITORY"]
    
    g = Github(github_token)
    repo = g.get_repo(repo_name)
    
    update_readme(repo)
