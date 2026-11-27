from config.settings import settings

print("Database configured:", bool(settings.DATABASE_URL))
print("JWT secret configured:", bool(settings.JWT_SECRET))
print("JWT algorithm:", settings.JWT_ALGORITHM)

print(
    "Token expiration:",
    settings.ACCESS_TOKEN_EXPIRE_MINUTES
)