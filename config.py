from os import environ

# Telegram Account Api Id And Api Hash
API_ID = int(environ.get("API_ID", "13232663"))
API_HASH = environ.get("API_HASH", "d3e503e917833501c9b50a0cce8e499c")

# Your Main Bot Token 
BOT_TOKEN = environ.get("BOT_TOKEN", "7281659989:AAH2dcVYwVSokcZv-9A0tYTjrvrCf_FbhvY")

# Owner ID For Broadcasting 
OWNER_ID = int(environ.get("OWNER_ID", "7523334989")) # Owner Id or Admin Id

# Give Your Force Subscribe Channel Id Below And Make Bot Admin With Full Right.
F_SUB = environ.get("F_SUB", "")

# Mongodb Database Uri For User Data Store 
MONGO_DB_URI = environ.get("MONGO_DB_URI", "mongodb+srv://gruperolyricoficial:gruperolyricoficial@cluster0.hgonwzp.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")

# Port To Run Web Application 
PORT = int(environ.get('PORT', 8080))
