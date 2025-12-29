init python:
    class RectCluster(object):
        def __init__(self, theDisplayable, numRects=12, areaWidth = 30, areaHeight = 30):
            self.sm = SpriteManager(update=self.update)
            self.rects = [ ]
            self.displayable = theDisplayable
            self.numRects = numRects
            self.areaWidth = areaWidth
            self.areaHeight = areaHeight
            
            for i in range(self.numRects):
                self.add(self.displayable)
        
        def add(self, d):
            s = self.sm.create(d)
            s.x = (random.random() - 0.5) * self.areaWidth * 2
            s.y = (random.random() - 0.5) * self.areaHeight * 2
            s.width = random.random() * self.areaWidth / 2
            s.height = random.random() * self.areaHeight / 2
            self.rects.append(s)
        
        def update(self, st):
            for s in self.rects:
                s.x = (random.random() - 0.5) * self.areaWidth * 2
                s.y = (random.random() - 0.5) * self.areaHeight * 2
                s.width = random.random() * self.areaWidth / 2
                s.height = random.random() * self.areaHeight / 2
            return 0

image n_rects_ghost1:
    RectCluster(Solid("#000"), 4, 15, 5).sm
    pos (580, 270)
    size (20, 25)
    alpha 0.0
    8.0
    easeout 12 alpha 1.0

image n_rects_ghost2:
    RectCluster(Solid("#000"), 4, 15, 5).sm
    pos (652, 264)
    size (20, 25)
    alpha 0.0
    8.0
    easeout 12 alpha 1.0

image n_rects_ghost3:
    RectCluster(Solid("#000"), 4, 15, 5).sm
    pos (616, 310)
    size (25, 15)
    alpha 0.0
    8.0
    easeout 12 alpha 1.0

image n_rects_ghost4:
    RectCluster(Solid("#000"), 4, 15, 5).sm
    pos (735, 310)
    size (25, 20)
    0.5
    easeout 0.25 zoom 4.5 xoffset 250 yoffset -250

image n_rects_ghost5:
    RectCluster(Solid("#000"), 4, 15, 5).sm
    pos (740, 376)
    size (25, 20)
    0.5
    easeout 0.25 zoom 4.5 xoffset 250 yoffset -100

