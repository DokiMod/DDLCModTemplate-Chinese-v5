image yuri half = "images/yuri/1l.png"
image yuri_half2:
    "images/yuri/1r.png"
    block:
        xoffset -360
        linear 0.2 xoffset -280
        repeat

label ch22_main:
    scene bg club_day2
    with dissolve_scene_half
    play music t6
    "又一天过去了，眨眼间已经到了社团活动的时间。"
    "几天下来，我对文学部已经相当适应了。"
    "走进部室，迎接我的又是那熟悉的一幕。"
    if renpy.random.randint(0,2) == 0:
        show yuri half zorder 2 at i11
        show yuri_half2 zorder 1 at i11
    else:
        show yuri 1s zorder 2 at t11
    y "欢迎回来，[player]......"
    hide yuri_half2
    mc "啊，你好啊优里......"
    "我不太确定是因为我，还是因为优里的脸色......"
    "但昨天的争吵余波未了，让气氛似乎依旧有些沉重。"
    y 2v "唔、唔......"
    "优里扭头望了一下身后，视线在教室里徘徊。"
    "夏树正在课桌前看漫画。"
    "令人惊讶的是，莫妮卡还没有到。"
    "突然，优里抓着我的胳膊，把我拉到了教室的角落。"
    show bg closet
    show yuri 2t zorder 2 at t11
    with wipeleft
    y "关于昨天那件事......"
    y "我......"
    y 2v "我真的需要道歉。"
    y "以前从来没有发生过这样的事..."
    y 2t "而且...可能我刚好被什么东西冲昏头脑了..."
    y "所以昨天我的精神状态不太稳定。"
    y 2w "我们通常不是这个样子的，请千万不要误会！"
    y "不光是我，夏树也是......"
    show yuri 2t
    mc "优里......"
    mc "你这么体贴人、还向我道歉，我已经很开心了。"
    mc "还是别太计较这件事了。"
    mc "就算是才来了这里几天的我，也能感觉到昨天有什么不对劲......"
    mc "也许只是因为昨天是我们第一次分享诗作，所以大家都有点太敏感了。"
    mc "不过无论原因是什么......"
    mc "这件事并没有破坏我对你的印象。"
    mc "不如说，我早就认定你人不坏了。"
    mc "而且，既然你都道歉了，我就更肯定你不是真心那样做的了。"
    y 3t "啊、啊......"
    y "[player]......"
    y 3u "别把这些话说得那么直白嘛......"
    y "这会让我有点开心过头的。"
    y 1s "你这么善解人意，我真的很开心......"
    y "我也很高兴你能加入社团。"
    y "只要有你在身边，一切似乎都明亮了起来，而且——"
    y 1t "啊——"
    y 4c "抱歉，我在说些什么......？"
    y "我只是——"
    show natsuki 2c zorder 3 at f33
    n "嘿，你们看到莫妮卡了吗？"
    show natsuki zorder 2 at t33
    show yuri 3n at h32
    y "啊——！"
    mc "没，没看到......"
    mc "我也在想她去哪了呢。"
    show natsuki zorder 3 at f33
    n 5g "奇怪......"
    n 5c "优里，我猜你大概也没见到她吧？"
    show natsuki zorder 2 at t33
    show yuri zorder 3 at f32
    y 4a "......"
    "夏树这么平静地对她说话，显然让优里吓了一跳。"
    y "没、没，我也没有......"
    show yuri zorder 2 at t32
    show natsuki zorder 3 at f33
    n 1u "天哪，这可一点也不像她的风格。"
    n "我知道有点傻，但是我实在忍不住有点担心......"
    show natsuki zorder 2 at t33
    show yuri zorder 3 at f32
    y 2t "......"
    show yuri zorder 2 at t32
    show natsuki 1h zorder 3 at f33
    n "不是？"
    n "为什么用那种眼神看我啊？"
    show natsuki zorder 2 at t33
    show yuri zorder 3 at f32
    y "呃、嗯......"
    y "夏树，关于昨天那件事......"
    y 3w "我、我只是想跟你道歉！"
    y "我发誓我说的话都只是一时冲动！"
    y 3t "从现在起，我会更加努力控制住自己的情绪......"
    y "所以——"
    show yuri zorder 2 at t32
    show natsuki zorder 3 at f33
    n 2c "优里，你到底在说什么啊？"
    n "你昨天是做了什么吗？"
    show natsuki zorder 2 at t33
    show yuri zorder 3 at f32
    y 3f "......诶？"
    show yuri zorder 2 at t32
    show natsuki zorder 3 at f33
    $ style.say_dialogue = style.normal
    n 2a "真是的......"
    $ style.say_dialogue = style.edited
    n "不管你在介意什么事，我觉得肯定没什么大不了啦。"
    n "我根本不记得有发生过什么坏事。"
    n "你是不是老喜欢把一些鸡毛蒜皮放在心上啊？"
    $ style.say_dialogue = style.normal
    show natsuki zorder 2 at t33
    show yuri zorder 3 at f32
    y 2o "......"
    y "但、但是......"
    show yuri zorder 2 at t32
    if renpy.random.randint(0, 3) == 0:
        $ style.say_dialogue = style.edited
        show natsuki mouth as nm zorder 3 at i33
        show n_moving_mouth zorder 3:
            xoffset 400
        n 2a "尼布斯水手服盲点生命线安安直瓣性无暇供给巩膜软化嘶吼大主教"
        hide nm
        hide n_moving_mouth
        $ style.say_dialogue = style.normal
    show natsuki zorder 3 at f33
    n 2j "总之，如果这样能让你好受些的话，那我就接受你的道歉好啦。"
    n "另外，其实我总是担心你是不是暗地里讨厌我什么的，所以能听到你坦诚布公，我还挺开心的。"
    n 2z "欸嘿嘿。"
    show natsuki zorder 2 at t33
    show yuri zorder 3 at f32
    y 3q "没、没有，我怎么会......！"
    y "我并不讨厌你的......"
    show yuri zorder 2 at t32
    show natsuki zorder 3 at f33
    n 2l "啊哈哈。"
    n "嘛，你是有点古怪，不过我也不讨厌你啦。"
    show natsuki zorder 2 at t33
    show yuri zorder 3 at f32
    y 3t "......"
    "夏树转向了我。"
    show yuri zorder 2 at t32
    show natsuki zorder 3 at f33
    n 2a "但是，你，还有待考察哦。"
    show natsuki zorder 2 at t33
    mc "喂......！"
    "突然，门猛地打开了。"
    show monika 1g at l41
    m "抱歉抱歉！非常抱歉！"
    mc "啊，你终于到了......"
    show monika zorder 3 at f41
    m "我真不是故意要迟到的......"
    m "希望你们没有在担心我之类的！"
    show monika zorder 2 at t41
    mc "没有啦......"
    mc "不过，夏树倒是挺担心的。"
    show natsuki zorder 3 at f33
    n 1p "我、我可没有！！"
    show natsuki zorder 2 at t33
    show monika zorder 3 at f41
    m 1k "啊哈哈。"
    show monika zorder 2 at t41
    show natsuki zorder 3 at f33
    n 1s "......话说回来，你为什么迟到了啊？"
    show natsuki zorder 2 at t33
    show monika zorder 3 at f41
    m 1e "啊......"
    m "嗯，我今天最后一节课是自习课。"
    m "说实话，我忘了注意时间......"
    m "啊哈哈......"
    show monika zorder 2 at t41
    show natsuki zorder 3 at f33
    n 2c "那也不合理啊。"
    n "你至少应该有听到下课铃吧。"
    show natsuki zorder 2 at t33
    show monika zorder 3 at f41
    m 1m "那想必是被我练钢琴的声音盖过去了吧......"
    show monika zorder 2 at t41
    show yuri zorder 3 at f32
    y 1e "钢琴......？"
    y "我都不知道你会弹钢琴诶，莫妮卡。"
    show yuri zorder 2 at t32
    show monika zorder 3 at f41
    m 1l "啊，我还差得远呢。"
    m 1m "虽然练了有一段时间了，不过我的水平还不够好。"
    show monika zorder 2 at t41
    show yuri zorder 3 at f32
    y 1a "但是......"
    y "你肯定也已经付出相当多的努力了。"
    y "所以，我还是很佩服你。"
    show yuri zorder 2 at t32
    show monika zorder 3 at f41
    m 5 "喔，谢谢你，优里~"
    show monika zorder 2 at t41
    show natsuki zorder 3 at f33
    n 2d "找个时间弹给我们听嘛！"
    show natsuki zorder 2 at t33
    show monika zorder 3 at f41
    m "啊哈哈，这个嘛......"
    "莫妮卡看着我说道。"
    m 1a "好吧，其实我正在写一首歌，不过还没写完......"
    m "大概还是等我弹得稍微好点了，再弹给大家听吧。"
    show monika zorder 2 at t41
    mc "听起来好厉害。"
    mc "我很期待哦。"
    show monika zorder 3 at f41
    m 1b "是吗？"
    m "这样的话......"
    m "我不会让你失望的，[player]。"
    show yuri zorder 1 at thide
    show natsuki zorder 1 at thide
    hide yuri
    hide natsuki
    show monika 5 zorder 2 at t11
    "莫妮卡冲我甜甜地笑着。"
    mc "啊......"
    mc "我不是想给你压力什么的！"
    m 1a "啊哈哈，不用担心。"
    m "反正我本来就打算秀一下的。"
    m "大概这就是为什么我最近越练越勤了吧。"
    mc "这样啊......"
    "我不太确定莫妮卡口中的“秀一下”，到底是指秀给文学部的所有人，还是只秀给我......"
    mc "那么，就祝你好运吧。"
    m 1j "谢谢~！"
    m 1a "话说，我没有错过什么吧？"
    mc "呃......其实没错过什么。"
    show monika zorder 1 at thide
    hide monika
    "我觉得还是不要说出我们三个之前的谈话内容比较好。"
    "况且夏树都已经跑到储藏间那边去了。"
    show yuri 2q zorder 2 at t11
    y "[player]......"
    y "唔......"
    y "你说的那些话让我很开心......"
    y "所以，今天我们如果能一起度过就好了。"
    y 3o "我是说——在社团里！"
    if poemwinner[0] == "natsuki":
        $ set_character_poem_appeal("yuri", 1, 1)
        mc "啊，可以啊。"
        mc "毕竟你送了我那本书，我想我也没有什么理由拒绝。"
        mc "只是，我觉得我应该先确认夏树没有在等我。"
        mc "昨天我们一起看完漫画后，她——"
        if get_appeal("natsuki") >= 2:
            y 3r "她没事的！"
            $ style.say_dialogue = style.normal
            y 3h "她自己在那边看漫画呢，看到了吧？"
            $ style.say_dialogue = style.edited
            y 3f "所以不要老是想着她了。"
            y "她早就习惯被无视了。"
            y "来吧，我们去那边。"
            $ style.say_dialogue = style.normal
            window hide(None)
            $ currentpos = get_pos()
            stop music
            scene black
            window auto
            $ pause(2.0)
            play music "<from " + str(currentpos) + " loop 10.893>bgm/6.ogg"
            jump ch22_main2
        else:
            y 3r "她、她没事的！"
            y 3h "她自己在那边看漫画呢。"
            y 3y6 "所以没关系的，对吧？"
            mc "啊——"
            mc "这样的话，我觉得没问题......"
    else:
        $ set_character_poem_appeal("yuri", 2, 1)
        mc "嗯，那当然。"
        mc "我本来也是这么打算的。"
    show yuri zorder 2 at h11
    y 3y5 "那好吧！"
    y "那我们现在开始吗？"
    y "我们去找个地方坐——"
    y 3n "啊、啊——"
    y "我会不会有点强迫你了......？"
    y 4c "实在抱歉！"
    y "我的心......不知道为什么，跳得很厉害......"
    mc "别想太多了。"
    mc "倒不如说，看你这样干劲十足也挺好的。"
    y 3q "嗯、是的！"
    y "不过......"
    y 3j "我真的需要冷静一下。"
    y "不然我没办法专心读书......"
    mc "慢慢来吧。"
    "优里深吸一口气，随后从书包里拿出了一本书。"
