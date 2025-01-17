# coding: utf-8

def get_text_script():
    return '<h1>第五周 - 纳什均衡</h1>'
    text_script = """
    1————－
    前面我们看到，有些博弈，每个参与人都没有严格占优策略，如何求得这种博弈的解，就是我们这一节要考虑的问题。为此，有必要再回顾一下什么是博弈的解。博弈的解，就是所有参与人，每人出一个策略构成的策略组合，这个策略组合隐含的基本性质就是，任何一个人都不可能单方面通过改变自己在其中的策略而获得更好的回报。显然，如果一个人的策略是占优策略，他不可能通过改变而获得更好回报；而如果一个人的策略不是占优策略，但其他人用了占优策略，同时这人用的是该占优策略的最佳应对策略，则他也不可能通过改变而获得更好回报的。这也就是上一节的内容。其实，上面这样的讲法给了我们进一步发展的思路：如果都没有占优策略，两个互为最佳应对的策略也构成博弈的解。
    2————－
    还是看前面提到的这个例子，我们已经知道了，两个参与人都没有占优策略，但不难验证，策略（A，A）是互为最佳应对的。也就是说，如果公司1选择策略A，公司2最好是选择A（回报4，其他的是2），关键是，此时恰好公司1也就没有改变策略的动机（回报4，其他是0）。因此，策略组（A，A）就是这个博弈的解。这种互为最佳应对的策略组也称为纳什均衡。
    当然，马上出来的一个问题是如何找到这样的互为最佳应对策略组。最简单，也是最不怕麻烦的方法就是一个个检查博弈的策略组，按照互为最佳应对的定义，看是不是。人们也提出了一些提高效率的方法，我们的教材上也有些介绍。但总的来说，寻找纳什均衡是一件不容易的事情。
    3————－
    不容易是一方面，另一方面的问题是一个博弈有可能存在多个纳什均衡。最典型的就是这种协调博弈，就像我们前面提到过的两个朋友在商场走失了，每人要决定去哪个门碰对方，收益矩阵写出来就是这个样子。只要两人做出了相同的选择，就会都是好结果，这里用回报1来表示，如果选择不一样，对两人就都不好，这里用回报0表示。按照互为最佳应对的定义，这个博弈有两个均衡，也就是有两个解，达到了其中任何一个都OK，但我们从这个博弈给的条件本身没法明确到底那一个更加可能，就像我们在商场和朋友如果没有预先说好什么，就知道有两个门的困境一样。这也有点像我们求解一元二次方程，有两个根，就方程本身而言，这两个根都是对的，但需要根据方程的具体应用背景才可以确定舍弃其中一个。具有多个纳什均衡的博弈类似，要预测博弈的单一结果，需要借助某些外部信息，例如你们两事先说好了，如果走失，就到南门碰头。
    4————－
    另外一种有多个纳什均衡的博弈是所谓鹰鸽博弈，这是反映鹰鸽博弈结构的典型收益矩阵。描述的应用背景是，如果两个人都温和，那么利益各半，如果两人都很凶，那么两败俱伤。如果一个温和一个凶狠，凶狠的就会得到较多利益。在这种情况下，能看出博弈的均衡不是两个人做同样选择，而是做不同选择，也就是一个是鹰，一个是鸽。尽管选择鸽策略的回报只有1，但你此时也不会改变策略了，改了回报变成0。注意，在推理中我们不能认为，也许你应该改策略，因为尽管你的回报从1变成0，少了，但对方的回报从5变成0，更少了。这样一种思维是违反我们最初关于博弈推理假设的，我们讲了，博弈推理中每人只是根据收益矩阵想着自己如何能最好，既不刻意帮别人，也不要做宁可自我损失以害别人的事情。在这个博弈中，同样，仅从博弈结构，我们不可能预测到底博弈的结果会是两个均衡中的哪一个，需要借助其他外部信息才可以。我们能知道的，是博弈的结果不会是那两个非均衡的策略组。因此一般说来，纳什均衡概念能有助于缩小预测范围，但它并不一定能给出唯一的预测。
    5————－
    至此，我们已经了解了博弈论的一些最基本的观念。就是占优策略、严格占优策略、最佳应对、严格最佳应对，以及互为最佳应对的策略组，也就是纳什均衡，它们在博弈的推理中（或者说求解中）扮演着重要作用。最后我们举了几个具有多个纳什均衡的博弈的例子。
    现在我们关心另一个关键问题，每个博弈都有纳什均衡吗？如果不存在纳什均衡，我们如何讨论博弈的解？其实，我们前面已经看到过一个博弈，它不存在互为最佳应对的策略组，当时我们是说它无解。那就是田忌赛马博弈，我们看到了，在任何策略组上，总有一方可以通过改变策略得到更好的回报。 
    6————－
    为了方便讨论，让我们来看一个最简单、也是最典型的不存在上述意义纳什均衡的博弈，这类博弈有一个特别的，也是很重要的名称，零和博弈（即无论什么策略组合，回报之和都为零），强调博弈双方具有针锋相对的关系。平常我们在社会生活中谈到的博弈，大都有这种性质。但我们现在已经知道了，博弈论中的博弈概念，除了包含零和博弈，还包容大量非零和博弈类型，博弈参与人不一定是针锋相对的。
    这是所谓硬币配对的博弈，两个人，独立选择出示硬币的某一面，如果不一致，那你就赢了，如果一致，你就输了。输的一方要把硬币交给赢方。一眼就能看出，这个博弈没有互为最佳应对策略组，和田忌赛马博弈一样，输的那位总可以想如果换了另外一个策略就是赢了。
    怎么讨论这种博弈的解呢？设想你是这种博弈的某一方，会怎样决定自己的行为？显然，你要考虑两点，第一，估计对方会出哪一面；第二，不要让对方猜出你出的是哪一面。因此，你到底出什么，就有某种随机性。这种随机性，既来自于你对对方随机性的考虑，也来自于你为了迷惑对方而表现出来的随机行为。因此，对这种随机性加以考虑，就是讨论这类博弈推理的关键。
    7————－
    这个时候，我们说你是以一定的概率在两个策略之间做选择，这个概率就是你的策略，为区别起见，称为“混合策略”，而博弈收益矩阵中给出的那些选项称为“纯策略”。准确地讲，在面对两个纯策略的情形，例如硬币配对博弈中一个H，另一个T，我们讲你的策略是概率p，实际上是说你以概率p选择H策略，用概率1-p选择T策略。
    8————－
    好了，现在来看我们面对的情况。说的还是博弈，前面说过博弈有三要素。现在基于给出的收益矩阵，参与人没问题，还是原来那两个，前面我们重新定义了策略，就是概率。回报是什么呢？收益矩阵中的那几个数显然不是了，它们是对应纯策略的，而且现在讨论的是混合策略，即概率策略。学过概率的都知道，在概率选择的情况下，一种自然的回报计算就是在选项回报上依照概率的加权平均，也就是回报的期望。给定了对应纯策略组合的收益矩阵，以及参与人的概率策略，就可以算得他们的回报。
    9——————
    现在看一个计算的例子，还是硬币配对博弈，这里标上了双方的混合策略，来看一看你和他分别的回报如何计算。按照前面所说，你的回报等于你在两种选择上的回报的加权平均，权就是对应的概率。就是这个式子。然后考虑其中的“你选H的回报”。这里，当你选H时，他会以一定的概率选H或者T，因此在计算“你选H的回报”的时候要考虑这种概率因素，于是也表达成一个加权平均的形式，只是此时的权要用他的概率了，就是这个样子。现在，就可以用上收益矩阵中的值了，得到你选H的回报为0.4。类似地，可算得你选T的回报为－0.4。将这两个数带入“你的回报”的式子，就得到了结果0.08。类似地，我们也能算出在这种情况下他的回报。
    10——————
    这样计算混合策略的回报，初接触会觉得有些复杂。不过，在研究博弈的时候，我们一般并不关心在每个策略下的具体回报，而是关心博弈的走向，或者说博弈的解，关心是否能达到均衡。在纯策略博弈的时候，我们说均衡就是互为最佳应对的策略组，在混合策略博弈的时候，这个概念是一样的，我们也要考虑互为最佳应对的策略组，只是，现在策略是概率，也就是要考虑互为最佳应对的概率了。最佳应对的含义也类似，就是改变概率策略后不会得到更好的回报，这里当然指的是前面介绍的在概率意义下的平均回报。
    11——————
    现在的问题就变成了，在这样的双人双策略的博弈中，如何确定互为最佳应对的概率策略？
    前面我们讲到过，你作为这种博弈的参与人，在每一次博弈局中，潜意识中考虑的事情之一就是要让对方不知道你要出什么，从而让他不能确定出某个纯策略要比另一个会带来更大的回报；他的回报大了，你的就会小了。这也就是说，你用的策略概率，如果是最优的话，就是让他在两个纯策略上的回报相等的概率。这样一种思路称为“无差异原理”，我们来看用它能否确定你的最佳概率策略。假设要求的概率是p，那么，他出H策略的回报就是p*1+(1-p)*(-1)=2p-1，类似地，他出T策略的回报就是-2p+1。按照无差异原理，最佳的p应该使这两个式子相等，也就得到了p=0.5。类似地，可以算得对方的最佳概率q=0.5。我们说，（0.5，0.5）就是这个博弈的混合策略纳什均衡，想一想这个结果，也是符合直觉的。如果你参与这个博弈，会刻意倾向出正面或者出反面吗？如果你倾向于出正面，也就是出正面的概率高，那么对方发现后就会总出正面，从而肯定就要赢你了。
    12——————
    下面来看另一个例子，通过它来进一步体会混合策略均衡的计算。这个例子的背景是橄榄球比赛的策略研究。收益矩阵是这个样子，其中体现了橄榄球的记分规则，例如防守方是不得分的，即便成功阻止了进攻。我们来看如何利用无差异原理计算互为最佳应对的概率策略。
    假设进攻方用概率p，这个式子左边是防守方采用防手抛球策略的回报，右边是防守方采用防手持球策略的回报，按照无差异原理，做它们的等式，就求得进攻方的最佳概率p＝1/3。完全类似地方法，我们也可以求得防守方的最佳策略概率为q=2/3.
    也就是说，p=1/3,q=2/3是这个博弈的互为最佳应对概率，也就是它的混合策略均衡。
    13——————
    好了，现在我们看来会计算这种混合策略均衡了。但喜欢刨根问底的学习者马上会产生许多疑问。至少会有下面两个：（1）是不是，如果一个博弈没有纯策略意义下的均衡，就一定有混合策略均衡？（2）一个博弈，如果有纯策略意义下的均衡，还可能有混合策略均衡吗？
    对于第一个问题的回答，那就是纳什的重大贡献了，他给出了肯定回答，证明了如果包括混合策略的话，任何博弈都存在均衡。也就是说，如果一个博弈没有纯策略均衡，就一定有混合策略均衡。
    对于第二个问题，回答也是肯定的，只要找到一个例子就可以了。注意，这里只是说“可能”，并不是一定有。下面我们看看例子。
    14——————
    不难看到，这是一个协调博弈，有两个纯策略均衡。按照无差异原理试求混合策略均衡，得到的p=q=2/3，在0和1之间，因此（2/3，2/3）是一个混合策略均衡。
    但是，我们也能意识到，正如不是所有博弈都有纯策略均衡一样，并不是所有博弈都有混合策略均衡的。教材上有这样的例子。
    15——————
    这一节我们讨论的是基础博弈论的核心概念，纳什均衡。纳什告诉我们，如果算上混合策略均衡，那么任何有限参与人、有限策略的博弈都有均衡。均衡可能有一个，也可能有多个，可能只有纯策略均衡或者只有混合策略均衡，也可能二者兼而有之。我们已经知道，均衡是一种稳定，是人们不得不满足于已有回报的稳定，尽管那些回报并不一定是最好的，甚至是比较差的，囚徒困境就是一个典型例子。下面我们来看就后面这个话题能有些什么认识。
    """
    return '\n'.join(['<p>' + text + '</p>' for text in text_script.split('\n')])

def build_graph(path):
    entity_set = set([])
    triplets = []
    with open(path, 'r') as kg_file:
        for line in kg_file:
            if line.strip().lower() == 'end':
                break
            if not line.strip():
                continue
            e1, r, e2 = line.strip().split(',')
            triplets.append((e1, r, e2))
            entity_set.add(e1)
            entity_set.add(e2)
    entity_dict = {entity: idx for idx, entity in enumerate(entity_set)}
    nodes = []
    for entity in entity_set:
        node = {
            'filter': [],
            'showstyle': '0',
            'entitytype': '0',
            'name': entity,
            'uuid': entity_dict[entity]
        }
        nodes.append(node)
    edges = []
    for idx, (e1, r, e2) in enumerate(triplets):
        edge = {
            'sourceid': entity_dict[e1],
            'targetid': entity_dict[e2],
            'name': r,
            'uuid': idx
        }
        edges.append(edge)
    return entity_dict, nodes, edges


if __name__ == '__main__':
    entity_dict, nodes, edges = build_graph()
