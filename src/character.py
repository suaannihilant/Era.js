import random
import engine.game as g


def init_character():
    character = {
        # 灵
        '姓名': '',
        '系统身份': '',  # '主角'/''
        'hash': g.get_hash(),
        '等级': 0,
        # 称呼
        '系统称呼': '',
        '自称': '',
        '尊称': '',
        '蔑称': '',
        '职业': '',
        '精力': 100,
        '精力上限': 100,
        # 关系
        '父亲': '',
        '母亲': '',
        '子女': [],
        '恋人': [],
        '妻子': [],
        '朋友': [],
        '仇人': [],
        '宝珠': [],
        '属性': [],
        '刻印': [],
        '性格': [],
        '技能': [],
        '魔法': [],
        '后天': [],
        '履历': [],
        # 肉
        '性别': '',
        '种族': '',
        '体力': 100,
        '体力上限': 100,
        '耐力': 100,
        '耐力上限': 100,
        '体型': '',
        '身高': 150,
        '体重': 50,
        '胸围': 50,
        '腰围': 50,
        '臀围': 50,
        '罩杯': 'A',
        '力量': 0,
        '敏捷': 0,
        '体质': [],
        # 服装
        # 内
        '内衣': '',
        '内裤': '',
        '袜子': '',
        # 中
        '帽子': '',
        '面具': '',
        '衣服': '',
        '手套': '',
        '裤子': '',
        '鞋子': '',
        # 外
        '外套': '',
        '项链': '',
        '手镯': [],
        '戒指': [],
        ##
        '纹身': [],
        # 装备
        '头部': '',
        '面部': '',
        '颈部': '',
        '上身': '',
        '左手': '',
        '右手': '',
        '双手': '',
        '手指': [],
        '下身': '',
        '脚部': '',
        '背包': [],
        '金钱': 0,

    }
    return character


def default_character():
    character = init_character()
    character['姓名'] = random.choice(g.data['姓名库']['中文']['姓'])
    character['姓名'] += random.choice(g.data['姓名库']['中文']['男名'])
    character['系统称呼'] = '你'
    return character


def get_player():
    for character in g.data['人物库']:
        if character['系统身份'] == '主角':
            return character
    return False