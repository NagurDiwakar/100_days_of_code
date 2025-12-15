"""
Makefile-like commands for common tasks
Run with: python scripts.py <command>
"""
import sys
import subprocess


def run_command(command):
    """Execute shell command"""
    print(f"Running: {command}")
    result = subprocess.run(command, shell=True)
    return result.returncode


def test():
    """Run tests"""
    return run_command("pytest -v --cov=app tests/")


def format_code():
    """Format code with black and isort"""
    run_command("black app/ tests/")
    return run_command("isort app/ tests/")


def lint():
    """Run linters"""
    run_command("flake8 app/")
    return run_command("mypy app/")


def dev():
    """Start development server"""
    return run_command("uvicorn app.main:app --reload --host 0.0.0.0 --port 8000")


def migrate():
    """Run database migrations"""
    return run_command("alembic upgrade head")


def migrate_create(message):
    """Create new migration"""
    return run_command(f'alembic revision --autogenerate -m "{message}"')


def docker_up():
    """Start Docker containers"""
    return run_command("docker-compose up -d")


def docker_down():
    """Stop Docker containers"""
    return run_command("docker-compose down")


def docker_logs():
    """View Docker logs"""
    return run_command("docker-compose logs -f api")


def help_text():
    """Show available commands"""
    commands = {
        "test": "Run tests with coverage",
        "format": "Format code with black and isort",
        "lint": "Run linters (flake8, mypy)",
        "dev": "Start development server",
        "migrate": "Run database migrations",
        "migrate-create <msg>": "Create new migration",
        "docker-up": "Start Docker containers",
        "docker-down": "Stop Docker containers",
        "docker-logs": "View Docker logs",
    }
    print("\nAvailable commands:")
    for cmd, desc in commands.items():
        print(f"  {cmd:25} - {desc}")
    print()


if __name__ == "__main__":
    if len(sys.argv) < 2:
        help_text()
        sys.exit(0)
    
    command = sys.argv[1]
    
    commands = {
        "test": test,
        "format": format_code,
        "lint": lint,
        "dev": dev,
        "migrate": migrate,
        "docker-up": docker_up,
        "docker-down": docker_down,
        "docker-logs": docker_logs,
        "help": help_text,
    }
    
    if command == "migrate-create" and len(sys.argv) > 2:
        sys.exit(migrate_create(sys.argv[2]))
    elif command in commands:
        sys.exit(commands[command]())
    else:
        print(f"Unknown command: {command}")
        help_text()
        sys.exit(1)