label natsuki_exclusive2_1:
    scene bg club_day
    with wipeleft_scene
    n "呃......！"
    "我听见夏树在储藏间里发出了窝火的叹息。"
    "看来她似乎正在为某些事情气恼不已。"
    "我走过去，看看能不能帮上忙。"
    play music t6 fadeout 1
    scene bg closet
    show natsuki 4r zorder 2 at t11
    with wipeleft_scene
    $ style.say_dialogue = style.normal
    mc "你是在找什么东西吗？"
    $ style.say_dialogue = style.edited
    n 4x "莫妮卡我丢你老莫莫莫莫莫莫莫莫莫莫莫莫莫莫莫莫莫莫莫莫莫莫莫莫莫莫莫莫莫莫莫莫莫莫莫莫莫莫莫莫莫莫莫莫莫莫莫莫莫莫莫莫莫莫莫莫莫莫莫"
    $ style.say_dialogue = style.normal
    $ _history_list[-1].what = "可恶的莫妮卡......"
    n "每次都不把我的东西放回原位！"
    n "如果老是有人乱摆你的东西，那么整理起来又有什么意义啊？"
    "夏树将叠成一摞的书本和套装盒推到书架另一头。"
    mc "漫画啊......"
    n 2c "我记得你也看漫画，对吧？"
    mc "啊——"
    mc "......偶尔吧......"
    "漫画这种东西，在弄清楚对方的态度前，你不能直接承认自己非常喜欢。"
    mc "......话说你是怎么知道的？"
    n 2k "我之前听你提起过。"
    n "更何况，你脸上都快把‘我喜欢看漫画’几个字给写出来了。"
    "这是想表达什么意思......？"
    mc "我、我明白了......"
    "在其中一层书架的一边，一摞杂七杂八的书中夹着一卷孤零零的漫画。"
    "我有点好奇，把它从把书堆里抽了出来。"
    n 1b "原来在{i}这里{/i}！"
    "夏树从我手里抢过了那卷漫画。"
    "接着她转过身，把那本漫画按照集数插回漫画盒中。"
    n 4d "啊哈，这下好多了！"
    n "看见一套漫画缺了一本，大概是世上最恼人的景象了。"
    mc "我懂这种感觉......"
    "我凑近看了眼她正欣赏着的这套漫画。"
    mc "《芭菲女孩》......？"
    "我从没听说过这个系列。"
    "这意味着，这漫画要么完全不在我的品味版图上，要么就是个粪作。"
    n 5g "你要是想指点江山的话，就到那扇门外头去，隔着门上的玻璃说去吧。"
    "她指着教室门。"
    mc "喂、喂，我可没有要指点江山......！"
    mc "我还什么都没说呢。"
    n 5c "你的语调已经表达出来了。"
    $ style.say_dialogue = style.normal
    n "不过 [player]，我得先告诉你一件事。"
    n 4l "你就把这句话当作是文学部给你上的一课吧：{nw}"
    $ _history_list[-1].what = "你就把这句话当作是文学部给你上的一课吧：不要以貌取书！"
    $ style.say_dialogue = style.edited
    n "不要以貌取取取取取取取取取取取取取取取取取取 取取取取 取取{space=20}取{space=40}取{space=120}取{space=160}取{space=200}取"
    $ style.say_dialogue = style.normal
    $ _history_list.pop()
    n "实际上——"
    "夏树从盒子里抽出《芭菲女孩》的第一卷。"
    n "我现在就可以告诉你，为什么是这个道理！"
    "她把漫画塞进我的手里。"
    mc "啊......"
    "我看着封面。"
    "上面画着四个盛装打扮的美少女，每个都摆出动漫女角色特有的妩媚姿势。"
    "这个......‘萌’得实在过头了。"
    n 4b "别傻站着啊！"
    mc "呜哇——"
    show natsuki zorder 1 at thide
    hide natsuki
    "夏树抓着我的手臂把我拖出了储藏间。"
    "然后她挨着墙坐在了窗沿底下。"
    "她拍了拍身边的地面，示意我坐在那里。"
    show bg club_day
    show natsuki 2a zorder 2 at t11
    with wipeleft
    mc "坐椅子上不是更舒服么......？"
    "我坐了下来。"
    n 2k "椅子不行。"
    n "那样我们俩就没法一起看了。"
    mc "诶？为什么？"
    mc "啊......我知道了，这样就能凑得更近一点吧......"
    n 2o "——！"
    n 5r "不、不要直接说出来嘛！"
    n "你弄得我都觉得怪怪的了！"
    "夏树交叉着双臂，挪远了一些。"
    mc "抱歉......"
    show natsuki 5g
    "我也没想到会和她坐得这么近......"
    "虽然这样也不坏啦。"
    "我打开了漫画。"
    "没过几秒，夏树又悄悄地挪近了几寸，以为我没有发现她偷偷缩小了我们俩之间的距离。"
    "我能感觉到她的视线越过了我的肩膀，想必她比我更想看这本漫画。"
    n 1k "哇，我有多久没读过这卷漫画的开头了......？"
    mc "嗯？"
    mc "你不会时不时回头翻一翻前面几卷吗？"
    n 2k "那倒也不一定。"
    n "可能等到读完整个系列，会回头看一下。"
    n 2c "喂，你有在认真看漫画吗？"
    mc "呃......"
    "我正在看，但是没什么特别的桥段，所以我可以一边看一边聊天。"
    "这部漫画似乎就是讲一群高中生的故事。"
    "典型的日常漫画剧情。"
    "我自己有些厌倦日常系的作品了，因为就算故事再有趣，也很少能弥补主线剧情缺失这一不足。"
    $ persistent.clear[0] = True
    $ renpy.save_persistent()
    scene n_cg1_bg
    show n_cg1_base
    with dissolve_cg
    mc "......你这样坐着不觉得无聊吗？"
    n "并没有！"
    mc "即便你只是在这看着我读？"
    n "这个嘛......！"
    n "我......觉得还好啊。"
    mc "既然你都这么说了......"
    mc "......把自己喜欢的作品推荐给别人，确实是件挺有趣的事。"
    mc "如果能让朋友开始看我喜欢的漫画，我也会很开心的。"
    mc "懂我意思吧？"
    n "......？"
    mc "嗯？"
    mc "不是这样吗？"
    show n_cg1_exp2 at cgfade
    n "唔......"
    n "我......"
    n "我也不是很清楚。"
    mc "......什么？"
    mc "你都不和自己的朋友一起看漫画吗？"
    hide n_cg1_exp2
    show n_cg1_exp3 at cgfade
    n "你能别在我伤口上撒盐吗？"
    n "真是的......"
    mc "啊......对不起......"
    n "哼。"
    n "说得好像我就能成功推荐朋友看漫画似的......"
    n "他们都觉得漫画是给小屁孩看的。"
    n "每当我提起漫画，他们就一脸震惊的样子，仿佛在说什么："
    n "‘诶？你都这个年龄了还看这种东西吗？’"
    n "让我超想揍爆他们的脸......"
    mc "呃，我刚好也认识这种人......"
    mc "说真的，能找到一个不对你的爱好评头论足的朋友已经够难了，更别说有着同样爱好的朋友了......"
    mc "我本来就是个失败者，所以身边也聚集着很多同类。"
    mc "但对你这样的人来说可能会难一点......"
    hide n_cg1_exp3
    n "嗯。"
    n "好吧，你说得还挺准确的。"
    "{i}......等会儿，她说的‘很准确’到底指的是哪部分啊？？{/i}"
    $ style.say_dialogue = style.normal
    n "我是说，我甚至都没法把漫画放在自己房间里......"

    $ style.say_dialogue = style.edited
    n "要是被我爸发现这些，他铁定把我打到半死。"
    $ style.say_dialogue = style.normal
    $ _history_list[-1].what = "我根本不知道我爸发现这些后会怎么样。"
    n "至少放在部室里挺安全的。"
    show n_cg1_exp3 at cgfade
    n "虽说这里有莫妮卡那个讨人厌的家伙......"
    n "呃、可恶！我难道就不能赢那家伙一次吗？"
    mc "没事啦，你把漫画放在这里，不是也得到回报了吗？"
    mc "你看，现在我不是正在这里读着吗？"
    n "哼，可是这又没解决我的任何问题。"
    mc "也许吧......"
    mc "但至少你也乐在其中，不是吗？"
    hide n_cg1_exp3
    show n_cg1_exp2 at cgfade
    n "——"
    n "......"
    n "......所以呢？"
    mc "啊哈哈。"
    hide n_cg1_exp2
    show n_cg1_exp3 at cgfade
    n "天哪，真的够了！"
    n "所以你到底还读不读了？"
    mc "好吧，好吧......"
    "我又翻了一页。"
    show black with dissolve_cg
    "......"
    "......"
    "........"
    ".........."
    "............"
    "时间就这样流逝着。"
    hide n_cg1_exp3
    show n_cg1_exp4 behind black at cgfade
    "夏树现在出奇地安静。"
    "我悄悄瞥了她一眼。"
    hide black with dissolve_cg
    "她似乎快要睡着了。"
    mc "嘿，夏树......"
    hide n_cg1_exp4
    show n_cg1_exp5 at cgfade
    n "嗯、嗯......？"
    "突然间，夏树直接倒在了我身上。"
    play sound fall
    $ style.say_dialogue = style.normal
    mc "喂、喂——"
    show n_cg1_exp5
    hide n_cg1_exp5

    show n_cg1b
    hide n_cg1_base

    $ currentpos = get_pos()
    $ audio.t6g = "<from " + str(currentpos) + " loop 10.893>bgm/6g.ogg"
    play music t6g
    $ ntext = glitchtext(96)
    $ style.say_dialogue = style.edited
    n "{color=#000}[ntext]{/color}"
    $ ntext = glitchtext(96)
    n "{color=#000}[ntext]{/color}"
    $ style.say_dialogue = style.normal

    stop music
    window hide(None)
    window auto
    scene bg club_day
    show monika 1r zorder 2 at t11
    m "哦天哪......"
    m 1d "夏树，你还好吗？"
    show monika zorder 2 at t21
    show natsuki 12b zorder 3 at f22
    n "......"
    show natsuki zorder 2 at t22
    show monika zorder 3 at f21
    m 1a "给你......"
    show monika zorder 2 at t21
    "莫妮卡从她的包里拿出一根像是能量棒的东西。"
    "然后她把这东西丢给了夏树。"
    "夏树的眼睛一下子又泛起了神采。"
    "她猛地一把抓起地上的能量棒，立刻扯掉了外包装。"
    show natsuki zorder 3 at f22
    n 1s "我不是跟你说过别让我吃——唔......"
    show natsuki zorder 2 at t22
    "她连话都没说完，就把那东西塞到了嘴里。"
    show natsuki zorder 1 at thide
    hide natsuki
    show monika 3b zorder 2 at t11
    m "[player]，不用担心。"
    m "她没事的。"
    m "只是时不时会出现这样的情况。"
    m 1a "所以我都会在包里为她备着一些零食。"
    m 5a "那么......！"
    m "要不我们现在来分享一下自己的诗吧？"

    return

