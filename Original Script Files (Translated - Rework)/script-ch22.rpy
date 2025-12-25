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
    y 3t "A-Ah..."
    y "[player]..."
    y 3u "Don't say those kinds of things so frankly..."
    y "They make me a little too happy."
    y 1s "I'm really glad that you're such an understanding person..."
    y "And I'm really glad that you joined this club."
    y "Everything is a little bit brighter with you around, and--"
    y 1t "Ah--"
    y 4c "Sorry, what am I saying right now...?"
    y "I just--"
    show natsuki 2c zorder 3 at f33
    n "Hey, have you guys seen Monika?"
    show natsuki zorder 2 at t33
    show yuri 3n at h32
    y "Ah--!"
    mc "No, I haven't..."
    mc "I was also kind of wondering where she was."
    show natsuki zorder 3 at f33
    n 5g "Man..."
    n 5c "Yuri, I'm guessing you haven't, either?"
    show natsuki zorder 2 at t33
    show yuri zorder 3 at f32
    y 4a "..."
    "Yuri is clearly taken aback by how calmly Natsuki is addressing her."
    y "N-No, I haven't..."
    show yuri zorder 2 at t32
    show natsuki zorder 3 at f33
    n 1u "Jeez, this isn't like her at all."
    n "I know it's stupid, but I can't help but worry a little bit..."
    show natsuki zorder 2 at t33
    show yuri zorder 3 at f32
    y 2t "..."
    show yuri zorder 2 at t32
    show natsuki 1h zorder 3 at f33
    n "What?"
    n "Why're you looking at me like that?"
    show natsuki zorder 2 at t33
    show yuri zorder 3 at f32
    y "U-Um..."
    y "Natsuki, about yesterday..."
    y 3w "I-I just wanted to apologize!"
    y "I promise I didn't mean any of the things I said!"
    y 3t "And I'll do my best to stay under control from now on..."
    y "So--"
    show yuri zorder 2 at t32
    show natsuki zorder 3 at f33
    n 2c "Yuri, what the heck are you talking about?"
    n "Did you do something yesterday?"
    show natsuki zorder 2 at t33
    show yuri zorder 3 at f32
    y 3f "...Eh?"
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
    n 2j "I'll accept your apology anyway, if it helps you feel better about it."
    n "Besides, it's kinda nice to hear, since I was always afraid you secretly hated me or something like that."
    n 2z "欸嘿嘿。"
    show natsuki zorder 2 at t33
    show yuri zorder 3 at f32
    y 3q "N-No, not at all...!"
    y "I don't hate you..."
    show yuri zorder 2 at t32
    show natsuki zorder 3 at f33
    n 2l "啊哈哈。"
    n "Well, you're kind of weird, but I don't hate you either."
    show natsuki zorder 2 at t33
    show yuri zorder 3 at f32
    y 3t "..."
    "Natsuki turns to me."
    show yuri zorder 2 at t32
    show natsuki zorder 3 at f33
    n 2a "You're still on trial, though."
    show natsuki zorder 2 at t33
    mc "Hey...!"
    "Suddenly, the door swings open."
    show monika 1g at l41
    m "抱歉抱歉！非常抱歉！"
    mc "啊，你终于到了......"
    show monika zorder 3 at f41
    m "我真不是故意要迟到的......"
    m "希望你们没有在担心我之类的！"
    show monika zorder 2 at t41
    mc "Nah..."
    mc "Well, Natsuki was."
    show natsuki zorder 3 at f33
    n 1p "I-I was not!!"
    show natsuki zorder 2 at t33
    show monika zorder 3 at f41
    m 1k "啊哈哈。"
    show monika zorder 2 at t41
    show natsuki zorder 3 at f33
    n 1s "...What took you so long, anyway?"
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
    m 1l "Ah, don't give me more credit than I deserve."
    m 1m "I guess I've been practicing for a while, but I'm still not really good yet."
    show monika zorder 2 at t41
    show yuri zorder 3 at f32
    y 1a "Still..."
    y "That must require a lot of dedication."
    y "So, I'm still impressed."
    show yuri zorder 2 at t32
    show monika zorder 3 at f41
    m 5 "Aw, well thanks, Yuri~"
    show monika zorder 2 at t41
    show natsuki zorder 3 at f33
    n 2d "You should play something for us sometime!"
    show natsuki zorder 2 at t33
    show monika zorder 3 at f41
    m "Ahaha, that's..."
    "Monika looks at me."
    m 1a "Well, I am working on writing a song, but it's not quite done yet..."
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
    m "I was hoping that I could share it with you, anyway."
    m "I guess that's why I've been practicing so much recently."
    mc "这样啊......"
    "I'm not sure if Monika was referring to the whole club, or just me..."
    mc "那么，就祝你好运吧。"
    m 1j "谢谢~！"
    m 1a "话说，我没有错过什么吧？"
    mc "呃......其实没错过什么。"
    show monika zorder 1 at thide
    hide monika
    "I choose not to bring up anything that the three of us talked about."
    "Besides, Natsuki has already run off into the closet."
    show yuri 2q zorder 2 at t11
    y "[player]..."
    y "Um..."
    y "Since your compliments put me in a good mood..."
    y "I was wondering if you would like to spend some time together today."
    y 3o "I mean--in the club!"
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
    y 3y5 "Okay!"
    y "Can we start now?"
    y "Let's find a place to sit--"
    y 3n "A-Ah--"
    y "I'm being a little forceful, aren't I...?"
    y 4c "I'm sorry!"
    y "My heart...just won't stop pounding, for some reason..."
    mc "Don't worry about it."
    mc "If anything, it's nice to see you have so much energy."
    y 3q "Y-Yeah!"
    y "But..."
    y 3j "I need to try to calm down."
    y "I won't be able to focus on reading like this..."
    mc "Take your time."
    "Yuri takes a deep breath, then pulls a copy of the book out of her bag."
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
    mc "...I think the most important thing is for everyone to get along..."
    mc "...And for the club to provide something that you can't get anywhere else."
    mc "I don't think it's about how many members, but rather the quality of each member."
    mc "That's what will end up making the Literature Club a special place."
    y 1u "I see..."
    y "I really agree with you."
    show blood_eye2 zorder 3:
        pos (568, 165)
    y 1f "Each member contributes their own qualities in a special way."
    y "With each change in members, the identity of the club as a whole will change, too."
    y 1h "I don't think that's necessarily a bad thing."
    y "Stepping out of your comfort zone once in a while..."
    y 1a "So if you would like to help Monika with the festival, then I'm on your side as well."
    hide blood_eye2
    mc "Alright."
    mc "Well, maybe we can all talk to Natsuki tomorrow..."
    "Yuri nods."
    show monika 1g zorder 3 at f21
    show yuri zorder 2 at t22
    m "Hey, Yuri..."
    show monika zorder 2 at t21
    show yuri zorder 3 at f22
    y 1t "Eh?"
    show yuri zorder 2 at t22
    show monika zorder 3 at f21
    m 1p "Um, I know things were a little awkward yesterday..."
    m "But I feel like you deserve to know that I still think you're a wonderful vice president."
    m 1e "And also, a wonderful friend."
    show monika zorder 2 at t21
    show yuri zorder 3 at f22
    y 3s "M-Monika..."
    show yuri zorder 2 at t22
    show monika zorder 3 at f21
    m 2e "I want to do everything I can to make this the best club ever."
    m "Okay?"
    show monika zorder 2 at t21
    show yuri zorder 3 at f22
    y "...Me too."
    show yuri zorder 2 at t22
    show monika zorder 3 at f21
    m 1a "Yeah..."
    m "Let's all go home for today."
    m "We'll talk about the festival tomorrow."
    show monika zorder 2 at t21
    show yuri zorder 3 at f22
    y 1m "Okay."
    y "I look forward to it."
    y 1a "Shall we go, [player]?"
    show yuri zorder 2 at t22
    show monika zorder 3 at f21
    m 1d "Um--"
    m 1p "Please don't take this the wrong way, but..."
    m "I'm going to chat a little bit with [player] before we leave."
    m 1d "Just to see what he thinks of his time here and all that..."
    m "It's important to me, as President."
    show monika zorder 2 at t21
    show yuri zorder 3 at f22
    y 2v "..."
    "Yuri looks a little troubled, but she doesn't protest."
    y 2t "Okay."
    y 2s "I trust your judgment, Monika."
    y "In that case, I'll see the two of you tomorrow."
    show yuri zorder 2 at t22
    show monika zorder 3 at f21
    m 1j "See you tomorrow~"
    show yuri zorder 1 at thide
    hide yuri
    "Monika waves as Yuri exits the classroom."

    show monika 2a zorder 2 at t11
    m "Phew..."
    m 2e "Things have been a bit hectic lately, haven't they?"
    show darkred:
        additive 0.2
        alpha 0
        linear 20 alpha 1.0
    show noise:
        alpha 0
        linear 20 alpha 0.1
    m "[player], I just wanted to make sure you're enjoying your time at this club."
    m "I would really hate to see you unhappy."
    m 2m "I feel kind of like I'm responsible for that, as President..."
    stop music
    m 4e "And I really do care about you...you know?"
    m "I don't like seeing the other girls give you a hard time."
    m 4r "With how mean Natsuki is and everything..."
    m 4m "And Yuri being a little bit...you know."
    m 5a "啊哈哈......"
    m "Sometimes it feels like you and I are the only real people here."
    m "You know what I mean?"
    m 1g "But it's weird, because in all the time you've been here, we've hardly gotten to spend any time together."
    m 1n "啊......我是说......"
    m "I guess it's technically only been a couple days..."
    m 1l "Sorry, I didn't mean to say something weird!"
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

