from app.models import User, Direction, Progress, Course
from app import db


def insert():
    dir1 = Direction(name="前端开发", content="""Web前端开发是从网页制作演变而来，名称上有很明显的时代特征。在互联网的演化进程中，网页制作是Web1.0时代的产物，早期网站主要内容都是静态，以图片和文字为主，用户使用网站的行为也以浏览为主。随着互联网技术的发展和HTML5、CSS3的应用，现代网页更加美观，交互效果显著，功能更加强大。""")
    dir2 = Direction(name="java开发", content="""Java，是由Sun Microsystems公司于1995年5月推出的Java程序设计语言和Java平台的总称。用Java实现的HotJava浏览器（支持Java applet）显示了Java的魅力：跨平台、动态的Web、Internet计算。从此，Java被广泛接受并推动了Web的迅速发展，常用的浏览器现均支持Java applet。""")
    dir3 = Direction(name="UI设计师", content="""“UI”的本义是用户界面，是英文User和interface的缩写。UI设计师简称UID（User Interface Designer），指从事对软件的人机交互、操作逻辑、界面美观的整体设计工作的人。
UI设计师的涉及范围包括商用平面设计、高级网页设计、移动应用界面设计及部分包装设计，是目前中国信息产业中最为抢手的人才之一。""")
    dir4 = Direction(name="PHP", content="PHP（外文名:PHP: Hypertext Preprocessor，中文名：“超文本预处理器”）是一种通用开源脚本语言。语法吸收了C语言、Java和Perl的特点，利于学习，使用广泛，主要适用于Web开发领域。PHP 独特的语法混合了C、Java、Perl以及PHP自创的语法。它可以比CGI或者Perl更快速地执行动态网页。用PHP做出的动态页面与其他的编程语言相比，PHP是将程序嵌入到HTML（标准通用标记语言下的一个应用）文档中去执行，执行效率比完全生成HTML标记的CGI要高许多；PHP还可以执行编译后代码，编译可以达到加密和优化代码运行，使代码运行更快。""")
    dir5 = Direction(name="Python", content="""Python   （英国发音：/ˈpaɪθən/ 美国发音：/ˈpaɪθɑːn/）, 是一种面向对象的解释型计算机程序设计语言，由荷兰人Guido van Rossum于1989年发明，第一个公开发行版发行于1991年。
Python是纯粹的自由软件， 源代码和解释器CPython遵循 GPL(GNU General Public License)许可。Python语法简洁清晰，特色之一是强制用空白符(white space)作为语句缩进。
Python具有丰富和强大的库。它常被昵称为胶水语言，能够把用其他语言制作的各种模块（尤其是C/C++）很轻松地联结在一起。常见的一种应用情形是，使用Python快速生成程序的原型（有时甚至是程序的最终界面），然后对其中有特别要求的部分，用更合适的语言改写，比如3D游戏中的图形渲染模块，性能要求特别高，就可以用C/C++重写，而后封装为Python可以调用的扩展类库。需要注意的是在您使用扩展类库时可能需要考虑平台问题，某些可能不提供跨平台的实现。
7月20日，IEEE发布2017年编程语言排行榜：Python高居首位   。
2018年3月，该语言作者在邮件列表上宣布 Python 2.7将于2020年1月1日终止支持。用户如果想要在这个日期之后继续得到与Python 2.7有关的支持，则需要付费给商业供应商。""")
    dir6 = Direction(name="Android", content="""android开发是指android平台上应用的制作，Android早期由“Android之父”之称的Andy Rubin创办，Google于2005年并购了成立仅22个月的高科技企业Android，展开了短信、手机检索、定位等业务，基于Linux的通用平台进入了开发。
软件开发需要掌握的知识体系有：Unix/Linux平台技术、企业级数据库技术、Java 语言核心技术、软件工程和设计模式、Android应用开发基础、互联网核心技术、Android系统级开发、JavaEE核心技术。""")
    dir7 = Direction(name="美工", content="""美工一般是指对平面，色彩 ，基调，创意等进行加工和创作的技术人才，分为平面美工、网页美工和三维美工。一般需要精通Photoshop等设计软件。""")
    dir8 = Direction(name="深度学习", content="""深度学习的概念源于人工神经网络的研究。含多隐层的多层感知器就是一种深度学习结构。深度学习通过组合低层特征形成更加抽象的高层表示属性类别或特征，以发现数据的分布式特征表示。  
深度学习的概念由Hinton等人于2006年提出。基于深度置信网络(DBN)提出非监督贪心逐层训练算法，为解决深层结构相关的优化难题带来希望，随后提出多层自动编码器深层结构。此外Lecun等人提出的卷积神经网络是第一个真正多层结构学习算法，它利用空间相对关系减少参数数目以提高训练性能。  
深度学习是机器学习中一种基于对数据进行表征学习的方法。观测值（例如一幅图像）可以使用多种方式来表示，如每个像素强度值的向量，或者更抽象地表示成一系列边、特定形状的区域等。而使用某些特定的表示方法更容易从实例中学习任务（例如，人脸识别或面部表情识别）。深度学习的好处是用非监督式或半监督式的特征学习和分层特征提取高效算法来替代手工获取特征。
深度学习是机器学习研究中的一个新的领域，其动机在于建立、模拟人脑进行分析学习的神经网络，它模仿人脑的机制来解释数据，例如图像，声音和文本。  
同机器学习方法一样，深度机器学习方法也有监督学习与无监督学习之分．不同的学习框架下建立的学习模型很是不同．例如，卷积神经网络（Convolutional neural networks，简称CNNs）就是一种深度的监督学习下的机器学习模型，而深度置信网（Deep Belief Nets，简称DBNs）就是一种无监督学习下的机器学习模型。""")
    dir9 = Direction(name="算法工程师", content="""算法（Algorithm）是一系列解决问题的清晰指令，也就是说，能够对一定规范的输入，在有限时间内获得所要求的输出。如果一个算法有缺陷，或不适合于某个问题，执行这个算法将不会解决这个问题。不同的算法可能用不同的时间、空间或效率来完成同样的任务。一个算法的优劣可以用空间复杂度与时间复杂度来衡量。算法工程师就是利用算法处理事物的人。""")
    dir10 = Direction(name="Hadoop", content="""Hadoop是一个由Apache基金会所开发的分布式系统基础架构。
用户可以在不了解分布式底层细节的情况下，开发分布式程序。充分利用集群的威力进行高速运算和存储。
Hadoop实现了一个分布式文件系统（Hadoop Distributed File System），简称HDFS。HDFS有高容错性的特点，并且设计用来部署在低廉的（low-cost）硬件上；而且它提供高吞吐量（high throughput）来访问应用程序的数据，适合那些有着超大数据集（large data set）的应用程序。HDFS放宽了（relax）POSIX的要求，可以以流的形式访问（streaming access）文件系统中的数据。
Hadoop的框架最核心的设计就是：HDFS和MapReduce。HDFS为海量的数据提供了存储，则MapReduce为海量的数据提供了计算。""")
    dir11 = Direction(name="Node.js", content="""Node.js是一个Javascript运行环境(runtime environment)，发布于2009年5月，由Ryan Dahl开发，实质是对Chrome V8引擎进行了封装。Node.js对一些特殊用例进行优化，提供替代的API，使得V8在非浏览器环境下运行得更好。
V8引擎执行Javascript的速度非常快，性能非常好。   Node.js是一个基于Chrome JavaScript运行时建立的平台， 用于方便地搭建响应速度快、易于扩展的网络应用。Node.js 使用事件驱动， 非阻塞I/O 模型而得以轻量和高效，非常适合在分布式设备上运行数据密集型的实时应用。""")
    dir12 = Direction(name="大数据开发", content="""大数据是对海量数据存储、计算、统计、分析等一系列处理手段，处理的数据量是TB级，甚至是PB或EB级的数据，是传统数据处理手段无法完成的，大数据涉及分布式计算、高并发处理、高可用处理、集群、实时性计算等等，汇集的是IT最热门、最流行的IT技术，大数据是机器学习、深度学习、AI等尖端可以领域的基础架构。""")
    dir13 = Direction(name="数据分析师", content="""数据分析师 是数据师的一种，指的是不同行业中，专门从事行业数据搜集、整理、分析，并依据数据做出行业研究、评估和预测的专业人员。""")
    dir14 = Direction(name="大数据架构", content="""大数据的普及。大数据架构技术，就是把大数据开发中一些通用的，重复使用的基础代码、算法封装为类库，降低大数据的学习门槛，降低开发难度，提高大数据项目的开发效率。""")
    dir15 = Direction(name="人工智能", content="""人工智能（Artificial Intelligence），英文缩写为AI。它是研究、开发用于模拟、延伸和扩展人的智能的理论、方法、技术及应用系统的一门新的技术科学。
人工智能是计算机科学的一个分支，它企图了解智能的实质，并生产出一种新的能以人类智能相似的方式做出反应的智能机器，该领域的研究包括机器人、语言识别、图像识别、自然语言处理和专家系统等。人工智能从诞生以来，理论和技术日益成熟，应用领域也不断扩大，可以设想，未来人工智能带来的科技产品，将会是人类智慧的“容器”。人工智能可以对人的意识、思维的信息过程的模拟。人工智能不是人的智能，但能像人那样思考、也可能超过人的智能。
人工智能是一门极富挑战性的科学，从事这项工作的人必须懂得计算机知识，心理学和哲学。人工智能是包括十分广泛的科学，它由不同的领域组成，如机器学习，计算机视觉等等，总的说来，人工智能研究的一个主要目标是使机器能够胜任一些通常需要人类智能才能完成的复杂工作。但不同的时代、不同的人对这种“复杂工作”的理解是不同的。""")
    dir16 = Direction(name="区块链", content="""区块链是分布式数据存储、点对点传输、共识机制、加密算法等计算机技术的新型应用模式。所谓共识机制是区块链系统中实现不同节点之间建立信任、获取权益的数学算法   。
区块链（Blockchain）是比特币的一个重要概念，它本质上是一个去中心化的数据库，同时作为比特币的底层技术。区块链是一串使用密码学方法相关联产生的数据块，每一个数据块中包含了一次比特币网络交易的信息，用于验证其信息的有效性（防伪）和生成下一个区块。""")

    u1 = User(username="白伟伟", number="20162163", password="20162163", direction=dir1)
    u2 = User(username="张三", number="20162164", password="20162164", direction=dir2)
    u3 = User(username="李四", number="20162165", password="20162165", direction=dir3)
    u4 = User(username="王五", number="20162166", password="20162166", direction=dir4)
    u5 = User(username="赵柳", number="20162167", password="20162167", direction=dir5)

    c1 = Course(name="html", cycle=20, direction=dir1)
    c2 = Course(name="css", cycle=20, direction=dir1)
    c3 = Course(name="javascript", cycle=20, direction=dir1)
    c4 = Course(name="bootstrap", cycle=20, direction=dir1)
    c5 = Course(name="jquery", cycle=20, direction=dir1)
    c6 = Course(name="jsp", cycle=20, direction=dir3)

    db.session.add_all([dir1, dir2, dir3, dir4, dir5, dir6, dir7, dir8, dir9, dir10, dir11, dir12, dir13, dir14, dir15, dir16])
    db.session.add_all([u1, u2, u3, u4, u5])
    db.session.add_all([c1, c2, c3, c4, c5, c6])
    db.session.commit()