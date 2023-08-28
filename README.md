# 小北原创UI自动化高阶框架selenium+pytest+allure+各种高级工具函数

# 免费开源的高级selenium的UI自动化框架，开箱即用，复用性高，可适用任何web项目中
# 原创作者：小北
# 微信：xiaobei_upup   扫码可添加作者答疑
![输入图片说明](screenshots/888f3f9e1e8bd0a003aac3d204afaa8.jpg)

# 软件架构
selenium+pytest+allure+各种工具函数

# 小北原创高级UI自动化框架亮点 ：
        1、使用pytest-xdist多线程并发执行测试用例，显著缩短用例执行时间
        2、使用pytest-rerunfailures的库实现失败用例重跑的功能
        3、使用cv2和numpy和pillow实现组件的颜色识别功能，能够完成一些跟颜色相关的用例覆盖
        4、使用pywinauto库来实现文件上传中识别文件资源管理器的功能
        5、使用ddddocr库和PIL库来图片来做验证码识别，免费开源的库，可识别复杂验证码
        6、使用python描述符封装元素定位的类，实现传入键值对出发get方法可以实现定位，对元素赋值出发set方法可以输入字符串
        7、使用fixture装饰器和生成器可以实现执行测试用例前自动登录，执行测试用例后自动登出
        8、使用fixture装饰器和生成器在conftest文件中全局管理driver
        9、使用@pytest.mark可以标记执行冒烟还是回归还是所有用例
        10、使用pytest.ini文件可以全局管理pytest的运行逻辑，达到一键运行pytest所有的配置项
        11、使用requirement.txt文件管理所有的库，实现安装配置一键化，运行pip3 install -r requirement.txt即可安装所有依赖
        12、使用.gitignore文件可以控制哪些内容是需要git跟踪的，哪些不用git跟踪，方便管理自动化代码
        13、重新封装断言库，让断言库更加详细和高效，能看见实际值和希望指的区别
        14、重新封装time库中的函数，让使用更方便
        15、封装了一个判断数据是否处于刷新状态的函数，在验证股票实时刷新阶段特别好用
        16、封装了一个发送邮件的函数，可以运行完不借助jenkins发送邮件到邮箱，一般真实场景中是用jenkins插件来实现发送邮件测试报告的
        17、封装了一个截图的工具函数，能够快速截图，遇到报错的时候就触发截图操作，方便后续allure观察报告
        18、使用asyncio和aiohttp实现异步操作
        19、封装了一个滑动的工具函数，方便实现滑动操作
        20、后续持续更新！！！！！！！！！！！！！！！！！！！！！

# 框架安装使用说明
1. 这里是列表文本第一步先安装对应的库，只需要一键运行  pip3 install -r requirement.txt 即可安全所有依赖库 【注意网络不好容易报错，报错之后重新安装即可】
2. 这里是列表文本第二步再下载对应的webdriver浏览器驱动： https://registry.npmmirror.com/binary.html?path=chromedriver/
3. 这里是列表文本再配置浏览器驱动解压文件夹的环境变量
4. 【运行测试用例】这里是列表文本pycharm中运行项目即可，或者项目目录下命令行输入pytest即可运行
5、【运行含有allure测试报告的测试用例】使用pytest运行allure测试报告，只需要使用pytest即可，因为pytest.ini文件中已经配置好了allure的配置参数
6、【查看allure测试报告】启动浏览器去查看allure测试报告，使用  allure serve ./reports
7、【选择哪些用例去执行】运行哪些测试用例，冒烟?回归？还是所有用例？在pytest.ini文件中修改addopts中的-m参数，-m "smoke" 即为冒烟！

# 参与贡献
后续可以进行对本仓库的贡献，不过现在暂时未开放全面的贡献机制
1.  Fork 本仓库
2.  新建 Feat_xxx 分支
3.  提交代码
4.  新建 Pull Request

# 捐赠小北喝瓶水 :sunglasses: 
![输入图片说明](screenshots/%E6%94%AF%E4%BB%98%E5%AE%9D%E6%94%AF%E4%BB%98%E7%A0%81.jpg)
![输入图片说明](%E5%BE%AE%E4%BF%A1%E6%94%AF%E4%BB%98%E7%A0%81.jpg)
