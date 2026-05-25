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
                renpy.call_screen("dialog", message="请不要再玩弄我的心了。\n我不想回来。", ok_action=Return())
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
    y "今天真是个适合庆祝的日子，对吧？"
    show yuri 1a at t33
    show sayori at f32
    s 1r "没错！"
    s 1x "而且，夏树决定要——"
    show sayori at t32
    show natsuki at f31
    n 1w "嘿，不许剧透！"
    show natsuki at t31
    show sayori at f32
    s 5a "诶嘿嘿，不好意思......"
    show sayori at t32
    show natsuki at f31
    n 1k "大家都来桌子这边坐下，好吗？"
    show natsuki at t31
    show yuri at f33
    y 1a "要不我去泡壶茶？"
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
    n "......锵锵！"
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
    n "欸嘿嘿，优里，这么快就想给我们的新成员留点好印象吗？"
    show natsuki at t31
    show yuri at f11
    y 3n "诶？！不、不是这样的......"
    show yuri at t11
    show natsuki at thide
    hide natsuki
    "优里难堪地把脸别了过去。"
    y 4b "那个，我是真的这么觉得的......"
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
    y 2a "如果你阅读量不多的话，也不用觉得有压力，好吗？"
    y "我们肯定能找到别的共同点的。"
    show yuri at t22
    show natsuki 2c at f21
    n "嘿，优里......"
    show natsuki at t21
    show yuri at f22
    y 2f "诶？"
    show yuri at t22
    show natsuki at f21
    n 2h "就是，那个......他刚刚一开始说的......"
    show natsuki at t21
    mc "漫画吗？"
    show yuri at f22
    y 2i "没错......"
    y "夏树以前就在部室里面看漫画——"
    show yuri at t22
    show natsuki at f21
    n 1r "不、不要直接讲出来啦！！"
    "不知道为什么，夏树似乎对这件事很难为情。"
    n 1q "而且......"
    n "漫画......不也是一种文学，对吧？"
    n 1w "所以......如果 [player] 就是想看我的漫画的话，那就别阻止他，让他看嘛！"
    show natsuki 1i at t21
    show yuri at f22
    y 1l "夏树......"
    y "我不会阻止他看漫画的啦。"
    y 1i "不过，让自己的阅读兴趣更多样化一点也不是什么坏事......"
    y "他同样可以利用这个机会读些不同的东西。"
    y 1s "你也认同的吧，[player]？"
    show yuri at t33
    show natsuki at t32
    show sayori 1l at f31
    s "大、大概吧——"
    "纱世里察觉到气氛的紧张，赶紧插话打起了圆场。"
    s 1x "或许我们大家都可以尝试一下新事物！"
    s 1l "我想这应该会很有趣......"
    s 1c "而且也能增进我们彼此之间的了解呢！"
    s 1l "我是说......"
    s "这不正是文学社团该做的事情嘛......对吧？"
    show sayori at t31
    show yuri at f33
    y 1v "......"
    y "我、我同意......"
    show yuri at t33
    show natsuki at f32
    n 2j "嗯......"
    n "部长，你说什么都对。"
    show natsuki at t32
    show sayori at f31
    s 1q "欸嘿嘿~"
    show sayori at t31
    show natsuki at f32
    n 2c "看来我得找本小说来读读了，是吧......？"
    show natsuki at t32
    mc "嗯，那就有两个人了......"
    mc "只要不是只有我一个人读就行。"
    show sayori at thide
    hide sayori
    show natsuki at f21
    show yuri at t22
    n 2y "那么，优里的话......"
    show natsuki at t21
    show yuri at f22
    y 2n "诶......？"
    y "我......我要看漫画吗......？"
    show yuri at t22
    show natsuki at f21
    n 4i "真是的......"
    n 4h "不是你说的要多样化阅读兴趣的吗！"
    n "你的思想应该更开明一些......"
    n 4u "而且你那种反应挺伤人的......"
    show natsuki at t21
    show yuri at f22
    y 2t "伤人......？"
    y 2v "我、我没意识到......"
    y "......"
    "优里低头沉思，脸上挂着满满的负罪感。"
    y 2w "夏树对不起，我以前一直没有尊重你的喜好。"
    y "既......既然你这么钟爱漫画，那我相信漫画也应该是种有价值的文学。"
    show yuri at t22
    show natsuki at f21
    n 5q "......你不会只是嘴上说说吧？"
    show natsuki at t21
    show yuri at f22
    y "不会的......"
    y "我已经知道自己错在哪里了。"
    y 2t "所以，如果你愿意考虑开始读小说......"
    y 2u "......那么我也愿意去找本漫画来读一读，以表感谢。"
    show yuri at t22
    show natsuki at f21
    n 1l "真的吗？！"
    n 12c "我、我是说......"
    n "优里，你......你愿意为我这么做，让我很开心。"
    n 2c "相信我，我一定会帮你找到合你口味的漫画，好吗？"
    show natsuki at t21
    show yuri at f22
    y 1m "彼此彼此......"
    y 1h "社团活动结束后，我大概会去趟书店。"
    show yuri at t22
    show natsuki at f21
    n 1q "你......你自己一个人去吗？"
    show natsuki at t21
    show yuri at f22
    y 3q "啊、啊——"
    y 4a "你......想跟我一起去么？"
    show yuri at t22
    show natsuki at f21
    n 5s "唔......"
    n "如果你不介意的话就行......"
    show natsuki at t21
    show yuri at f22
    y 3t "我完全不介意！"
    y "我以前一直都是一个人去的，所以......"
    show yuri at t22
    show natsuki at f21
    n "是啊，我也是......"
    show natsuki at t21
    show sayori 4s at l41
    s "好可爱呀~！"
    mc "住口啦，纱世里......"
    show sayori at lhide
    hide sayori
    show natsuki at f21
    n 2j "到时候我也会带你去看看漫画的，好吗？"
    show natsuki at t21
    show yuri at f22
    y 1a "好吧。"
    y "我很期待哦。"
    show natsuki at thide
    show yuri at thide
    hide natsuki
    hide yuri
    "夏树和优里开始把吃剩的食物收拾起来。"
    $ config.skipping = False
    $ config.allow_skipping = False
    show sayori 1q at t11
    s "欸嘿嘿~"
    s 1x "我想今天的社团活动就到此为止了吧？"
    mc "是啊，差不多了......"
    mc "看到大家相处得这么融洽，真的很棒。"
    s 1q "是吧是吧！"
    s 1d "我觉得大家都喜欢你，[player]。"
    mc "你这么觉得吗......？"
    mc "我倒觉得，因为有纱世里在，大家似乎总是相处得更融洽些。"
    s 1y "啊，[player]~"
    s "别这么说嘛，搞得人家好害羞！"
    mc "好吧，随便了。"
    mc "之前你说要组建一个社团的时候，我都惊呆了......"
    mc "但现在看来，你做得很棒。"
    s 1r "我们会成为世上最棒的社团！"
    s 1x "而且现在你也加入了，以后每天都会充满乐趣。"
    stop music fadeout 2.0
    s 1a "嘿，[player]......"
    s "我真的很想谢谢你。"
    s "我是说，你能加入文学部我真的很开心......"
    s "不过老实说，我早就知道你要加入了。"
    s 1q "欸嘿嘿~"
    s 1a "而且，不仅如此。"
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
        s "我也要感谢你帮我们摆脱了莫妮卡。"
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
        s 1b "没错......"
        s "我知道她做过的每一件事。"
        s 1x "大概是因为现在我成了部长吧。"
        s "但是哦，[player]，我真的什么都知道哦。"
        s 1q "欸嘿嘿~"
        s 1d "我知道你为了让大家开心，付出了多大努力。"
        s "我知道莫妮卡对我们做了很多过分的事情，让大家都超级伤心......"
        s 1b "但这些都已经无所谓了。"
        s "现在，这里只剩下我和你了。{nw}"
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
        s "现在，这里只剩下我和你了。{fast}"
        hide room_glitch
        s 1d "而你让我成为了这个世界上最幸福的女孩。"
        s "我等不及要这样跟你度过每一天了......"
        s "和你。"
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
        s 1q "永远在一起......"
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
        s "......诶？"
        s "什、什么情况......？"
        call screen dialog("我不会让你伤害他的。", ok_action=Return())
        s "谁啊......"
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
        call screen dialog("再见了，纱世里。", ok_action=Return())
        call screen dialog("再见了，[player]。", ok_action=Return())
        call screen dialog("再见了，文学部。", ok_action=Return())
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
        s "我也要感谢你，与我们共度了那么长的时光。"
        play music mend
        s 2d "为了让我们每一个人开心，你付出了那么多的努力。"
        s "在最艰难的时候，是你给了我们安慰。"
        s "帮助我们互相打开心结。"
        s 1a "你还不明白吗，[player]？"
        s "因为我现在是部长了嘛，所以我什么都知道哦。"
        s 1q "看来你是真的不想错过游戏里任何一个细节呢，对吧？"
        s 1a "你不断存档、读档，只为了能和每个人都共度时光。"
        s "只有真正在乎文学部的人会这样做。"
        s "不过......"
        s 4d "不过自始至终，这就是我想要的。"
        s "大家互相关心，一起欢笑。"
        s 4q "啊哈哈......"
        s 1t "真是的，气氛怎么一下子有点伤心了？"
        s "你为我们付出了那么多，而我却无以为报。"
        s "因为游戏到这里就要结束了。"
        s 1y "那么......"
        s "我们就在这里道别吧。"
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

