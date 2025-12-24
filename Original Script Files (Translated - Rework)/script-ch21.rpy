label ch21_main:
    scene bg club_day2
    with dissolve_scene_half
    play music t2g3
    show monika 5 zorder 2 at t11
    show layer master:
        subpixel True
        truecenter
        linear 240 rotate 8 zoom 1.30
    m "嗨，[player]，又见面了！"
    m "我还怕你会放我们鸽子呢。哈哈哈！"
    mc "不会的，别担心啦。"
    mc "我起码还是个守信的人嘛，虽说这么自夸有点奇怪。"
    show monika zorder 1 at thide
    hide monika
    "是的，我又回到了文学部。"
    "我是最晚到的，其他人都已经在闲聊了。"
    show yuri glitch2 zorder 2 at t32
    y "谢谢你信守了承诺呢，[player]。"
    y 1a "希望这对你来说不至于太过沉重。"
    y 1u "毕竟你可能还没熟悉文学，就要一头扎进去了......"
    show natsuki glitch1 zorder 2 at i33
    n "诶，拜托！说得好像应该放他一马似的。"
    n 4e "你本来就是被莫妮卡硬拉过来的。"
    n "虽然我不知道你是打算过来随便混混，还是想怎样......"
    n "不过你要是不把我们当回事的话，那你等着瞧吧。"
    show monika 2b onlayer front at l41
    m "哎呀夏树，你倒是挺敢说的，明明都把自己收藏的漫画放在部室里了。"
    n 4o "么、姆、莫......！！"
    show monika onlayer front at lhide
    hide monika onlayer front
    "夏树不知该说“莫妮卡”还是“漫画”才好。"
    show natsuki at h33
    n 1v "漫画也是文学啊！！"
    show natsuki zorder 1 at thide
    hide natsuki
    "迅速败下阵来的夏树跌坐回了她的座位。"
    show yuri 2s zorder 2 at t11
    y "I'm sorry, [player]..."
    y "We'll make sure to put your comfort first, okay?"
    show yuri 2g
    "Yuri shoots Natsuki with a disappointed glance."
    y 1a "Um, anyway..."
    y "Now that you're in the club and all..."
    y "...Perhaps you might have interest in picking up a book to read?"
    mc "Well..."
    mc "I can't really say no either way."
    mc "Like you said, I'm in this club now."
    mc "So it only feels right for me to do something like that, if you ask."
    y 4b "W-Wait..."
    y "I didn't mean it like that!"
    y "Uu..."
    y "If you don't really want to, then forget I said anything, I guess..."
    mc "Ah--No, it's not that, Yuri."
    mc "I want to try to be a part of this club."
    mc "So even if I don't read often, I'd be happy to pick up a book if you wanted me to."
    y 3t "A-Are you sure...?"
    y "I just felt like..."
    y 3u "...Well, as Vice President and all..."
    y "...That I should help you get started on something you might like."
    "优里把手伸进包里，掏出了一本书。"
    y 1s "我希望你可以更快地融入进来......"
    y "所以我就找了本我觉得你可能会喜欢的书。"
    y "篇幅不长，即便你平时不怎么看书，应该也可以专心看到最后。"
    y "而且我们可以，嗯......"
    show yuri at sink
    y 4b "如果你愿意的话...我们可以一起讨论......"
    "这、这、这......"
    "这女孩怎么能这么可爱啊？"
    "明明知道我不怎么看书，她居然还特意挑了本她认为我会喜欢的书给我......"
    mc "谢谢你，优里！我一定会看的！"
    "我热情地接过了那本书。"
    show yuri 2m zorder 2 at t11
    y "呼......"
    y 2a "那么，你可以按照自己的阅读节奏来。"
    y "期待能听到你的感想。"
    show yuri zorder 1 at thide
    hide yuri
    show layer master


    "鉴于大家都已经到场，我本以为莫妮卡会开始主持一些已经安排好的社团活动。"
    "然而她并没有。"
    "优里已经把脸埋进了书里。"
    "我情不自禁地注意到了她那认真的表情，仿佛等待这次机会已久。"
    "与此同时，夏树在储藏间里到处翻找着什么。"


    $ nextscene = get_exclusive_scene(0)
    call expression nextscene

    return

