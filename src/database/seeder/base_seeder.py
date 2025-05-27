from typing import List, Dict, Any
from src.database.db import SessionLocal

class BaseSeeder:
    def __init__(self, model_class, data: List[Dict[str, Any]], unique_field: str = None):
        self.model_class = model_class
        self.data = data
        self.unique_field = unique_field
        self.db = SessionLocal()

    def seed(self):
        try:
            print(f"Seeding {self.model_class.__name__}...")

            for item in self.data:
                # Check if unique field exists
                if self.unique_field:
                    existing = self.db.query(self.model_class).filter(
                        getattr(self.model_class, self.unique_field) == item[self.unique_field]
                    ).first()
                    if existing:
                        print(f"Skipping {self.model_class.__name__} with {self.unique_field}={item[self.unique_field]} (already exists)")
                        continue

                # Create new instance
                new_item = self.model_class(**item)
                self.db.add(new_item)
                print(f"Created {self.model_class.__name__}: {item}")

            self.db.commit()
            print(f"{self.model_class.__name__} seeding completed successfully")

        except Exception as e:
            self.db.rollback()
            print(f"Error seeding {self.model_class.__name__}: {e}")
            raise
        finally:
            self.db.close()
