import os
import re

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

def update_readme():
    readme_path = "README.md"
    if os.path.exists(readme_path):
        with open(readme_path, 'r') as file:
            readme_content = file.read()
        print(f"Existing README.md found. Content length: {len(readme_content)}")
    else:
        print(f"README.md not found. Creating a new file.")
        readme_content = "# LeetCode SQL 50\n\n"

    table_pattern = r'\| Day \| Problem Title \| Solution Link \|\n\|-----\|---------------\|---------------\|\n(.*?)(?=\n\n|\Z)'
    table_match = re.search(table_pattern, readme_content, re.DOTALL)

    directories = [d for d in os.listdir('.') if os.path.isdir(d) and d.startswith(tuple(str(i) for i in range(10)))]
    print(f"Found {len(directories)} problem directories")
    table_rows = []

    for directory in sorted(directories, key=lambda x: int(x.split('.')[0])):
        problem_info = get_problem_info(directory)
        if problem_info:
            day, problem_id, problem_name = problem_info
            table_rows.append(generate_table_row(day, problem_id, problem_name, directory))

    new_table = "| Day | Problem Title | Solution Link |\n|-----|---------------|---------------|\n" + "".join(table_rows)

    if table_match:
        updated_content = re.sub(table_pattern, new_table, readme_content, flags=re.DOTALL)
    else:
        updated_content = readme_content + "\n" + new_table + "\n"

    if updated_content != readme_content:
        with open(readme_path, 'w') as file:
            file.write(updated_content)
        print(f"README.md updated successfully. New content length: {len(updated_content)}")
    else:
        print("No changes needed in README.md")

if __name__ == "__main__":
    update_readme()