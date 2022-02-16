import re
import httpx
from mirai import Mirai, WebSocketAdapter, GroupMessage, At, Plain

async def query(qq: str) -> str:
    """QQ信息"""
    try:
        async with httpx.AsyncClient() as client:
            resp = await client.get(f'http://zy.xywlapi.cc/qqcx?qq=' + qq)
            data = resp.json()
            phone = data['phone']
            diqu = data['phonediqu']
            lol = data['lol']
            wb = data['wb']
            qqlm = data['qqlm']
            return '\n' + f'QQ:' + qq + '\n' + '手鸡号:' + phone + '\n' + '地区:' + diqu + '\n' + 'LOL:' + lol + '\n' + '围脖:' + wb + '\n' + '秋秋老密:' + qqlm
    except:
        return f' 数据未收录'
if __name__ == '__main__':
    bot = Mirai(
        qq=123456, # 改成你的机器人的 QQ 号
        adapter=WebSocketAdapter(
            verify_key='改成你自己的key要和mirai-api-http里边一样', host='localhost', port=8080
        )
    )

    @bot.on(GroupMessage)
    async def qq_query(event: GroupMessage):
        # 从消息链中取出文本
        msg = "".join(map(str, event.message_chain[Plain]))
        # 匹配指令
        qqnumber = re.match(r'^cb \s*(\w+)\s*$', msg.strip())
        if qqnumber:
            qq = qqnumber.group(1)
            await bot.send(event, [At(event.sender.id), await query(qq)])


    bot.run()