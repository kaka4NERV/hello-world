from sys import exit
from textwrap import dedent


class Scene(object):

    def enter(self):
        print("Nothing there")
        exit(1)

    find_cave = False
    find_meat = False
    find_sword = False


class Engine(object):

    def __init__(self, scene_map):
        self.scene_map = scene_map

    def play(self):
        current_scene = self.scene_map.opening_scene()
        last_scene = self.scene_map.next_scene('finished')

        begeining_message()
        input("<<<请按回车继续>>>")
        while current_scene != last_scene:   # 通过结束场景后循环结束
            next_scene_name = current_scene.enter()   # 进入场景，并将通过流程后返回的场景名称字符串赋值给next_scene_name
            current_scene = self.scene_map.next_scene(next_scene_name)   # 通过传入参数将对应的场景对象赋值给current_scene

        # be sure to print out the last scene
        current_scene.enter()


class Death(Scene):

    def enter(self):
        print(dedent("""
            你进入了洞穴深处，
            发现了小女孩的衣服及尸体残肢，
            以及洞穴更深处一双幽绿的眼睛，
            一头凶恶的狼人从黑暗中向你扑来，
            没有熬制狼人药水，你的银剑只能擦伤狼人坚硬的皮毛，
            这场战斗你毫无胜算，你死了。
            你作为狩魔猎人的宿命终结于今天。
            没有人会记得你。
            """))
        return 'finished'


class Riverside(Scene):

    def enter(self):
        choice = input(dedent("""
                    调查以下线索：
                    1.血腥气息
                    2.一块不明动物的腐肉
                    3.1把玩具木剑
                    请输入数字进行选择-->
                    """))

        if choice == '1':
            return 'blood_scent'
        elif choice == '2':
            return 'broken_meat'
        elif choice == '3':
            return 'wooden_sword'
        else:
            print("请按提示进行选择！")
            return 'riverside'


class BloodScent(Scene):

    @staticmethod
    def message():
        print(dedent("""
            这气味似乎是人血，
            沿着河边一路传向远方树林中，
            最终消失在一个隐蔽的黝黑洞口前面，
            洞口里隐约传来嘶吼声以及恶臭气息，
            你不清楚里面会发生什么。
            """))

    def enter(self):
        if not Scene.find_cave:
            Scene.find_cave = True

        self.message()
        choice = input(dedent("""
                    采取以下行动：
                    1.深入洞穴
                    2.返回河边
                    请输入数字进行选择-->
                    """))
        if choice == '1':
            if Scene.find_sword:
                return 'ending02'
            elif Scene.find_meat:
                return 'ending01'
            else:
                return 'death'
        elif choice == '2':
            return 'riverside'
        else:
            print("请按提示进行选择！")
            return 'riverside'


class BrokenMeat(Scene):

    @staticmethod
    def message():
        print(dedent("""
            你无法分辨腐肉属于哪种动物，
            但直觉告诉你这不属于人类。
            你在天黑前找到了村里的猎人，
            他告诉你这闻起来像是狼肉，
            而且看起来像是狼的心脏。
            狩魔猎人们都知道，
            可以用狼的心脏作为诱饵吸引一种凶猛的怪物-狼人，
            看来这个小女孩凶多吉少了。
            """))
        input("<<<请按回车继续>>>")
        print(dedent("""
            你已经获知了这次任务可能会与狼人扯上关系，
            因此你熬制了一瓶狼人药水并涂在银剑上。
            """))
        input("<<<请按回车继续>>>")

    def enter(self):
        if not Scene.find_meat:
            Scene.find_meat = True
            self.message()
            print("你回到了河边")
            return 'riverside'
        else:
            self.message()
            if Scene.find_sword:
                return 'ending03'
            else:
                print("你回到了河边")
                return 'riverside'


class WoodenSword(Scene):

    @staticmethod
    def message():
        print(dedent("""
            你拿着木剑找到了村长，
            他认出了这是Kara的朋友Rick的。
            你来到了Rick家，他看上去惊慌而又害怕。
            他对你说，
            铁匠曾经告诉Kara河边埋有宝藏，
            于是昨晚Kara叫上他带着木剑来到河边。
            但他们只挖出了一块散发着臭气的烂肉，
            后来他看到树林中有一头直立行走的狼，
            于是害怕的一个人逃走了。
            """))
        input("<<<请按回车继续>>>")
        print(dedent("""
            你获得了两条关键信息：
            Kara遇上了狼人，恐怕已经凶多吉少；
            事情可能与铁匠有关,但你需要更多证据。
            你已经获知了这次任务可能会与狼人扯上关系，
            因此你熬制了一瓶狼人药水并涂在银剑上。
            """))
        input("<<<请按回车继续>>>")

    def enter(self):
        if not Scene.find_sword:
            Scene.find_sword = True
            self.message()
            print("你回到了河边")
            return 'riverside'
        else:
            self.message()
            if Scene.find_meat and Scene.find_cave is False:
                return 'ending03'
            else:
                print("你回到了河边")
                return 'riverside'


