from asyncio import sleep
from dispatch import Dispatch


@Dispatch
async def msg(text):
    await sleep(2)
    print(text)


@Dispatch
async def long_operation():
    print('long_operation started')
    await sleep(5)
    print('long_operation finished')


@Dispatch
async def main():
    await msg('first')

    long_operation()

    await msg('second')

    await long_operation()


if __name__ == "__main__":
    main()
