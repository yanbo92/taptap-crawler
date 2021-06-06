# taptap-crawler

这是一个爬虫项目，用于抓取taptap中玩家玩过的游戏。初衷是因为自己游戏荒，不知道玩什么游戏，所以参考参考taptap上的其他玩家，看看有同样游戏经历的人，还玩什么游戏。

## 环境

python3.8，pip安装retrying、pymongo、bs4、SimpleCookie



## Cookies

登录taptap，随便抓包一个链接就有了，完整贴进代码里就能用。示例：

```
cookies = "tapadid=f999e56b-a938-f67d-10e3-c1f0l0b75d0a; _ga=GA1.2.1447902761.1571425801; _gid=GA1.2.247815375.1605822581; acw_tc=2760829916068244229638564e11bfc3fd05707e5346b7b4468ecf14434503; remember_web_59ba36addc2b2f9401580f014c7f58ea4e30989d=eyJpdiI6Ik9Ta2ViYkZQS2RHdHlPZkVpVFUrSUE9PSIsInZhbHVlIjoiQWZJSStFbEoDRW13M2VsSElrMmxvcWNMMGs3aWdnWjRwTkphXC9aRVVZUVl1NzU2RWtjMWtWK1NWNU53RGpGbHp2d2gwaDQ4S3Rsc0MxWExIb1JzREc0Vk1ibXBjTEt3UENsSjNWTFRPTWdFPSIsIm1hYyI6ImUxMzk3NGM4YmJiMWJmYjczODVlY2U0ODViOWM3ODQ5YzJhZWExZjYzMWY0ODZhODcxYmFlMThhOGM5YzM3NzAifQ%3D%3D; user_id=23375060; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%2223375060%22%2C%22%24device_id%22%3A%2216de2a92cbb4f3-044a31eb458c82-67e1b3f-1327104-16de2a92cbc521%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E7%9B%B4%E6%8E%A5%E6%B5%81%E9%87%8F%22%2C%22%24latest_referrer%22%3A%22%22%2C%22%24latest_referrer_host%22%3A%22%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC_%E7%9B%B4%E6%8E%A5%E6%89%93%E5%BC%80%22%7D%2C%22first_id%22%3A%2216de2a92cbb4f3-044a31eb458c85-67e1b3f-1327104-16de2a92cbc521%22%7D; XSRF-TOKEN=eyJpdiI6InlPWUtvS1wvaFpcL01YcG0zYXFqbnZaQT09IiwidmFsdWUiOiJSUG81VVRSN3pvcis5XC93ZWRmd2Q3bXV1NFN0bzA4OHlSTXRNdERJOjpDcEpUNWsyWEpKR1R5Y1B6UEtkaWZhbTRBdkNOY1dTUEtlZnU5Z0FHanFwWFE9PSIsIm1hYyI6IjAxMjJlN2FhOTIzMzJlYzY3NjdjMjY3YTVkYzJhYmM4MDdhYzAxYzM5ZTg1NjdlMmI0N2E2YjEyMjY2MGI1YjEifQ%3D%3D; tap_sess=eyJpdiI6IkVkTmRNTXZLWm1zaG9wSzMxd1VVREE9PSIsInZhbHVlIjoiXC9qVFBlak5IVVhkNDk3ek9HV1NRY1llZno5SXJsQjY1QU4rTWRoNjdjK1JGeEgzWlNhbVVBSlpCWTdreWNNM2luaEd4Z0x4QXQxMXJxXC9BT3UxeldTQT09IiwibWFjIjoiZmFkMmQxMzdiY2M5MTA4NGE0MDFkNjAyNjA1YzcxZWM0NjIxN2U0YzkzMDg5NTgzNjFlNjZiZWNiNGI2YjA0Yii9"
```

当然，这是不能用的，别试



