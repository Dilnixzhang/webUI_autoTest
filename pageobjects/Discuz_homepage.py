import time
from  pageobjects.base import BasePage
from selenium.webdriver.common.by import By
from framework.logger import Logger

#定义homepage类 调用getlog（）
logger = Logger(logger="BasePage").getlog()
class HomePage(BasePage):
    #用户登录
    home_page_input_login_loc = (By.NAME,'username')
    home_page_input_psw_loc = (By.NAME,'password')
    home_page_button_login_loc = (By.CSS_SELECTOR,'.fastlg em')
    #进入默认版块
    home_page_section_loc = (By.CSS_SELECTOR,'.bm_c h2 a')
    send_page_title_input_loc = (By.CSS_SELECTOR,'.bm_c .px')
    send_page_msg_input_loc = (By.CSS_SELECTOR,'.tedt .pt')
    send_page_button_loc = (By.CSS_SELECTOR,'.bm_c button')
    #回复帖子
    reply_page_input_loc = (By.CSS_SELECTOR,'.plc textarea')
    reply_page_button_loc = (By.ID,'fastpostsubmit')
    #删除帖子
    admin_page_del_loc = (By.XPATH,"//th/a[2]")
    admin_page_del_button_loc = (By.LINK_TEXT,'删除主题')
    admin_page_del_submit_loc = (By.XPATH,'//p/button[@name=\'modsubmit\']')
    #进入管理中心
    admin_page_center_loc = (By.LINK_TEXT,'管理中心')
    # driver.switch_to.window(driver.window_handles[0])

    #登录管理中心
    # admin_page_center_lginput_loc = (By.NAME,'admin_password')
    admin_page_center_lginput_loc = (By.CSS_SELECTOR,'.loginform input')
    # admin_page_center_lginsb_loc = (By.CSS_SELECTOR, '.loginnoflaot input')
    admin_page_center_lginsb_loc = (By.CSS_SELECTOR,'#loginform > p.loginnofloat > input')

    #创建新版块 论坛 创建
    add_forum_loc = (By.XPATH,'//ul/li[7]/em/a')
    # add_forum_loc = (By.ID,'#header_forum')
    add_new_section_loc = (By.CSS_SELECTOR,'.lastboard a')
    #添加版块名字
    add_new_section_input_loc = (By.NAME,'newforum[1][]')
    add_new_section_sbm_loc = (By.CSS_SELECTOR,'.fixsel input')
    #进入新版块
    home_page_index_loc = (By.CSS_SELECTOR,'.nvhm')
    #pt > div:nth-child(1) > a.nvhm
    home_page_new_section_loc = (By.CSS_SELECTOR,'tr:nth-last-child(2) h2 a')
    #category_1 > table > tbody > tr:nth-child(7) > td:nth-child(2) > h2 > a
    # category_1 > table > tbody > tr:nth-child(4) > td:nth-child(2) > h2 > a
    #搜索帖子
    search_input_loc = (By.NAME,'srchtxt')
    search_button_loc = (By.CSS_SELECTOR,'.scbar_btn_td button')
    search_haotest_loc= (By.CSS_SELECTOR,'.pbw h3 a')

    #发起投票
    send_vote_fatie_loc = (By.CSS_SELECTOR,'#newspecial > img ')
    send_vote_faqi_loc = (By.CSS_SELECTOR,'#editorbox > ul > li:nth-child(2) > a')
    # send_vote_btn_loc = (By.CSS_SELECTOR,'.poll a')
    send_vote_title_input_loc = (By.NAME,'subject')
    send_vote_select1_loc = (By.CSS_SELECTOR,'#pollm_c_1 > p:nth-child(1) > input')
    send_vote_select2_loc = (By.CSS_SELECTOR,'#pollm_c_1 > p:nth-child(2) > input')
    send_vote_select3_loc = (By.CSS_SELECTOR, '#pollm_c_1 > p:nth-child(3) > input')
    # send_vote_describe_input_loc = (By.CSS_SELECTOR,'body')
    send_vote_sbm_btn_loc = (By.CSS_SELECTOR,'#postsubmit')
    #topicsubmit
    #进行投票
    send_vote_select1_input_loc = (By.CSS_SELECTOR,'#option_1')
    send_vote_select2_input_loc = (By.CSS_SELECTOR, '#option_2')
    send_vote_select3_input_loc = (By.CSS_SELECTOR, '#option_3')
    send_vote_select_submit_loc = (By.CSS_SELECTOR, '#pollsubmit')

    #获得投票的选项名称和比例
    get_vote_title_loc = (By.CSS_SELECTOR,'#thread_subject')
    get_vote_select1_loc = (By.CSS_SELECTOR,'#poll > div.pcht > table > tbody > tr:nth-child(1) > td.pvt > label')#.pvt label
    get_vote_percent1_loc = (By.CSS_SELECTOR,'#poll > div.pcht > table > tbody > tr:nth-child(2) > td:nth-child(2)')
    get_vote_select2_loc = (By.CSS_SELECTOR,'#poll > div.pcht > table > tbody > tr:nth-child(3) > td.pvt > label')
    get_vote_percent2_loc = (By.CSS_SELECTOR, '#poll > div.pcht > table > tbody > tr:nth-child(4) > td:nth-child(2)')
    get_vote_select3_loc = (By.CSS_SELECTOR, '#poll > div.pcht > table > tbody > tr:nth-child(5) > td.pvt > label')
    get_vote_percent3_loc = (By.CSS_SELECTOR, '#poll > div.pcht > table > tbody > tr:nth-child(6) > td:nth-child(2)')
    #退出
    send_page_logout_loc = (By.PARTIAL_LINK_TEXT, '退出')

    #登录
    def login(self,username,password):
        # try:
            self.sendkeys(username,*self.home_page_input_login_loc)
            self.sendkeys(password,*self.home_page_input_psw_loc)
            self.click(*self.home_page_button_login_loc)
            time.sleep(5)
        #     logger.info("登陆成功")
        # except Exception as e:
        #     logger.error("登录失败")



    #默认板块发帖
    def posting(self,title,msg):
        self.click(*self.home_page_section_loc)
        self.sendkeys(title,*self.send_page_title_input_loc)
        self.sendkeys(msg,*self.send_page_msg_input_loc)
        self.click(*self.send_page_button_loc)
        time.sleep(10)

    #新版块发帖
    def newposting(self,title,msg):
        self.click(*self.home_page_index_loc)
        self.click(*self.home_page_new_section_loc)
        self.sendkeys(title, *self.send_page_title_input_loc)
        self.sendkeys(msg, *self.send_page_msg_input_loc)
        self.click(*self.send_page_button_loc)
        time.sleep(10)

    #回帖
    def reply(self,message):
        self.sendkeys(message,*self.reply_page_input_loc)
        self.click(*self.reply_page_button_loc)
        time.sleep(5)

    #管理员删除帖子
    def delete_msg(self):
        #进入默认板块
        self.click(*self.home_page_section_loc)
        #选中主题
        self.click(*self.admin_page_del_loc)
        #删除主题
        self.click(*self.admin_page_del_button_loc)
        #确定删除主题
        self.click(*self.admin_page_del_submit_loc)
        time.sleep(5)

    #添加新版块
    def add_new_section(self,pwd,content):
        self.click(*self.admin_page_center_loc)
        time.sleep(5)
        #跳转 登录管理中心
        self.driver.switch_to.window(self.driver.window_handles[1])
        self.sendkeys(pwd,*self.admin_page_center_lginput_loc)
        self.click(*self.admin_page_center_lginsb_loc)
        time.sleep(5)
        # #需要跳转，添加新版块
        self.driver.switch_to.window(self.driver.current_window_handle)
        # self.driver.switch_to.window(self.driver.window_handles[1])
        self.click(*self.add_forum_loc)
        time.sleep(5)
        self.driver.switch_to.frame(0)

        self.click(*self.add_new_section_loc)
        self.sendkeys(content,*self.add_new_section_input_loc)
        self.click(*self.add_new_section_sbm_loc)

    #搜索haotest帖子
    def search(self,content):
        self.sendkeys(content,*self.search_input_loc)
        self.click(*self.search_button_loc)
        time.sleep(3)
        #跳转新窗口
        self.driver.switch_to.window(self.driver.window_handles[1])
        time.sleep(3)
        self.click(*self.search_haotest_loc)
        self.driver.switch_to.window(self.driver.window_handles[2])
        time.sleep(3)

     #发起投票
    def send_vote(self,title,select1,select2,select3):
        #进入默认板块
        self.click(*self.home_page_section_loc)
        #进入新版块
        # self.click(*self.home_page_new_section_loc)
        #发起投票
        self.click(*self.send_vote_fatie_loc)
        self.click(*self.send_vote_faqi_loc)
        # self.click(*self.send_vote_btn_loc)
        #填写投票标题、选项、描述
        self.sendkeys(title,*self.send_vote_title_input_loc)
        # self.driver.switch_to.frame(0)
        self.sendkeys(select1,*self.send_vote_select1_loc)
        self.sendkeys(select2,*self.send_vote_select2_loc)
        self.sendkeys(select3, *self.send_vote_select3_loc)
        # self.sendkeys(describe,*self.send_vote_describe_input_loc)
        self.click(*self.send_vote_sbm_btn_loc)
        time.sleep(3)

    #进行投票
    def send_vote_submit(self):
        # self.click(*self.send_vote_select1_input_loc)
        # self.click(*self.send_vote_select2_input_loc)
        self.click(*self.send_vote_select3_input_loc)
        self.click(*self.send_vote_select_submit_loc)
        print("投票成功")

    #获得选项和比例
    def get_vote(self):
        title = self.get_text(*self.get_vote_title_loc)
        print("主题：",title)
        select1 = self.get_text(*self.get_vote_select1_loc)
        persent1 = self.get_text(*self.get_vote_percent1_loc)
        print("选项：",select1,"比例：",persent1)
        select2 = self.get_text(*self.get_vote_select2_loc)
        persent2 = self.get_text(*self.get_vote_percent2_loc)
        print("选项：", select2, "比例：", persent2)
        select3 = self.get_text(*self.get_vote_select3_loc)
        persent3 = self.get_text(*self.get_vote_percent3_loc)
        print("选项：", select3, "比例：", persent3)
        time.sleep(5)

     #退出
    def logout(self):
        self.click(*self.send_page_logout_loc)