label ch22_main2:
    if get_character_poem_appeal("natsuki", 2) == 1:
        $ set_character_poem_appeal("natsuki", 2, 0)
    $ poemwinner[1] = "yuri"


    scene bg club_day2
    show yuri 3a at i11
    with wipeleft
    $ nextscene = f"yuri_exclusive2_{get_appeal('yuri')}_ch22"
    call expression nextscene

    return

label ch22_end:
    stop music fadeout 1.0
    scene black
    with wipeleft_scene
    call screen confirm("你解锁了一首特别诗篇。\n想现在就读读看吗？", Return(True), Return(False))
    if _return:
        call expression "poem_special_" + str(persistent.special_poems[1])
        scene black with Dissolve(1.0)
    else:
        pass
    if not faint_effect and renpy.random.randint(0,2) == 0:
        $ faint_effect = True
    else:
        $ faint_effect = None
    scene bg club_day2
    show monika 4b zorder 2 at t32
    if faint_effect:
        show layer master at dizzy(0.5, 1.0)
        show layer screens at dizzy(0.5, 1.0)
        show expression Solid("ff0000") as i1 onlayer front:
            additive 1.0
        show expression Solid("#440000") as i2 onlayer front:
            additive 0.4
        show veins onlayer front:
            additive 0.5
    with wipeleft_scene
    if faint_effect:
        play music t3g3
    else:
        play music t3
    if renpy.random.randint(0,2) == 0:
        $ config.mouse = {"default": [
                                    ("gui/mouse/s_head2.png", 0, 0),
                                    ("gui/mouse/s_head2.png", 0, 0),
                                    ("gui/mouse/s_head2.png", 0, 0),
                                    ("gui/mouse/s_head2.png", 0, 0),
                                    ("gui/mouse/s_head.png", 0, 0),
                                    ("gui/mouse/s_head.png", 0, 0),
                                    ("gui/mouse/s_head2.png", 0, 0),
                                    ("gui/mouse/s_head2.png", 0, 0),
                                    ("gui/mouse/s_head2.png", 0, 0),
                                    ("gui/mouse/s_head2.png", 0, 0),
                                    ("gui/mouse/s_head2.png", 0, 0),
                                    ("gui/mouse/s_head2.png", 0, 0),
                                    ("gui/mouse/s_head2.png", 0, 0),
                                    ("gui/mouse/s_head2.png", 0, 0),
                                    ("gui/mouse/s_head.png", 0, 0),
                                    ]}



    m "好了，各位！"
    m "我们都已经读完彼此的诗了，对吧？"
    $ config.mouse = None
    m "我们今天需要商量点别的事，请大家都坐到房间的前面来......"
    show natsuki 3c zorder 3 at f31
    n "是关于学园祭吗？"
    show natsuki zorder 2 at t31
    show monika 1j zorder 3 at f32
    m "嗯，差不多~"
    show monika 1a zorder 2 at t32
    show natsuki 1m zorder 3 at f31
    n "呃。我们真的非要准备学园祭不可吗？"
    n "我们好像也没办法在短短几天内，拼凑出什么像样的东西来啊。"
    n "可能到头来不仅没办法吸引到新成员，还会让我们自己出丑。"
    if faint_effect:
        $ currentpos = get_pos() + 2.0
        stop music fadeout 2.0
        show black onlayer front:
            alpha 0.0
            linear 2.0 alpha 1.0
    show natsuki zorder 2 at t31
    show yuri 2g zorder 3 at f33
    y "我也有这种担心呢。"
    if faint_effect:
        hide black onlayer front
        hide veins onlayer front
        hide i1 onlayer front
        hide i2 onlayer front
        show layer master
        show layer screens
        play music "<from " + str(currentpos) + " loop 4.618>bgm/3.ogg"
    y "临时抱佛脚什么的，我真的不擅长......"
    show yuri zorder 2 at t33
    show monika zorder 3 at f32
    m 1b "别想那么多嘛！"
    m "我们就弄得简单点，好吗？"
    m 2a "你听我说......"
    m 2m "我知道自从 [player] 加入社团后，大家都变得更加......有活力了......而且我们也开始了一些社团活动。"
    m 2d "但是现在还不是自满的时候。"
    m "我们还是只有四个社团成员......"
    m 2a "而学园祭是我们招募更多成员的唯一机会，明白吗？"
    show monika zorder 2 at t32
    show natsuki zorder 3 at f31
    n 5g "但是招新又有什么好处呢？"
    n "如果只是想成为正式社团的话，我们已经有足够的社员了。"
    n "人越多只会越吵，也越难管。"
    show natsuki zorder 2 at t31
    show monika zorder 3 at f32
    m 1g "夏树......"
    m "我觉得你这么想就不对了。"
    m "难道你不想和更多人分享你的热情吗？"
    m 3e "不想鼓舞他们去寻找当初将大家带到这里的那些感触吗？"
    m "文学部应该是一个能让人们自由表达自我的地方，而这正是其它社团所做不到的。"
    m "这里应该是一个亲密得让人不想离开的地方。"
    m 2e "我知道你也是这样想的，对吧？"
    m 2b "我知道我们都是这么想的！"
    m "所以说我们应该在学园祭上努力做出点什么......哪怕只是不起眼的小事！"
    m "对吧，[player]？"
    show monika 2a zorder 2 at t32
    mc "啊......"
    show natsuki zorder 3 at f31
    n 42c "拜托哦，莫妮卡！"
    n "你不能因为 [player] 不擅长回绝别人，就硬要他来同意你的意见啊。"
    stop music fadeout 1
    n 1c "莫妮卡，你想想。"
    n "你真的觉得我们有谁在加入文学部时考虑过别人的事吗？"
    n "优里在 [player] 来之前甚至连话都不说的。"
    n 2b "至于我，我只是觉得留在这儿比待在家好点罢了。"
    n "而 [player] 一开始甚至对文学都没什么兴趣。"
    n "这就是全部成员的情况了。"
    n 4w "抱歉，但你真的是唯一一个对招揽新人有兴趣的人。"
    n "我们觉得现在这样就挺好的。"
    n 4q "我知道你毕竟是部长，但是你这次确实应该考虑一下我们其他人的意见。"
    show natsuki zorder 2 at t31
    show monika zorder 3 at f32
    m 1g "......"
    "莫妮卡很明显被夏树的话吓了一跳。"
    play music t9
    m 1m "你说得......完全不对。"
    m 2m "我敢肯定，优里和 [player] 也希望能多招一点新成员......"
    m 2p "......对吧？"
    show monika zorder 2 at t32
    show yuri zorder 3 at f33
    y 4b "......"
    show yuri zorder 2 at t33
    mc "......"
    "我不知道优里是怎么想的，但我其实并不在乎。"
    "如果我表现得像莫妮卡期待中那样热情的话，那我就是在说谎了。"
    "不过，如果要我来救场的话......"
    mc "唔——"
    show monika zorder 3 at f32
    m 1i "免了。"
    m "夏树说得没错，不是吗？"
    m 1g "这个社团......"
    m "不过是给一小群人打发时间的地方罢了。"
    m 1r "为什么我会认为大家都会以我的角度考虑呢？"
    show monika zorder 2 at t32
    mc "但这也不代表我们反对找新成员啊......"
    show monika zorder 3 at f32
    m 1i "[player]，你到底是为了什么才加入的？"
    m "你那时期望的是什么呢？"
    show monika zorder 2 at t32
    mc "嗯——"
    "我最好还是不要如实发言吧？"
    show monika zorder 3 at f32
    m 1p "事实上......"
    m "如果我没记错的话，你甚至连拒绝加入的机会都没有。"
    show monika zorder 1 at thide
    hide monika
    "莫妮卡坐了下来，双眼盯着她的桌子。"
    m "这样一来，这一切又有什么意义呢？"
    m "或许办这个社团一开始就是个错误？"
    mc "......"
    show yuri zorder 3 at f33
    y 2g "夏树，看你干的好事......"
    show yuri zorder 2 at t33
    show natsuki zorder 3 at f31
    n 1p "啥？我吗？"
    n 1s "我只是把我想的讲出来罢了......"
    n "实话实说有什么错吗？"
    show natsuki zorder 2 at t31
    show yuri zorder 3 at f33
    y 2l "这和实话实说没关系。"
    y "是你说话的方式有问题。"
    y 2h "另外，你也没有权力代表我们所有人发言......"
    show yuri zorder 2 at t33
    show natsuki zorder 3 at f31
    n 1e "你根本就不理解！"
    n 5s "我只是......"
    n "我只是想要一个能够舒舒服服地和朋友打发时间的地方而已。"
    n 5u "我就希望社团能保持这个样子，有错吗？"
    n "因为真的......实在是没有几个这样的地方能留给我了......"
    n 5x "现在莫妮卡还想把它夺走！"
    show natsuki zorder 2 at t31
    mc "她没有想夺走——"
    show natsuki zorder 3 at f31
    n 1g "你错了，[player]。"
    n "那并不一样。"
    n 1q "如果按她的方向来，很快这里就会变味了。"
    n "如果我想要的是那种社团，那我可能早就加入什么别的白痴社团了。"
    n 12d "但是这里......"
    n "这里......"
    n 12e "至少还有那么一点点时间......"
    n "能让我感到安心。"
    "夏树开始收拾自己的东西。"
    n 12d "我还是回家算了。"
    n "我感觉......我现在不属于这里。"
    show natsuki zorder 2 at t31
    show yuri zorder 3 at f33
    y 3t "夏树......"
    show natsuki zorder 1 at thide
    hide natsuki
    "夏树无视了优里，径直走出了教室。"
    show yuri zorder 2 at t11
    y 3v "......"
    y "这下糟了......"
    y "我都不知道该怎么办了......"
    mc "那......"
    mc "你对学园祭有什么想法吗？"
    y 4b "我、我不知道......"
    $ style.say_dialogue = style.normal
    y "我其实有点无所谓吧......"
    show black zorder 3
    show y_glitch_head zorder 3:
        xpos 630 ypos -50 zoom 2.0
    $ style.say_dialogue = style.edited
    $ currentpos = get_pos() / 2.07
    play music "<from " + str(currentpos) + " loop 1.532>bgm/9g.ogg"
    y "谁想在乎那个烦人的幼稚鬼啊？"
    $ style.say_dialogue = style.normal
    $ currentpos = get_pos() * 2.07
    play music "<from " + str(currentpos) + " loop 3.172>bgm/9.ogg"
    hide black
    hide y_glitch_head
    y "我是说，我确实更喜欢现在这个安静平和的社团......"
    y "而且我只是觉得......和你在这里挺好的......"
    y 2t "但是！"
    y "毕竟我是副部长......"
    y "我不该像那样逃避我的责任......"
    show black zorder 3
    show y_glitch_head zorder 3:
        xpos 430 ypos -450 zoom 4.5
    $ style.say_dialogue = style.edited
    $ currentpos = get_pos() / 2.07
    play music "<from " + str(currentpos) + " loop 1.532>bgm/9g.ogg"
    y "那家伙就算是自杀了，也不会有人为她哭泣的。"
    $ style.say_dialogue = style.normal
    $ currentpos = get_pos() * 2.07
    stop music
    $ pause(0.5)
    play sound "sfx/stab.ogg"
    show blood_eye zorder 3:
        pos (710,380) zoom 2.5
    $ pause(0.75)
    stop sound
    play music "<from " + str(currentpos) + " loop 3.172>bgm/9.ogg"
    hide black
    hide y_glitch_head
    hide blood_eye
    y 2l "我应该尽力考虑所有人的感受，然后做出对社团来说正确的决定。"
    y 1t "那么，[player] 你呢？"
    y "你想从这个社团中得到什么？"
    "优里问了和莫妮卡相同的问题。"
    "我决定给个委婉的回答，至少比一言不发好点。"
    mc "......我觉得所有人都能好好相处是最重要的......"
    mc "......以及文学部本身是否能提供别的地方没有的东西。"
    mc "我觉得这并不取决于成员的数量，而是取决于他们的品质。"
    mc "这一点最终能让文学部变成一个特别的地方。"
    y 1u "这样啊......"
    y "你说得没错呢。"
    show blood_eye2 zorder 3:
        pos (568, 165)
    y 1f "每个成员都能以自己的方式为社团贡献力量。"
    y "虽然随着成员的更迭，社团的整体特质也会逐渐改变。"
    y 1h "不过我不觉得这一定是坏事。"
    y "偶尔也踏出自己的舒适圈也还不错嘛......"
    y 1a "所以如果你想帮莫妮卡准备学园祭的话，我也会站在你这边的。"
    hide blood_eye2
    mc "好的。"
    mc "那么，也许我们可以明天再和夏树好好谈谈......"
    "优里点了点头。"
    show monika 1g zorder 3 at f21
    show yuri zorder 2 at t22
    m "嘿，优里......"
    show monika zorder 2 at t21
    show yuri zorder 3 at f22
    y 1t "诶？"
    show yuri zorder 2 at t22
    show monika zorder 3 at f21
    m 1p "唔，我知道昨天的气氛有点尴尬......"
    m "但是我觉得我还是应该告诉你，你是个很棒的副部长。"
    m 1e "而且，也是个很棒的朋友。"
    show monika zorder 2 at t21
    show yuri zorder 3 at f22
    y 3s "莫、莫妮卡......"
    show yuri zorder 2 at t22
    show monika zorder 3 at f21
    m 2e "为了让文学部成为最棒的社团，我会尽我一切努力的。"
    m "好吗？"
    show monika zorder 2 at t21
    show yuri zorder 3 at f22
    y "......我也会。"
    show yuri zorder 2 at t22
    show monika zorder 3 at f21
    m 1a "嗯......"
    m "那我们今天就先回家吧。"
    m "关于学园祭的事情还是明天再讨论吧。"
    show monika zorder 2 at t21
    show yuri zorder 3 at f22
    y 1m "好的。"
    y "我很期待哦。"
    y 1a "所以一起走吗，[player]？"
    show yuri zorder 2 at t22
    show monika zorder 3 at f21
    m 1d "唔——"
    m 1p "你先别误会，只不过我......"
    m "我需要在走之前和[player]说几句话。"
    m 1d "只是问问他这段时间以来的感受......"
    m "作为部长，这对我挺重要的。"
    show monika zorder 2 at t21
    show yuri zorder 3 at f22
    y 2v "......"
    "优里看起来有点苦恼，但她并没有反对。"
    y 2t "好吧。"
    y 2s "我相信你的判断，莫妮卡。"
    y "那么，明天再见吧。"
    show yuri zorder 2 at t22
    show monika zorder 3 at f21
    m 1j "明天见~"
    show yuri zorder 1 at thide
    hide yuri
    "莫妮卡在优里离开教室时挥了挥手。"

    show monika 2a zorder 2 at t11
    m "呼......"
    m 2e "最近事情开始变成一团乱麻了，对吧？"
    show darkred:
        additive 0.2
        alpha 0
        linear 20 alpha 1.0
    show noise:
        alpha 0
        linear 20 alpha 0.1
    m "[player]，我只是想确保你在文学部里过得愉快。"
    m "我会非常不愿意看到你不开心。"
    m 2m "我觉得这应当是我作为部长的责任......"
    stop music
    m 4e "而且我真的很在乎你......你知道吗？"
    m "我不喜欢看到她们为难你。"
    m 4r "毕竟夏树有点太刻薄......"
    m 4m "而优里也有点......你懂的。"
    m 5a "啊哈哈......"
    m "有时候我会觉得，这里仿佛只有你我是真正的人。"
    m "你明白我的意思吧？"
    m 1g "但挺奇怪的，你来这都这么久了，我们却几乎没有单独相处过呢。"
    m 1n "啊......我是说......"
    m "虽然你实际加入社团好像也才那么几天......"
    m 1l "抱歉，我不是故意要说一些奇怪的话的！"
    m 1e "其实有些事情，我早就想跟你说了......"
    m "一些我知道只有你才能理解的事情。"
    stop music fadeout 3.0
    show black onlayer front:
        alpha 0.0
        0.25
        linear 3.0 alpha 1.00
    m "所以这就是为什么——\"{space=5000}{w=0.75}{nw}"
    m 1g "等一下，还没说完呢！\"{space=5000}{w=0.5}{nw}"
    m "不要啊！\"{space=5000}{w=0.5}{nw}"
    m "快停下！\"{space=5000}{w=1.0}{nw}"
    window hide(None)
    window auto
    hide black onlayer front





    return

