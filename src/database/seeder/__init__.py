from .base_seeder import BaseSeeder
from .user_seeder import UserSeeder

# Export classes to be imported directly
__all__ = ['BaseSeeder', 'UserSeeder']

def get_seeder_class(class_name: str):
    """Get seeder class from name"""
    for seeder_class in BaseSeeder.__subclasses__():
        if seeder_class.__name__ == class_name:
            return seeder_class
    return None

def run_seeders(seeder_class: str = None):
    try:
        print("Starting database seeding...")
        success = True

        if seeder_class:
            # Run specific seeder
            seeder = get_seeder_class(seeder_class)
            if seeder:
                try:
                    seeder().seed()
                    print(f"{seeder_class} seeding completed successfully!")
                except Exception as e:
                    print(f"Error seeding {seeder_class}: {e}")
                    success = False
            else:
                print(f"Error: Seeder class '{seeder_class}' not found")
                print("Available seeders:", [cls.__name__ for cls in BaseSeeder.__subclasses__()])
                success = False
        else:
            # Run all seeders
            for seeder_class in BaseSeeder.__subclasses__():
                try:
                    seeder_class().seed()
                except Exception as e:
                    print(f"Error seeding {seeder_class.__name__}: {e}")
                    success = False

        if success:
            print("Database seeding completed successfully")
        else:
            print("Database seeding completed with errors")

    except Exception as e:
        print(f"Error during seeding: {e}")
        raise
