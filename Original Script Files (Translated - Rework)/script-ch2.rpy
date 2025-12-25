

label ch2_main:
    scene bg club_day
    with dissolve_scene_half
    play music t2
    "又一天过去了，眨眼间已经到了社团活动的时间。"
    "几天下来，我对文学部已经相当适应了。"
    "走进部室，迎接我的又是那熟悉的一幕。"
    show sayori 2x zorder 2 at t11
    s "嗨，[player]~"
    mc "哟，这不纱世里嘛。"
    mc "你今天看起来心情很不错嘛。"
    s 1q "欸嘿嘿~"
    s "我只是还不太习惯看见你出现在社团里，没别的意思。"
    mc "这样啊......"
    mc "...这么小一件事都能让你这么高兴啊。"
    mc "不过似乎你也总是为这种小事开心呢。"
    s 1d "说起来......"
    s "我有点饿了......"
    s "要和我一起去买零食吗？"
    mc "不了，谢谢。"
    s 4h "诶？？"
    s "这、这一点也不像你！！"
    mc "我有我的理由。"
    mc "要不检查下你的钱包吧，纱世里？"
    s 4l "诶、诶？"
    show sayori at s11
    s "为什么......突然要看啊？"
    mc "没有啥原因，真的。"
    mc "我只是想看看。"
    s 1l "啊、啊......"
    show sayori zorder 2 at t11
    "纱世里紧张地拿出了她的零钱包。"
    "她笨拙地摸索着扣子，将钱包打开。"
    "然后，她把钱包倒过来，将里面的东西都倒在桌面上。"
    "掉出来的只有两枚小硬币。"
    s 5a "啊、啊哈哈......"
    mc "我就知道......"
    mc "纱世里，我早就看穿你了。"
    s 5c "这不公平！"
    s "你怎么知道的？"
    mc "很简单。"
    mc "如果你一开始就有足够的钱，来部室之前你肯定就买好零食了。"
    mc "所以，要么就是你不饿，只是想找个借口出去走走......"
    mc "要么就是，你早就花光了所有的钱，然后试图装健忘骗我借钱给你！"
    mc "不过，还有一点......"
    mc "......你就没有不饿的时候！"
    mc "这么一来，就只剩下最后一种可能了！"
    s 4p "呜哇啊啊~！"
    s "我投降好吧！"
    s "别搞得我那么内疚好吧！"
    mc "你要是觉得内疚的话，那就说明你确实应该感到内疚......"
    show yuri 1c zorder 2 at t33
    y "啊哈哈。"
    "优里突然咯咯地笑了起来。"
    show sayori 4g
    mc "诶？"
    "我都没注意到她在听我们说话。"
    "她把脸埋在书里，就跟往常一样。"
    show yuri 3n at h33
    y "啊、啊！"
    y "我刚刚没有在听——！"
    y 3o "只不过是......书里的东西......"
    show sayori zorder 3 at f32
    s 1h "优——里——......"
    s "快让 [player] 借我点钱......"
    show sayori zorder 2 at t32
    show yuri zorder 3 at f33
    y 3h "这......！"
    y "纱世里，别这样把我牵扯进来啊......"
    y "更何况......"
    y 1k "你应该根据自己的经济能力来买东西......"
    y "而且坦白说，耍这么个小把戏，你的痛苦也算是受到点报应了。"
    show sayori 1b
    mc "......"
    y 3n "啊——！"
    y "我刚刚是不是......"
    y 4c "我、我不是那个意思！！"
    y "我看这本书看得太入迷了......"
    y "唔......"
    show yuri zorder 2 at t33
    show sayori zorder 3 at f32
    s 1r "啊哈哈！"
    s 3x "我真的很挺喜欢你有话直说的样子，优里......"
    s "虽说很少见，但那也是你有趣的一面哦！"
    show sayori zorder 2 at t32
    show yuri zorder 3 at f33
    y 3v "这......"
    y "你怎么会那样想......"
    show yuri zorder 2 at t33
    show sayori zorder 3 at f32
    s 1x "你说的倒也没错啦......"
    s "我做了错事，所以就得接受抱怨。"
    show sayori zorder 2 at t32
    show yuri zorder 3 at f33
    y 3h "是‘报应’啦......"
    show yuri zorder 2 at t33
    show sayori zorder 3 at f32
    s 1l "反正就那个词啦！"
    show sayori zorder 2 at t32
    show yuri zorder 3 at f33
    y "难得你会这么说，纱世里......"
    y 1a "我想，我们每个人心中都有只小恶魔，对吧？"
    show yuri zorder 2 at t33
    show sayori zorder 3 at f32
    s 1q "欸嘿嘿......"
    show sayori zorder 2 at t32
    mc "别听她瞎说。"
    mc "纱世里知道她在做什么。"
    mc "别忘了，她在跟我说之前，就已经告诉你们她会把我带到社团来......"
    show sayori zorder 3 at f32
    s 1h "但、但是......！"
    s "你要不是为了小蛋糕，也不会来嘛......"
    s "所以我只好耍点小诡计，骗夏树去做蛋糕了！"
    show sayori zorder 2 at t32
    mc "拜托，对我有点信心好嘛，纱世里。"
    show sayori zorder 3 at f32
    s 1l "欸嘿嘿......"
    play sound "sfx/slap.ogg"
    show white zorder 4:
        alpha 0.6
        linear 0.25 alpha 0.0
    show sayori 4p zorder 3 at hf32
    "{i}啪！{/i}"
    hide white
    s 4p "噫呀——！"
    "不知道从哪里冒出来的某个东西冷不丁地打到了纱世里脸上，然后滚到了桌子上。"
    s 4j "嗷......"
    s "什么东西——"
    s 4n "诶？？"
    s "是、是曲奇诶！"
    "真的诶，是一块塑料包装的超大曲奇。"
    "纱世里环顾了一下四周。"
    s 4m "这、这就是奇迹吗？"
    s "一定是因为我受到了报复！"
    show sayori zorder 2 at t32
    mc "是‘报应’啦......"
    show sayori 4n
    show yuri zorder 3 at f33
    y 1u "其实你这个词差不多算是用对了......"
    show yuri zorder 2 at t33
    show natsuki 3z zorder 3 at f31
    n "啊哈哈哈！"
    n "这曲奇{i}本来{/i}就是我打算给你的。"
    n 3d "但我接着又听到你把小蛋糕的事情给说漏嘴了。"
    n "不过能看到你那反应，倒也算是扯平了吧。啊哈哈！"
    show natsuki zorder 2 at t31
    show sayori zorder 3 at f32
    s 4m "夏、夏树！"
    s "你人好好哦！"
    s 4s "我超开心的......"
    "纱世里抱住了曲奇。"
    show sayori zorder 2 at t32
    mc "天哪，你赶紧吃就是了......"
    "纱世里一下子就拆开了包装，大口咬了下去。"
    show sayori zorder 3 at f32
    s 4q "尊好次......"
    show sayori zorder 3 at hf32
    s 4o "唔——！"
    "纱世里突然捂住了嘴。"
    s 4p "我咬到舌头了......"
    show sayori zorder 2 at t32
    show natsuki zorder 3 at f31
    n 3a "欸嘿嘿。"
    n "你吃个曲奇还挺一波三折的嘛。"
    "夏树咬了一口自己的曲奇。"
    show natsuki zorder 2 at t31
    show sayori zorder 3 at f32
    s 1c "啊，夏树，你这个看上去也很好吃嘛！"
    s "我能尝尝吗？"
    show sayori zorder 2 at t32
    show natsuki zorder 3 at f31
    n 4e "拜托......"
    n "蹭吃的还带挑三拣四啊！"
    show natsuki zorder 2 at t31
    show sayori zorder 3 at f32
    s 1h "但你的是巧克力味的......"
    show sayori zorder 2 at t32
    show natsuki zorder 3 at f31
    n 4c "是啊，不然你觉得我为啥要给你那块？"
    show natsuki zorder 2 at t31
    show sayori zorder 3 at f32
    s 1g "好吧......"
    s 1q "不过你能把这块分享给我，还是让我很开心。"
    s "诶嘿嘿~"
    show sayori behind natsuki zorder 2 at t21
    "纱世里起身走到夏树身后，伸出双臂搂住了她。"
    n 12c "啊——真是的......"
    n "行啦行啦。"
    "夏树手里还拿着曲奇，便用手肘把纱世里轻轻推开。"
    show sayori 1n at h21
    s "......{i}啊呜。{/i}"
    "纱世里突然弯下身，咬了一口夏树的曲奇。"
    n 1p "{i}喂、喂！！{/i}"
    n "你还真就上嘴抢啊？！"
    s 1q "唔呼呼呼！"
    show sayori at lhide
    hide sayori
    "嘴巴塞得满满的纱世里，快步跑到了安全的地方。"
    show yuri 1c
    "优里和我也笑了起来。"
    show yuri 1a
    show natsuki zorder 3 at f31
    n 1w "天哪！你有时简直跟一小孩差不多诶！"
    n 1h "莫妮卡！你能不能说说纱世里——"
    n 1c "——诶？"
    "夏树看了看四周。"
    "莫妮卡并不在部室。"
    n 4q "呃......"
    n "所以说，莫妮卡去哪了？"
    show natsuki zorder 2 at t31
    show yuri 2f zorder 3 at f33
    y "好问题......"
    y "她有和你们说今天会晚点来之类的吗？"
    show sayori 1b zorder 3 at f32
    show yuri zorder 2 at t33
    s "没有......"
    show sayori zorder 2 at t32
    mc "啊，我也不知道。"
    show yuri zorder 3 at f33
    y 2l "唔......"
    y "那可有点反常。"
    show yuri zorder 2 at t33
    show sayori zorder 3 at f32
    s 1g "希望她没事......"
    show sayori zorder 2 at t32
    show natsuki 3k zorder 3 at f31
    n "她肯定不会有事的。"
    n "她也许只是今天刚好有事要做。"
    n 3t "毕竟她还是蛮受欢迎的......"
    show natsuki zorder 2 at t31
    show sayori 4m zorder 3 at f32
    s "诶？"
    s "你该不会觉得她......"
    s "她交了一个......！"
    show sayori zorder 2 at t32
    show yuri 1a zorder 3 at f33
    y "啊哈哈，那也不奇怪嘛。"
    y "她可能比我们所有人加起来都更有魅力。"
    show yuri zorder 2 at t33
    show sayori 1r zorder 3 at f32
    s "诶嘿嘿，确实是这样......"
    show sayori zorder 2 at t32
    show natsuki 1p zorder 3 at f31
    n "这又是哪跟哪啊喂？！"
    hide natsuki
    hide sayori
    hide yuri
    with wipeleft
    "突然，门猛地打开了。"
    show monika 1g at l41
    m "抱歉抱歉！非常抱歉！"
    mc "啊，你终于到了......"
    m "我真不是故意要迟到的......"
    m "希望你们没有在担心我之类的！"
    show sayori 4n zorder 3 at f42
    s "诶？？"
    s "所以莫妮卡最终在社团和男朋友之间选择了社团！"
    s "你的意志力真的很强诶！"
    show sayori zorder 2 at t42
    show monika zorder 3 at f41
    m 1l "什、什么男朋友......？"
    m "你们到底在说什么啊？"
    "莫妮卡疑惑地看向我。"
    show monika zorder 2 at t41
    mc "啊，就当无事发生吧......"
    mc "话说，你是被什么事情耽误了吗？"
    show monika zorder 3 at f41
    m 1e "啊......"
    m "嗯，我今天最后一节课是自习课。"
    m "说实话，我忘了注意时间......"
    m "啊哈哈......"
    show monika zorder 2 at t41
    show natsuki 2c zorder 3 at f43
    n "那也不合理啊。"
    n "你至少应该有听到下课铃吧。"
    show natsuki zorder 2 at t43
    show monika zorder 3 at f41
    m 1m "那想必是被我练钢琴的声音盖过去了吧......"
    show monika zorder 2 at t41
    show yuri 1e zorder 3 at f44
    y "钢琴......？"
    y "我都不知道你会弹钢琴诶，莫妮卡。"
    show yuri zorder 2 at t44
    show monika zorder 3 at f41
    m 1l "啊，其实也不算会弹......！"
    m "我最近才开始学。"
    m 1m "我一直都蛮想学钢琴的。"
    show monika zorder 2 at t41
    show sayori 4x zorder 3 at f42
    s "很酷诶！"
    s "莫妮卡，弹几首曲子给我们听听吧！"
    show sayori zorder 2 at t42
    show monika zorder 3 at f41
    m "这......"
    "莫妮卡看着我说道。"
    m 1a "大概还是等我弹得稍微好点了，再弹给大家听吧。"
    show monika zorder 2 at t41
    show sayori zorder 3 at f42
    s 4q "好耶~！"
    show sayori zorder 2 at t42
    mc "听起来好厉害。"
    mc "我也很期待哦。"
    show monika zorder 3 at f41
    m 1b "是吗？"
    m "这样的话......"
    m "我不会让你失望的，[player]。"
    show sayori zorder 1 at thide
    show natsuki zorder 1 at thide
    show yuri zorder 1 at thide
    show monika 5 zorder 2 at t11
    hide sayori
    hide natsuki
    hide yuri
    "莫妮卡冲我甜甜地笑着。"
    mc "啊......"
    mc "我不是想给你压力什么的！"
    m 1a "啊哈哈，不用担心。"
    m "我最近练习得蛮多的。"
    m "等我准备好之后，有机会的话我会很乐意分享的。"
    mc "这样啊......"
    mc "那么，就祝你好运吧。"
    m 1j "谢谢~！"
    m 1a "话说，我没有错过什么吧？"
    mc "呃......其实没错过什么。"
    show monika zorder 1 at thide
    hide monika
    "我选择不提纱世里的调皮恶作剧。"
    "不过我敢肯定，夏树最后还是会跟她抱怨的。"
    "看起来大家都已经安定下来了。"
    "纱世里竟然已经吃完了整块曲奇。"
    "优里回到了书本前，而夏树也消失在储藏间里了。"



    $ nextscene = get_exclusive_scene(1)
    call expression nextscene



    return


