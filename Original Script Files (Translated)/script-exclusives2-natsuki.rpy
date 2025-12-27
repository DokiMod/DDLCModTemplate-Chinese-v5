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
    "I didn't exactly expect to be sitting this close to her, either..."
    "Not that I can say it's a particularly bad thing."
    "I open the book."
    "It's only a few seconds before Natsuki once again inches closer, reclaiming the additional space while she hopes I won't notice."
    "I can feel her peering over my shoulder, much more eager to begin reading than I am."
    n 1k "Wow, how long has it been since I read the beginning...?"
    mc "Hm?"
    mc "You don't go back and flip through the older volumes every now and then?"
    n 2k "Not really."
    n "Maybe sometimes after I've already finished the series."
    n 2c "Hey, are you paying attention?"
    mc "Uh..."
    "I am, but nothing's really happened yet, so I can talk at the same time."
    "It looks like it's about a bunch of friends in high school."
    "Typical slice-of-life affair."
    "I kind of grew out of these, since it's rare for the writing to be entertaining enough to make up for the lack of plot."
    $ persistent.clear[0] = True
    $ renpy.save_persistent()
    scene n_cg1_bg
    show n_cg1_base
    with dissolve_cg
    mc "...Are you sure this isn't boring for you?"
    n "It's not!"
    mc "Even though you're just watching me read?"
    n "Well...!"
    n "I'm...fine with that."
    mc "If you say so..."
    mc "...I guess it's fun sharing something you like with someone else."
    mc "I always get excited when I convince any of my friends to pick up a series I enjoy."
    mc "You know what I mean?"
    n "...?"
    mc "Hm?"
    mc "You don't?"
    show n_cg1_exp2 at cgfade
    n "Um..."
    n "That's not..."
    n "Well, I wouldn't really know."
    mc "...What do you mean?"
    mc "Don't you share your manga with your friends?"
    hide n_cg1_exp2
    show n_cg1_exp3 at cgfade
    n "Could you not rub it in?"
    n "Jeez..."
    mc "Ah... Sorry..."
    n "Hmph."
    n "Like I could ever get my friends to read this..."
    n "They just think manga is for kids."
    n "I can't even bring it up without them being all like..."
    n "'Eh? You still haven't grown out of that yet?'"
    n "Makes me want to punch them in the face..."
    mc "Urgh, I know those kinds of people..."
    mc "Honestly, it takes a lot of effort to find friends who don't judge, much less friends who are also into it..."
    mc "I'm already kind of a loser, so I guess I gravitated toward the other losers over time."
    mc "But it's probably harder for someone like you..."
    hide n_cg1_exp3
    n "Hm."
    n "Yeah, that's pretty accurate."
    "{i}...Wait, which part??{/i}"
    $ style.say_dialogue = style.normal
    n "I mean, I feel like I can't even keep it in my own room..."

    $ style.say_dialogue = style.edited
    n "要是被我爸发现这些，他铁定把我打到半死。"
    $ style.say_dialogue = style.normal
    $ _history_list[-1].what = "我根本不知道我爸发现这些后会怎么样。"
    n "At least it's safe here in the clubroom."
    show n_cg1_exp3 at cgfade
    n "'Cept Monika's kind of a jerk about it..."
    n "Ugh! I just can't win, can I?"
    mc "Well, it paid off in the end, didn't it?"
    mc "I mean, here I am, reading it."
    n "Well, it's not like that solves any of my problems."
    mc "Maybe..."
    mc "But at least you're enjoying yourself, right?"
    hide n_cg1_exp3
    show n_cg1_exp2 at cgfade
    n "——"
    n "......"
    n "......所以呢？"
    mc "啊哈哈。"
    hide n_cg1_exp2
    show n_cg1_exp3 at cgfade
    n "Jeez, that's enough!"
    n "Are you gonna keep reading, or what?"
    mc "Yeah, yeah..."
    "I flip the page."
    show black with dissolve_cg
    "......"
    "......"
    "....."
    "......."
    "........."
    "Time passes."
    hide n_cg1_exp3
    show n_cg1_exp4 behind black at cgfade
    "Natsuki is strangely quiet now."
    "I glance over at her."
    hide black with dissolve_cg
    "It looks like she's started to fall asleep."
    mc "嘿，夏树......"
    hide n_cg1_exp4
    show n_cg1_exp5 at cgfade
    n "Y-Yeah...?"
    "Suddenly, Natsuki collapses straight into me."
    play sound fall
    $ style.say_dialogue = style.normal
    mc "H-Hey--"
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
    "Monika reaches into her bag and pulls out some kind of protein bar."
    "She throws it in Natsuki's direction."
    "Natsuki's eyes suddenly light up again."
    "She snatches the bar from the floor and immediately tears off the wrapper."
    show natsuki zorder 3 at f22
    n 1s "我不是跟你说过别让我吃唔……"
    show natsuki zorder 2 at t22
    "She doesn't even finish her sentence before stuffing it into her mouth."
    show natsuki zorder 1 at thide
    hide natsuki
    show monika 3b zorder 2 at t11
    m "Don't worry, [player]."
    m "她没事的。"
    m "It just happens every now and then."
    m 1a "That's why I always keep a snack in my bag for her."
    m 5a "话说回来......！"
    m "Why don't we all share poems now?"

    return

