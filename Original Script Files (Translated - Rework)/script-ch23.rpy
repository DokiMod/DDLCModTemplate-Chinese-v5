image noface1:
    topleft
    xtile 10 ytile 10
    block:
        block:
            choice:
                "images/sayori/noface1.png"
            choice:
                "images/sayori/noface1b.png"
        block:
            choice:
                0.075
            choice:
                0.3
            choice:
                0.4
            choice:
                0.5
            choice:
                0.6
        repeat
image noface2:
    "images/sayori/noface2.png"
    xalign 0.95 yalign 0.47

label ch23_main:
    if renpy.random.randint(0,15) == 0 and not seen_eyes_this_chapter:
        $ quick_menu = False
        scene white
        show noface1
        show noface2
        with dissolve_scene_half
        play sound "sfx/gnid.ogg"
        $ pause(7)
        $ quick_menu = True
        scene bg club_day2
        show yuri 2 zorder 2 at i11
    else:
        scene bg club_day2
        with dissolve_scene_half

    play music t6
    show yuri 2y5 zorder 2 at t11
    y "Hi, [player]!"
    y "I've been waiting for you."
    y 2d "Are you ready to continue reading?"
    y "I brought my best tea today--"
    show yuri 2f
    show natsuki 4w zorder 3 at f33
    n "Monika!"
    n "I told you not to--"
    n 1g "Ugh..."
    n "Is she really late again?"
    show natsuki zorder 2 at t33
    show yuri zorder 3 at f32
    y 1h "Inconsiderate as usual, Natsuki."
    show yuri zorder 2 at t32
    show natsuki zorder 3 at f33
    n 4c "Excuse me?"
    show natsuki zorder 2 at t33
    show yuri zorder 3 at f32
    y 1r "Must you always interrupt my conversations with your incessant yelling?"
    show yuri zorder 2 at t32
    show natsuki zorder 3 at f33
    n 1o "What are you talking about?!"
    n 1q "You say that like I do it on a regular basis or something."
    n "I just wasn't paying attention, okay? I'm sorry."
    n 4u "Seriously... What's gotten into you lately?"
    if get_appeal("natsuki") >= 2:
        n "Look..."
        n "I did some thinking about yesterday."
        n 2q "I was a little more hostile than I meant to be..."
        n 1q "I guess I really felt threatened or something."
        n 1h "But I know this is something we're doing together."
        n 1q "Another new member wouldn't hurt, as long as they're cool..."
        n 5w "And I guess another girl would be nice this time..."
        n 5u "So..."
        show natsuki zorder 2 at t33
        show yuri zorder 3 at f32
        $ style.say_dialogue = style.normal
        y 2u "夏树啊......"
        $ style.say_dialogue = style.edited
        y 1f "没人在乎你的。"
        y "Why don't you go look for some coins under the vending machines or something?"
        $ style.say_dialogue = style.normal
        show yuri zorder 2 at t32
        show natsuki zorder 3 at f33
        n 1p "——！"
        n 1r "......"
        n 12f "......"
        show natsuki at thide
        hide natsuki
        $ pause(1.0)
        show monika 1g at l31
        m "噢，天哪......"
        m "我又是最后一个到的啊！"
        show yuri zorder 3 at f32
        y 1f "你又去练习钢琴了吗？"
        show yuri zorder 2 at t32
        show monika zorder 3 at f31
        m 5a "是的......"
        m "啊哈哈......"
        show monika zorder 2 at t31
        show yuri zorder 3 at f32
        y 1m "你还真是有毅力呢。"
        y "不但创办了这个社团，现在又开始学钢琴......"
        show yuri 1a zorder 2 at t32
        show monika zorder 3 at f31
        m 1a "嗯，也许不是毅力......"
        m 3a "我觉得是热情驱使着我。"
        m "It motivates me to work hard for the festival, too."
    else:
        show natsuki zorder 2 at t33
        show yuri zorder 3 at f32
        y 2n "Me?"
        y 2o "N-Nothing..."
        show yuri zorder 2 at t32
        show natsuki zorder 3 at f33
        n "..."
        show natsuki zorder 2 at t33
        show yuri zorder 3 at f32
        y 2v "Is it really that bad...?"
        show yuri zorder 2 at t32
        show natsuki zorder 3 at f33
        n 2m "See, it {i}is{/i} something."
        show natsuki zorder 2 at t33
        show yuri zorder 3 at f32
        y 3p "I'll get over it!"
        y 3y6 "It's not even anything noteworthy..."
        y 3o "I've just been feeling a little on edge lately..."
        y 3n "A-Anyway, we don't need to talk about it!"
        show yuri zorder 2 at t32
        show natsuki zorder 3 at f33
        n 2q "Well, I just felt like I needed to bring it up."
        n 5q "It's not like I really care or anything..."
        show natsuki zorder 2 at t33
        show yuri 3e
        show monika 1g at l31
        m "噢，天哪......"
        m "我又是最后一个到的啊！"
        show natsuki zorder 3 at f33
        n 2c "Well, [player] just walked in too."
        show natsuki zorder 2 at t33
        show yuri zorder 3 at f32
        y 1f "你又去练习钢琴了吗？"
        show yuri zorder 2 at t32
        show monika zorder 3 at f31
        m 5a "是的......"
        m "啊哈哈..."
        show monika zorder 2 at t31
        show yuri zorder 3 at f32
        y 1m "你还真是有毅力呢。"
        y "不但创办了这个社团，现在又开始学钢琴......"
        show yuri 1a zorder 2 at t32
        show monika zorder 3 at f31
        m 1a "嗯，也许不是毅力......"
        m 3a "我觉得是热情驱使着我。"
        m "It motivates me to work hard for the festival and..."
        m 3n "Um..."
        show monika zorder 2 at t31
        show natsuki zorder 3 at f33
        n 5s "..."
        show natsuki zorder 2 at t33
        show monika zorder 3 at f31
        m 1l "Right..."
        m "I-I forgot..."
        show monika zorder 1 at thide
        hide monika
        show yuri zorder 3 at f32
        y 2v "Um, about that, Natsuki..."
        y "We were all talking yesterday, and..."
        y 2t "Well...we decided that we would like to support the festival as well."
        y 2l "However...!"
        y 2h "I understand how you feel about not wanting the club to change."
        y "I think we all kind of feel that way."
        y 2f "So as long as we're all working together, this club will never become something we don't want."
        show yuri zorder 2 at t32
        show natsuki zorder 3 at f33
        n "..."
        show natsuki zorder 2 at t33
        show yuri zorder 3 at f32
        y 2v "Um, also..."
        y "If you help us out with the festival..."
        y 3r "...Then I'll buy you a new manga!"
        show yuri 3t zorder 2 at t32
        show natsuki zorder 3 at f33
        n 5h "..."
        n 2z "Ahahaha!"
        n "Sorry, that last part was really funny."
        n 2c "Look..."
        n "I did some thinking about yesterday."
        n 2q "I was a little more hostile than I meant to be..."
        n 1q "I guess I really felt threatened or something."
        n 1h "But I know this is something we're doing together."
        n 1q "Another new member wouldn't hurt, as long as they're cool..."
        n 5w "And I guess another girl would be nice this time..."
        n 5e "...But more importantly, I would hate to see the event suck just because I chose to back out!"
        n "I'm a pro, you know!"
        n 5c "So I'm gonna help too, and we'll make sure it's done right."
        show natsuki zorder 2 at t33
        show yuri zorder 3 at f32
        y 2s "Thank goodness..."
        y "Isn't that great, Monika?"
        show yuri zorder 2 at t32
        show natsuki zorder 3 at f33
        n 2k "...Monika?"
        show natsuki zorder 2 at t33
        show monika 1o zorder 3 at f31
        m "Ah--"
        m 1n "Yeah, that's wonderful!"
        m "It wouldn't be the same without you, Natsuki."
    m 5 "Anyway, [player]..."
    m "What do you want to do today?"
    m "I was thinking we could--"
    show monika zorder 2 at t31
    show yuri zorder 3 at f32
    y 1l "We already have plans today."
    show yuri zorder 2 at t32
    show monika zorder 3 at f31
    m 1r "Ah..."
    m "Is that so, Yuri?"
    show monika zorder 2 at t31
    show yuri zorder 3 at f32
    y 1y6 "That's correct."
    y "[player] is already engaged in a novel that we're reading together."
    y 1y5 "Aren't you glad I've already gotten him into literature, Monika?"
    show yuri 1a zorder 2 at t32
    show monika zorder 3 at f31
    m 2l "I..."
    m "I suppose..."
    m "I was just--"
    m 1r "Actually, it doesn't matter."
    m 1i "It really doesn't."
    m "You guys can do whatever you want."
    show monika zorder 2 at t31
    show yuri zorder 3 at hf32
    y 2y1 "{i}（太好了！）{/i}{w=0.5}{nw}"
    y 2u "Um... Thank you for understanding, Monika."
    if poemwinner[2] == "natsuki":
        $ poemwinner[2] = "yuri"
        $ set_character_poem_appeal("yuri", 1, 1)
        $ set_character_poem_appeal("yuri", 2, 1)
        $ set_character_poem_appeal("yuri", 3, 1)

    scene bg club_day2
    show yuri 3 zorder 2 at t11
    with wipeleft_scene
    call yuri_exclusive2_2_ch22

    return