label ch2_end:
    stop music fadeout 1.0
    scene bg club_day
    show monika 4b zorder 2 at t32
    with wipeleft_scene
    play music t3
    m "好了，各位！"
    m "我们都已经读完彼此的诗了，对吧？"
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
    show yuri 2g zorder 3 at f33
    show natsuki zorder 2 at t31
    y "我也有这种担心呢。"
    y "临时抱佛脚什么的，我真的不擅长......"
    show yuri zorder 2 at t33
    show monika zorder 3 at f32
    m 1b "别想那么多嘛！"
    m "我们就弄得简单点，好吗？"
    m 1a "做一点小装饰，其实也差不多了。"
    m "纱世里已经在做海报了，我也设计了一些能在赏诗会期间分发的诗册。"
    show monika zorder 2 at t32
    show natsuki 3c zorder 3 at f31
    n "好吧，这些都很不错......"
    n "但你还是没说清楚，我们到底要在赏诗会上做什么啊。"
    show natsuki zorder 2 at t31
    show monika zorder 3 at f32
    m 1d "啊，抱歉！我还以为你已经知道了。"
    m 1b "我们要上台表演！"
    show monika zorder 2 at t32
    show natsuki zorder 3 at f31
    n 3h "表演？"
    show natsuki zorder 2 at t31
    show yuri zorder 3 at f33
    y 3n "表......"
    y 3o "呃，莫妮卡......"
    show yuri zorder 2 at t33
    show monika zorder 3 at f32
    m 1k "没错！我们要举办一场诗朗诵表演。"
    m 1b "我们每个人都要选一首诗，在赏诗会上朗诵。"
    m "不过最棒的部分是，其他人也有机会上台进行诗朗诵！"
    m 1a "纱世里会在海报上写明这一点，以便有意者提前做好准备。"
    show yuri zorder 2 at t44
    show monika zorder 2 at t43
    show natsuki zorder 2 at t42
    show sayori 4q at l41
    s "诶嘿嘿~"
    "紗世里一直在给海报上色，她把它拿起来给我们看了看。"
    show natsuki 4w zorder 3 at f42
    n "你是在开玩笑吗，莫妮卡？"
    n "你不会......你不会已经把这些海报贴出去了吧？"
    show natsuki zorder 2 at t42
    show monika zorder 3 at f43
    m 1d "诶？是的，我已经贴了......"
    m "你真的觉得这个主意有那么糟吗......？"
    show monika zorder 2 at t43
    show natsuki 1s zorder 3 at f42
    n "好吧，倒也没有。"
    n "这个主意也不算糟。"
    n 1w "但是我可不想参加这个哦！"
    n 1x "我{i}绝不{/i}可能像你说的那样，在一大群人面前表演的！"
    show natsuki zorder 2 at t42
    show yuri zorder 3 at f44
    y 3r "我...我同意夏树！"
    y 3w "我这辈子......也不会......做那样的事情的......"
    "想到这里，优里害怕地摇了摇头。"
    show yuri zorder 2 at t44
    show sayori 1g zorder 3 at f41
    s "各位......"
    show sayori zorder 2 at t41
    show monika zorder 3 at f43
    m 1g "纱世里，先别说了......"
    m "我明白她们心里在想什么。"
    m "要知道几天前，夏树和优里还从来没有跟别人分享过她们的诗......"
    m "让她们当着一屋子的人大声朗诵自己的诗，确实要求太高了。"
    m 1r "我好像确实忽略了这一点。"
    m "唉，实在对不起。"
    show monika zorder 2 at t43
    show natsuki 5g zorder 3 at f42
    n "......"
    show natsuki zorder 2 at t42
    show monika zorder 3 at f43
    m 1i "......但是！"
    m "我觉得我们还是应该竭尽全力！"
    m 1d "毕竟这个社团的命运只能靠我们自己。"
    m "如果我们成功举办了赏诗会，并且演出效果不错的话......"
    m 3a "那就会激励别人也这么做！"
    m "表演的人越多，我们就能更好地告诉大家，文学到底是什么！"
    show monika zorder 2 at t43
    show sayori 1r zorder 3 at f41
    s "是的!"
    s 1x "文学就是表达出你们的感情......"
    s "挖掘自己的内心......"
    s "发现新的视界......"
    s "然后玩得开心就行了！"
    show sayori zorder 2 at t41
    show monika zorder 3 at f43
    m 4b "没错！"
    m "正因如此，我们今天才会相聚在社团里。"
    m 4e "你们难道不想和他人分享吗？"
    m "难道就不想鼓舞其他人，让他们体会到当初引领各位来到这里的那些感受吗？"
    m 1e "我知道你们想的。"
    m "我知道我们都很想。"
    m 1b "而如果我们只需要花上两分钟，站在房间前朗诵一首诗的话......"
    m "......那我相信大家一定可以做到的！"
    show monika 1a zorder 2 at t43
    show natsuki 5s zorder 3 at f42
    n "......"
    show natsuki zorder 2 at t42
    show yuri 4b zorder 3 at f44
    y "......"
    show yuri zorder 2 at t44
    show sayori 1g
    "夏树和优里沉默不语。"
    "纱世里看起来则有些担心。"
    "那想必我是别无选择了......"
    mc "我同意......"
    mc "我不觉得这样的要求很过分。"
    mc "纱世里和莫妮卡一直努力地想吸引新成员。"
    mc "我觉得我们至少该帮她们分担一点。"
    show natsuki zorder 3 at f42
    n 5h "好吧......或许你说的没错，但是......"
    n "......"
    "夏树似乎也没什么可反驳的了。"
    n "唔......"
    n 1q "......那，行吧！"
    n "看来我也只能忍一下了。"
    show natsuki zorder 2 at t42
    show sayori zorder 3 at f41
    s 4r "太好了~！"
    show sayori 4a zorder 2 at t41
    show monika zorder 3 at f43
    m 1e "呼......"
    m "谢谢你，夏树。"
    m "那你呢，优里......？"
    show monika zorder 2 at t43
    show yuri zorder 3 at f44
    y "......"
    "优里郁闷地看着周围其他人满怀期待的脸。"
    y "唉......"
    y "那、那我也别无选择了啊......"
    show yuri zorder 2 at t44
    show sayori zorder 3 at f41
    s 4r "啊哈哈！那就是全员参加咯！"
    s "你最好了，优里~"
    show sayori 4a zorder 2 at t41
    show yuri zorder 3 at f44
    y "这个社团迟早会要了我的命啊......"
    show yuri zorder 2 at t44
    show monika zorder 3 at f43
    m 1l "哦，天哪......"
    m 1n "没事的，优里。"
    m "不过话说回来......"
    m 1b "我们还是开始准备赏诗会吧！"
    m "我希望你们每个人都选一首自己的诗。"
    m "我们会在彼此面前进行朗诵练习。"
    show monika 1a zorder 2 at t43
    show natsuki zorder 3 at f42
    n 1p "不、不、不行！！"
    show natsuki zorder 2 at t42
    show yuri 3n zorder 3 at f44
    y "莫妮卡......！"
    y "这太突然了吧......！"
    show yuri zorder 2 at t44
    show monika zorder 3 at f43
    m 2a "呃，要是连在社团成员面前朗诵都不敢，又怎么能指望在陌生人面前朗诵呢？"
    show monika zorder 2 at t43
    show yuri 4c zorder 3 at f44
    show natsuki 1o
    y "哦不......"
    show yuri zorder 2 at t44
    show monika zorder 3 at f43
    m 2a "别担心。"
    m "我会打头阵，让大家更自在一些。"
    show monika zorder 2 at t43
    show sayori 1r zorder 3 at f41
    s "那我能当下一位吗？？"
    show sayori zorder 2 at t41
    show monika zorder 3 at f43
    m "啊哈哈，当然可以。"
    m 2d "这样的话，我看看......"
    "莫妮卡快速翻动笔记本，寻找着她心里想着的那一首诗。"
    "接着她便站在了讲台后面。"
    show monika zorder 2 at t11
    show sayori zorder 1 at thide
    show natsuki zorder 1 at thide
    show yuri zorder 1 at thide
    hide sayori
    hide natsuki
    hide yuri
    m 1a "这首诗题为《飞翔的方式》。"
    m 1r "咳咳......"
    show monika 1a
    "莫妮卡开始朗诵她的诗。"
    "她那清晰又自信的声音在整间房内回荡。"
    "不仅如此，她那抑扬顿挫的语调也很质朴清新。"
    "她十分清楚如何将感情投入到自己朗诵的每一行诗句中，给文字带来生气。"
    "她是之前就朗诵过诗篇，还是说她天生就如此在行？"
    "我朝周围看了看。"
    "所有人的视线都放在莫妮卡身上。"
    "纱世里一脸惊讶。"
    "优里脸上带着我不能理解的紧张表情。"
    show monika 1j
    "终于，莫妮卡完成了朗诵。"
    "我们四个都鼓起了掌。"
    "莫妮卡深吸了一口气，微笑了起来。"
    show monika 1a
    show sayori 4m zorder 3 at f33
    s "莫妮卡，你......你的表现好棒啊！"
    show sayori zorder 2 at t33
    show monika zorder 3 at f32
    m 1j "啊哈哈，非常感谢。"
    m 1a "希望我树立了一个好的榜样。"
    m "准备好接棒上场了吗，纱世里？"
    show monika zorder 2 at t32
    show yuri 2r at l31
    y "下......下一个让我来！！"
    show sayori at h33
    s 1n "呜哇！优里突然火力全开啦！"
    "优里手中攥着一张纸，站了起来。"
    "她低着头，快速走向讲台。"
    show monika zorder 1 at thide
    show sayori zorder 1 at thide
    show yuri zorder 2 at t11
    hide monika
    hide sayori
    y 2v "这首诗的题目是——！"
    "优里紧张地看着我们。"
    s "你可以的，优里......"
    y "题......题目叫......《绯红眼眸之残影》。"
    "优里开始朗诵诗，声音有些颤抖。"
    "明明刚刚她还特别抗拒的。"
    "为什么她突然之间变得这么努力了？"
    show yuri 2l
    "读过开头的几行过后，优里的声音发生了变化。"
    "简直就和她沉浸到书本里的时候一样。"
    "她的语调不再颤抖，每个音节铿锵有力，迸发出勇猛而自信的气势。"
    "这首诗通篇都是结构上的迂回曲折，而她的咬字与节奏将其表现得淋漓尽致。"
    "优里一直封存于脑海深处的那团飞旋跳动的热情火焰，如今难得可以一睹真容......！"
    show yuri 2t
    "她的朗诵戛然而止。"
    "所有人都呆住了。"
    "优里猛然回到了现实中，环顾四周，似乎自己也困惑不已。"
    y 3o "我......"
    "......看来需要我来救场了。"
    "我带头鼓起了掌。"
    "大家都随后鼓掌起来，给了优里应得的认可。"
    "我们刚刚并不是不想为她鼓掌。"
    "而是因为她的表现出乎了所有人的意料，结果大家都没回过神，忘记了鼓掌。"
    "伴随着我们的掌声，优里把诗紧贴在胸口，跑回了自己的座位。"
    show yuri at lhide
    hide yuri
    show monika 1a zorder 2 at t11
    m "优里，你表现得非常棒。"
    m "谢谢你的分享。"
    y "......"
    "似乎优里已经筋疲力尽了......"
    show sayori 1q zorder 2 at t31
    s "好啦~"
    s "那下一位就让我上了！"
    "纱世里从座位上跳了起来，兴高采烈地走向讲台。"
    show sayori zorder 2 at t11
    show monika zorder 1 at thide
    hide monika
    s 1x "这首诗叫做......《我的大草地》。"
    s "啊......"
    s 1s "......啊哈哈！"
    s 4s "不好意思，我刚刚傻笑了......"
    s 4q "诶嘿嘿......"
    mc "纱世里......"
    s 1l "这比我想象中要难好多啊！"
    s "为什么你们做起来都那么轻松啊？"
    show monika 3a zorder 2 at t31
    show sayori 1b
    m "啊......"
    m "尽量别把它当成是在对着别人朗诵就行。"
    m "想象一下你是在对着自己朗诵，就像对着镜子，或者在脑中默念一样。"
    m "毕竟这是你自己写的诗，所以这样做的效果最好。"
    show sayori 1i
    s "明白了，明白了......"
    s "好的，那么......"
    show monika zorder 1 at thide
    hide monika
    show sayori 1c
    "纱世里开始了朗诵。"
    "不知怎地，这首诗和她温柔的声线仿佛是天作之合。"
    "不过这首诗并不像纱世里本人那样，欢快得无忧无虑。"
    "它带着些安宁，又有着苦乐参半的感觉。"
    "如果我是在纸上读到这首诗，那我大概不会想这么多..."
    "但是听到纱世里用她的声音读出来时，这首诗就有了全新的含义。"
    "可能纱世里说她喜欢我的诗时，大概也是这个意思吧。"
    "就有一种，我本以为我早已相当了解她，但现在自己对她的理解又更深一层的感觉。"
    "纱世里读完了，我们鼓起了掌。"
    s 3q "我做到了~！"
    mc "做得不错，纱世里！"
    s "欸嘿嘿，连 [player] 都喜欢哦。"
    s "我想这一定是个好兆头吧~"
    mc "你这是在说什么呀......？"
    show monika 2b zorder 3 at f31
    m "效果非常好啊，纱世里。"
    m "诗的基调与你相当契合。"
    m "只不过，如果你的其它诗也用这种风格来朗诵的话，效果也许会稍逊一筹吧......"
    show monika zorder 2 at t31
    show sayori zorder 3 at f32
    s 1g "诶？我不是很明白......"
    show sayori zorder 2 at t32
    show monika zorder 3 at f31
    m 1a "换句话说，我读过你其他的诗，它们不太适合这种温柔的表达方式。"
    m "那些诗可能需要以更有力道的方式来呈现，而力量的多少则取决于你所读的内容......"
    show monika zorder 2 at t31
    show sayori zorder 3 at f32
    s 1x "哦，我懂你的意思了！"
    s "就是......嗯，我已经有在练习这些了......"
    s 5 "只不过站在大家面前有些难为情而已......"
    s "欸嘿嘿......"
    show sayori zorder 2 at t32
    show monika zorder 3 at f31
    m 4a "那下次我可要让你选一首更有挑战性的诗哦。"
    m "你也知道离学园祭也只剩下没几天了吧？"
    show monika zorder 2 at t31
    show sayori zorder 3 at f32
    s 1q "好......吧。"
    show sayori zorder 2 at t32
    show monika zorder 3 at f31
    m 1a "那么，下一个谁来......？"
    m "夏树可以吗？"
    show natsuki 5s zorder 3 at f33
    show monika zorder 2 at t31
    n "哼。"
    n "别把我排在 [player] 之前上场。"
    n "何况我也没法跟你们相比啊......"
    n "那么，倒不如先让 [player] 降低一下大家的标准，然后我再上场，免得我成降低预期的了。"
    show natsuki zorder 2 at t33
    show sayori zorder 3 at f32
    s 1g "夏树......"
    show sayori zorder 2 at t32
    mc "没事，没多大事。"
    mc "长痛不如短痛，我也想赶紧搞定。"
    mc "但是在读的内容上，我好像没啥选择了......"
    mc "那我就读我昨天写的诗吧。"
    "我站起来，走到了讲台前。"
    show natsuki 2c zorder 2 at t44
    show sayori 1a zorder 2 at t43
    show monika 1a zorder 2 at t42
    show yuri 1e zorder 2 at t41
    "大家都将目光集中在我一个人身上，让我感到格外尴尬。"
    "我朗诵了我的诗。"
    "由于我对自己的写作水平不是特别有信心，所以我很难有感情地朗诵手里的诗作。"
    "尽管如此，在我读完的那一刻，我还是收获了掌声。"
    mc "抱歉，我表现得没大家那么好......"
    show monika zorder 3 at f42
    m 1a "别太担心。"
    m "我觉得你的能力倒是问题不大，你对自己的写作水平缺乏信心才是最大的问题。"
    m "不过随着时间推移，你会越来越有信心的。"
    show monika zorder 2 at t42
    mc "嗯......也许吧。"
    show monika zorder 3 at f42
    m 1j "好了！"
    m 1a "那么接下来，夏树，只剩你了。"
    show monika zorder 2 at t42
    show natsuki zorder 3 at f44
    n 2g "好吧，好吧。"
    n "我这就上场。"
    "夏树不情愿地离开座位，走向讲台。"
    show sayori zorder 1 at thide
    show monika zorder 1 at thide
    show yuri zorder 1 at thide
    show natsuki zorder 2 at t11
    hide sayori
    hide monika
    hide yuri
    n 2c "这首诗的题目是......"
    n 2q "它叫做......"
    n 1x "不、不是，你们都盯着我干嘛？！"
    m "因为现在是你在读诗啊..."
    n 2x "哼......"
    n 2h "算了......这首诗题为《跳跃》。"
    "夏树深吸了一口气。"
    show natsuki 2c
    "开始朗诵后，她的别扭态度稍微消散了一些。"
    "尽管她还是有些没精打采，但她的诗却自有节奏和韵律。"
    "这就是夏树的标志性风格，在大声朗读情况下，表现出人意料地好。"
    "辞藻如若在空中跃动，仿佛给诗赋予了生命。"
    show natsuki 2s
    "夏树读完了，大家都鼓起掌来。"
    "她气鼓鼓地回到了座位上。"
    show monika 2a zorder 3 at f31
    m "还不错啊！"
    show monika zorder 2 at t31
    show natsuki 5w zorder 3 at f32
    n "你嘴上倒是说得轻松......"
    n "你可别强迫我再来一次了。"
    show natsuki zorder 2 at t32
    show monika 1d zorder 3 at f31
    m "啊，好啦......"
    m "这下你至少做好了心理准备，可以在别人面前进行诗朗诵了吧？"
    show monika zorder 2 at t31
    show natsuki 2c zorder 3 at f32
    n "就是说，在别人面前诗朗诵可容易得多了！!"
    n "对着别人，我随便摆出什么样的脸色都可以。"
    n 2q "但如果是在朋友面前......"
    n "就真的很......难为情。"
    show natsuki zorder 2 at t32
    show sayori 1b zorder 3 at f33
    s "还真让人意外啊，夏树......"
    s "我觉得对我来说恰恰相反。"
    show sayori zorder 2 at t33
    show natsuki zorder 3 at f32
    n "总之，就是这样了嘛，所以说......"
    show natsuki zorder 2 at t32
    show monika zorder 3 at f31
    m 1a "呃，我想既然如此......"
    m "你就不用太担心自己在学园祭时的表现了。"
    m 2b "那么，感谢大家的参与。"
    m "虽然可能会有点难，不过希望大家都对赏诗会是什么样子有了大致的了解。"
    m 4b "请务必在学园祭开始前选好一首诗，并且多加练习，好吗？"
    m "我会去做诗册，所以还请事先告诉我你们要朗诵那首诗。"
    show monika zorder 2 at t31
    mc "坏了......"
    mc "我大概还是另找一些诗来朗诵得了。"
    show monika zorder 3 at f31
    m 1j "那也可以的！"
    m 1a "不是自己的诗也没关系。"
    m "你能为社团付出这么多努力，已经很让我惊喜了。"
    m 5 "我真的非常高兴。"
    show monika zorder 2 at t31
    mc "啊......好吧，小意思啦......"
    play music t8 fadeout 1.0
    show monika zorder 2 at t11
    show sayori zorder 1 at thide
    show natsuki zorder 1 at thide
    hide sayori
    hide natsuki
    m 4b "好了，各位！"
    m "那么今天就到这里吧。"
    m "我知道学园祭迫在眉睫，但是明天大家还是试着写首诗吧。"
    m "到目前为止，这项活动的效果都非常棒，所以我想把它继续下去。"
    m "而关于学园祭，我们会在明天完成规划，然后用周末的时间来进行准备。"
    m "星期一就是咱们的大日子啦！"
    show sayori 4r zorder 2 at t31
    s "我都等不及啦~！"
    show yuri 4b zorder 2 at t33
    y "我做得到的......我做得到的......"
    mc "好吧——"
    hide sayori
    hide monika
    hide yuri
    with wipeleft
    "我站了起来。"
    "虽然我的热忱比不上像纱世里和莫妮卡，但我也会尽己所能。"
    "如果是为了社团......"
    "以及为了给莫妮卡留下好印象......"
    "那么我就必须全力以赴。"
    show sayori 1a zorder 2 at t32
    mc "准备好回家了吗，纱世里？"
    show sayori at h32
    s 1x "嗯！"
    show natsuki 2d zorder 3 at f33
    n "看看你们俩，总是这样结伴回家。"
    show monika 5 zorder 3 at f31
    show natsuki zorder 2 at t33
    m "还怪可爱的，不是吗？"
    show monika zorder 2 at t31
    show sayori zorder 3 at f32
    s 1q "欸嘿嘿~"
    show sayori zorder 2 at t32
    mc "天哪，各位......"
    mc "别那么大惊小怪嘛。"
    show natsuki zorder 2 at t44
    show sayori zorder 2 at t43
    show monika zorder 2 at t42
    show yuri 1u zorder 3 at f41
    y "不过你们好像乐在其中嘛......"
    show yuri zorder 2 at t41
    mc "这个嘛......"
    mc "啊......"
    "这要我怎么回应啊？"
    show sayori zorder 3 at f43
    s 1d "没关系的，[player]，不说出来也不要紧。"
    show sayori zorder 2 at t43
    mc "......不管了。我们走吧。"
    scene bg residential_day
    with wipeleft_scene
    $ ch2_winner = poemwinner[1].capitalize()
    if ch2_winner == "Sayori" or ch2_winner == "Yuri":
        $ ch2_winner = "优里"
    elif ch2_winner == "Natsuki":
        $ ch2_winner = "夏树"

    "我又一次和纱世里结伴走回家。"
    "虽然只过了短短几天，但很多事情都已经改变了。"
    "不过今天回家路上，纱世里比往常要更安静一些。"
    mc "嘿，纱世里......"
    show sayori 1k at t11
    s "......"
    s 1n "......对不起！我走神了！"
    mc "啊，怪不得......"
    s 1d "唔......"
    s "我刚刚......在想之前的事情。"
    s "我很喜欢像这样一起......"
    s 1y "我、我是说......"
    "纱世里笨拙地组织着语言。"
    s 1a "就是......假设有一天，[ch2_winner]提出要跟你一起回家......"
    mc "哈？！"
    s "你会怎么做？"
    mc "这是个什么问题......？"
    mc "你可有点把我难住了......"
    s 1y "欸嘿嘿......"
    menu:
        "这个嘛......"
        "我会和[ch2_winner]一起回家。":
            if poemwinner[1] == "natsuki":
                call ch2_end_natsuki
            else:
                call ch2_end_yuri
        "我仍然会和纱世里一起回家。":
            call ch2_end_sayori

    "但话又说回来，距离学园祭只剩下几天了......"
    "谁知道到时候会发生什么呢？"
    return
