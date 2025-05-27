from src.models.user import User
from src.services.auth_service import AuthService
from .base_seeder import BaseSeeder

class UserSeeder(BaseSeeder):
    def __init__(self):
        # User data
        users_data = [
            {
                "email": "admin@example.com",
                "password": AuthService.hash_password("admin123")
            },
            {
                "email": "user@example.com",
                "password": AuthService.hash_password("user123")
            }
        ]

        # Call BaseSeeder constructor
        super().__init__(
            model_class=User,
            data=users_data,
            unique_field="email"
        )

def seed_users():
    seeder = UserSeeder()
    seeder.seed()