label ch23_end:
    stop music fadeout 1.0
    scene black
    with wipeleft_scene
    call screen confirm("", Return(True), Return(True))
    if _return:
        call expression "poem_special_" + str(persistent.special_poems[2])
        scene black with Dissolve(1.0)
    else:
        pass
    scene bg club_day2
    show monika 4b zorder 2 at t32
    with wipeleft_scene
    play music t3
    m "好了，各位！"
    m "It's time to figure out the festival preparations."
    m 1i "Let's hurry and get this over with."
    if get_appeal("natsuki") >= 2:
        show natsuki 4q zorder 3 at f31
        n "..."
    else:
        show natsuki 4q zorder 3 at f31
        n "Jeez..."
        n "Why is the mood so weird today?"
        n "Look, even Yuri isn't immune to it."
    show natsuki zorder 2 at t31
    show yuri 4b zorder 3 at f33
    y "Uu..."
    y "Stagnating air is common foreshadowing that something terrible is about to happen..."
    show yuri zorder 2 at t33
    show monika zorder 3 at f32
    m 2r "Look, can we just get this done?"
    m 2d "I'm going to be printing and assembling all the poetry pamphlets."
    if get_appeal("natsuki") >= 2:
        m 2i "夏树，你可以去做小蛋糕。"
        m "I know you're at least good at that."
        show monika zorder 2 at t32
        show natsuki zorder 3 at f31
        n 5u "..."
        show natsuki zorder 2 at t31
        show monika zorder 3 at f32
    else:
        m "Natsuki, I was thinking--"
        show monika zorder 2 at t32
        show natsuki zorder 3 at f31
        n 2d "I want to make cupcakes!"
        show natsuki 2a zorder 2 at t31
        show monika zorder 3 at f32
        m 2a "...Yeah, that."
        m "Glad we're on the same page."
    m 1m "优里，你可以..."
    m 1r "...Well, it doesn't matter."
    m 1i "Do whatever you want, as long as you think it'll help."
    show monika zorder 2 at t32
    show yuri zorder 3 at f33
    y 2h "Monika..."
    y "I'm not useless, you know!"
    show yuri zorder 2 at t33
    show monika zorder 3 at f32
    m 2p "I-I know that!"
    show monika zorder 2 at t32
    show yuri zorder 3 at f33
    y 1l "I already know what I'd like to do."
    y 1h "We can't run a successful poetry event without having the right atmosphere for the occasion."
    y "So I'm going to make decorations and set up some nice mood lighting."
    show yuri zorder 2 at t33
    show monika zorder 3 at f32
    m 2j "There, see?"
    m "That's a great idea!"
    m 1a "And that gives us all something to do."
    show monika zorder 2 at t32
    show yuri zorder 3 at f33
    y 2f "Eh?"
    y "What about [player]?"
    show yuri zorder 2 at t33
    show monika zorder 3 at f32
    m 2b "[player] is going to help me."
    show monika 2a zorder 2 at t32
    show natsuki zorder 3 at f31
    n 4e "Wait, you?"
    n "You have the easiest job, Monika!"
    show natsuki zorder 2 at t31
    show monika zorder 3 at f32
    m 1i "Sorry, but that's just how it is."
    show monika zorder 2 at t32
    show natsuki zorder 3 at f31
    n 1f "Like hell it is!"
    n "What are you trying to pull?"
    show natsuki zorder 2 at t31
    show yuri zorder 3 at f33
    y 3h "I-I agree with Natsuki!"
    y "Not only is your work already most suitable for one person..."
    y 3l "But my task is laborious enough to benefit from an extra pair of hands."
    show yuri zorder 2 at t33
    show natsuki zorder 3 at f31
    n 4c "Mine too!"
    show natsuki zorder 2 at t31
    show yuri zorder 3 at f33
    y 1h "What, your cupcakes?"
    y "Please."
    show yuri zorder 2 at t33
    show natsuki zorder 3 at f31
    n 1o "Like {i}you{/i} would fucking know!"
    n 1x "All you care about now is dragging [player] around with you and your stupid books."
    n 1f "You {i}and{/i} Monika!"
    show natsuki zorder 2 at t31
    show monika zorder 3 at f32
    m 2g "Hey!"
    m "I didn't even do anything!"
    show monika zorder 2 at t32
    show natsuki zorder 3 at f31
    n 3e "Okay, then why not let [player] decide who to help instead of abusing your power?"
    show natsuki zorder 2 at t31
    show monika zorder 3 at f32
    m 1p "I'm not...abusing my power."
    show monika zorder 2 at t32
    show yuri zorder 3 at f33
    y 2h "Yes you are, Monika."
    y "Just let [player] make the choice, okay?"
    show yuri zorder 2 at t33
    show monika zorder 3 at f32
    m 1r "Okay, fine!"
    m "Fine."
    show monika 1h zorder 2 at t32
    show natsuki zorder 3 at f31
    n 3w "天哪......"
    n "[player], I know how fed up you are with these two by now."
    n 3c "We can just--"
    show natsuki zorder 2 at t31
    show yuri zorder 3 at f33
    y 2r "Natsuki, shut your fucking mouth and let him decide for himself."
    show yuri zorder 2 at t33
    show natsuki zorder 3 at f31
    n 1o "{i}You{/i} shut your mouth!"
    show natsuki zorder 2 at t31
    show monika zorder 3 at f32
    m 1r "老天爷啊..."
    m 1i "This is never going to end. Just make the choice, okay?"
    show monika zorder 2 at t32
    python:
        madechoice = renpy.display_menu([("夏树。", "natsuki"), ("优里。", "yuri"), ("莫妮卡。", "monika")], screen="rigged_choice")

    if madechoice != "monika":
        window hide(None)
        $ musicpos = get_pos()
        stop music
        scene white
        show yuripupils zorder 10
        $ pause(3.0)
        show bg club_day:
            alpha 0.05
            yoffset 0 ytile 2
            linear 5.25 yoffset -720
            repeat
        show noise:
            alpha 0.1
        $ gtext = glitchtext(80)
        window auto
        menu:
            "[gtext]"
            "莫妮卡":
                pass
            "莫妮卡":
                pass
            "莫妮卡":
                pass
            "莫妮卡":
                pass
            "莫妮卡":
                pass
            "莫妮卡":
                pass
            "莫妮卡":
                pass
            "莫妮卡":
                pass
            "莫妮卡":
                pass
            "莫妮卡":
                pass
        scene bg club_day
        $ audio.t3m = "<from " + str(musicpos) + " loop 4.618>bgm/3.ogg"
        play music t3m
        show monika 5 at i11
    else:
        show natsuki zorder 1 at thide
        show yuri zorder 1 at thide
        hide natsuki
        hide yuri

    m 5a "耶，你选了我诶！"
    m "We can meet at your house this weekend."
    m "I promise it'll be fun."
    m "周日你方便吗？"
    show natsuki 1e zorder 3 at f31
    n "你他娘的在开什么玩笑？"
    n "这可一点都不公平！"
    show natsuki zorder 2 at t31
    show monika zorder 3 at f32
    m 2i "哪里不公平了，夏树。"
    m "这是他自己选的。"
    show monika zorder 2 at t32
    show yuri 3r zorder 3 at f33
    y "不，这很有问题！"
    y "把脏活累活全都抛给我们，结果自己把 [player] 带走了。"
    y "简直是厚颜无耻！"
    show yuri zorder 2 at t33
    show monika zorder 3 at f32
    m 2r "优里，我甚至都还没给你分配工作呢。"
    m 2i "我都让你自己决定要做些什么了。"
    m "你这样真的有点无理取闹了。"
    stop music
    show monika zorder 2 at t32
    show yuri zorder 3 at f33
    y 2y4 "我又无理取闹上了？"
    y 2y3 "啊哈哈哈！"
    y "莫妮卡啊，我都不敢相信你竟然是这种自私自利的妄想狂！"
    y "只要有什么事情你没参与到，你就会把 [player] 从我身边拖走，每次都是这样。"
    y 1y1 "你到底是在嫉妒呢？"
    y "还是疯了呢？"
    y 1y3 "还是说，你对自己的憎恨溢了一地，恨到开始随便把别人当出气筒了？"
    y 1y4 "那我这边给你个小建议吧：考虑一下自杀怎么样？"
    y "这对你的精神健康可是大有裨益的哦。"
    show yuri zorder 2 at t33
    show natsuki zorder 3 at f31
    n 5u "优里，你这话说得有点恐怖了......"
    show natsuki zorder 2 at t31
    show monika zorder 3 at f32
    m 1r "别管她了，夏树。"
    m 1i "我认为她并不想让我们俩在这里继续待着。"
    show monika zorder 2 at t32
    show yuri zorder 3 at f33
    y 2y3 "看吧，也没那么难嘛。"
    y "我只是想跟他再多独处一会而已。"
    y "这种要求很过分吗？"
    hide natsuki
    hide monika
    hide yuri
    with wipeleft
    "优里赶着莫妮卡和夏树出了教室门口。"
    show monika 5a zorder 2 at t11
    m "喂，[player]......"
    m "优里真的有点那个，对吧？"
    show monika zorder 1 at thide
    hide monika
    "Monika giggles as Yuri pushes her out the door."
    python:
        try: renpy.file(config.basedir + "/have a nice weekend!")
        except: open(config.basedir + "/have a nice weekend!", "w").write("G2pilVJccjJiQZ1poiM3iYZhj3I0IRbvj3wxomnoeOatVHUxZ2ozGKJgjXMzj2LgoOitBOM1dSDzHMatdRpmQZpidNehG29mkTxwmDJbGJxsjnVeQT9mTPSwSAOwnuWhSE50ByMpcuJoqGstJOCxqHCtdvG3HJV0TOGuwOIyoOGhwOHgm2GhlZpyISJik3J/") # 不想翻译这个
        try: os.remove(config.basedir + "/hxppy thxughts.png")
        except: pass
        try: os.remove(config.basedir + "/CAN YOU HEAR ME.txt")
        except: pass
        try: os.remove(config.basedir + "/iiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiii.txt")
        except: pass

    play music t10y
    show yuri 2m zorder 2 at t11
    y "终于啊。"
    y 2y1 "终于啊！"
    y 2s "这才是我想要的一切。"
    y 1y6 "[player]，没必要去和莫妮卡度过整个周末了。"
    y "没必要听她说话。"
    y 1y5 "你直接来我家吧。"
    y 3y5 "想想一整天，就只有我们两个人......"
    y "听起来不是很棒吗？"
    y 3y1 "啊哈哈哈！"
    y 3y4 "哇哦......我是不是有什么地方不对劲，对吗？"
    y "但我跟你说哦？"
    y 1y3 "我已经一点都不在乎了。"
    y "I've never felt this good my whole life."
    y 1y4 "Just being with you is a far greater pleasure than anything I could imagine."
    y "I'm addicted to you."
    y 3y4 "It feels like I'm going to die if I'm not breathing the same air as you."
    y 4a "Doesn't it feel nice to have someone care about you so much?"
    y "To have someone who wants to revolve their entire life around you?"
    y 2y6 "But if it feels so good..."
    y 2y4 "Then why does it feel more and more like something horrible is going to happen?"
    y 2y6 "Maybe that's why I tried stopping myself at first..."
    y "But the feeling is too strong now."
    y 3y1 "[player]，我已经什么都不在乎了！"
    y "我必须要告诉你！"
    y 3y4 "我......我爱你爱到要疯了！"
    y "就像是每一寸肌肤......每一滴血液......都在尖叫着你的名字。"
    y 3y3 "无论后果如何都已经无所谓了！"
    y "莫妮卡有没有在听我也不管了！"
    y 3w "[player]，求你了，看看我有多爱你。"
    y 3m "我爱你爱到甚至偷了你的笔拿去自慰。"
    y 3y4 "我满脑子只想扒开你的表皮，在你的体内游走。"
    y 3y6 "我想要让你永远属于我。"
    y "而我也将只属于你。"
    y "听起来是不是很完美啊？"
    y 3s "告诉我吧，[player]。"
    y "告诉我你会成为我的爱人。"
    y "你愿意接受我的告白吗？"

    menu:
        "接受。":
            jump yuri_kill
        "不接受。":
            jump yuri_kill