label ch2_end_sayori:
    mc "纱世里......"
    mc "你真的觉得我会抛下你而选择[ch2_winner]吗？"
    s 1e "诶？！"
    s "但、但是......"
    if poemwinner[1] == "natsuki":
        s "况且她那么可爱，还那么有趣......"
    else:
        s "况且她长得又漂亮，脑袋也聪明......"
    mc "唉哟......"
    mc "反正我天天都能在部室见到她。"
    mc "而你跟我一起回家的时候，看上去总是那么的开心......"
    mc "我怎么可能毁了你的好心情呢。"
    s 1y "你真傻，[player]......"
    s "有时候你实在太为我着想了。"
    s "如果[ch2_winner]想和你结伴回家的话，那也是无可厚非的，所以......"
    mc "纱世里，我已经下定决心了。"
    mc "我有时候还真搞不懂你......"
    s "抱歉......"
    mc "再说了，假设一件永远都不会发生的事情，又有什么意义呢？"
    s 1k "唔......"
    show sayori at thide
    hide sayori
    "对话逐渐停了下来。"
    "纱世里居然这么在乎这件事，我感觉有点奇怪......"
    "但我想尊重她，也想让她开心。"
    return

label ch2_end_natsuki:
    mc "和夏树一起走回家，唔......"
    "为什么这个想法会让我心跳不已啊......？"
    mc "我是说......"
    mc "如果我拒绝她的话，我有点怕她对我做些什么......"
    s 1x "不是因为她可爱又有趣吗？"
    jump ch2_end_shared

