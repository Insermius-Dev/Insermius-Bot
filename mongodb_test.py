import asyncio
from getpass import getpass
from urllib.parse import quote
import os

from beanie import Document, init_beanie
from motor.motor_asyncio import AsyncIOMotorClient

from dotenv import load_dotenv

load_dotenv()


class TestModel(Document):
    txtvalue: str
    numvalue: int
    boolvalue: bool


class User(Document):
    username: str
    active: bool


password = os.getenv("MONGO_PASSWORD")
username = os.getenv("MONGO_USERNAME")
host = os.getenv("MONGO_HOST")

async def main():
    conn_str = f"mongodb+srv://{username}:{quote(password)}@{host}/?retryWrites=true&w=majority"
    db = AsyncIOMotorClient(conn_str)

    await init_beanie(database=db.beanie_test, document_models=[TestModel, User])

    # print the current values in the database
    print(await db.beanie_test.list_collection_names())

    # await TestModel.delete_all()
    # tm = TestModel(name="test")
    # await tm.save()
    # print(await TestModel.find_all().to_list())

    await User.delete_all()

    await TestModel.delete_all()
    tm = TestModel(txtvalue="test1", numvalue=1, boolvalue=True)
    await tm.save()
    tm = TestModel(txtvalue="test2", numvalue=2, boolvalue=False)
    await tm.save()

    # # add a new user
    # user = User(username="Larss", active=True)
    # await user.save()

    # get bool value and num value from the users based on their txtvalue
    test_models_num = await TestModel.find(TestModel.txtvalue == "test1").to_list()
    print(test_models_num[0].numvalue)
    print(test_models_num[0].boolvalue)


if __name__ == "__main__":
    asyncio.run(main())
