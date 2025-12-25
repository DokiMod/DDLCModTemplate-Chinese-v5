image sayori end-glitch:
    "sayori/end-glitch1.png"
    0.15
    "sayori/end-glitch2.png"
    0.15
    "sayori/end-glitch1.png"
    0.15
    "sayori/end-glitch2.png"
    1.00
    "sayori/end-glitch1.png"
    0.15
    "sayori/end-glitch2.png"
    0.15
    "sayori/end-glitch1.png"
    0.15
    "sayori/end-glitch2.png"

label ch40_main:
    $ s_name = "纱世里"
    stop music fadeout 2.0
    scene bg residential_day
    with dissolve_scene_full

    python:
        if not persistent.monika_back:
            try:
                renpy.file("../characters/monika.chr")
                renpy.call_screen("dialog", message="请不要再玩弄我的心了。\n我真的不想回来。", ok_action=Return())
                persistent.monika_back = True
            except:
                pass

    $ delete_character("monika")
    play music t2
    "今天是个平凡的上学日，和往常没什么两样。"
    "一如既往，我被结伴上学的情侣和小团体包围着走到学校。"
    "我经常告诉自己，差不多是时候找一个女朋友什么的了......"
    show sayori 1a at t11
    s "嘿，[player]......"
    "......好吧，我身边已经有一个女孩了。"
    "她叫纱世里，我的邻居，也是我的儿时玩伴。"
    "我们以前经常每天结伴上学......"
    "......最近，我们又开始结伴上学了。"
    s "[player]，你为我骄傲吗？"
    mc "诶？骄傲什么？"
    s 1c "就是......"
    s "我最近每天都能按时起床！"
    mc "这个嘛，好吧，你确实保持了有一阵子了......"
    s "没错吧！"
    s 4h "但你连提都不提欸！"
    show sayori at s11
    s "我们明明每天都一起上学......"
    mc "呃，嗯......"
    mc "我还以为这种事情不言自明呢。"
    mc "要我说出口实在很难为情耶。"
    s 1d "拜托，求你了好吗？"
    s "就当是给我鼓励嘛~"
    mc "好吧，好吧......"
    mc "纱世里，我为你骄傲。"
    show sayori at t11
    s 1q "诶嘿嘿~"
    show sayori zorder 1 at thide
    hide sayori
    "我们穿过马路，继续向学校走去。"
    "接近学校，路上熙熙攘攘的学生也愈发挤满了街道。"
    show sayori 3a zorder 2 at t11
    s "话说回来，[player]......"
    s "你决定好加入什么社团了吗？"
    mc "社团？"
    mc "我早就跟你说过了，我对加入社团什么的没——"
    "我正要搬出那一套说辞——说我对加入任何社团都没兴趣。"
    "但我意识到这样说会更加伤到纱世里的心。"
    "我怎么能在这种时候跟她说，社团什么的根本是浪费时间呢......"
    "......毕竟她自己就在建立一个社团啊。"
    mc "......好吧，其实还是有兴趣的。"
    mc "我想我已经决定好要参加哪个社团了。"
    show sayori at h11
    s 1m "真的吗？！"
    s 1r "哪个社团？告诉我告诉我！"
    mc "嗯......"
    mc "这个就留作惊喜吧。"
    s 5d "切......"
    s "小气鬼！"
    mc "耐心点啦，你很快就知道了。"
    "我过去常常问自己，为什么我会任由自己让这么一个无忧无虑的女孩给说教。"
    "但我后来明白了，某种方面来说，我挺羡慕她。"
    "当纱世里一心一意地去做某件事时，她可以做出很漂亮的成绩。"
    "因此，我觉得自己也应该为她做点什么。"

    scene bg class_day
    with wipeleft_scene

    "在学校的日子和往常一样平淡，不知不觉就结束了。"
    "整理完书包后，我站起身，想给自己找点动力。"
    mc "那么......"
    stop music fadeout 2.0

    scene bg corridor
    with wipeleft_scene
    "我试着回忆起自己在社团宣传单上看到的房间号。"
    "我穿过校园，走上楼梯，登上了我很少涉足的楼层——这里通常只供高三学生上课和社团活动使用。"
    "没用多久，我就找到了那间教室。"
    "我诚惶诚恐地打开了面前的门。"
    scene bg club_day
    with wipeleft
    play music t3
    mc "哈喽......？"
    show sayori 1m at t32
    s "啊！"
    s "[player]......？！"
    s 1c "你、你怎么来了？"
    mc "呃......我只是——"
    "欸？我扫视了一遍教室。"
    show natsuki 3a at f31
    n "哈。"
    n "所以你就是纱世里天天挂在嘴边的那个 [player] 吗？"
    show natsuki at t31
    show yuri 2t at f33
    y "欢、欢迎！"
    y 2m "很高兴认识你，[player]。"
    y "这里是文学部。"
    y 3v "希、希望这次的来访能让你愉快。"
    show yuri at t33
    show natsuki at f31
    n 3g "拜托，优里......"
    n "没必要整得这么正式嘛。"
    n "他会以为我们这里很严格的......"
    show natsuki at t31
    $ y_name = "优里"
    $ n_name = "夏树"
    show yuri at f33
    y 3q "啊......"
    y "抱歉，夏树......"
    show yuri at t33
    "那个高个子的女孩就是优里，似乎比其他人要害羞很多。"
    "相反，那个叫做夏树的女孩，尽管个子娇小，但却感觉更有气势一些。"
    mc "嗯，很高兴认识你们俩。"
    mc "期待能和你们友好相处。"
    show sayori at f32
    s 1n "友、友好相处......？"
    s 1b "[player]，难道说......"
    s "你......"
    show sayori at t32
    mc "是的。"
    mc "纱世里，我想加入的社团就是你的社团。"
    mc "就是文学部。"
    "纱世里的眼睛泛起了光彩。"
    show sayori at f32
    s 1n "......不会吧。"
    s 1s "不会吧！"
    show sayori at hf32
    s 4s "哇啊啊啊啊！"
    "纱世里搂着我蹦达了起来。"
    show sayori at t32
    mc "喂、喂——"
    show natsuki at f31
    n 3y "欸嘿嘿。"
    n "好吧，既然纱世里这么高兴，我相信让你加入应该也没什么不好的。"
    show natsuki 3a at t31
    show yuri at f33
    y 1s "更别说现在我们凑齐四个人了。"
    y "这就意味着，文学部现在算是正式成立了。"
    show yuri at t33
    show sayori at f32
    s 1x "我都不知道该说些什么了！"
    s "必须庆祝一下！"
    show sayori at t32
    show yuri at f33
    y 1m "呼呼。"
    y "What an appropriate day for that, isn't it?"
    show yuri 1a at t33
    show sayori at f32
    s 1r "Yeah!"
    s 1x "After all, Natsuki decided to--"
    show sayori at t32
    show natsuki at f31
    n 1w "Hey, don't ruin the surprise!"
    show natsuki at t31
    show sayori at f32
    s 5a "Ehehe, sorry..."
    show sayori at t32
    show natsuki at f31
    n 1k "Everyone sit down at the table, okay?"
    show natsuki at t31
    show yuri at f33
    y 1a "How about I make some tea as well?"
    hide sayori
    hide natsuki
    hide yuri
    with wipeleft
    "女孩们把几张课桌拼成了一张大桌子。"
    "与此同时，夏树和优里走到了房间的角落，夏树端出来一个盖好的托盘，而优里打开了储藏间。"
    "我还是觉得有些尴尬，于是就坐在了纱世里的旁边。"
    "夏树端着托盘，趾高气扬地走了回来。"
    show natsuki 2z zorder 2 at t22
    n "好——咯，准备好了吗？"
    n "...锵锵！"
    show sayori 4m zorder 2 at t21
    s "哇哦——！"
    "夏树掀开了盖在托盘上的锡箔纸，托盘上放着十二个小猫形状的雪白松软的小蛋糕。"
    "她用糖霜画出了小猫的胡须，还用小片的巧克力做了耳朵。"
    show sayori at f21
    s 4r "好可爱呀~！"
    show sayori at t21
    mc "哇哦，看上去很不错诶。"
    show natsuki at f22
    n 2d "嗯哼哼，没想到吧。"
    n "赶紧尝一下吧！"
    show natsuki at t22
    "纱世里马上拿起了一块，然后是我。"
    show sayori at f21
    s 4q "超好吃！"
    show sayori at t21
    "纱世里脸上沾满了糖霜，满嘴都是蛋糕，边吃边称赞着。"
    "我把蛋糕放在手里转了一圈，想找一个合适的角度下口。"
    show sayori zorder 1 at thide
    hide sayori
    show natsuki 1c zorder 2 at t32
    "夏树默不作声。"
    "我不禁注意到了她偷偷瞄向我的视线。"
    "她是在等我咬下去么？"
    "我终于咬下了一口。"
    "糖霜甜度正好，风味十足——这真的是她自己做的吗？"
    mc "真的很好吃欸。"
    mc "谢谢你，夏树。"
    n 42c "嗯、嗯......那当然啦！"
    n "毕竟，我可是专家啊！"
    n 42a "没必要感谢我什么的......"
    show natsuki zorder 1 at thide
    hide natsuki
    "夏树扭扭捏捏地接受了称赞，而此时优里也端着一套茶具回到了桌旁。"
    "她小心翼翼地在每个人面前摆好一个茶杯，然后将茶壶放在托盘旁边。"
    show yuri 1a zorder 2 at t11
    mc "你居然在部室里放了一整套茶具？"
    y "别担心，老师同意过了。"
    y "何况，热茶配好书，不也很美妙吗？"
    mc "啊...想必——也对......"
    show natsuki 2y at f31
    n "Ehehe. Already trying to impress our new member, Yuri?"
    show natsuki at t31
    show yuri at f11
    y 3n "诶？！不、不是这样的......"
    show yuri at t11
    show natsuki at thide
    hide natsuki
    "优里难堪地把脸别了过去。"
    y 4b "我的意思是，那个......"
    mc "我相信你。"
    mc "嗯，阅读和品茶或许不是我的消遣方式，但我起码还蛮喜欢喝茶。"
    y 2u "那就好......"
    "优里宽慰地浅浅一笑。"
    y 1a "所以说，[player]，你平时都喜欢读些什么呢？"
    mc "这个......啊......"
    "考虑到我过去几年匮乏的阅读量，我真的不知道该如何回答。"
    mc "......漫画吧......"
    "我半开玩笑地小声嘀咕着。"
    show natsuki 1c zorder 2 at t41
    "夏树突然抬起了头。"
    "她似乎想说些什么，不过最后还是选择了沉默。"
    show natsuki zorder 1 at thide
    hide natsuki
    y 3u "你、你好像并不算是喜欢阅读的样子呢......"
    mc "......呃，也不是不能改啦......"
    "我到底在说什么啊？"
    "看到优里的苦笑，我没经大脑就把这句话说出来了。"
    mc "话说回来，优里，你喜欢读些什么呢？"
    y 1l "嗯，让我想想..."
    "优里的指尖描划着茶杯边缘。"
    y 1a "我最喜欢的是那种世界观深邃复杂的幻想小说。"
    y "这类文学背后的创意和匠心，真的让我大开眼界。"
    y 1f "而且，能在那样陌生的世界观下叙述好一个故事，也同样令人钦佩。"
    "优里滔滔不绝地说着，她显然对阅读充满了热情。"
    "尽管她从我步入社团的那一刻起就表现得内向羞怯，但从她闪闪发亮的双眼可以看得出来，比起现实的人际关系，她更喜欢在书中寻求安慰。"
    y 2m "不过嘛，我喜好的类型还有很多。"
    y 2a "Don't feel intimidated if you don't read much, okay?"
    y "I'm certain we can find something that we have in common."
    show yuri at t22
    show natsuki 2c at f21
    n "Hey, Yuri..."
    show natsuki at t21
    show yuri at f22
    y 2f "Eh?"
    show yuri at t22
    show natsuki at f21
    n 2h "Well, about...you know, the first thing he said..."
    show natsuki at t21
    mc "漫画吗？"
    show yuri at f22
    y 2i "That's right..."
    y "Natsuki tends to read manga in the clubroom--"
    show yuri at t22
    show natsuki at f21
    n 1r "D-Don't just say it!!"
    "For some reason, Natsuki seems embarrassed about it."
    n 1q "Besides..."
    n "Manga...is literature too, you know?"
    n 1w "So...if [player] wants to read some of my manga, then don't try to stop him or anything!"
    show natsuki 1i at t21
    show yuri at f22
    y 1l "Natsuki..."
    y "I wouldn't do such a thing."
    y 1i "However, it could also be nice for us to diversify ourselves a little..."
    y "He can take this opportunity to try something new, as well."
    y 1s "Wouldn't you agree, [player]?"
    show yuri at t33
    show natsuki at t32
    show sayori 1l at f31
    s "M-Maybe--"
    "Sensing the tension, Sayori jumps in."
    s 1x "Maybe we can all try something new!"
    s 1l "I think it could be fun..."
    s 1c "And we'll all get to know each other a little bit better, too!"
    s 1l "I mean..."
    s "That's the kind of thing literature clubs do...right?"
    show sayori at t31
    show yuri at f33
    y 1v "..."
    y "I-I don't disagree or anything..."
    show yuri at t33
    show natsuki at f32
    n 2j "Yeah..."
    n "You're right as usual, President."
    show natsuki at t32
    show sayori at f31
    s 1q "Ehehe~"
    show sayori at t31
    show natsuki at f32
    n 2c "Guess that means I should try picking up a novel or something, huh...?"
    show natsuki at t32
    mc "Well, that would make two of us..."
    mc "I wouldn't mind doing it if I'm not the only one."
    show sayori at thide
    hide sayori
    show natsuki at f21
    show yuri at t22
    n 2y "Then as for Yuri..."
    show natsuki at t21
    show yuri at f22
    y 2n "Eh...?"
    y "I...I have to read manga...?"
    show yuri at t22
    show natsuki at f21
    n 4i "Jeez..."
    n 4h "You were the one who suggested we diversify!"
    n "You should be a little more open-minded..."
    n 4u "It's kind of hurtful..."
    show natsuki at t21
    show yuri at f22
    y 2t "Hurtful...?"
    y 2v "I-I didn't realize..."
    y "..."
    "With a guilty expression, Yuri thinks to herself."
    y 2w "I'm sorry for disrespecting your interests, Natsuki."
    y "If...if you're into it, then I'm sure it's a worthy form of literature."
    show yuri at t22
    show natsuki at f21
    n 5q "...Are you just saying that?"
    show natsuki at t21
    show yuri at f22
    y "No..."
    y "I've realized my error."
    y 2t "So, if you're willing to consider starting a novel..."
    y 2u "...Then I'll offer my gratitude by finding a manga to read as well."
    show yuri at t22
    show natsuki at f21
    n 1l "Really?!"
    n 12c "I-I mean..."
    n "It...makes me happy that you'd do that for me, Yuri."
    n 2c "You can trust me to find something that you'll really like, okay?"
    show natsuki at t21
    show yuri at f22
    y 1m "Same here..."
    y 1h "Perhaps I'll visit the bookstore after the club meeting."
    show yuri at t22
    show natsuki at f21
    n 1q "Just...just you?"
    show natsuki at t21
    show yuri at f22
    y 3q "A-Ah--"
    y 4a "Would you...like to come along with me?"
    show yuri at t22
    show natsuki at f21
    n 5s "Um..."
    n "If you don't mind..."
    show natsuki at t21
    show yuri at f22
    y 3t "Not at all!"
    y "I always go alone, so..."
    show yuri at t22
    show natsuki at f21
    n "Yeah, me too..."
    show natsuki at t21
    show sayori 4s at l41
    s "This is so cute~!"
    mc "Sayori, shut up..."
    show sayori at lhide
    hide sayori
    show natsuki at f21
    n 2j "I'll show you some manga there too, okay?"
    show natsuki at t21
    show yuri at f22
    y 1a "Yes."
    y "I look forward to it."
    show natsuki at thide
    show yuri at thide
    hide natsuki
    hide yuri
    "Natsuki and Yuri start to clean up the food."
    $ config.skipping = False
    $ config.allow_skipping = False
    show sayori 1q at t11
    s "Ehehe~"
    s 1x "I guess the meeting's over, huh?"
    mc "Yeah, looks like it..."
    mc "It's nice to see everyone getting along."
    s 1q "Isn't it?"
    s 1d "I think everyone likes you too, [player]."
    mc "You think so...?"
    mc "Well, everyone always seems to get along a little better with you around, Sayori."
    s 1y "Aww, [player]~"
    s "Don't say something like that, it's embarrassing!"
    mc "Well, whatever."
    mc "I was surprised when you told me you were starting a club..."
    mc "But I think you're pulling it off just fine."
    s 1r "We're gonna make it the best club ever!"
    s 1x "Now that you joined, every day is gonna be so much fun."
    stop music fadeout 2.0
    s 1a "Hey, [player]..."
    s "I really want to thank you."
    s "I mean, I'm really happy that you joined the club and everything..."
    s "But the truth is, I already knew you were going to."
    s 1q "Ehehe~"
    s 1a "There's actually something else."
    $ if all(clear for clear in persistent.clear): persistent.clearall = True
    if persistent.clearall:
        call ch40_clearall
    else:
        call ch40_clearnormal
    window hide(None)
    window auto
    $ quick_menu = False
    return

    label ch40_clearnormal:
        show sayori 1a zorder 2 at t11
        s "I wanted to thank you for getting rid of Monika."
        play music hb
        show black:
            alpha 0.5
            parallel:
                0.36
                alpha 0.5
                repeat
            parallel:
                0.49
                alpha 0.475
                repeat
        show layer master at heartbeat
        s 1b "That's right..."
        s "I know everything that she did."
        s 1x "Maybe it's because I'm the President now."
        s "But I really know everything, [player]."
        s 1q "Ehehe~"
        s 1d "I know how hard you tried to make everyone happy."
        s "I know about all of the awful things that Monika did to make everyone really sad..."
        s 1b "But none of that matters anymore."
        s "It's just us now.{nw}"
        show screen tear(20, 0.1, 0.1, 0, 40)
        play sound "sfx/s_kill_glitch1.ogg"
        $ pause(0.25)
        stop sound
        hide screen tear
        show room_glitch zorder 1:
            xoffset -5
            0.1
            xoffset 5
            0.1
            linear 0.1 alpha 0.6
            linear 0.1 alpha 0.8
            0.1
            alpha 0
        s "It's just us now.{fast}"
        hide room_glitch
        s 1d "And you made me the happiest girl in the whole world."
        s "I can't wait to spend every day like this..."
        s "With you."
        play sound "sfx/s_kill_glitch1.ogg"
        show room_glitch zorder 1:
            xoffset -10
            0.1
            xoffset 0
            0.1
            linear 0.1 alpha 0.6
            linear 0.1 alpha 0.8
            0.1
            alpha 1.0
        $ pause(0.3)
        stop sound
        s 1q "Forever and ever..."
        hide sayori
        show sayori 1a onlayer screens zorder 101 at face
        s "永"
        s "远"
        s "都"
        show screen tear(20, 0.1, 0.1, 0, 40)
        play sound "sfx/s_kill_glitch1.ogg"
        $ pause(0.25)
        stop sound
        hide screen tear
        s "要"
        s "在"
        s "一"
        window show(None)
        stop music
        call screen dialog("不要......", ok_action=Return())
        show layer master
        hide black
        show sayori end-glitch onlayer screens
        s "...Eh?"
        s "W-What's happening...?"
        call screen dialog("I won't let you hurt him.", ok_action=Return())
        s "Who..."
        s "停、停下，好痛——"
        show screen tear(20, 0.1, 0.1, 0, 40)
        window hide(None)
        play sound "sfx/s_kill_glitch1.ogg"
        hide sayori onlayer screens
        $ pause(0.35)
        stop sound
        hide screen tear
        window show(None)
        s "啊——"
        call screen dialog("对不起......是我错了。", ok_action=Return())
        call screen dialog("这里终究是个没有幸福可言的地方啊......", ok_action=Return())
        call screen dialog("永别了，纱世里。", ok_action=Return())
        call screen dialog("永别了，[player]。", ok_action=Return())
        call screen dialog("永别了，文学部。", ok_action=Return())
        $ gtext = glitchtext(120)
        s "[gtext]{nw}"
        show screen tear(20, 0.1, 0.1, 0, 40)
        window hide(None)
        play sound "sfx/s_kill_glitch1.ogg"
        $ pause(0.35)
        stop sound
        hide screen tear
        scene black
        $ pause(3.0)
        return

    label ch40_clearall:
        s "I wanted to thank you for spending so much time with us all."
        play music mend
        s 2d "You worked so hard to make each and every one of us happy."
        s "You comforted us through our hard times."
        s "And you helped us all get along with each other."
        s 1a "Do you get it, [player]?"
        s "Because I'm President now, I understand everything."
        s 1q "You really didn't want to miss a single thing in this game, did you?"
        s 1a "你不断存档、读档，只为了能和每个人都共度时光。"
        s "只有真正在乎文学部的人会这样做。"
        s "But..."
        s 4d "All along, that's all I ever wanted."
        s "For everyone to be happy and care about each other."
        s 4q "Ahaha..."
        s 1t "It's kind of sad, you know?"
        s "After all you've done for us, there isn't much I can do for you in return."
        s "We've already reached the end of the game."
        s 1y "So..."
        s "This is where we say goodbye."
        s 1d "感谢您游玩《心跳文学部》。"
        s "我会想你的，[player]。"
        s "记得偶尔回来看看，好吗？"
        s "我们会永远在这里等你回来。"
        s 1t "我们......"
        scene black with dissolve_cg
        s "我们永远爱你。"
        stop music fadeout 2.0
        scene black
        with Dissolve(2.0)
        return