label ch2_end_yuri:
    mc "和优里一起走回家，唔......"
    "为什么这个想法会让我心跳不已啊......？"
    mc "我是说......"
    mc "看到她在社交方面这么努力，如果拒绝她的话，我会非常内疚，所以......"
    s 1x "不是因为她漂亮还聪明吗？"
    jump ch2_end_shared

label ch2_end_shared:
    mc "我可完全没这个意思！"
    s 4s "啊哈哈！你承认了！"
    mc "拜托......"
    mc "假设一件永远都不会发生的事情，根本就没有意义啊。"
    s 1d "好吧，也许是吧......"
    s "但是我就是喜欢想一想。"
    s 1y "很快你就不再需要我了，对吧？"
    mc "需要你......是什么意思？"
    mc "纱世里......"
    mc "我实在搞不懂你现在都在琢磨些什么。"
    s "抱歉......"
    mc "每个人都是不同的......"
    mc "社团里没有任何一个人可以替代你。"
    s 1k "唔......"
    s "既然你都这么说了......"
    show sayori at thide
    hide sayori
    "对话逐渐停了下来，只留我一人倍感尴尬。"
    "可是她用这样一个奇怪的问题来套我的话，某种程度上也算是她的错......"
    "我不能对她撒谎。"
    "但我不想从她身边夺走能让她开心的东西。"
    "这就是为什么我会说，假设是没有意义的。"
    return

