import orm
import asyncio
from models import User, Blog, Comment

async def init(loop):
    await orm.create_pool(loop=loop, user='root', password='469924', db='awesome')

    u = User(name='Test', email='test@example.com', passwd='1234567890', image='about:blank')

    await u.save()

loop = asyncio.get_event_loop()
loop.run_until_complete(init(loop))
loop.run_forever()
