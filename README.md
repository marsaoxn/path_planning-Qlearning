path planning + Q-learning

房间例子：
网上的例子，原来的代码有问题，有以下修改：
1、while循环是死循环，加上计数器，或者改为for循环
2、根据Qlearning算法原理，第二层是循环语句不是判断语句
思考：第二层是判断语句也可以得到结果

test1：
对比房间例子只是修改了R矩阵，相当于只是修改了迷宫

test1_v1:
实现英文论文中的算法
4.28，r矩阵和q矩阵不能同时迭代，r一定，q才会收敛

test1_v2:
实现中文论文中的算法

test1_v3:
在v2的基础上，修改了两点：
1、可以经过多次点，但是不能经过多次边
2、减少拐弯的算法，修改为在选择时增加判断（不可行）
4.27改进：1、起点为4度点
         2、优先选择非桥（把4度点的奖赏调低）
         3、少拐弯，内2度点第二高

test1_v4：
修改r矩阵思路，r矩阵储存边与边的信息，目前看到如下几点优势：
1、边拐弯的奖赏容易设置
2、边也可以判断出桥，那么理论上也可以达到v3的结果、
（注意赋值和copy的区别）
5.12完成：
        1所有拐弯：0.8
        2所有直线（非桥）：1
        3所有桥：0.5
        4去掉回头路
        
v5_point、v5_side:
整合后的版本，只需要关心图的输入，后续全部自动处理。两个方法对偶。

draw：
后续工作，通过r矩阵画出图，或者根据图得到r矩阵。
