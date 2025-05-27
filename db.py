import click
from src.database.db import init_db
from src.database.seeder import run_seeders

@click.group()
def cli():
    """Database management commands"""
    pass

@cli.command()
def migrate():
    """Create database tables"""
    print("Creating database tables...")
    init_db()

@cli.command()
@click.option('--class', 'seeder_class', help='Run specific seeder class (e.g., UserSeeder)')
def seed(seeder_class):
    """Seed database with sample data"""
    print("Seeding database...")
    run_seeders(seeder_class)

if __name__ == "__main__":
    cli()
