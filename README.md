# 小北原创UI自动化高阶框架selenium+pytest

## 介绍
免费开源的高级selenium自动化框架，开箱即用，复用性高，可适用任何web项目中
原创作者：小北
微信：xiaobei_upup   扫码可添加作者答疑
![输入图片说明](screenshots/888f3f9e1e8bd0a003aac3d204afaa8.jpg)


# 捐赠小北喝瓶水 :sunglasses: 
![输入图片说明](screenshots/%E6%94%AF%E4%BB%98%E5%AE%9D%E6%94%AF%E4%BB%98%E7%A0%81.jpg)
![输入图片说明](%E5%BE%AE%E4%BF%A1%E6%94%AF%E4%BB%98%E7%A0%81.jpg)

#### 软件架构
软件架构说明


# 安装教程 ：需要安装的库，只需要一键运行  pip3 install -r requirement.txt即可

        注意网络不好容易报错，报错之后重新安装即可，
        selenium
        pytest
        allure-pytest
        多线程并发执行用例插件
        pytest-xdist
        失败重跑的插件
        pytest-rerunfailures
        图片处理相关的库 可以理解为PIL
        pillow
        文件上传的识别文件资源管理器的库
        pywinauto
        图片验证码识别的库
        ddddocr

#### 使用说明
1. 这里是列表文本先安装对应的库，只需要一键运行  pip3 install -r requirement.txt 即可
2. 这里是列表文本再下载对应的webdriver浏览器驱动： https://registry.npmmirror.com/binary.html?path=chromedriver/
3. 这里是列表文本再配置浏览器驱动解压文件夹的环境变量
4. 这里是列表文本pycharm中运行项目即可，或者项目目录下命令行输入pytest即可运行

#### 参与贡献

1.  Fork 本仓库
2.  新建 Feat_xxx 分支
3.  提交代码
4.  新建 Pull Request


#### 特技

1.  使用 Readme\_XXX.md 来支持不同的语言，例如 Readme\_en.md, Readme\_zh.md
2.  Gitee 官方博客 [blog.gitee.com](https://blog.gitee.com)
3.  你可以 [https://gitee.com/explore](https://gitee.com/explore) 这个地址来了解 Gitee 上的优秀开源项目
4.  [GVP](https://gitee.com/gvp) 全称是 Gitee 最有价值开源项目，是综合评定出的优秀开源项目
5.  Gitee 官方提供的使用手册 [https://gitee.com/help](https://gitee.com/help)
6.  Gitee 封面人物是一档用来展示 Gitee 会员风采的栏目 [https://gitee.com/gitee-stars/](https://gitee.com/gitee-stars/)


# run all testcases
pytest
# run allure report
pytest --alluredir ./reports testcases/
# start up serve to browse report
allure serve ./reports
# run pytest to choose which you want to run
pytest -m test