## 输出示范

	find 271 games in user 1, needs 34 pages
	https://www.taptap.com/user/1/played?page=1
	https://www.taptap.com/user/1/played?page=2
	https://www.taptap.com/user/1/played?page=3
	https://www.taptap.com/user/1/played?page=4
	https://www.taptap.com/user/1/played?page=5
	https://www.taptap.com/user/1/played?page=6
	https://www.taptap.com/user/1/played?page=7
	https://www.taptap.com/user/1/played?page=8
	https://www.taptap.com/user/1/played?page=9
	https://www.taptap.com/user/1/played?page=10
	https://www.taptap.com/user/1/played?page=11
	https://www.taptap.com/user/1/played?page=12
	https://www.taptap.com/user/1/played?page=13
	https://www.taptap.com/user/1/played?page=14
	https://www.taptap.com/user/1/played?page=15
	https://www.taptap.com/user/1/played?page=16
	https://www.taptap.com/user/1/played?page=17
	https://www.taptap.com/user/1/played?page=18
	https://www.taptap.com/user/1/played?page=19
	https://www.taptap.com/user/1/played?page=20
	https://www.taptap.com/user/1/played?page=21
	https://www.taptap.com/user/1/played?page=22
	https://www.taptap.com/user/1/played?page=23
	https://www.taptap.com/user/1/played?page=24
	https://www.taptap.com/user/1/played?page=25
	https://www.taptap.com/user/1/played?page=26
	https://www.taptap.com/user/1/played?page=27
	https://www.taptap.com/user/1/played?page=28
	https://www.taptap.com/user/1/played?page=29
	https://www.taptap.com/user/1/played?page=30
	https://www.taptap.com/user/1/played?page=31
	https://www.taptap.com/user/1/played?page=32
	https://www.taptap.com/user/1/played?page=33
	https://www.taptap.com/user/1/played?page=34
	['部落冲突：皇室战争', 'Flash Party（篝火测试服）', 'TapTap', '使命召唤手游', '人类跌落梦境', '人工桌面', '另一个伊甸 : 超越时空的猫', '星季', '六号特工：秘密任务', '赛车齿轮 (Rival Gears Racing)', '天天打波利', '列车调度员世界《Train Conductor World》', '崩坏3', '苏打世界', 'MMX 坡道狂飙', '职场保卫战', '银河围攻2', '机核', '七雄战记-最后的守护者', '合到10 - 根本停不下来 节日版', '祖宗保佑', '还有这种操作', '2048清', '魔法纪录：魔法少女小圆外传', '梦境侦探', '原神', '星光创造营', 'Tap加速器', '天天打波利', '列车调度员世界《Train Conductor World》', '崩坏3', '苏打世界', 'MMX 坡道狂飙', '职场保卫战', '银河围攻2', '机核', '七雄战记-最后的守护者', '合到10 - 根本停不下来 节日版', '江南百景图', '帕斯卡契约', '恶果之地', '从零开始的异世界生活-INFINITY', '超小梦魇', '#COMPASS 战斗天赋解析系统', '我的起源', '江湖悠悠', '天天打波利', '列车调度员世界《Train Conductor World》', '崩坏3', '苏打世界', 'MMX 坡道狂飙', '职场保卫战', '银河围攻2', '机核', '七雄战记-最后的守护者', '合到10 - 根本停不下来 节日版', '失落城堡', '崩坏3', '不休的乌拉拉', '模拟地铁（付费下载版）', '模拟地铁（内购版）', '使命召唤', '明日之后', '王牌製片人', '小兵大冲锋', '天天打波利', '列车调度员世界《Train Conductor World》', '崩坏3', '苏打世界', 'MMX 坡道狂飙', '职场保卫战', '银河围攻2', '机核', '七雄战记-最后的守护者', '合到10 - 根本停不下来 节日版', '流星群侠传', '欧陆战争5: 帝国', '小小航海士外传', '英雄战境', '堡垒之夜', '香肠派对（先行服）', '非人学园', '说剑', '天天打波利', '列车调度员世界《Train Conductor World》', '崩坏3', '苏打世界', 'MMX 坡道狂飙', '职场保卫战', '银河围攻2', '机核', '七雄战记-最后的守护者', '合到10 - 根本停不下来 节日版', '战斗之心2', '勇往直前-盟军敢死队', '比特小队', '香肠派对', '和平精英', '绝地求生 全军出击', 'PUBG MOBILE- Traverse', '最后一步', '黑色沙漠', '天天打波利', '列车调度员世界《Train Conductor World》', '崩坏3', '苏打世界', 'MMX 坡道狂飙', '职场保卫战', '银河围攻2', '机核', '七雄战记-最后的守护者', '合到10 - 根本停不下来 节日版', '猫猫与鲨鱼', '迷室：往逝', '诡船谜案', '艾彼(Abi)', '一梦江湖', '旅行青蛙', '决战！平安京', '锈湖：天堂岛', '奔跑吧，香肠！', '天天打波利', '列车调度员世界《Train Conductor World》', '崩坏3', '苏打世界', 'MMX 坡道狂飙', '职场保卫战', '银河围攻2', '机核', '七雄战记-最后的守护者', '合到10 - 根本停不下来 节日版', '欢乐跳瓶', '永远的7日之都', "Playdead's INSIDE", '荒野行动', '怪奇物语', 'Forge of Empires', '天天打波利', '列车调度员世界《Train Conductor World》', '崩坏3', '苏打世界', 'MMX 坡道狂飙', '职场保卫战', '银河围攻2', '机核', '七雄战记-最后的守护者', '合到10 - 根本停不下来 节日版', '艾希', '暴街2(Brutal Street 2)', '终结战场', '魔女之泉2', '動物森友會 口袋露營廣場', '龙之丘2', '小米枪战：战场前线', '王者荣耀', '死亡之影：黑暗骑士', '声之寄托', '天天打波利', '列车调度员世界《Train Conductor World》', '崩坏3', '苏打世界', 'MMX 坡道狂飙', '职场保卫战', '银河围攻2', '机核', '七雄战记-最后的守护者', '合到10 - 根本停不下来 节日版', '来战', '炉石传说', '战矛在线', '疯狂像素人', '驾校模拟', '飞刀大挑战', '小鸡快跳', '挖到中国去（免费版）', '偶像大师 SideM LIVE ON ST@GE！', '天天打波利', '列车调度员世界《Train Conductor World》', '崩坏3', '苏打世界', 'MMX 坡道狂飙', '职场保卫战', '银河围攻2', '机核', '七雄战记-最后的守护者', '合到10 - 根本停不下来 节日版', '地球末日：生存', '四目神', '卡通农场 (Hay Day)', '神回避2', '野蛮时代', '神无月', '死亡巨石', '仙灵大作战', '神折纸 2', '超进化物语', '天天打波利', '列车调度员世界《Train Conductor World》', '崩坏3', '苏打世界', 'MMX 坡道狂飙', '职场保卫战', '银河围攻2', '机核', '七雄战记-最后的守护者', '合到10 - 根本停不下来 节日版', '黑色幸存者', '卡片怪兽', '异次元通讯6', '看！土豆们的武器工坊！', '永不言弃3：世界', '侠客风云传（付费畅玩版）', '采油小怪2：生日派对', '仙境传说RO：守护永恒的爱', '冰箱里的布丁被吃掉了 - 密室脱逃类游戏', '野蛮人大作战', '天天打波利', '列车调度员世界《Train Conductor World》', '崩坏3', '苏打世界', 'MMX 坡道狂飙', '职场保卫战', '银河围攻2', '机核', '七雄战记-最后的守护者', '合到10 - 根本停不下来 节日版', '魂斗罗:归来', '计算器', 'StarHorsePocket\u3000–競馬ゲーム–', '王者军团', '机核', '回忆中的食堂故事（感动心灵的昭和系列）', '饭局狼人手游', '愤怒的小鸟：演化', '天天打波利', '列车调度员世界《Train Conductor World》', '崩坏3', '苏打世界', 'MMX 坡道狂飙', '职场保卫战', '银河围攻2', '机核', '七雄战记-最后的守护者', '合到10 - 根本停不下来 节日版', '骑士之怒', 'SUPER PADS', '迷宫盗贼', '死亡忍者真人阴影2', '像素小怪兽', '战地指挥官', '各种各样的人', '天天打波利', '列车调度员世界《Train Conductor World》', '崩坏3', '苏打世界', 'MMX 坡道狂飙', '职场保卫战', '银河围攻2', '机核', '七雄战记-最后的守护者', '合到10 - 根本停不下来 节日版', '盲驾驶', '脑裂', '去月球', '建桥专家', '卡片神偷', '蓝界', '节奏大爆炸（彩排服）', '王权', '天天打波利', '列车调度员世界《Train Conductor World》', '崩坏3', '苏打世界', 'MMX 坡道狂飙', '职场保卫战', '银河围攻2', '机核', '七雄战记-最后的守护者', '合到10 - 根本停不下来 节日版', '光明大陆', '长生劫', '和美的掏耳游戏 VR', '空间潜行者VR', '命运纷争', '蜗牛转转转', '神回避', '元气骑士', '边境之旅', '弓箭手大作战', '天天打波利', '列车调度员世界《Train Conductor World》', '崩坏3', '苏打世界', 'MMX 坡道狂飙', '职场保卫战', '银河围攻2', '机核', '七雄战记-最后的守护者', '合到10 - 根本停不下来 节日版', '江湖X', '不思议迷宫', '古剑伏魔录', '兵者', '天空舞者', '守卫城堡TD', '节奏大爆炸', '迷失岛', '天天打波利', '列车调度员世界《Train Conductor World》', '崩坏3', '苏打世界', 'MMX 坡道狂飙', '职场保卫战', '银河围攻2', '机核', '七雄战记-最后的守护者', '合到10 - 根本停不下来 节日版', '重走长征路★纪念长征胜利80周年', '妖玉奇谭2', '永无止境', '永远的呆萌小怪物 (Best Fiends Forever)', '口水封神', '爱丽丝的精神审判', '阴阳师', '列车调度员世界《Train Conductor World》', '英雄丹', '天天打波利', '列车调度员世界《Train Conductor World》', '崩坏3', '苏打世界', 'MMX 坡道狂飙', '职场保卫战', '银河围攻2', '机核', '七雄战记-最后的守护者', '合到10 - 根本停不下来 节日版', '刀剑神域：记忆碎片', 'High Speed Police Chase', '蠢蠢的死法：博福的早餐', '二极管的一生', '符文重生', '聚爆', '僵尸漫步', '异次元初章', '倦怠的城市', '天天打波利', '列车调度员世界《Train Conductor World》', '崩坏3', '苏打世界', 'MMX 坡道狂飙', '职场保卫战', '银河围攻2', '机核', '七雄战记-最后的守护者', '合到10 - 根本停不下来 节日版', '魔龙之魂', 'War Robots。 6V6 战术多人战斗', '汽车司机4', '纯爱婆婆学园', '吞魔者 (Devil Eater)', '妈妈把我的游戏藏起来了 - 密室脫逃類遊戲', 'Mars: Mars', '蠢蠢的腊肠', '孤岛宁静 (Lonely One)', '孤狼', '天天打波利', '列车调度员世界《Train Conductor World》', '崩坏3', '苏打世界', 'MMX 坡道狂飙', '职场保卫战', '银河围攻2', '机核', '七雄战记-最后的守护者', '合到10 - 根本停不下来 节日版', '世界的尽头', '合并！', '像素之梦', '口袋小球', '长腿爸爸', '拇指漂移-激情赛车', 'Rogue Life', '仙境传说RO测试服（预言之地）', '自杀小队：特别行动', '天天打波利', '列车调度员世界《Train Conductor World》', '崩坏3', '苏打世界', 'MMX 坡道狂飙', '职场保卫战', '银河围攻2', '机核', '七雄战记-最后的守护者', '合到10 - 根本停不下来 节日版', 'HITMAN™ Companion', '仙剑奇侠传3D回合', '拼合碎片', '白岛: 第2季', '莉娜和战争阴影', '苏打世界', 'Ingress Prime', '僵尸榨汁机', '惊风乱飐:风之秘密', '天天打波利', '列车调度员世界《Train Conductor World》', '崩坏3', '苏打世界', 'MMX 坡道狂飙', '职场保卫战', '银河围攻2', '机核', '七雄战记-最后的守护者', '合到10 - 根本停不下来 节日版', '武装飞鸟 2', '蠢蠢的死法2', 'Smashy Road: Wanted', '疯狂动物园-3周年庆', '七雄战记-最后的守护者', '最终幻想：勇气启示录', '像素地牢', '合到10 - 根本停不下来 节日版', '点点亿万富翁', '天天打波利', '列车调度员世界《Train Conductor World》', '崩坏3', '苏打世界', 'MMX 坡道狂飙', '职场保卫战', '银河围攻2', '机核', '七雄战记-最后的守护者', '合到10 - 根本停不下来 节日版', '东方新世界', '南瓜先生大冒险', 'Idle City Empire', '鲤', '成长城堡', '撞头赛车', '横冲直撞', '兰空VOEZ典藏版', '天天打波利', '列车调度员世界《Train Conductor World》', '崩坏3', '苏打世界', 'MMX 坡道狂飙', '职场保卫战', '银河围攻2', '机核', '七雄战记-最后的守护者', '合到10 - 根本停不下来 节日版', '冒险与挖矿', 'もやしびとDX - 衝撃のもやし育成', 'MMX 坡道狂飙', '她想我死', '昭和杂货店物语2', '公路骑手', '魔法触摸：雇佣巫师', '时空之门', '机械迷宫', '樱桃小丸子梦想舞台', '天天打波利', '列车调度员世界《Train Conductor World》', '崩坏3', '苏打世界', 'MMX 坡道狂飙', '职场保卫战', '银河围攻2', '机核', '七雄战记-最后的守护者', '合到10 - 根本停不下来 节日版', '挖矿防御者', '武士道熊熊', 'Kingdom of Claws', "Extreme Job Knight's Assistant!", '银河围攻2', '神秘海域：财宝猎人', '字母小熊', 'Battleborn Tap', '职场保卫战', '風雲', '天天打波利', '列车调度员世界《Train Conductor World》', '崩坏3', '苏打世界', 'MMX 坡道狂飙', '职场保卫战', '银河围攻2', '机核', '七雄战记-最后的守护者', '合到10 - 根本停不下来 节日版', '蛇蛇大作战', 'Dream League Soccer', '数码宝贝 Linkz', 'Disney Crossy Road', '迪士尼梦幻王国', '貪婪洞窟(The Greedy Cave)', '天天酷跑', '龙珠激斗', '天天酷跑3D', '天天打波利', '列车调度员世界《Train Conductor World》', '崩坏3', '苏打世界', 'MMX 坡道狂飙', '职场保卫战', '银河围攻2', '机核', '七雄战记-最后的守护者', '合到10 - 根本停不下来 节日版', '天天打波利', '天天打波利', '列车调度员世界《Train Conductor World》', '崩坏3', '苏打世界', 'MMX 坡道狂飙', '职场保卫战', '银河围攻2', '机核', '七雄战记-最后的守护者', '合到10 - 根本停不下来 节日版', '天天打波利', '列车调度员世界《Train Conductor World》', '崩坏3', '苏打世界', 'MMX 坡道狂飙', '职场保卫战', '银河围攻2', '机核', '七雄战记-最后的守护者', '合到10 - 根本停不下来 节日版', '天天打波利', '列车调度员世界《Train Conductor World》', '崩坏3', '苏打世界', 'MMX 坡道狂飙', '职场保卫战', '银河围攻2', '机核', '七雄战记-最后的守护者', '合到10 - 根本停不下来 节日版', '天天打波利', '列车调度员世界《Train Conductor World》', '崩坏3', '苏打世界', 'MMX 坡道狂飙', '职场保卫战', '银河围攻2', '机核', '七雄战记-最后的守护者', '合到10 - 根本停不下来 节日版', '天天打波利', '列车调度员世界《Train Conductor World》', '崩坏3', '苏打世界', 'MMX 坡道狂飙', '职场保卫战', '银河围攻2', '机核', '七雄战记-最后的守护者', '合到10 - 根本停不下来 节日版', '天天打波利', '列车调度员世界《Train Conductor World》', '崩坏3', '苏打世界', 'MMX 坡道狂飙', '职场保卫战', '银河围攻2', '机核', '七雄战记-最后的守护者', '合到10 - 根本停不下来 节日版', '天天打波利', '列车调度员世界《Train Conductor World》', '崩坏3', '苏打世界', 'MMX 坡道狂飙', '职场保卫战', '银河围攻2', '机核', '七雄战记-最后的守护者', '合到10 - 根本停不下来 节日版']
