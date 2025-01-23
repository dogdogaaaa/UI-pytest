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
        颜色识别库
        opencv-python

# 软件架构
selenium+pytest+allure+各种工具函数

# 高级UI自动化框架亮点 ：
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
        1、第一步先安装对应的库，只需要一键运行  pip3 install -r requirement.txt 即可安全所有依赖库 【注意网络不好容易报错，报错之后重新安装即可】
        2、第二步再下载对应的webdriver浏览器驱动： https://registry.npmmirror.com/binary.html?path=chromedriver/
        3、再配置浏览器驱动解压文件夹的环境变量
        4、【运行测试用例】这里是列表文本pycharm中运行项目即可，或者项目目录下命令行输入pytest即可运行
        5、【运行含有allure测试报告的测试用例】使用pytest运行allure测试报告，只需要使用pytest即可，因为pytest.ini文件中已经配置好了allure的配置参数
        6、【查看allure测试报告】启动浏览器去查看allure测试报告，使用  allure serve ./reports
        7、【选择哪些用例去执行】运行哪些测试用例，冒烟?回归？还是所有用例？在pytest.ini文件中修改addopts中的-m参数，-m "smoke" 即为冒烟！
