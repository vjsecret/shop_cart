目的是想證明有能力使用django、python coding與資料庫基本概念，由於時間有限的考量，先跳過寫測試程式  

參考http://dokelung-blog.logdown.com/posts/235592-django-notes-table-of-contents 後，建立簡單的購物車  

練習主題:  
FrontEnd: 展示會使用bootstrap、輪播功能  
了解RESTful API  
了解Entity-relationship model  
RDB基本概念:正規劃、多對多、一對多、一對一  
使用ajax  

django:  
1	建置與環境設定  
2	視圖與URL  
3	模板初探  
4	模板的變量與標籤  
5	模型與資料庫  
6	後台管理系統admin  
7	使用者互動與表單  
8	表單的驗證與模型化  
9	Cookies與Sessions  
10	用戶的登入與登出  
11	權限與註冊  

endpoint:  
path('index', LoginView.as_view(template_name='index.html'), name="index"),  
path('login', LoginView.as_view(template_name='login.html'), name="login"),  
path('logout/', views.logout_view, name='logout'),  
path('register/', views.register, name='register'),  
path('showinfo/<attr>/', views.showinfo),  
path('car', views.car),  
path('comic', views.comic),  
path('article', views.article),  
path('member/<attr>/', views.member),  
path('member/manager/<attr>/', views.manager),  
path('topic/<int:topic_id>/',views.topic,name='topic'), #path('<int:topic_id>/',views.topic,name='topic'),  
path('new_topic/',views.new_topic,name='new_topic'),  
path('new_entry/<int:topic_id>/',views.new_entry,name='new_entry'),  
path('edit_entry/<int:entry_id>/', views.edit_entry, name='edit_entry'),

網站規劃:
menu: comic， article， store，序號兌換，我的最愛(comic， article，商品)，搜尋功能 (1)每一頁的首頁顯示排行榜；顯示所有商品小圖示，預設以XXX分類排序；搜尋功能 (2)可以選擇依分類排序:熱門、.... (3)點圖示可進去詳細介紹頁面，(顯示集數:for comic, article使用；未購買圖片下面顯示加入購物車；購買完圖示下面顯示瀏覽:導至每集的sub) 在每一集被使用者點擊時記錄點擊次數(一個ip只能點一次)=>排行榜使用 記錄每個使用者對每一集的點擊總次數 (4)點store圖示可進去列出店家販賣商品:顯示所有商品小圖示，預設以熱門商品排序，可以選擇依分類排序

後台: (1)如果身分為superuser:則多了會員管理 (2)會員中心: 文章分類管理(新增、修改分類)、文章管理(新增、修改內容、...) comic分類管理(新增、修改分類)、comic管理(新增、修改內容、...) 商品圖片上傳、內容修改 遊戲區:會員等級達成則顯示可玩(有次數限制)，否則顯示灰 紅利點數區:顯示目前擁有紅利 消費紀錄 序號兌換紀錄 訂單管理
