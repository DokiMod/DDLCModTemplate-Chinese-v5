image exception_bg = "#dadada" # maybe #d0d0d0?
image fake_exception = Text("发生异常。", size=40, style="_default")
image fake_exception2 = Text("File \"game/script-ch5.rpy\", line 307\n查看 traceback.txt 了解详情。", size=20, style="_default") 
# 不翻译 File "game/script-ch5.rpy", line 307 系故意为之
image splash_glitch:
    subpixel True
    "images/bg/splash-glitch.png"
    alpha 0.0
    pause 0.5
    linear 0.5 alpha 1.0
    pause 2.5
    linear 0.5 alpha 0.0
    "gui/menu_bg.png"
    topleft
    alpha 0.0
    parallel:
        xoffset 0 yoffset 0
        linear 0.25 xoffset -100 yoffset -100
        repeat
    parallel:
        linear 0.5 alpha 1.0
    parallel:
        ypos 0
        pause 1.0
        easeout 1.0 ypos -500
image splash_glitch2:
    subpixel True
    "gui/menu_bg.png"
    topleft
    block:
        xoffset 0 yoffset 0
        linear 0.05 xoffset -100 yoffset -100
        repeat

image splash_glitch_m:
    subpixel True
    "gui/menu_art_m.png"
    zoom 0.5
    xpos 0.5 ypos 0.5
    pause 0.1
    parallel:
        xpos 0.3 ypos 1.2
        linear 0.08 ypos 0.1
        repeat
    parallel:
        pause 0.5
        alpha 0.0

image splash_glitch_n:
    subpixel True
    "gui/menu_art_n.png"
    zoom 0.5
    pause 0.2
    xpos 0.8 ypos 0.8
    pause 0.05
    xpos 0.2 ypos 0.7
    pause 0.05
    xpos 0.4 ypos 0.2
    pause 0.05
    xpos 0.7 ypos 1.2
    pause 0.05
    xpos 0.1 ypos 1.0
    pause 0.05
    xpos 0.2 ypos 0.6
    pause 0.05
    xpos 0.9 ypos 0.4
    pause 0.05
    alpha 0.0

image splash_glitch_y:
    subpixel True
    "gui/menu_art_y.png"
    zoom 0.5
    ypos 1.3
    block:
        xpos 0.85
        pause 0.02
        xpos 0.81
        pause 0.02
        repeat


