<!-- github支持LaTeX设置 -->
<head>
    <script src="https://cdn.mathjax.org/mathjax/latest/MathJax.js?config=TeX-AMS-MML_HTMLorMML" type="text/javascript"></script>
    <script type="text/x-mathjax-config">
        MathJax.Hub.Config({
            tex2jax: {
            skipTags: ['script', 'noscript', 'style', 'textarea', 'pre'],
            inlineMath: [['$','$']]
            }
        });
    </script>
</head>
<!--  -->
# ML_Learn
记录机器学习的学习历程

## 机器学习实战
![pic][1]

### charpter2 K-近邻算法
以电影类型分类为例，我们可以明确每部电影在风格上会同相同题材的电影相近。例如动作片之间有什么共同的特征，这个特征又和爱情片之间存在明显的差异呢？

我们可以使用电影中打斗次数和接吻次数，使用KNN算法自动划分电影题材。

> KNN算法优缺点：

+ 优点：精度高、对异常值不敏感、无输入数据假定。
+ 缺点：计算复杂度高、空间复杂度高。
+ 适用数据范围：数值型和标称型。

使用距离来表示数据之间的近邻程度，上面电影分类的例子就是使用接吻次数、打斗次数（数值）之间的距离来判断待分类电影的类型，`最近`电影的分类标签（频数最高的）则判定为未知电影的分类。

> 介绍几种距离算法：

+ 欧式距离
两个向量点$xA$和$xB$之间的距离
$$d = \sqrt{(xA_0-xB_0)^2+(xA_1-xB_1)^2}$$

[1]:  https://tse2-mm.cn.bing.net/th/id/OIP.eV8F2zYO8rfJxx-R8KV9LAHaHa?w=175&h=180&c=7&o=5&dpr=2&pid=1.7    "机器学习书籍图片"