class Finished(Scene):

    def enter(self):
        print("游戏结束。")
        return 'finshed'


class Ending01(Scene):

    def enter(self):
        print(dedent("""
            你进入了洞穴深处，
            发现了小女孩的衣服及尸体残肢，
            以及洞穴更深处一双幽绿的眼睛，
            一头凶恶的狼人从黑暗中向你扑来，
            你与狼人展开了战斗，
            涂过狼人药剂的银剑对付狼人十分有效，
            你杀死了狼人。
            你将Kara的剩余部分用衣服包起，
            愿她能在别处安息。
            """))
        input("<<<请按回车继续>>>")
        print(dedent("""
            你将Kara的遗骸交给村长，
            并带着赏金回到了狩魔猎人城堡。
            任务结束。
            """))
        return 'finished'


class Ending02(Scene):

    def enter(self):
        print(dedent("""
            你进入了洞穴深处，
            发现了小女孩的衣服及尸体残肢，
            以及洞穴更深处一双幽绿的眼睛，
            一头凶恶的狼人从黑暗中向你扑来，
            你与狼人展开了战斗，
            涂过狼人药剂的银剑对付狼人十分有效，
            你杀死了狼人。
            你将Kara的剩余部分用衣服包起，
            愿她能在别处安息。
            """))
        input("<<<请按回车继续>>>")
        print(dedent("""
            你在狼人尸体上捡到了一件精巧的铁铸饰物，
            这种锻造技巧并不多见，
            必定和铁匠有一定关系。
            """))
        input("<<<请按回车继续>>>")
        return 'after_ending'


class Ending03(Scene):

    def enter(self):
        print(dedent("""
            你知道Kara可能已经遇害并且这事和铁匠有关，
            但当你回到河边时血腥气味已经接近消失了，
            你无法找到其他线索了，
            任务失败,你空手回到了狩魔猎人城堡。
            """))
        return 'finished'


class AfterEnding(Scene):

    def enter(self):
        print(dedent("""
            回到村子领取赏金的路上你经过了铁匠铺，
            是否进去找铁匠当面对质？
            """))
        choice = input("请输入是或否==>")

        if choice == '是':
            print(dedent("""
                铁匠承认了狼人是他儿子，
                得知儿子已经被你杀死，
                他抄起一把草叉向你发动攻击。
                很明显他不是你的对手，
                你侧身拔剑，将他刺了个对穿，
                这是他该有的下场。
                """))
            input("<<<请按回车继续>>>")
            print(dedent("""
                成为杀人凶手的你拿不到赏金了，
                并且还受到了领近村庄的通缉，
                将Kara的遗骸草草埋葬后，
                你双手空空逃回了狩魔猎人城堡。
                """))
            return 'finished'
        elif choice == '否':
            print(dedent("""
                事情该到此为止了。
                你将Kara的遗骸交给村长，
                并带着赏金回到了狩魔猎人城堡。
                """))
            return 'finished'
        else:
            print("你输入了错误的回答!")
            return 'finished'


class Map(object):

    scenes = {
        'riverside': Riverside(),
        'blood_scent': BloodScent(),
        'broken_meat': BrokenMeat(),
        'wooden_sword': WoodenSword(),
        'ending01': Ending01(),
        'ending02': Ending02(),
        'ending03': Ending03(),
        'after_ending': AfterEnding(),
        'death': Death(),
        'finished': Finished()
    }

    def __init__(self, start_scene):
        self.start_scene = start_scene

    def next_scene(self, scene_name):
        val = Map.scenes.get(scene_name)
        return val

    def opening_scene(self):
        return self.next_scene(self.start_scene)


def begeining_message():
    print(dedent("""
            你是一位狩魔猎人，
            某天你接到了溪木村村长的委托需要前来调查村里小女孩Kara的失踪事件，
            你从村口的铁匠口中了解到她经常在河边出现。
            你来到河边，运用猎人感应发现了以下3样线索，
            你闻到了一股微弱的血腥气息，
            在一堆被挖开的泥土旁有一块不明动物的腐肉，
            靠近村庄方向的地上有1把玩具木剑。
            夜晚即将降临，而且看起来似乎会下雨，
            为了防止线索消失，你应该尽快开始调查。
        """))


a_map = Map('riverside')
a_game = Engine(a_map)
a_game.play()
