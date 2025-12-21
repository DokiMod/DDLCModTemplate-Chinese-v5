label ch0_main:
    stop music fadeout 2.0
    scene bg residential_day
    with dissolve_scene_full
    play music t2

    python:
        try: renpy.file("../characters/monika.chr")
        except: renpy.jump("ch0_kill")

    $ restore_characters()
    s "喂！！等等我！！！"
    "我看见一个吵吵闹闹的女孩从远处朝我跑来，一边猛挥着手，仿佛完全意识不到这样会引来全世界的注意。"
    "她叫纱世里，我的邻居，也是我的儿时玩伴。"
    "怎么说，换做现在，我大概不会想跟她交朋友。但是，因为和她相识太久，我们就自然而然地合拍了。"
    "我们以前经常这样结伴上学，但上了高中以后，她睡过头的频率就越来越高，我也就有点懒得等她了。"
    "每当她像这样狂追不舍的时候，我还真的有点想一走了之。"
    "然而我也别无选择，只是叹了口气，在路口等着，好让纱世里赶上我。"
    $ s_name = "纱世里"
    show sayori 4p zorder 2 at t11
    s 4p "哈啊......哈啊......"
    s "我怎么又睡过头了！"
    s "但是！这次我追上你了哦！"
    mc "也许如此，但这只是因为我决定停下来等你吧。"
    show sayori at s11
    s 5c "欸——？你这话说得好像是想抛下我然后自己走呢！"
    s "[player]，你好过分哦！"
    mc "毕竟我可不想让路人在看到你这番奇怪行为后，把我和你一起当成笨蛋情侣之类的。"
    show sayori zorder 2 at t11
    s 1a "好吧，好吧。"
    s "但你最后也确实等了我嘛。"
    s "想必，即便心里想使坏，你本质上也还是个温柔的人嘛~"
    mc "随你吧，纱世里，你高兴就好......"
    s 1q "欸嘿嘿~"
    show sayori zorder 1 at thide
    hide sayori
    "我们穿过马路，继续向学校走去。"
    "接近学校，路上熙熙攘攘的学生也愈发挤满了街道。"
    show sayori 3a zorder 2 at t11
    s "话说回来，[player]......"
    s "你决定好加入什么社团了吗？"
    mc "社团？"
    mc "我早就跟你说过了，我对社团活动没兴趣。"
    mc "学校有哪些社团，我也压根没找过。"
    show sayori at s11
    s 4h "欸？你骗人的吧？！"
    s "你跟我说过今年你要参加社团的！"
    mc "有吗......？"
    "也许我真有可能说过，不过大概是为了应付她不断跳跃的话题，然后就随口附和了。"
    "纱世里有点担心过头了，我倒是挺满足的。平平淡淡的生活，闲暇时间就沉浸在动画和游戏里。"
    s 4j "嗯哼？但是！"
    s "我刚刚还在说呢，我很担心你上大学前还搞不清楚怎么和人打交道，而且你没有什么特长。"
    s "我真的很在乎你过得开不开心啊！"
    s "我知道你现在这么过日子还挺开心的，但一想到过几年你就会变成一个完全融入不了社会的废宅，我都要害怕死了！"
    s 4g "这回你能不能相信我一下？"
    s "真别让我一直担心你啦......"
    mc "好吧，真是拿你没辙......"
    mc "我会去一些社团转转，这样你大概会开心吧。"
    mc "当然，我可不保证我一定会加入什么社团。"
    s 1h "那你至少答应我去浅浅地试一下吧？"
    mc "好吧，这我可以跟你保证。"
    show sayori zorder 2 at t11
    s 4r "好耶~！"
    "我怎么就任由自己让这么一个无忧无虑的女孩给说教了呢？"
    "不仅如此，更吓人的是，在她面前我却一点也强硬不起来，只能乖乖顺着她的意思。"
    "我猜是看到她这么担心后，最起码想让她轻松一点吧 —— 毕竟她肯定是过度紧张了。"

    scene bg class_day
    with wipeleft_scene

    "在学校的日子和往常一样平淡，不知不觉就结束了。"
    "整理完书包后，我茫然地盯着墙，完全没有半点动力。"
    mc "啊，社团..."
    "纱世里希望我能去看看学校里的社团。"
    "我想除了动漫部外，我大概是别无选择了......"

    s "哈——喽——？"
    show sayori 1b zorder 2 at t11
    mc "纱世里......？"
    "纱世里肯定是趁我发呆时悄悄溜进教室的。"
    "四处张望了一下，我才意识到教室里只剩下我俩了。"
    s 1a "本来以为能在教室外面等到你，结果看你一直坐在这里发呆，我就进来了。"
    s "讲真，你有时比我还过分欸......我已经记下了哦！"
    mc "你自己的社团活动都快迟到了，你也没必要等我啊。"
    s 1y "嗯......这个嘛，我觉得可能需要有人推你一把，所以我就......"
    mc "就想什么？"
    s 1a "就是，你就可以加入我的社团了！"
    mc "纱世里......"
    s 4r "嗯哼？？"
    mc "...加入你的社团，那是不可能的。"
    show sayori at s11
    s 5d "欸欸欸？！为什么啊！"
    "纱世里是文学部的副部长。"
    "讲真，我压根没觉得她会对文学有任何兴趣。"
    "其实我敢说，她十有八九只是觉得帮忙成立新社团会很好玩。"
    "由于她是社团成立后第一个加入的成员，她自然而然地接过了“副社长”的职位。"
    "话虽如此，我对文学的兴趣绝对比她还差许多。"
    mc "你没听错。我已经决定去动漫部了。"
    show sayori zorder 2 at t11
    s 1g "拜托！来我这嘛！"
    mc "不是，你为什么要这么在意啊？"
    s 5b "这个嘛......"
    s "因为我昨天和她们说，今天一定能带来一个新成员来......"
    s "然后夏树连纸杯蛋糕都做好了诶......"
    s "欸嘿嘿......"
    mc "不要随便做无法兑现的许诺啊喂！"
    "我都说不清楚她到底是真的脑袋一片空白，还是说她已经狡猾到早有预谋。"
    "我长叹了一口气。"
    mc "好吧...看在小蛋糕的份上，我去参观一下，这样可以了吧？"
    show sayori at h11
    s 4r "好耶！跟我来~！"

    stop music fadeout 2.0

    scene bg corridor
    with wipeleft_scene

    "就这样，今天，我为了区区一个纸杯蛋糕而出卖了自己的灵魂。"
    "我垂头丧气地跟着纱世里穿过校园，走上楼梯，登上了我很少涉足的楼层——这里通常只供高三学生上课和社团活动使用。"
    "元气满满的纱世里，一口气拉开了教室的门。"

    scene bg club_day
    with wipeleft
    play music t3
    show sayori 4 at l41
    s "各位！我把新成员带过来了~！"
    mc "我不是说过不要叫我‘新成——’"
    show sayori at lhide
    hide sayori
    "欸？我扫视了一遍教室。"
    show yuri 1a zorder 2 at t11
    y "欢迎来到文学部。很高兴见到你。"
    y "纱世里经常跟我说你的好话。"
    show yuri zorder 2 at t22
    show natsuki 4c zorder 2 at t21
    n "真的假的？你带了个男生过来？"
    n "太毁气氛了吧。"
    show yuri zorder 2 at t33
    show natsuki zorder 2 at t32
    show monika 1k zorder 2 at t31
    m "啊，是 [player] 啊! 你怎么也来了！"
    m "欢迎来到文学部！"
    show monika 1a
    mc "......"
    "看着眼前这幅景象，我根本说不出话来。"
    "这个社团里......"
    "{i}...全都是超级可爱的女孩子啊啊啊！！{/i}"

    show monika zorder 1 at thide
    show yuri zorder 1 at thide
    show natsuki zorder 3 at f32
    hide monika
    hide yuri

    n 2c "你到底在看什么啊？"
    n "有话直说吧。"
    mc "抱...抱歉......"
    show natsuki zorder 2 at t32
    show yuri 2l zorder 3 at f33
    y "夏树......"
    $ n_name = '夏树'
    show yuri zorder 2 at t33
    show natsuki zorder 3 at f32
    n 5s "哼。"
    show natsuki zorder 2 at t32

    "我并不认识这个看起来态度很嚣张的女生。很明显，这位应该就是夏树。"
    "她身材娇小，看上去像是一年级的学妹。"
    "根据纱世里说的话，今天的小蛋糕也就是她做的。"

    show sayori 2q zorder 3 at f31
    s "她闹脾气的时候，你当没看见就行啦~"
    "纱世里悄悄在我耳旁说道，接着又转向其他女孩子。"
    s 1x "总之！这位元气满满的孩子就是夏树了。"
    s "然后这位是优里，全社团最聪明的人！"
    $ y_name = '优里'
    show sayori zorder 2 at t31
    show yuri zorder 3 at f33
    y 4b "别、别这么说..."
    "优里看起来更加成熟，却有点害羞，似乎不太跟得上纱世里和夏树这种人的节奏。"
    show yuri zorder 2 at t33
    mc "啊......那个，很高兴认识你们两位。"
    show yuri zorder 1 at thide
    show natsuki zorder 1 at thide
    hide yuri
    hide natsuki
    show sayori zorder 3 at f31
    s 1a "哦对了，你好像已经认识莫妮卡了，对吧？"
    $ m_name = '莫妮卡'
    show sayori zorder 2 at t31
    show monika 2a zorder 3 at f32
    m "没错。"
    m "[player]，很高兴又和你见面啦。"
    show monika 5a at hop
    "莫妮卡冲我甜甜地笑着。"
    "我们的确互相认识——好吧，虽然我们基本没怎么聊过天。我跟她在去年还是同班同学呢。"
    "莫妮卡可以说是班级里最受欢迎的女生——聪明，漂亮，又擅长运动。"
    "可以说，和我是不同世界的人。"
    "所以，看到她这么真诚地朝我微笑，我有点......"
    mc "我、我也很高兴见到你，莫妮卡。"
    show monika zorder 1 at thide
    hide monika
    show sayori zorder 3 at f31
    s 4x "快坐下吧，[player]！这边给你留了座位，你可以坐在我或者莫妮卡旁边哦。"
    s "我去拿蛋糕咯~"
    show sayori zorder 2 at t31
    show natsuki 1e zorder 3 at f32
    n "慢着！我做的蛋糕，我来拿！"
    show natsuki zorder 2 at t32
    show sayori zorder 3 at f31
    s 5a "不好意思，我有点兴奋过头了~"
    show sayori zorder 2 at t31
    show yuri 1a zorder 3 at f33
    y "那我去泡壶茶，怎么样？"
    hide sayori
    hide natsuki
    hide yuri
    with wipeleft
    "女孩们把几张课桌拼成了一张大桌子。"
    "正如纱世里所说，桌面被加宽了，所以莫妮卡和她旁边都留了一个空位。"
    "与此同时，夏树和优里走到了房间的角落，夏树端出来一个盖好的托盘，而优里打开了储藏间。"
    "我还是觉得有些尴尬，于是就坐在了纱世里的旁边。"
    "夏树端着托盘，趾高气扬地走了回来。"
    show natsuki 2z zorder 2 at t32
    n "好——咯，准备好了吗？"
    n "...锵锵！"
    show sayori 4m zorder 2 at t31
    show monika 2d zorder 2 at t33
    s "哇哦——！"
    "夏树掀开了盖在托盘上的锡箔纸，托盘上放着十二个小猫形状的雪白松软的小蛋糕。"
    "她用糖霜画出了小猫的胡须，还用小片的巧克力做了耳朵。"
    show sayori zorder 3 at f31
    s 4r "好可爱呀~！"
    show sayori zorder 2 at t31
    show monika zorder 3 at f33
    m 2b "夏树，我都不知道你的烘焙技术居然这么厉害！"
    show monika zorder 2 at t33
    show natsuki zorder 3 at f32
    n 2d "嗯哼哼，没想到吧。"
    n "赶紧尝一下吧！"
    "纱世里马上拿起了一块，然后是莫妮卡，接着是我。"
    show natsuki zorder 2 at t32
    show sayori zorder 3 at f31
    s 4q "超好吃！"
    "纱世里脸上沾满了糖霜，满嘴都是蛋糕，边吃边称赞着。"
    "我把蛋糕放在手里转了一圈，想找一个合适的角度下口。"
    show sayori zorder 1 at thide
    show monika zorder 1 at thide
    hide sayori
    hide monika
    show natsuki 1c zorder 2 at t32
    "夏树默不作声。"
    "我不禁注意到了她偷偷瞄向我的视线。"
    "她是在等我咬下去么？"
    "我终于咬下了一口。"
    "糖霜甜度正好，风味十足——这真的是她自己做的吗？"
    mc "真的很豪赤欸。"
    mc "谢谢你，夏树。"
    n 5h "为、为什么要谢我？我又不是......！"
    "{i}（这句话好像有点耳熟啊......）{/i}"
    show natsuki at s32
    n 5s "...又不是为了你才做的。"
    mc "诶？我觉得其实就是吧。纱世里不是说——"
    show natsuki zorder 2 at t32
    n 12c "那，也许是吧！"
    n "但，反正不是为了...就、总之就...不是为 {i}你{/i} 而做的！笨蛋......"
    mc "好吧，真是拿你没辙..."
    show natsuki zorder 1 at thide
    hide natsuki
    "我放弃理解夏树的古怪逻辑，只能草草结束了对话。"
    "优里端着一套茶具，回到了桌旁。"
    "她小心翼翼地在每个人面前摆好一个茶杯，然后将茶壶放在托盘旁边。"
    show yuri 1a zorder 2 at t21
    mc "你居然在部室里放了一整套茶具？"
    y "别担心，老师同意过了。"
    y "何况，热茶配好书，不也很美妙吗？"
    mc "啊...想必——也对......"
    show monika 4a zorder 2 at t22
    m "欸嘿嘿，别被吓到了，优里只是想给你留个好印象。"
    show yuri at h21
    y 3n "诶？！不、不是这样的......"
    "优里难堪地把脸别了过去。"
    y 4b "我的意思是，那个......"
    mc "我相信你。"
    mc "嗯，阅读和品茶或许不是我的消遣方式，但我起码还蛮喜欢喝茶。"
    y 2u "那就好......"
    "优里宽慰地浅浅一笑。"
    "莫妮卡挑了挑眉，也微笑地看着我。"
    show yuri zorder 1 at thide
    hide yuri
    show monika zorder 2 at t11
    m 1 "所以，你为什么会想来文学部呢？"
    mc "呃......"
    "我最怕的就是这个问题啊。"
    "直觉告诉我，千万不能告诉莫妮卡，我其实是被纱世里拖过来的。"
    mc "那个，我还没有加入过哪个社团，而且纱世里在这里好像也蛮开心的，所以我就......"
    m 1j "没问题！不用不好意思！"
    m 1b "我们会给你家一般的感觉，好吗？"
    m "作为文学部的部长，我的职责就是让社团充满乐趣和活力，创造更有趣的社团时光！"
    show monika 1a
    mc "莫妮卡，讲真，我其实有些惊讶。"
    mc "你是怎么想到自己成立一个社团的？"
    mc "以你的能力，大概在任何一个大社团里都能成为管理层。"
    mc "你去年不还是辩论部的部长么？"
    m 5 "啊哈哈，这个嘛......"
    m "说实话，我无法忍受大社团里的勾心斗角。"
    m "感觉一天到晚都只是在为了预算和宣传还有如何准备活动而争论不休，别无它事......"
    m "我更愿意选择自己真正喜欢的东西，然后做出点名堂来。"
    m 1b "而且，要是这样能鼓励他人接触文学，那么我也算是在实现梦想呢！"
    show monika 1a
    show sayori 3q zorder 2 at t31
    s "莫妮卡真的是个很棒的部长！"
    show yuri 1 zorder 2 at t33
    "优里也点头同意。"
    show sayori zorder 1 at thide
    show yuri zorder 1 at thide
    hide sayori
    hide yuri
    mc "那我倒是有点惊讶，这个社团居然只有这么些人。"
    mc "新社团刚起步一定很难吧。"
    m 3b "确实不简单。"
    m "没有多少人愿意把全部精力投入到全新的事物中......"
    m "尤其是像文学这种，没法在第一时间吸引到注意力的东西。"
    m "你必须付出加倍的努力，才能向大家证明，你们这个社团既有趣又值得。"
    m "同时，这也让学园祭之类的校园活动，变得更加重要。"
    m 2k "我有自信能在我们毕业之前，将文学部发展壮大！"
    m "对吧，各位？"
    show monika 2a zorder 2 at t22
    show sayori 4r zorder 2 at t21
    s "没错！"
    show monika zorder 2 at t33
    show sayori zorder 2 at t32
    show yuri 1a zorder 2 at t31
    y "我们会竭尽全力。"
    show monika zorder 2 at t44
    show sayori zorder 2 at t43
    show yuri zorder 2 at t42
    show natsuki 4d zorder 2 at t41
    n "还用我说嘛！"
    "大家都踊跃赞成。"
    "这些截然不同的女孩们，却都感兴趣于同一个目标......"
    "想必莫妮卡一定花了不少功夫去找这三个成员。"
    "可能这就是为什么在听说会有新成员加入时，她们全都这么高兴。"
    "不过我还是不知道，我自己对文学的热情程度能不能赶得上她们......"
    show sayori zorder 1 at thide
    show monika zorder 1 at thide
    show natsuki zorder 1 at thide
    show yuri zorder 2 at t32
    hide sayori
    hide monika
    hide natsuki
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
    show monika 1d zorder 3 at f33
    m "真的吗？我可没想到你会去读恐怖小说哎，优里。"
    m "像你这种温柔的人，也看恐怖小说的吗......"
    show monika zorder 2 at t33
    show yuri zorder 3 at f32
    y 1a "可能我会给大家这样的印象吧。"
    y "但如果一个故事能发人深省、或者将我带到另一个世界，那我真的会手不释卷的。"
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
    show monika zorder 1 at thide
    show yuri zorder 1 at thide
    hide monika
    hide yuri
    show natsuki 1r zorder 2 at t42
    show sayori 4q behind natsuki at l41
    s "诶嘿嘿，你的小蛋糕，还有你的诗......"
    s "你做的每件事，都和你本人一样可爱~"
    show sayori behind natsuki at t21
    "纱世里溜到夏树背后，把手搭在她的肩上。"
    show natsuki at h42
    n 1v "{i}我才不可爱呢！！{/i}"
    show natsuki zorder 2 at t11
    show sayori zorder 1 at thide
    hide sayori
    mc "夏树，你也自己写诗的吗？"
    n 1c "嗯？大概也就偶尔写写吧。"
    n "不过你问这个干嘛？"
    mc "我觉得很厉害啊。"
    mc "为什么不找个时间分享一下你的诗作呢？"
    n 5q "不、不行！"
    "夏树移开了视线。"
    n "反正...你们不会喜欢的......"
    mc "啊......是对自己不够自信吗？"
    show yuri 2f zorder 2 at t31
    y "我能理解夏树的感受。"
    y "分享那种水平的文字，需要的可不仅仅是自信。"
    y 2k "最真挚的文字是写给自己的。"
    y "所以分享的前提是，你愿意向读者敞开心扉、暴露自己脆弱的一面，甚至展现内心最深处。"
    show natsuki zorder 1 at thide
    hide natsuki
    show monika 2a zorder 2 at t33
    m "那优里，你也有写作的经验吗？"
    m "如果你愿意分享一下你的作品，没准在榜样作用下，夏树分享作品也会更自在的。"
    show yuri at s31
    y 3o "......"
    mc "想必优里也是一样的情况吧......"
    show sayori 2g zorder 2 at t32
    s "噢......我倒是很想读大家的诗......"
    show sayori zorder 1 at thide
    show yuri zorder 1 at thide
    show monika zorder 1 at thide
    hide sayori
    hide yuri
    hide monika
    "气氛短时间陷入了沉默。"
    show monika 5a zorder 3 at f32
    m "就这样吧！"
    m "各位，我有个主意~"
    show yuri 3e zorder 2 at t31
    show natsuki 2k zorder 2 at t33
    ny "...？"
    "夏树和优里疑惑地看向莫妮卡。"
    m 2b "我们每个人都回家写一首自己的诗吧！"
    m "然后下次社团活动的时候，我们就可以彼此分享了。"
    m "这样的话，大家就扯平了！"
    show monika 2a zorder 2 at t32
    show natsuki zorder 3 at f33
    n 5q "呃——嗯......"
    show natsuki zorder 2 at t33
    show yuri 3v zorder 3 at f31
    y "......"
    show natsuki zorder 2 at t44
    show monika zorder 2 at t43
    show yuri zorder 2 at t42
    show sayori 4r at l41
    s "好耶——！就这么办！"
    show monika zorder 3 at f43
    m 1a "而且，既然我们现在有新成员加入，那我觉得这样的活动就能让大家相处得更自在一点，还能加强社团的凝聚力。"
    m "不是吗，[player]？"
    show monika zorder 2 at t43
    "莫妮卡又冲我甜甜地笑着。"
    mc "等会儿......还有一个问题。"
    show monika zorder 3 at f43
    m 1d "诶？还有什么问题吗？"
    "既然话题又回到了拉我进社团这件事上，我终于能直截了当、一吐为快了。"
    show monika zorder 2 at t43
    mc "我从来都没说过我要加入文学部啊！"
    mc "虽然纱世里说服了我过来看看，但我可没下过任何决定。"
    mc "我还有别的一些社团要看，而且......呃......"
    show monika 1g
    show sayori 1g
    show natsuki 4g
    show yuri 2e
    "我的思路戛然而止。"
    "四个女生全都用失落的眼神看着我。"
    show monika at s43
    m 1p "但、但是......"
    show yuri at s42
    y 2v "抱歉，我还以为......"
    show natsuki at s44
    n 5s "哼。"
    show sayori at s41
    s 1k "[player]......"
    mc "你、你...你们都......"
    "我......我对这些可爱的女生超没辙啊。"
    "这种情况下，我还怎么可能做出头脑清醒的决定啊？"
    "不过，只要付出写几首诗的代价，我就能每天和这些可爱的女生待在一起的话......"
    mc "......行吧。"
    mc "好了，那我就这么定了。"
    mc "我要加入文学部。"
    show monika 1e zorder 2 at t43
    show yuri 3f zorder 2 at t42
    show natsuki 1k zorder 2 at t44
    show sayori 4b zorder 2 at t41
    "女孩们的眼神一个接一个地泛起了光彩。"
    show sayori at h41
    s 4r "太——棒——了！我好开心~"
    "纱世里搂着我蹦达了起来。"
    mc "喂、你别——"
    show yuri zorder 3 at f42
    y 1m "你刚刚真的把我吓坏了......"
    show yuri zorder 2 at t42
    show natsuki zorder 3 at f44
    n 5q "如果你真的只是来蹭蛋糕吃的，那我绝对会气炸。"
    show natsuki zorder 2 at t44
    show monika zorder 3 at f43
    m 5 "那么，正式欢迎你！"
    m "欢迎来到文学部！"
    show monika zorder 2 at t43
    mc "啊......那，谢谢。"
    show yuri zorder 1 at thide
    show natsuki zorder 1 at thide
    show sayori zorder 1 at thide
    show monika zorder 2 at t11
    hide yuri
    hide natsuki
    hide sayori
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
    "与此同时，优里和夏树开始整理桌子，大家继续有一搭没一搭地闲聊着。"
    show sayori 1a zorder 2 at t11
    s "对了, [player], 既然你正好来了, 咱们要不一起走回家吧？"
    "对哦——因为纱世里总是要在放学后参加社团活动，所以我们就再也没有一起回过家。"
    mc "好啊，我们走吧。"
    s 4q "好耶~"

    scene bg residential_day
    with wipeleft_scene

    "就这样，我们俩离开了部室，踏上了回家的路。"
    "一路上，我的思绪都在四位女孩间游转："
    show sayori 1 zorder 2 at t41
    "纱世里，"
    show natsuki 4 zorder 2 at t42
    "夏树，"
    show yuri 1 zorder 2 at t43
    "优里，"
    show monika 1 zorder 2 at t44
    "当然，还有莫妮卡。"
    "每天放学后泡在文学社团里，我真的会感到快乐吗？"
    "说不定我还有机会和当中的哪个女生拉近距离..."
    hide sayori
    hide natsuki
    hide yuri
    hide monika
    with wipeleft
    "没错！"
    "我只要充分利用条件就行了，好运总有一天会来的。"
    "看来万事都要从今晚写的这首诗诗开始了..."

    return

label ch0_kill:
    $ s_name = "纱世里"
    show sayori 1b zorder 2 at t11
    s "......"
    s "......"
    s "什、什么......"
    s 1g "......"
    s "这..."
    s "这是怎么回事......？"
    s "哦，不......"
    s 1u "不要啊......"
    s "这不可能。"
    s "一点都不合理。"
    s 4w "这都是哪跟哪？"
    s "我到底又是谁？"
    s "停下来！"
    s "求！求！你！停！下！来！啊！！！"

    $ delete_character("sayori")
    $ delete_character("natsuki")
    $ delete_character("yuri")
    $ delete_character("monika")
    $ renpy.quit()
    return

