import os
import motor.motor_asyncio

client = motor.motor_asyncio.AsyncIOMotorClient(os.environ["MONGODB_URL"])
db = client.AutolifyDatabase