label ch5_main:
    stop music fadeout 2.0
    scene bg residential_day
    with dissolve_scene_full

    "今天就是学园祭了。"
    "先不说平时如何，我原以为今天一定会跟纱世里一起走路上学。"
    "但纱世里没接我的电话。"
    "我考虑过直接去她家叫醒她，但又觉得似乎有点做过头了。"
    "与此同时，学园祭活动的准备工作也差不多完成了。"
    if ch4_scene == "natsuki":
        "我小心翼翼地将两个托盘叠放在一起，一个人把蛋糕全端了出来。"
        "夏树的短信现在像风暴一样轰炸着我，但是我两只手都腾不开，根本没办法回复她。"
    else:
        "我和优里上色的条幅已经干了，我轻轻将它卷好带了出来。"
        "她发来一条友好的短信，提醒我别忘带什么东西，我让她大可放心。"
    "有趣的是，我对赏诗会的感受可能跟夏树差不多。"
    "我更期待赏诗会赶紧结束，接着就能和纱世里以及[ch4_name]一起尽情享受学园祭了。"
    "不过以我对莫妮卡的了解，我相信赏诗会肯定会大获成功。"

    scene bg club_day with wipeleft_scene
    show monika 5 zorder 2 at t11
    m "[player]！"
    m "你今天可是第一个到的呢。"
    m "谢谢你来得这么早！"
    mc "这下有意思了，我还以为至少优里会比我早到呢。"
    "莫妮卡正在将诗册摆在教室的每一张课桌上。"
    "这些诗册肯定就是她在周末准备的，里面收录了我们要朗诵的那些诗。"
    "我最后还是随便在网上找了一首莫妮卡可能会喜欢的诗，然后就交给她了。"
    "所以，一会儿我就要朗诵那首诗了。"
    m 1d "你没和纱世里一起来，这让我有点惊讶。"
    mc "啊，她又睡过头了......"
    mc "那个小笨蛋。"
    mc "今天是这么重要的日子，按理说她应该浑身是劲，准时爬起来的......"
    "嘴上这么说着，我却忽然想起纱世里昨天对我说的那些话......"
    "我突然感觉大事不妙，心里知道这对她来说应该没那么简单。"
    "而我当初那么说，只是因为我习惯了那么想。"
    "不过......"
    "或许到头来，我还是应该去她家里叫醒她？"
    m 1k "啊哈哈。"
    m 4b "你应该为她再负责一点的，[player]！"
    m "尤其是你昨天还和她进行了那样一番情感交流......"
    m "但今早你好像有点让她的心思吊着了哦？"
    show monika 4a
    mc "情感交流吗......？"
    mc "莫妮卡——你怎么连这个都知道啊？？"
    m 2a "那当然了。"
    m "毕竟我是社团的部长。"
    mc "但、但、但是——！"
    "我甚至尴尬地结巴起来。"
    "纱世里真的这么快就把昨天的事告诉莫妮卡了？"
    if sayori_confess:
        "不会真说了我们现在是......情侣了？"
        "我可还没打算向其他人公开呢......"
    else:
        "不会真说了昨天她告白被我拒绝的事了？"
        "搞得我像是个坏人一样......"
        "但是我最清楚怎样做对她最好，不是吗？"
    mc "天哪......"
    mc "你知道的绝非事情全貌，所以......"
    m 2j "不用担心。"
    m "我知道的可能比你想象的还多得多哦。"
    mc "诶......？"
    "莫妮卡和平时一样友善，但听完这句话后，我不知为何，忽觉脊背阵阵发凉。"
    m 5 "嘿，你想不想看一眼这些诗册？"
    m "效果相当不错哦！"
    mc "嗯，可以啊。"
    "我从摆在桌上的诗册中拿了一本。"
    mc "嗯，效果确实挺好的。"
    mc "诗册这么精致，一定能让大家更加认真看待文学部。"
    m "是啊，我也是这么想的！"
    show monika zorder 1 at thide
    hide monika
    "我翻了几页。"
    "每位成员选择的诗都工整地印刷在各自的分页上，整个册子看上去很有专业的质感。"
    "我认出了那天夏树和优里练习时所朗诵的诗。"
    mc "这是......？"
    "我翻到了纱世里的诗。"
    "她那天练习时朗诵的不是这首。"
    "这是一首我从来没读过的......"
    $ poem_db.show_poem("poem_s3")
    mc "啊——"
    "这到底是啥......？"
    "读着这首诗，我的心仿佛沉到了谷底。"
    show monika 1d zorder 2 at t11
    m "[player]？"
    m "怎么了？"
    mc "啊，没事......"
    "这首诗感觉与纱世里所写的其他诗都截然不同。"
    "但绝对不止于此......"
    mc "我、我改主意了！"
    mc "我准备去接纱世里过来，所以......"
    m "啊——"
    m 1b "好吧，没问题！"
    m "快去快回，好吗？"
    scene bg corridor with wipeleft
    "我迅速离开了教室。"
    m "别把自己累坏了哦~"
    "莫妮卡在后面喊道。"
    "我加快了脚步。"

    scene bg residential_day with wipeleft_scene
    "我到底在想什么啊？"
    "我真该为了纱世里再多努力一点的。"
    "叫她起床，甚至只是等她一起上学，真的不算什么难事才对的。"
    "就算单纯只是陪着她走去学校，都能让她非常开心。"
    "更何况......"
    "我昨天才告诉她，一切都会和从前没有两样。"
    "对她来说这样就够了，我也一定会尽力做到。"

    scene bg house with wipeleft
    "我赶到纱世里家，敲了敲门。"
    "虽然我没指望会有人回应，毕竟她也根本没接电话。"
    "就和昨天一样，我自己打开了门，直接走了进去。"
    scene black with wipeleft
    mc "纱世里？"
    "她真是个大睡虫啊......"
    "我咽了下口水。"
    "我不敢相信，到头来我还真得这么做了。"
    "真要跑到她家叫她起床......"
    if sayori_confess:
        "倒也确实是男朋友应该做的事情，对吧？"
    else:
        "这种事情不应该是男朋友才做的吗？"
    "不管怎样......"
    "感觉就应该这么做。"

    "我站在纱世里的房间外，敲了敲门。"
    mc "纱世里？"
    mc "醒醒啦，小傻瓜......"
    "没有回应。"
    "我真的不想就这样走进她的房间......"
    "这样算是侵犯隐私了吧？"
    "但她实在让我别无他法。"
    "我轻轻地打开了房门。"
    mc "{cps=30}.......纱世——{/cps}{nw}"
    $ persistent.playthrough = 1
    $ persistent.anticheat = renpy.random.randint(100000, 999999)
    $ renpy.save_persistent()
    $ delete_character("sayori")
    $ in_sayori_kill = True
    window hide(None)
    window auto
    play music td
    show s_kill_bg2
    show s_kill2
    show s_kill_bg as s_kill_bg at s_kill_bg_start
    show s_kill as s_kill at s_kill_start
    $ pause(3.75)
    show s_kill_bg2 as s_kill_bg
    show s_kill2 as s_kill
    $ pause(0.01)
    show screen tear(20, 0.1, 0.1, 0, 40)
    play sound "sfx/s_kill_glitch1.ogg"
    $ pause(0.25)
    stop sound
    hide screen tear
    hide s_kill_bg
    hide s_kill
    show s_kill_bg_zoom zorder 1
    show s_kill_bg2_zoom zorder 1
    show s_kill_zoom zorder 3
    show s_kill2_zoom zorder 3
    show s_kill as s_kill_zoom_trans zorder 3:
        truecenter
        alpha 0.5
        zoom 2.0 xalign 0.5 yalign 0.05
        pause 0.5
        dizzy(1, 1.0)
    $ pause(2.0)
    show noise zorder 3:
        alpha 0.0
        linear 3.0 alpha 0.25
    show vignette zorder 3:
        alpha 0.0
        linear 3.0 alpha 0.75
    $ pause(1.5)
    show white zorder 2
    show splash_glitch zorder 2
    $ pause(1.5)
    show screen tear(20, 0.1, 0.1, 0, 40)
    play sound "sfx/s_kill_glitch1.ogg"
    $ pause(0.2)
    stop sound
    hide screen tear
    $ pause(4.0)
    show screen tear(20, 0.1, 0.1, 0, 40)
    play sound "sfx/s_kill_glitch1.ogg"
    $ pause(0.2)
    stop sound
    hide screen tear
    hide splash_glitch
    show splash_glitch2 zorder 2
    show splash_glitch_m zorder 2
    show splash_glitch_n zorder 2
    show splash_glitch_y zorder 2
    $ pause(0.75)
    hide white
    hide splash_glitch2
    hide splash_glitch_m
    hide splash_glitch_n
    hide splash_glitch_y
    show exception_bg zorder 2
    show fake_exception zorder 2:
        xpos 0.1 ypos 0.05
    show fake_exception2 zorder 2:
        xpos 0.1 ypos 0.15
    python:
        try: sys.modules['renpy.error'].report_exception("哦，天哪...我是不是不小心把什么东西给弄坏了？等会儿，我应该可以把这东西修好的......吧......\n但话又说回来了！直接把她删掉，会不会省事多了？毕竟把事情变得那么复杂的人就是她啊。啊哈哈！既然如此，那我就试试看吧。", False)
        except: pass
    $ pause(6.0)


    "......"
    hide fake_exception
    hide fake_exception2
    hide exception_bg
    "什么鬼啊......？"
    "{i}搞什么鬼啊？？{/i}"
    "这是什么噩梦吗？"
    "这......这绝对是。"
    "这不是真的。"
    "这绝对不可能是真的。"
    "纱世里绝对不会做这种事。"
    "就在几天前，一切都还很正常的。"
    "就是因为这样，我才不敢相信我眼前所见到的这一幕啊......！"
    scene black with dissolve_cg
    "我尽力压制着想呕吐的冲动。"
    "就在昨天......"
    "我还告诉纱世里我会守护她。"
    "我告诉她，我知道怎样才对她最好、一切都会好起来的。"
    "可是，为什么......？"
    "她为什么要这么做......"
    "我什么忙都没帮到吗？"
    "我到底做错了什么？"
    if sayori_confess:
        "是我向她告白导致的吗......"
        "我真不该向她告白的。"
        "她根本就不需要我的告白。"
        "她甚至都已经告诉了我，别人的关心让她有多么痛苦。"
        "那我到底还为什么要向她告白，弄得她更加痛苦了呢？"
    else:
        "是我拒绝了她的告白导致的吗......"
        "肯定是这件事把她压垮了。"
        "她那万分痛苦的嚎哭，依旧在我耳边回响。"
        "在她最需要我的时候，为什么我还能对她做这样的事？"
    "为什么我如此自私啊？"
    "这全都是我的错——！"
    "我的思绪蜂拥而至，反复呈现本可阻止这场悲剧的一切举措。"
    "如果我再多花点时间陪她就好了。"
    "如果陪她走路上学就好了。"
    if sayori_confess:
        "还有，如果和她保持往常的朋友关系就好了......"
    else:
        "还有，如果能接受她的告白，实现她想要的感情就好了......"
    "......那样我就可以阻止这件事了。"
    "我知道我本可以阻止的！"
    "去它丫的文学部。"
    "去它丫的学园祭。"
    "我刚刚......失去了我最好的朋友。"
    "失去了跟我一起长大的人。"
    "她永远地离开了。"
    "我没办法让她复活。"
    "这并不是一个让我有机会重来、尝试不同选择的游戏。"
    "我只有这么一次机会，而我却大意了。"
    "现在的我，到死都会怀抱着这份罪恶感。"
    "我的生命中没有任何东西比她更重要......"
    "但是我依然无法给予她所需要的东西。"
    "而且现在......"
    "我永远无法重来了。"
    "永远。"
    "永远。"
    "永远。"
    "永远。"
    "永远......"
    $ in_sayori_kill = False


    return