label yuri_kill:
    $ quick_menu = False
    window hide(None)
    stop music
    $ pause(1.0)


    window auto
    $ persistent.yuri_kill = 1
    $ in_yuri_kill = True
label yuri_kill_1:
    window auto
    $ persistent.autoload = "yuri_kill_1"
    $ renpy.save_persistent()
    $ quick_menu = False
    stop music
    scene bg club_day
    show yuri 3d at i11
    y "......啊哈哈哈。"
    y "啊哈哈哈哈哈哈!"
    $ style.say_dialogue = style.normal
    y 3y5 "啊哈哈哈哈哈哈哈哈!"
    $ style.say_dialogue = style.edited
    y 3y3 "啊哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈{nw}"
    window hide(None)
    window auto
    $ style.say_dialogue = style.normal

    play sound "sfx/yuri-kill.ogg"
    $ starttime = datetime.datetime.now()

    $ pause(1.43 - (datetime.datetime.now() - starttime).total_seconds())
    show yuri stab_1

    $ pause(2.18 - (datetime.datetime.now() - starttime).total_seconds())
    show yuri stab_2
    show blood:
        pos (610,485)

    $ pause(3.43 - (datetime.datetime.now() - starttime).total_seconds())
    show yuri stab_3

    $ pause(4.18 - (datetime.datetime.now() - starttime).total_seconds())
    show yuri stab_2
    show blood:
        pos (610,485)
    show yuri stab_4 with ImageDissolve("images/yuri/stab/4_wipe.png", 0.25)

    $ pause(5.68 - (datetime.datetime.now() - starttime).total_seconds())
    show yuri stab_5

    $ pause(6.38 - (datetime.datetime.now() - starttime).total_seconds())
    show yuri stab_6:
        2.55
        easeout_cubic 0.5 yoffset 300
    show blood as blood2:
        pos (635,335)

    $ pause(8.93 - (datetime.datetime.now() - starttime).total_seconds())
    hide blood
    hide blood2

    $ pause(9.18 - (datetime.datetime.now() - starttime).total_seconds())
    play sound fall

    $ pause(9.43 - (datetime.datetime.now() - starttime).total_seconds())
    scene black

    $ pause(11.43 - (datetime.datetime.now() - starttime).total_seconds())

    scene black
    show y_kill
    with dissolve_cg
