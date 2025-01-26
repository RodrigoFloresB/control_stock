from src.database import init_db
from src.cli import execute_menu

if __name__ == "__main__":
    init_db()
    execute_menu()