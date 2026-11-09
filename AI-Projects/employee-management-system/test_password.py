from security.token import (
    create_access_token,
    verify_access_token
)

token = create_access_token(
    user_email="admin@gmail.com",
    role="admin"
)

print("Generated JWT:")
print(token)

decoded = verify_access_token(token)

print("\nDecoded payload:")
print(decoded)

invalid_token = verify_access_token("invalid.token.value")

print("\nInvalid token:")
print(invalid_token)