from pymongo import MongoClient
import urllib.parse

# MongoDB Credentials
MONGO_USERNAME = "afnan1663"
MONGO_PASSWORD = urllib.parse.quote_plus("afnan9945100950")  # Replace with your password
MONGO_CLUSTER = "khans.0g6sq.mongodb.net"
MONGO_DB_NAME = "AadhaarDB"

# MongoDB Connection String
MONGO_URI = f"mongodb+srv://{MONGO_USERNAME}:{MONGO_PASSWORD}@{MONGO_CLUSTER}/{MONGO_DB_NAME}?retryWrites=true&w=majority&appName=khans"
try:
    client = MongoClient(MONGO_URI, serverSelectionTimeoutMS=60000)
    db = client[MONGO_DB_NAME]  # Access the database
    users_collection = db["users"]  # ✅ Ensure this is defined
    print("✅ Connected to MongoDB Atlas!")
except Exception as e:
    print(f"❌ MongoDB Connection Failed: {e}")
    client = None

# Export the collections
__all__ = ["users_collection"]  # ✅ Explicitly declare exports