label yuri_kill_2:
    $ quick_menu = True
    $ persistent.autoload = "yuri_kill_2"
    $ renpy.save_persistent()
    python:
        _history_list = []
        m.add_history(None, "", """欢迎来到文学部！我一直以来的梦想，就是能在自己喜欢的事情上做出点名堂来，所以我凭借着自己对文学的热忱，创立了这个文学部。呐，现在你也是文学部的一员啦~快快来这款可爱的游戏里帮我圆梦吧！文学部的生活轻松惬意，每天除了跟社团成员闲聊，就是举办各种有趣的社团活动！社团里的其他成员全都个性鲜明，而且超~级可爱~接下来就让我向你介绍一下其他成员吧~纱世里，青春阳光的少女，总是元气满满，开朗健谈！快乐就是她最珍视的事！夏树，看似可爱娇小的少女，但却有着惊人的魄力，可能随时都会给你自信一击！优里，羞怯内向又神秘的少女，喜欢在文学的世界里寻找慰藉。......当然了，还有我！文学部的部长，莫妮卡！你能跟所有人都交上朋友，让文学部的氛围变得更加融洽吗？我超~级期待哦~不过呢，我也知道你其实是个善解人意的小可爱，所以啊——花最多的时间来陪我吧，你能保证吗？欢迎来到文学部！我一直以来的梦想，就是能在自己喜欢的事情上做出点名堂来，所以我凭借着自己对文学的热忱，创立了这个文学部。呐，现在你也是文学部的一员啦~快快来这款可爱的游戏里帮我圆梦吧！文学部的生活轻松惬意，每天除了跟社团成员闲聊，就是举办各种有趣的社团活动！社团里的其他成员全都个性鲜明，而且超~级可爱~接下来就让我向你介绍一下其他成员吧~纱世里，青春阳光的少女，总是元气满满，开朗健谈！快乐就是她最珍视的事！夏树，看似可爱娇小的少女，但却有着惊人的魄力，可能随时都会给你自信一击！优里，羞怯内向又神秘的少女，喜欢在文学的世界里寻找慰藉。......当然了，还有我！文学部的部长，莫妮卡！你能跟所有人都交上朋友，让文学部的氛围变得更加融洽吗？我超~级期待哦~不过呢，我也知道你其实是个善解人意的小可爱，所以啊——花最多的时间来陪我吧，你能保证吗？欢迎来到文学部！我一直以来的梦想，就是能在自己喜欢的事情上做出点名堂来，所以我凭借着自己对文学的热忱，创立了这个文学部。呐，现在你也是文学部的一员啦~快快来这款可爱的游戏里帮我圆梦吧！文学部的生活轻松惬意，每天除了跟社团成员闲聊，就是举办各种有趣的社团活动！社团里的其他成员全都个性鲜明，而且超~级可爱~接下来就让我向你介绍一下其他成员吧~纱世里，青春阳光的少女，总是元气满满，开朗健谈！快乐就是她最珍视的事！夏树，看似可爱娇小的少女，但却有着惊人的魄力，可能随时都会给你自信一击！优里，羞怯内向又神秘的少女，喜欢在文学的世界里寻找慰藉。......当然了，还有我！文学部的部长，莫妮卡！你能跟所有人都交上朋友，让文学部的氛围变得更加融洽吗？我超~级期待哦~不过呢，我也知道你其实是个善解人意的小可爱，所以啊——花最多的时间来陪我吧，你能保证吗？花最多的时间来陪我吧，你能保证吗？花最多的时间来陪我吧，你能保证吗？花最多的时间来陪我吧，你能保证吗？花最多的时间来陪我吧，你能保证吗？花最多的时间来陪我吧，你能保证吗？花最多的时间来陪我吧，你能保证吗？花最多的时间来陪我吧，你能保证吗？花最多的时间来陪我吧，你能保证吗？花最多的时间来陪我吧，你能保证吗？花最多的时间来陪我吧，你能保证吗？花最多的时间来陪我吧，你能保证吗？花最多的时间来陪""")

    $ style.say_dialogue = style.edited
    scene black
    window show(None)
    if not renpy.music.get_playing(channel='music') == audio.t6s:
        $ audiostart = str(renpy.random.random() * 360)
        $ audio.t6s = "<from " + audiostart + " loop 43.572>bgm/6s.ogg"
        play music t6s
    show y_kill
    label yuri_kill_loop:
        $ persistent.yuri_kill += 1
        if persistent.yuri_kill < 1440:
            $ gtext = glitchtext(renpy.random.randint(8, 80))
            if config.developer:
                y "[persistent.yuri_kill] [gtext]"
            else:
                y "[gtext]"
            $ _history_list.pop()
            jump yuri_kill_loop
        else:
            $ delete_all_saves()
            jump yuri_kill_3

