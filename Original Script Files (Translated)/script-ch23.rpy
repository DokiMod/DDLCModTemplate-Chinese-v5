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
    y "你来了，[player]！"
    y "我一直在等你呢。"
    y 2d "准备好继续一起看书了吗？"
    y "我今天带了我最好的茶——"
    show yuri 2f
    show natsuki 4w zorder 3 at f33
    n "莫妮卡！"
    n "我不是跟你说过别把——"
    n 1g "呃......"
    n "她这是又迟到了吗？"
    show natsuki zorder 2 at t33
    show yuri zorder 3 at f32
    y 1h "夏树，你还是和平常一样毫不顾及别人的感受啊。"
    show yuri zorder 2 at t32
    show natsuki zorder 3 at f33
    n 4c "你说什么？"
    show natsuki zorder 2 at t33
    show yuri zorder 3 at f32
    y 1r "每次我说话的时候，你就非得在旁边没完没了地大吼大叫打断我吗？"
    show yuri zorder 2 at t32
    show natsuki zorder 3 at f33
    n 1o "你到底在说什么啊？！"
    n 1q "说得好像我每天都会这样做似的。"
    n "我刚刚只是没注意到，好吗？真的不好意思。"
    n 4u "说真的......最近的你到底怎么了？"
    if get_appeal("natsuki") >= 2:
        n "你听我说......"
        n "我已经好好反思过昨天的行为了。"
        n 2q "我确实说得有点过分了......"
        n 1q "其实，我当时大概是被吓到了之类的吧。"
        n 1h "但我知道我们都在努力让社团变好。"
        n 1q "再来一两个新成员也不会怎么样，只要他们人好......"
        n 5w "而且我觉得再来一个女生的话，也挺好的......"
        n 5u "所以说......"
        show natsuki zorder 2 at t33
        show yuri zorder 3 at f32
        $ style.say_dialogue = style.normal
        y 2u "夏树啊......"
        $ style.say_dialogue = style.edited
        y 1f "没人在乎你的。"
        y "你这种体型还不如钻到售货机底下捡硬币呢。"
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
        m "这股热情也激励着我努力准备学园祭。"
    else:
        show natsuki zorder 2 at t33
        show yuri zorder 3 at f32
        y 2n "我吗？"
        y 2o "没、没事的......"
        show yuri zorder 2 at t32
        show natsuki zorder 3 at f33
        n "..."
        show natsuki zorder 2 at t33
        show yuri zorder 3 at f32
        y 2v "我真的有那么不对劲吗......？"
        show yuri zorder 2 at t32
        show natsuki zorder 3 at f33
        n 2m "看吧，{i}肯定{/i}有问题。"
        show natsuki zorder 2 at t33
        show yuri zorder 3 at f32
        y 3p "我自己会处理好的！"
        y 3y6 "那事情根本不值一提......"
        y 3o "我只是最近一直觉得有点紧张......"
        y 3n "总、总之，我们没必要讨论这个！"
        show yuri zorder 2 at t32
        show natsuki zorder 3 at f33
        n 2q "好吧，我只是觉得我需要挑明了讲讲而已。"
        n 5q "我其实也没有很在意......"
        show natsuki zorder 2 at t33
        show yuri 3e
        show monika 1g at l31
        m "噢，天哪......"
        m "我又是最后一个到的啊！"
        show natsuki zorder 3 at f33
        n 2c "没事，[player] 也是刚刚才到。"
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
        m "这股热情也激励着我努力准备学园祭，而且......"
        m 3n "唔......"
        show monika zorder 2 at t31
        show natsuki zorder 3 at f33
        n 5s "......"
        show natsuki zorder 2 at t33
        show monika zorder 3 at f31
        m 1l "好吧......"
        m "我、我忘记我要说什么了......"
        show monika zorder 1 at thide
        hide monika
        show yuri zorder 3 at f32
        y 2v "呃，说到学园祭，夏树......"
        y "我们昨天后来又稍微谈了下，然后......"
        y 2t "嗯......我们觉得应该支持学园祭的活动。"
        y 2l "不过......！"
        y 2h "我理解你不希望这个社团发生改变的想法。"
        y "我觉得某种角度上，我们跟你的感受是一样的。"
        y 2f "所以只要我们还在一同为了社团努力，它就永远不会变成我们不喜欢的样子。"
        show yuri zorder 2 at t32
        show natsuki zorder 3 at f33
        n "......"
        show natsuki zorder 2 at t33
        show yuri zorder 3 at f32
        y 2v "唔，还有......"
        y "如果你也能帮忙准备学园祭的话......"
        y 3r "......那我就买一本新的漫画送给你！"
        show yuri 3t zorder 2 at t32
        show natsuki zorder 3 at f33
        n 5h "......"
        n 2z "啊哈哈！"
        n "不好意思，你最后的那段话真的很好笑。"
        n "你听我说......"
        n "我已经好好反思过昨天的行为了。"
        n 2q "我确实说得有点过分了......"
        n 1q "其实，我当时大概是被吓到了之类的吧。"
        n 1h "但我知道我们都在努力让社团变好。"
        n 1q "再来一两个新成员也不会怎么样，只要他们人好......"
        n 5w "而且我觉得再来一个女生的话，也挺好的......"
        n 5e "......不过更重要的是，要是学园祭活动只是因为我没有加入就办得很糟，那我可不愿意看到！"
        n "毕竟你也知道我可是专家啊！"
        n 5c "所以我还是决定来帮忙，确保我们万无一失。"
        show natsuki zorder 2 at t33
        show yuri zorder 3 at f32
        y 2s "谢天谢地啊......"
        y "莫妮卡，这样真的很棒啊，不是吗？"
        show yuri zorder 2 at t32
        show natsuki zorder 3 at f33
        n 2k "......莫妮卡？"
        show natsuki zorder 2 at t33
        show monika 1o zorder 3 at f31
        m "啊——"
        m 1n "是啊，那太好了！"
        m "夏树，你肯定会帮上大忙的，、。"
    m 5 "话说回来，[player]......"
    m "你今天想做些什么呢？"
    m "我在想其实我们可以——"
    show monika zorder 2 at t31
    show yuri zorder 3 at f32
    y 1l "我们今天已经有计划了。"
    show yuri zorder 2 at t32
    show monika zorder 3 at f31
    m 1r "啊......"
    m "是这样吗，优里？"
    show monika zorder 2 at t31
    show yuri zorder 3 at f32
    y 1y6 "对啊。"
    y "[player] 正和我读一本小说读得起劲呢。"
    y 1y5 "我终于带领他进入文学的世界了，难道莫妮卡你不开心吗？"
    show yuri 1a zorder 2 at t32
    show monika zorder 3 at f31
    m 2l "我......"
    m "我以为......"
    m "我只是在——"
    m 1r "其实，没关系的。"
    m 1i "真的没什么。"
    m "你们想干什么都可以。"
    show monika zorder 2 at t31
    show yuri zorder 3 at hf32
    y 2y1 "{i}（太好了！）{/i}{w=0.5}{nw}"
    y 2u "唔......莫妮卡，感谢你能理解。"
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
    m "是时候分配一下学园祭的准备工作了。"
    m 1i "我们赶紧把这件事搞定吧。"
    if get_appeal("natsuki") >= 2:
        show natsuki 4q zorder 3 at f31
        n "......"
    else:
        show natsuki 4q zorder 3 at f31
        n "见鬼了......"
        n "为什么今天的气氛这么奇怪啊？"
        n "你看，就连优里都不能免疫。"
    show natsuki zorder 2 at t31
    show yuri 4b zorder 3 at f33
    y "唔......"
    y "死气沉沉的气氛通常预示着，有可怕的事情要发生了......"
    show yuri zorder 2 at t33
    show monika zorder 3 at f32
    m 2r "行啦，咱能不能快点搞定？"
    m 2d "我会去印刷和装订所有的诗册。"
    if get_appeal("natsuki") >= 2:
        m 2i "夏树，你可以去做小蛋糕。"
        m "我知道你至少还挺擅长做这个的。"
        show monika zorder 2 at t32
        show natsuki zorder 3 at f31
        n 5u "......"
        show natsuki zorder 2 at t31
        show monika zorder 3 at f32
    else:
        m "夏树，我只是在想——"
        show monika zorder 2 at t32
        show natsuki zorder 3 at f31
        n 2d "我想做纸杯蛋糕！"
        show natsuki 2a zorder 2 at t31
        show monika zorder 3 at f32
        m 2a "......嗯，那好。"
        m "很高兴我们还在同一频道上。"
    m 1m "优里，你可以..."
    m 1r "......好吧，其实无所谓的。"
    m 1i "你随便想做啥都行，只要你觉得对学园祭有帮助就行了。"
    show monika zorder 2 at t32
    show yuri zorder 3 at f33
    y 2h "莫妮卡......"
    y "真的，我才没有那么没用啊！"
    show yuri zorder 2 at t33
    show monika zorder 3 at f32
    m 2p "我、我当然知道！"
    show monika zorder 2 at t32
    show yuri zorder 3 at f33
    y 1l "我已经想好我要做什么了。"
    y 1h "一个成功的赏诗会，怎么能没有合适的气氛呢。"
    y "所以我会去做些装饰，再弄些漂亮的灯光烘托气氛。"
    show yuri zorder 2 at t33
    show monika zorder 3 at f32
    m 2j "看吧？"
    m "这就是个不错的主意啊！"
    m 1a "那现在我们所有人都有事可做了。"
    show monika zorder 2 at t32
    show yuri zorder 3 at f33
    y 2f "诶？"
    y "那 [player] 呢？"
    show yuri zorder 2 at t33
    show monika zorder 3 at f32
    m 2b "[player] 会来帮我的忙。"
    show monika 2a zorder 2 at t32
    show natsuki zorder 3 at f31
    n 4e "等会儿，帮你？"
    n "可是莫妮卡，你的工作不是最简单的吗？"
    show natsuki zorder 2 at t31
    show monika zorder 3 at f32
    m 1i "抱歉，但就是这么安排的。"
    show monika zorder 2 at t32
    show natsuki zorder 3 at f31
    n 1f "这凭什么啊！"
    n "你到底想搞什么？"
    show natsuki zorder 2 at t31
    show yuri zorder 3 at f33
    y 3h "我、我同意夏树说的！"
    y "你的工作本身就时候一个人做完......"
    y 3l "况且我的工作更耗时费力，所以更需要多一个人来帮忙。"
    show yuri zorder 2 at t33
    show natsuki zorder 3 at f31
    n 4c "我的也是！"
    show natsuki zorder 2 at t31
    show yuri zorder 3 at f33
    y 1h "什么，做纸杯蛋糕那种也算吗？"
    y "得了吧。"
    show yuri zorder 2 at t33
    show natsuki zorder 3 at f31
    n 1o "{i}你{/i}他妈懂个毛线哦！！"
    n 1x "你唯一关心的只不过是如何把 [player] 拴在你和你那些白痴才会看的书旁边吧。"
    n 1f "不仅你是这样，连莫妮卡{i}也是{/i}这样！"
    show natsuki zorder 2 at t31
    show monika zorder 3 at f32
    m 2g "喂！"
    m "我可什么都没做啊！"
    show monika zorder 2 at t32
    show natsuki zorder 3 at f31
    n 3e "好啊，那就别滥用自己的权力，不如让 [player] 自己决定去帮谁呗？"
    show natsuki zorder 2 at t31
    show monika zorder 3 at f32
    m 1p "我才没有......滥用权力。"
    show monika zorder 2 at t32
    show yuri zorder 3 at f33
    y 2h "是的，莫妮卡，你就是在滥用。"
    y "就让 [player] 自己选，可以吗？"
    show yuri zorder 2 at t33
    show monika zorder 3 at f32
    m 1r "好吧，好吧！"
    m "那行吧。"
    show monika 1h zorder 2 at t32
    show natsuki zorder 3 at f31
    n 3w "天哪......"
    n "[player]，我知道你肯定已经受够她们两个了。"
    n 3c "要不咱直接——"
    show natsuki zorder 2 at t31
    show yuri zorder 3 at f33
    y 2r "夏树，闭上你的臭嘴，让他自己做决定好吗？"
    show yuri zorder 2 at t33
    show natsuki zorder 3 at f31
    n 1o "该闭嘴的是{i}你{/i}，好吧？！"
    show natsuki zorder 2 at t31
    show monika zorder 3 at f32
    m 1r "老天爷啊......"
    m 1i "再吵下去就没完没了了。你还是赶快做决定吧，好吗？"
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
    m "我们这周末可以在你家见面了。"
    m "我保证会很有意思的。"
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
    y 2y4 "我无理取闹？"
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
    "莫妮卡咯咯笑着，被优里推出了门。"
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
    y 2s "这才是我想要的一切啊。"
    y 1y6 "[player]，没必要去和莫妮卡度过整个周末了。"
    y "没必要听她说话。"
    y 1y5 "你直接来我家吧。"
    y 3y5 "想想一整天，就只有我们两个人......"
    y "听起来不是很棒吗？"
    y 3y1 "啊哈哈哈！"
    y 3y4 "哇哦......我是不是有什么地方不对劲，对吗？"
    y "但我跟你说哦？"
    y 1y3 "我已经一点都不在乎了。"
    y "我这辈子从来没感觉这么好过。"
    y 1y4 "只是和你待在一起，就已经是远超我所能想象到的极致愉悦了。"
    y "我已经对你上瘾了。"
    y 3y4 "感觉就像，一旦不能和你呼吸同一片空气，我就马上会死掉似的。"
    y 4a "有这么一个超级在乎你的人，这种感觉不是超棒吗？"
    y "有这么一个愿意整个人生都把你视为中心的人？"
    y 2y6 "但如果这感觉真是这么好的话......"
    y 2y4 "那为什么我越来越觉得会有恐怖的事情发生呢？"
    y 2y6 "也许这就是为什么我一开始还打算阻止我自己......"
    y "但是这份感情现在实在是太过强烈了。"
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
    n "好耶，终于到学园祭时间了！"
    show natsuki 4k zorder 2 at t11
    n "哇哦，你居然到得比我早？"
    n "我还以为我已经够早——{nw}"
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
    m 2r "......"
    m 2l "啊哈哈哈！"
    m "嘛，还真是难堪呢。"
    m 2d "等会儿，[player]，难道你们整个周末都待在这里吗？"
    m "哦天哪......"
    m 2g "我没想到脚本已经崩坏到这种程度了。"
    m "真的非常抱歉！"
    m "那肯定很无聊吧......"
    m 2e "我会帮你清理干净的，好吗？"
    m "稍微等我一下就好......"
    $ console.clear_history()
    $ console("os.remove(\"characters/yuri.chr\")", "yuri.chr 已成功删除。")
    $ delete_character("yuri")
    $ pause(1.0)
    $ console("os.remove(\"characters/natsuki.chr\")", "natsuki.chr 已成功删除。")
    $ delete_character("natsuki")
    $ pause(1.0)
    m 2a "差不多搞定了。"
    m 2j "在此之前我想再吃一个小蛋糕，很快就好！"
    $ gtext = glitchtext(10)
    "莫妮卡揭开锡箔纸，从[gtext]的托盘里拿出了一个纸杯蛋糕。"
    m 2b "这蛋糕真的是最好吃的！"
    m "我得赶紧再吃一个，不然以后就没机会再吃了。"
    m 2a "你懂的，赶在这些蛋糕还有其他东西消失之前。"
    m "......不过，我真的不能让你再继续等下去了。"
    m 2j "稍微忍耐一下，好吗？"
    m 2a "应该只要几秒钟就好。"

    show screen tear(8, offtimeMult=1, ontimeMult=10)
    $ pause(1.5)

    $ delete_all_saves()
    $ persistent.playthrough = 3
    $ persistent.anticheat = renpy.random.randint(100000, 999999)
    $ persistent.autoload = "ch30_main"
    $ renpy.save_persistent()
    $ renpy.full_restart(transition=None, label="splashscreen")

    return

