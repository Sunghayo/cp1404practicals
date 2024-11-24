"""
Project Management Program
Estimated Time: 120 minutes
Actual Time: 130 minutes
"""

import datetime
from project import Project


def load_projects(filename='projects.txt'):
    """Load projects from file."""
    projects = []
    with open(filename) as file:
        # Skip header
        file.readline()
        for line in file:
            parts = line.strip().split('\t')
            project = Project(parts[0], parts[1], parts[2], parts[3], parts[4])
            projects.append(project)
    return projects


def save_projects(projects, filename='projects.txt'):
    """Save projects to file."""
    with open(filename, 'w') as file:
        # Write header
        file.write("Name\tStart Date\tPriority\tCost Estimate\tCompletion Percentage\n")
        for project in projects:
            file.write(f"{project.name}\t{project.start_date.strftime('%d/%m/%Y')}\t"
                       f"{project.priority}\t{project.cost_estimate}\t"
                       f"{project.completion_percentage}\n")


def display_projects(projects):
    """Display projects in two groups: incomplete and complete."""
    print("Incomplete projects:")
    incomplete_projects = [project for project in projects if not project.is_complete()]
    for project in sorted(incomplete_projects):
        print(f"  {project}")

    print("Completed projects:")
    completed_projects = [project for project in projects if project.is_complete()]
    for project in sorted(completed_projects):
        print(f"  {project}")


def filter_projects_by_date(projects):
    """Display projects that start after specified date."""
    date_string = input("Show projects that start after date (dd/mm/yy): ")
    date = datetime.datetime.strptime(date_string, "%d/%m/%y").date()
    filtered_projects = [project for project in projects if project.start_date >= date]
    for project in sorted(filtered_projects, key=lambda x: x.start_date):
        print(project)


def add_project():
    """Add a new project."""
    print("Let's add a new project")
    name = input("Name: ")
    start_date = input("Start date (dd/mm/yy): ")
    priority = input("Priority: ")
    cost_estimate = float(input("Cost estimate: $"))
    percent_complete = input("Percent complete: ")

    # Convert date format from dd/mm/yy to dd/mm/yyyy
    date = datetime.datetime.strptime(start_date, "%d/%m/%y")
    start_date = date.strftime("%d/%m/%Y")

    return Project(name, start_date, priority, cost_estimate, percent_complete)


def update_project(projects):
    """Update a project's completion percentage and priority."""
    for i, project in enumerate(projects):
        print(f"{i} {project}")

    choice = int(input("Project choice: "))
    project = projects[choice]
    print(project)

    new_percentage = input("New Percentage: ")
    new_priority = input("New Priority: ")
    project.update(new_percentage, new_priority)


def main():
    """Main program for project management."""
    print("Welcome to Pythonic Project Management")
    projects = load_projects()
    print(f"Loaded {len(projects)} projects from projects.txt")

    MENU = """- (L)oad projects  
- (S)ave projects  
- (D)isplay projects  
- (F)ilter projects by date
- (A)dd new project  
- (U)pdate project
- (Q)uit"""

    while True:
        print(MENU)
        choice = input(">>> ").lower()

        if choice == 'l':
            filename = input("Filename to load projects from: ")
            projects = load_projects(filename)
        elif choice == 's':
            filename = input("Filename to save projects to: ")
            save_projects(projects, filename)
        elif choice == 'd':
            display_projects(projects)
        elif choice == 'f':
            filter_projects_by_date(projects)
        elif choice == 'a':
            projects.append(add_project())
        elif choice == 'u':
            update_project(projects)
        elif choice == 'q':
            save_choice = input("Would you like to save to projects.txt? ")
            if save_choice.lower() != "no, i think not.":
                save_projects(projects)
            print("Thank you for using custom-built project management software.")
            break


if __name__ == '__main__':
    main()