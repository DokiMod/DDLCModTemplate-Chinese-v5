label ch20_from_ch10:
    scene bg residential_day
    with dissolve_scene_half
    play music t2
    jump ch20_main2

label ch20_main:
    stop music fadeout 2.0
    scene bg residential_day
    with dissolve_scene_full
    play music t2

label ch20_main2:
    "It's an ordinary school day, like any other."
    "Mornings are usually the worst, being surrounded by couples and friend groups walking to school together."
    "Meanwhile, I've always walked to school alone."
    "I always tell myself it's about time I meet some girls or something like that..."
    "But I have no motivation to join any clubs."
    "I'm perfectly content just getting by on the average while spending my free time on games and anime."
    "There's always the anime club, but it's not like there would be any girls in it anyway..."

    scene bg class_day
    with wipeleft_scene

    "在学校的日子和往常一样平淡，不知不觉就结束了。"
    "整理完书包后，我茫然地盯着墙，完全没有半点动力。"
    mc "啊，社团..."
    "There really aren't any that interest me."
    "Besides, most of them would probably be way too demanding for me to want to deal with."
    "我想除了动漫部外，我大概是别无选择了......"

    $ m_name = "???"

    m "...[player]?"
    window hide(None)
    show monika g2 zorder 2 at t11
    $ pause(0.75)
    show screen tear(20, 0.1, 0.1, 0, 40)
    play sound "sfx/s_kill_glitch1.ogg"
    $ pause(0.25)
    stop sound
    hide screen tear
    window show(None)
    show monika 1 zorder 2 at t11
    mc "......莫妮卡？"
    $ m_name = "莫妮卡"
    m 1b "Oh my goodness, I totally didn't expect to see you here!"
    m 5 "It's been a while, right?"
    mc "Ah..."
    mc "Yeah, it has."
    "Monika smiles sweetly."
    "We do know each other - well, we rarely talked, but we were in the same class last year."
    "Monika was probably the most popular girl in class - smart, beautiful, athletic."
    "Basically, completely out of my league."
    "So, having her smile at me so genuinely feels a little..."
    mc "What did you come in here for, anyway?"
    m 1a "Oh, I've just been looking for some supplies to use for my club."
    m 1d "Do you know if there's any construction paper in here?"
    m "Or markers?"
    mc "I guess you could check the closet."
    mc "...You're in the debate club, right?"
    m 5 "Ahaha, about that..."
    m "I actually quit the debate club."
    mc "Really? You quit?"
    m "Yeah..."
    m 2e "To be honest, I can't stand all of the politics around the major clubs."
    m "It feels like nothing but arguing about the budget and publicity and how to prepare for events..."
    m "I'd much rather take something I personally enjoy and make something special out of it."
    mc "In that case, what club did you decide to join?"
    m 1b "Actually, I'm starting a new one!"
    m "是一个文学社团哦！{nw}"
    show screen tear(20, 0.1, 0.1, 0, 40)
    window hide(None)
    play sound "sfx/s_kill_glitch1.ogg"
    $ pause(0.25)
    stop sound
    hide screen tear
    window show(None)
    m "是一个文学社团哦！{fast}"
    window auto
    mc "文学吗......？"
    "That sounds kind of...dull?"
    mc "How many members do you have so far?"
    m 5 "Um..."
    m "Ahaha..."
    m "It's kind of embarrassing, but there are only three of us so far."
    m "It's really hard to find new members for something that sounds so boring..."
    mc "Well, I can see that..."
    m 3d "But it's really not boring at all, you know!"
    m "Literature can be anything. Reading, writing, poetry..."
    m 3e "I mean, one of my members even keeps her manga collection in the clubroom..."
    mc "Wait...really?"
    m 2k "Yeah, it's funny, right?"
    m 2e "She always insists that manga is literature, too."
    m "I mean, she's not wrong, I guess..."
    m "And besides, a member's a member, right?"
    "...Did Monika say \"she\"?"
    "Hmm..."
    m 1a "Hey, [player]..."
    m "By any chance...are you still looking for a club to join?"
    mc "Ah--"
    mc "I mean, I guess so, but..."
    m "In that case..."
    m 5 "Is there any chance you could do me a big favor?"
    m "I won't ask you to join, but..."
    m "If you could at the very least visit my club, it would make me really happy."
    m "Please?"
    mc "Um..."
    "Well, I guess I have no reason to refuse..."
    "Besides, how could I ever refuse someone like Monika?"
    mc "Sure, I guess I could check it out."
    m 1k "Aah, awesome!"
    m 1b "You're really sweet, [player], you know that?"
    mc "I-It's nothing, really..."
    m 1a "Shall we go, then?"
    m "I'll look for the materials another time - you're more important."

    stop music fadeout 2.0

    scene bg corridor
    with wipeleft_scene

    "就这样，今天，我为了莫妮卡和她那无可抗拒的微笑而出卖了自己的灵魂。"
    "我害羞地跟着莫妮卡穿过校园，走上楼梯，登上了我很少涉足的楼层——这里通常只供高三学生上课和社团活动使用。"
    "元气满满的莫妮卡，一口气拉开了教室的门。"

    scene bg club_day2
    with wipeleft
    play music t3

    if renpy.random.randint(0, 2) == 0:
        show monika g1 at l31
    else:
        show monika 3b at l31
    m "我回来啦~！"
    m "而且我还带了位客人过来！"
    show yuri 2t zorder 2 at t33
    if not config.skipping:
        show screen invert(0.15, 0.3)
    y "诶？"
    y "客、客人？"
    show natsuki 4c zorder 2 at t32
    n "真的假的？你带了个男生过来？"
    n "太毁气氛了吧。"
    show monika 3m zorder 3 at f31
    m "Don't be mean, Natsuki..."
    m 3b "...But anyway, welcome to the club, [player]!"
    show monika 3a zorder 2 at t31
    mc "......"
    "看着眼前这幅景象，我根本说不出话来。"
    "这个社团里......"
    "{i}...全都是超级可爱的女孩子啊啊啊！！{/i}"

    show natsuki zorder 3 at f32
    n 5c "So, let me guess..."
    n "You're Monika's boyfriend, right?"
    show natsuki zorder 2 at t32
    mc "Wha--"
    mc "No, I'm not!"
    show yuri zorder 3 at f33
    y 2l "夏树......"
    $ n_name = '夏树'
    "The girl with the sour attitude, whose name is apparently Natsuki, is one I don't recognize."
    "Her small figure makes me think she's probably a first-year."

    show yuri zorder 2 at t33
    show monika zorder 3 at f31
    m 2l "A-Anyway, this is Natsuki, energetic as usual..."
    m 2b "And this is Yuri, the Vice President!"
    $ y_name = '优里'
    show monika 2a zorder 2 at t31
    show yuri zorder 3 at f33
    y 4 "I-It's nice to meet you..."
    "优里看起来更加成熟，却有点害羞，似乎不太跟得上夏树这种人的节奏。"
    show yuri zorder 2 at t33
    mc "Yeah... It's nice to meet both of you."
    show monika zorder 3 at f31
    m 1a "So, I ran into [player] in a classroom, and he decided to come check out the club."
    m "Isn't that great?"
    show monika zorder 2 at t31
    show natsuki zorder 3 at f32
    n 4e "Wait! Monika!"
    n "Didn't I tell you to let me know in advance before you brought anyone new?"
    n 4q "I was going to...well, you know..."
    show natsuki zorder 2 at t32
    show monika zorder 3 at f31
    m 1e "Sorry, sorry!"
    m "I didn't forget that, but I just happened to run into him."
    show monika zorder 2 at t31
    show yuri zorder 3 at f33
    y 1a "In that case, I should at least make some tea, right?"
    show yuri zorder 2 at t33
    show monika zorder 3 at f31
    m 1b "Yeah, that would be great!"
    m "Why don't you come sit down, [player]?"
    hide monika
    hide natsuki
    hide yuri
    with wipeleft
    "The girls have a few desks arranged to form a table."
    "Yuri walks to the corner of the room and opens the closet."
    "Meanwhile, Monika and Natsuki sit across from each other."
    "Still feeling awkward, I take a seat next to Monika."
    show monika 1a zorder 2 at t11
    m "So, I know you didn't really plan on coming here..."
    m "但我们会给你家一般的感觉，好吗？"
    m 1j "作为文学部的部长，我的职责就是让社团充满乐趣和活力，创造更有趣的社团时光！"
    mc "我有点惊讶，这个社团居然只有这么些人。"
    mc "新社团刚起步一定很难吧。"
    m 3b "确实不简单。"
    m "没有多少人愿意把全部精力投入到全新的事物中......"
    m "尤其是像文学这种，没法在第一时间吸引到注意力的东西。"
    m "你必须付出加倍的努力，才能向大家证明，你们这个社团既有趣又值得。"
    m "同时，这也让学园祭之类的校园活动，变得更加重要。"
    m 2k "我有自信能在我们毕业之前，将文学部发展壮大！"
    m "对吧，夏树？"
    show monika zorder 2 at t22
    show natsuki 4q zorder 2 at t21
    n "呃......"
    n "......大概吧。"
    "Natsuki reluctantly agrees."
    "这些截然不同的女孩们，却都感兴趣于同一个目标......"
    "想必莫妮卡一定花了不少功夫去找这两个成员。"
    "优里端着一套茶具，回到了桌旁。"
    "她小心翼翼地在每个人面前摆好一个茶杯，然后将茶壶放在桌子中央。"
    show natsuki zorder 1 at thide
    show monika zorder 1 at thide
    hide natsuki
    hide monika
    show yuri 1a zorder 2 at t21
    mc "你居然在部室里放了一整套茶具？"
    y "别担心，老师同意过了。"
    y "何况，热茶配好书，不也很美妙吗？"
    mc "啊...想必——也对......"
    show monika 4a zorder 3 at f22
    m "欸嘿嘿，别被吓到了，优里只是想给你留个好印象。"
    show monika zorder 2 at t22
    show yuri at hf21
    y 3n "诶？！不、不是这样的......"
    "优里难堪地把脸别了过去。"
    y 4b "我的意思是，那个......"
    show yuri zorder 2 at t21
    mc "我相信你。"
    mc "嗯，阅读和品茶或许不是我的消遣方式，但我起码还蛮喜欢喝茶。"
    show yuri zorder 3 at f21
    y 2u "那就好......"
    show yuri zorder 2 at t21
    "优里宽慰地浅浅一笑。"
    show monika zorder 1 at thide
    hide monika
    show yuri 1a zorder 2 at t32
    y "所以说，[player]，你平时都喜欢读些什么呢？"
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
    y "那些蕴含深层心理要素的故事也能让我沉浸其中。"
    y 2a "作者竟能刻意利用你在想象力上的匮乏，完全打你一个措手不及，这不是很神奇吗？"
    y "话又说回来，最近我倒是读了不少恐怖小说呢......"
    mc "啊，其实我之前也读过一本恐怖小说......"
    "我好不容易抓住了个稍微能有所共鸣的东西。"
    "不然再这样下去，优里就要变成对牛弹琴了。"
    show monika 1j zorder 3 at f33
    m "啊哈哈，确实是意料之中呢，优里。"
    m 1a "还蛮符合你的性格的。"
    show monika zorder 2 at t33
    show yuri zorder 3 at f32
    y 1a "哦，是吗？"
    y "说真的，如果一个故事能发人深省、或者将我带到另一个世界，那我真的会手不释卷的。"
    y "超现实恐怖小说会改变你看待世界的方式，哪怕只有一小会儿。"
    show yuri zorder 2 at t32
    show natsuki 5q zorder 3 at f31
    n "呃，我讨厌恐怖小说......"
    show natsuki zorder 2 at t31
    show yuri zorder 3 at f32
    y 1f "哦？为什么？"
    show yuri zorder 2 at t32
    show natsuki zorder 3 at f31
    n 5c "呃，我只不过......"
    "夏树在刹那间朝我瞥了一眼。"
    n 5q "当我没说。"
    show natsuki zorder 2 at t31
    show monika zorder 3 at f33
    m 1a "这就很合理了。你平常更喜欢写可爱的东西，对吧，夏树？"
    show monika zorder 2 at t33
    show natsuki 1o zorder 3 at f31
    n "什、什么啊？"
    n "你从哪里冒出来的这种奇怪想法？"
    show natsuki zorder 2 at t31
    show monika zorder 3 at f33
    m 3b "上次社团活动结束后，你在教室里掉了一张小纸片。"
    m "你写了一首诗，好像叫作——"
    show monika zorder 2 at t33
    show natsuki 1p zorder 3 at f31
    n "不要讲得那么大声啦！！"
    n "还有，把它还给我！"
    show natsuki zorder 2 at t31
    show monika zorder 3 at f33
    m 1j "好吧，好吧~"
    show monika 1a zorder 2 at t33
    mc "夏树，你也自己写诗的吗？"
    show natsuki zorder 3 at f31
    n 1c "嗯？大概也就偶尔写写吧。"
    n "不过你问这个干嘛？"
    show natsuki zorder 2 at t31
    mc "我觉得很厉害啊。"
    mc "为什么不找个时间分享一下你的诗作呢？"
    show natsuki zorder 3 at f31
    n 5q "不、不行！"
    "夏树移开了视线。"
    n "反正...你们不会喜欢的......"
    show natsuki zorder 2 at t31
    mc "啊......是对自己不够自信吗？"
    show yuri zorder 3 at f32
    y 2f "我能理解夏树的感受。"
    y "分享那种水平的文字，需要的可不仅仅是自信。"
    y 2k "最真挚的文字是写给自己的。"
    y "所以分享的前提是，你愿意向读者敞开心扉、暴露自己脆弱的一面，甚至展现内心最深处。"
    show yuri zorder 2 at t32
    show monika 2a zorder 3 at f33
    m "那优里，你也有写作的经验吗？"
    m "如果你愿意分享一下你的作品，没准在榜样作用下，夏树分享作品也会更自在的。"
    show yuri at s32
    y 3o "......"
    mc "想必优里也是一样的情况吧......"
    "气氛短时间陷入了沉默。"
    show monika zorder 3 at f33
    m 5a "嘿，我突然想到了个好主意！"
    m "要不这样？"
    show monika zorder 2 at t33
    show natsuki 2k zorder 3 at f31
    show yuri 3e zorder 3 at f32
    ny "......？"
    "夏树和优里疑惑地看向莫妮卡。"
    show natsuki zorder 2 at t31
    show yuri zorder 2 at t32
    show monika zorder 3 at f33
    m 2b "我们每个人都回家写一首自己的诗吧！"
    m "然后下次社团活动的时候，我们就可以彼此分享了。"
    m "这样的话，大家就扯平了！"
    show monika 2a zorder 2 at t33
    show natsuki zorder 3 at f31
    n 5q "呃——嗯......"
    show natsuki zorder 2 at t31
    show yuri 3v zorder 3 at f32
    y "......"
    show yuri zorder 2 at t32
    show monika 2m zorder 3 at f33
    m "Ah..."
    m "I mean, I thought it was a good idea..."
    show monika zorder 2 at t33
    show yuri zorder 3 at f32
    y 2l "Well..."
    y "...I think you're right, Monika."
    y 2f "We should probably start finding activities for all of us to participate in together."
    y 2h "I did decide to take on the responsibility of Vice President, after all..."
    y "I need to do my best to nurture the club as well as its members."
    y 2a "Besides, now that we have a new member..."
    y "It seems like a good step for us to take."
    y "Do you agree as well, [player]?"
    show yuri zorder 2 at t32
    mc "等一下......还有一个问题。"
    show monika zorder 3 at f33
    m 1d "诶？还有什么问题吗？"
    "既然话题又回到了拉我进社团这件事上，我终于能直截了当、一吐为快了。"
    show monika zorder 2 at t33
    mc "我从来都没说过我要加入文学部啊！"
    mc "虽然莫妮卡说服了我过来看看，但我可没下过任何决定。"
    mc "我还有别的一些社团要看，而且......呃......"
    show monika 1g
    show natsuki 4g
    show yuri 2e
    "我的思路戛然而止。"
    "三位女生全都用失落的眼神看着我。"
    show monika at s33
    m 1p "但、但是......"
    show yuri at s32
    y 2v "抱歉，我还以为......"
    show natsuki at s31
    n 5s "哼。"
    mc "欸......？"
    "The girls exchange glances before Monika turns back to me."
    show monika zorder 3 at f33
    m 1m "I...guess I need to tell you the truth, [player]."
    m "The thing is..."
    m 1p "...We don't have enough members yet to form an official club."
    m "We need four..."
    m "And I've been trying really, really hard to find new members."
    m "And if we don't find one more before the festival..."
    show monika zorder 2 at t33
    mc "......"
    "我......我对这些可爱的女生超没辙啊。"
    "这种情况下，我还怎么可能做出头脑清醒的决定啊？"
    "I would feel terrible for letting everyone down in this situation..."
    "And besides, the club itself seems pretty relaxed..."
    "所以说，只要付出写几首诗的代价，我就能每天和这些可爱的女生待在一起的话......"
    mc "......行吧。"
    mc "好了，那我就这么定了。"
    mc "我要加入文学部。"
    show monika 1e zorder 2 at t33
    show yuri 3f zorder 2 at t32
    show natsuki 1k zorder 2 at t31
    "女孩们的眼神一个接一个地泛起了光彩。"
    show monika zorder 3 at f33
    m "Oh my goodness, really?"
    m "Do you really mean that, [player]?"
    show monika zorder 2 at t33
    mc "Yeah..."
    mc "It could be fun, right?"
    show yuri zorder 3 at f32
    y 1m "你刚刚真的把我吓坏了......"
    show yuri zorder 2 at t32
    show natsuki zorder 3 at f31
    n 5q "讲真，你要是真就这么一走了之，那我绝对会气炸。"
    show natsuki zorder 2 at t31
    show monika zorder 3 at f33
    m "[player], I'm so happy..."
    m 1k "We can become an official club now!"
    m 1e "Thank you so much for this. You're really amazing."
    m "I'll do everything I can to give you a great time, okay?"
    show monika zorder 2 at t33
    mc "啊......那，谢谢。"
    show yuri zorder 1 at thide
    show natsuki zorder 1 at thide
    show monika zorder 2 at t11
    hide yuri
    hide natsuki
    m 3b "好了，各位！"
    m "这么一来，今天的社团活动到这里就正式圆满结束了。"
    m "各位要记得今晚的任务："
    m "每个人写一首诗，明天带到社团活动来，这样我们就可以分享了！"
    "莫妮卡又一次看向了我。"
    m 1a "[player]，期待你的表现哦。"
    show monika 5 at hop
    m "诶嘿嘿~"
    mc "没、没问题..."
    show monika zorder 1 at thide
    hide monika
    "我真的能用我那平庸的写作水平打动班级之星莫妮卡么？"
    "焦虑之情已经开始在我心中翻涌了。"
    "与此同时，优里开始整理茶具，大家继续有一搭没一搭地闲聊着。"
    mc "I guess I'll be on my way, then..."
    show monika 5a zorder 2 at t11
    m "Okay!"
    m "I'll see you tomorrow, then."
    m "I can't wait!"

    scene bg residential_day
    with wipeleft_scene

    "就这样，我离开了部室，踏上了回家的路。"
    "一路上，我的思绪都在三位女孩间游转："
    show natsuki 4a zorder 2 at t31
    "夏树，"
    show yuri 1a zorder 2 at t32
    "优里，"
    show monika 1a zorder 2 at t33
    "当然，还有莫妮卡。"
    "每天放学后泡在文学社团里，我真的会感到快乐吗？"
    "说不定我还有机会和当中的哪个女生拉近距离..."
    hide natsuki
    hide yuri
    hide monika
    with wipeleft
    "没错！"
    "我只要充分利用条件就行了，好运总有一天会来的。"
    "看来万事都要从今晚写的这首诗诗开始了..."

    stop music fadeout 2.0
    scene black with dissolve_scene_full
    $ config.skipping = False
    $ config.allow_skipping = False
    $ allow_skipping = False

    call screen confirm("你解锁了一首特别诗篇。\n想现在就读读看吗？", Return(True), Return(False))
    if _return:
        call expression "poem_special_" + str(persistent.special_poems[0])
    else:
        pass

    return

