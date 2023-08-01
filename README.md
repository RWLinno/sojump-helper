# 问卷星社区互填助手

---

version : 1.0

release date : 2023.8.1

author : RWLinno

---

### 功能：

支持速刷互填社区的点数，使得自己的问卷更多曝光，从而达到快速回收问卷的目的。



### 使用方法：

1. 首先进入互填社区的页面

![step1](https://github.com/RWLinno/sojump-helper/blob/main/pic/step1.jpg)

2. 按`ctrl+U` 查看网页源代码，随后`ctrl+A`全选，`ctrl+C`复制。

![step2](https://github.com/RWLinno/sojump-helper/blob/main/pic/step2.jpg)

3. `ctrl+V`粘贴到程序目录下的page.txt文本中。

![step3](https://github.com/RWLinno/sojump-helper/blob/main/pic/step3.jpg)

4.最后安装相应环境，运行main.py即可，点击按钮即可。

![step4](https://github.com/RWLinno/sojump-helper/blob/main/pic/step4.jpg)

5.结果：社区上有很多问卷还处理不了(有些要手机端、有些限定复选数等等)，但10秒能够处理一个简单的问卷，经过我实践基本上2分钟就能刷200~400点数了。

![step5](https://github.com/RWLinno/sojump-helper/blob/main/pic/step5.jpg)



### 常见问题

##### 如何看待脚本刷问卷

- 有时候互填社区的点数一不留神就-999了根本填不回来，所以我觉得问卷星这设计本身就有问题。用这个的话一般隔一两天等问卷社区更新了用一次就好了，不会浪费太多时间。

- 这其实算作弊，好孩子不要用。这是一个不太道德的项目，我写这个是想锻炼自己，没有盈利，侵删。
- 社区互填这功能在我看来也是问卷星的黑色地带，不会有很认真填的，就让我来加速它的堕落。

##### 关于原理

让大家复制网页源代码是因为做登录太麻烦了，然后又不想涉及隐私，所以干脆让大家登进去弄。

main.py把网页中的问卷地址记录下来，并且一个个发起自动填写。

auto.py 是自动填写一个问卷，原理很简单，对每个问题点击和传参，再随便再打乱(补充)一下选和填的东西。

##### 关于后续更新

时间有限，写的东西只处理选择填空，能够满足大部分需要了，有些限手机端、上传文件、限定选项的问卷搞不来。

问卷星为了反爬会更新，网上很多其他同类项目都用不了了，这个是截止到2023.8.1程序有效的。

主要还是做来玩吧，说不定我上传到 github 隔一个月就莫得了，要是没人需要的话也不会更新。

如果有人需要的话可以联系我，点个star，我去做新增内容。