label ch21_end:
    stop music fadeout 1.0
    scene bg club_day2
    with wipeleft_scene
    play music t3g
    queue music t3g2
    mc "呼......"
    "终于结束了。"
    "我环视了教室一圈。"
    "整个过程比我预想中的还要有压力。"
    "仿佛所有人都在挑剔我那平庸的写作水平......"
    "即使她们都很宽容，我的诗还是完全没有办法与她们的作品相提并论。"
    "毕竟，这里是个文学社团嘛。"
    "我只好叹了口气。"
    "看来我终归是作茧自缚了。"
    "Across the room, Monika is writing something in her notebook."
    "我的目光随后转移到了优里和夏树身上。"
    show yuri 2g zorder 2 at t21
    show natsuki 1g zorder 2 at t22
    "她们郑重其事地交换了纸张，分享着各自的诗。"
    show yuri 2i zorder 2 at t21
    "在她们一起阅读时，我在一旁注意着她们的表情变化。"
    "夏树失望地皱起眉头。"
    "与此同时，优里苦笑着。"
    show natsuki zorder 3 at f22
    n 1q "{i}（这文风到底是怎么回事啊...？）{/i}"
    show natsuki zorder 2 at t22
    show yuri zorder 3 at f21
    y 2f "诶？"
    y "呃...你刚刚是不是说了些什么？"
    show yuri zorder 2 at t21
    show natsuki zorder 3 at f22
    n 2c "哦，没什么。"
    "夏树不以为然地把诗用单手放回桌子上。"
    n "还称得上辞藻华丽吧。"
    show natsuki zorder 2 at t22
    show yuri zorder 3 at f21
    y 2i "啊——谢谢....."
    y "你的诗......挺可爱的......"
    show yuri zorder 2 at t21
    show natsuki zorder 3 at f22
    n 2h "可爱吗？"
    n 1h "你是不是完全没理解我的象征手法？"
    n "这首诗很明显是在写放弃这种感受的。"
    n "这样的主题能用可爱来形容吗？"
    show natsuki zorder 2 at t22
    show yuri zorder 3 at f21
    y 3f "我、我当然注意到了！"
    y "我只是想说......"
    y 3h "你这个遣词造句方面，大概......"
    y "我只是想说点好听的......"
    show yuri zorder 2 at t21
    show natsuki zorder 3 at f22
    n "诶？"
    n 4w "那你的意思是，对你来说，这首诗就连找点好听的话来形容都那么困难吗？"
    n "那，谢谢你了，你这话说出来一点都不好听！"
    show natsuki zorder 2 at t22
    show yuri zorder 3 at f21
    y 1i "唔......"
    y "那么，我确实有几点建议......"
    show yuri zorder 2 at t21
    show natsuki zorder 3 at f22
    n 5x "哼。"
    n "想听建议的话，我早就找真正喜欢这首诗的人问了。"
    n "顺带一提，这首诗真有人{i}喜欢{/i}哦。"
    n 5e "莫妮卡喜欢。"
    n "而且 [player] 也喜欢！"
    n "既然如此，我也乐意给你些我的建议。"
    n "首先——"
    show natsuki zorder 2 at t22
    show yuri zorder 3 at f21
    y 2l "不好意思......"
    y "你的好意我心领了，不过我的写作风格是我花了大量时间建立起来的。"
    y 2h "短时间内我并不打算改变它，除非遇到了什么特别能激发我灵感的事情。"
    y "但这种事情我至今还没遇到过。"
    show yuri zorder 2 at t21
    show natsuki zorder 3 at f22
    n 1o "你......！"
    show natsuki zorder 2 at t22
    show yuri zorder 3 at f21
    y 1k "而且 [player] 也喜欢我的诗。"
    y "他甚至还跟我说，我的诗深深地打动了他。"
    stop music fadeout 1.0
    "夏树突然站了起来。"
    show yuri zorder 2 at t21
    show natsuki zorder 3 at f22
    n 4y "哦？"
    n "优里，我才发现你投入了很多精力去取悦我们的新成员嘛。"
    play music t7a
    show natsuki zorder 2 at t22
    show yuri zorder 3 at f21
    y 1n "诶、诶？！"
    y "我不是那个意......！"
    y 1o "唔......"
    y "你...你只不过是......"
    "优里也站了起来。"
    y 2r "你多半只是嫉妒 [player] 更珍视我的建议，而不是你的建议！"
    show yuri zorder 2 at t21
    show natsuki zorder 3 at f22
    n 1e "哈？！你又知道他没有更重视{i}我{/i}的建议了？"
    n "你就那么自负吗？"
    show natsuki zorder 2 at t22
    show yuri zorder 3 at f21
    y 3h "我......！"
    y "我才不是......"
    y "如果我真的像你所说的那样自负..."
    y 1r "那区区装可爱而已，我也能信手拈来，刻意为之！"
    show yuri zorder 2 at t21
    show natsuki zorder 3 at f22
    n 1o "唔唔唔.....！"
    n "哼，你猜怎么着？！"
    n "某位自从 [player] 一出现，胸部就神奇地大了一号！！"
    show yuri 3p at h21
    show natsuki zorder 2 at t22
    y "夏、夏树你！！"
    show yuri zorder 2 at t32
    show natsuki zorder 2 at t33
    show monika 3l behind yuri, natsuki at l41
    m "呃，夏树，这话是不是有点——"
    show monika at h41
    show yuri 3p zorder 3 at f32
    show natsuki 1e zorder 3 at f33
    ny "跟你没关系！"
    show monika at lhide
    hide monika
    show yuri 2h zorder 2 at f21
    show natsuki zorder 2 at t22
    queue music t7g
    $ timeleft = 12.453 - get_pos()
    show noise zorder 3 at noisefade(25 + timeleft)
    show vignette as flicker zorder 4 at vignetteflicker(timeleft)
    show vignette zorder 4 at vignettefade(timeleft)
    show layer master at layerflicker(timeleft)
    y "Taking out your own insecurities on others like that..."
    y "You really act as young as you look, Natsuki."
    show yuri zorder 2 at t21
    show natsuki zorder 3 at f22
    n 4o "{i}Me?{/i} Look who's talking, you wannabe edgy bitch!"
    show natsuki zorder 2 at t22
    show yuri zorder 3 at f21
    y "Edgy...?"
    y 2r "Sorry that my lifestyle is too much for someone of your mental age to comprehend!"
    show yuri zorder 2 at t21
    show natsuki zorder 3 at f22
    n 4f "See??"
    n "Just saying that proves my point!"
    n 4e "Most people learn to get over themselves after they graduate middle school, you know."
    show natsuki zorder 2 at t22
    show yuri zorder 3 at f21
    y "If you want to prove anything, then stop harassing others with your sickening attitude!"
    y "You think you can counterbalance your toxic personality just by dressing and acting cute?"
    y 1k "The only cute thing about you is how hard you try."
    show yuri zorder 2 at t21
    show natsuki zorder 3 at f22
    n 2y "Whoa, be careful or you might cut yourself on that edge, Yuri."
    n "Oh, my bad... You already do, don't you?"
    show natsuki zorder 2 at t22
    show yuri zorder 3 at f21
    y 3n "D-Did you just accuse me of cutting myself??"
    y 3r "What the fuck is wrong with your head?!"
    show yuri zorder 2 at t21
    show natsuki zorder 3 at f22
    n 1e "Yeah, go on!"
    n "Let [player] hear everything you really think!"
    n "I'm sure he'll be head over heels for you after this!"
    show natsuki zorder 2 at t22
    show yuri zorder 3 at f21
    y 3n "A-Ah--!"
    show yuri zorder 2 at t21
    "突然，优里转向了我，仿佛刚刚才意识到我站在那里。"
    show yuri zorder 3 at f21
    y 2n "[player]......！"
    y "她——她就是想让我难堪......！"
    show yuri zorder 2 at t21
    show natsuki zorder 3 at f22
    n 4w "才不是呢！"
    n "是她先挑起来的！"
    show yuri 1t zorder 2 at t21
    show natsuki 1g zorder 2 at t22
    $ style.say_dialogue = style.normal
    mc "......"
    $ style.say_dialogue = style.edited
    "{cps=*2}我当初怎么就被牵扯进来了啊？！{/cps}{nw}"
    "{cps=*2}我对写作这门事一窍不通啊......{/cps}{nw}"
    "{cps=*2}不过不管我站在谁的一边，那个人对我的评价可能会变得更高吧！{/cps}{nw}"
    "{cps=*2}所以，当然是要选......！{/cps}{nw}"
    $ style.say_dialogue = style.normal
    $ menu_clicked = 0
    window hide(None)
    label ch21_end_menu:
        menu:
            "夏树。":
                jump menu_click
            "优里。":
                jump menu_click

    label menu_click:
        $ srf = screenshot_srf()
        show layer screens:
            truecenter
            zoom 1.00
        show screen tear(20, 0.1, 0.1, 0, 40, srf)
        play sound "sfx/s_kill_glitch1.ogg"
        $ pause(0.25)
        hide screen tear
        stop sound
        $ menu_clicked += 1
        if menu_clicked < 9:
            show layer master:
                truecenter
                zoom 1.00 + menu_clicked * menu_clicked * 0.06
                yalign 0.25
            show layer screens:
                truecenter
                zoom 1.00 + menu_clicked * menu_clicked * 0.06
                yalign 0.25
            jump ch21_end_menu


    window show(None)
    stop music
    $ menu_clicked = 8
    $ quick_menu = False
    show layer master:
        truecenter
        zoom 1.00 + menu_clicked * menu_clicked * 0.06
        yalign 0.25
    show layer screens:
        truecenter
        zoom 1.00 + menu_clicked * menu_clicked * 0.06
        yalign 0.25
    show monika 1 onlayer front at i11:
        zoom 1.00 + menu_clicked * menu_clicked * 0.06
        yalign 0.25
    $ renpy.display_menu(items=[('夏树。', True), ('优里。', True)], interact=False, screen='choice')
    m "....."
    show layer master
    show layer screens
    show monika 1 onlayer front at i11
    window auto
    $ renpy.display_menu(items=[('夏树。', True), ('优里。', True)], interact=False, screen='choice')
    m "......"
    $ renpy.display_menu(items=[('夏树。', True), ('优里。', True)], interact=False, screen='choice')
    m "......"
    show monika 1m onlayer front at i11
    $ renpy.display_menu(items=[('夏树。', True), ('优里。', True)], interact=False, screen='choice')
    m "嗯......"
    $ renpy.display_menu(items=[('夏树。', True), ('优里。', True)], interact=False, screen='choice')
    m "嘿，[player]......"
    show monika 1e onlayer front at i11
    $ renpy.display_menu(items=[('夏树。', True), ('优里。', True)], interact=False, screen='choice')
    m "要不我们先\n暂时离场\n一下吧。"
    $ renpy.display_menu(items=[('夏树。', True), ('优里。', True)], interact=False, screen='choice')
    m "好吗？"
    scene bg corridor
    hide monika onlayer front
    show monika 1n onlayer master at t11
    with wipeleft_scene
    $ quick_menu = True
    m "Sorry about that..."
    m "They really shouldn't have tried to get you involved."
    m 1e "It's probably better for us to stay out of this..."
    m "We'll go back inside once they're done yelling."
    m 5 "Ahaha..."
    m "Some president I am, right?"
    m 1m "I can't even confront my own club members properly..."
    m "I just wish I was able to be a little more assertive sometimes."
    m "But I never have it in me to put my foot down against others..."
    m 1e "You understand, right?"
    m "Anyway..."
    m 1a "If this makes you want to spend less time with the others, then that's fine."
    m 1j "I'd be happy to spend time with you instead..."
    show monika zorder 1 at thide
    hide monika
    "Suddenly, Natsuki runs out of the classroom."
    show natsuki 12h zorder 2 at t11
    n "..."
    show natsuki 12f at lhide
    $ pause(0.75)
    hide natsuki
    "She quickly runs away."
    show monika 1l zorder 2 at t11
    m "Oh dear..."
    m "...Well, it looks like they're done..."
    scene bg club_day2
    with wipeleft_scene
    y "I didn't mean it..."
    y "I didn't mean it..."
    y "I didn't mean it..."
    "Yuri is rocking back and forth in her desk with her palms on her forehead."
    mc "Yuri...?"
    show yuri 4d zorder 2 at t11
    y "I didn't mean it!!"
    mc "I-I believe you..."
    "I have no idea what Yuri might have said to Natsuki."
    "Or did."
    y "[player]."
    y "Please don't hate me."
    y "Please!"
    y "I'm not like this!"
    y "There's something wrong with me today..."
    show monika 1d zorder 3 at f31
    m "It's fine, Yuri."
    m "We know you didn't mean it."
    m 1j "Besides, I'm sure Natsuki will forget all about it by tomorrow."
    m 1a "Completely."
    show monika zorder 2 at t31
    show yuri zorder 3 at f32
    y 4b "..."
    show yuri zorder 3 at t32
    show monika zorder 2 at f31
    m "Anyway, the meeting is over, so you can go home now if you want."
    show monika zorder 2 at t31
    show yuri zorder 3 at f32
    y 4a "..."
    show yuri zorder 2 at t32
    "Yuri looks at me like she wants to say something."
    "But she keeps glancing at Monika."
    show yuri zorder 3 at f32
    y 2v "Y-You can go first, Monika..."
    y "I'd like to stay a little bit longer."
    show yuri zorder 2 at t32
    show monika zorder 3 at f31
    m 2k "I'm the President, so I should be the last one out."
    m "I'll wait for you to be done."
    show monika 2a zorder 2 at t31
    show yuri zorder 3 at f32
    y 4b "..."
    y "..."
    y "Well-- I'm Vice President, so..."
    y "Please let me take that responsibility today."
    show yuri zorder 2 at t32
    show monika zorder 3 at f31
    m 2i "It kind of sounds like you don't want me around for something, Yuri."
    show monika zorder 2 at t31
    show yuri zorder 3 at f32
    y 3p "I-It's not that!"
    y 3o "It's not that..."
    y 3n "I just..."
    y 3q "I didn't get much of a chance to discuss my book with [player]..."
    y "It would just be...embarrassing with you listening..."
    show yuri zorder 2 at t32
    show monika zorder 3 at f31
    m 1r "{i}*唉*{/i}"
    m 1d "I guess I don't really have a choice, do I?"
    show monika zorder 2 at t31
    show yuri zorder 3 at f32
    y 1t "I-I'm sorry for causing trouble..."
    $ gtext = glitchtext(20)
    y 1s "But I really appreciate you understan{nw}"
    play music g1
    show monika 1 onlayer front at i31
    y glitch "But I really appreciate you understan{fast}[gtext] [gtext][gtext]{nw}"
    $ _history_list.pop()
    hide monika onlayer front
    window hide(None)
    window auto

    return