label yuri_kill_3:
    python:
        try: os.remove(config.basedir + "/have a nice weekend!")
        except: pass
    $ persistent.autoload = "yuri_kill_3"
    $ renpy.save_persistent()
    $ config.skipping = False
    $ config.allow_skipping = False
    $ allow_skipping = False
    $ quick_menu = False
    $ style.say_dialogue = style.normal
    $ gtext = glitchtext(renpy.random.randint(8, 80))
    if not renpy.music.get_playing(channel='music') == audio.t6s:
        $ audiostart = str(renpy.random.random() * 360)
        $ audio.t6s = "<from " + audiostart + " loop 43.572>bgm/6s.ogg"
        play music t6s
    scene bg club_day
    "[gtext]"
    window auto
    n "Alright, it's festival time!"
    show natsuki 4k zorder 2 at t11
    n "Wow, you got here before me?"
    n "I thought I was pretty ea--{nw}"
    show natsuki scream at h11
    n "噫呀！"
    n "啊啊啊啊啊啊啊啊啊啊啊啊啊——！！！"
    $ pause(1.0)
    show natsuki scream at h11
    $ pause(0.75)
    show natsuki vomit at h11
    $ pause(1.25)
    show natsuki at lhide
    hide natsuki
    "夏树跑了出去。"
    m "......"
    show monika 2b zorder 2 at t11
    m "我来啦！"
    m 2d "[player]，发生什么事了吗？"
    m "夏树刚刚从我身边跑了出去......"
    m 2i "......哦......"
    m "......哦。"
    m 2r "..."
    m 2l "Ahahaha!"
    m "Well, that's a shame."
    m 2d "Wait, were you here the entire weekend, [player]?"
    m "Oh, jeez..."
    m 2g "I didn't realize the script was broken that badly."
    m "I'm super sorry!"
    m "It must have been pretty boring..."
    m 2e "I'll make it up to you, okay?"
    m "Just gimme a sec..."
    $ console.clear_history()
    $ console("os.remove(\"characters/yuri.chr\")", "yuri.chr deleted successfully.")
    $ delete_character("yuri")
    $ pause(1.0)
    $ console("os.remove(\"characters/natsuki.chr\")", "natsuki.chr deleted successfully.")
    $ delete_character("natsuki")
    $ pause(1.0)
    m 2a "I'm almost done."
    m 2j "I just want to have a cupcake real quick!"
    $ gtext = glitchtext(10)
    "Monika lifts the foil from [gtext]'s tray and takes a cupcake."
    m 2b "Seriously, these are the best!"
    m "I really just had to have one, since it's the last time I'll ever get the chance to."
    m 2a "You know, before they stop existing and everything."
    m "...But anyway, I really shouldn't be making you wait any longer."
    m 2j "Just bear with me, okay?"
    m 2a "This should only take a second."

    show screen tear(8, offtimeMult=1, ontimeMult=10)
    $ pause(1.5)

    $ delete_all_saves()
    $ persistent.playthrough = 3
    $ persistent.anticheat = renpy.random.randint(100000, 999999)
    $ persistent.autoload = "ch30_main"
    $ renpy.save_persistent()
    $ renpy.full_restart(transition=None, label="splashscreen")

    return

