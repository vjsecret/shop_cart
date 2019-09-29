from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse, Http404
from django import template
from django.contrib import auth
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.urls import reverse
from django.contrib.auth.forms import UserCreationForm
from func1.models import Topic, Entry
from func1.forms import TopicForm,EntryForm
import pymysql
import datetime
import json
from django.views.decorators.csrf import csrf_exempt

def addCar(request):
    if request.method == 'POST':
        print("==========fred: showinfo post=============")
        db = pymysql.connect(host="localhost", user="test1", password="123", db="item")
        # if str== "comic":
        #     db = pymysql.connect(host="localhost", user="test1", password="123", db=attr)
        # else:
        #     db = pymysql.connect(host="localhost", user="test1", password="123", db="comic")
        cursor = db.cursor()
        # 按字典返回 
        # cursor = db.cursor(pymysql.cursors.DictCursor)
        
        print(request.path)
        print(request.path_info)
        print(request.content_params)
        print(request.scheme)
        # listA=request.content_params
        # for ix in range(0,len(listA)):
        #     print(listA[ix])
        print(request.POST)
        var1 = request.POST.getlist('title', '')
        print(var1)
        var2 = request.POST.getlist('price', '')
        print(var2)
        print(type(var2))
        print(var2[0])
        #result = str(result_list)

        cursor.execute("DROP TABLE IF EXISTS listi")
        sql = """CREATE TABLE `listi` (
        `id` int(10) DEFAULT NULL,
        `title` char(20) NOT NULL,
        `price` int(10) DEFAULT NULL
        )"""
        cursor.execute(sql)
        #print("Created table Successfull.")
        # cursor.execute("DROP TABLE IF EXISTS idlisti")
        # sql = """CREATE TABLE `idlisti` (
        # `id` int(10) DEFAULT NULL
        # )"""
        # cursor.execute(sql)
        # cursor.execute("DROP TABLE IF EXISTS titlelisti")
        # sql = """CREATE TABLE `titlelisti` (
        # `title` char(20) NOT NULL
        # )"""
        # cursor.execute(sql)
        # cursor.execute("DROP TABLE IF EXISTS pricelisti")
        # sql = """CREATE TABLE `pricelisti` (
        # `price` int(10) DEFAULT NULL
        # )"""
        # cursor.execute(sql)
        
        listAS=[]
        #list=[1, str(var1), int(var2[0])]
        listAS.append(2)
        listAS.append(str(var1[0]))
        listAS.append(int(var2[0]))
        print(type(int(var2[0])))

        a=3
        #sql = "INSERT INTO listi(ID,TITLE,PRICE) VALUES (1,'"+ listAS[1] +"',' + listAS[2] +')"
        sql = "INSERT INTO listi(ID,TITLE,PRICE) VALUES ( '"+str(listAS[0])+"','" + listAS[1] + "','" + var2[0] + "')"
        #sql = """INSERT INTO listi(ID, TITLE,PRICE) VALUES (1, '酒菜',130)""" 
        try:
            cursor.execute(sql)
            db.commit()
            print("add success")
        except:
            print("add fail")
            db.rollback()
        db.close()

        a = {}
        a["result"] = "post_success"
        #return HttpResponse(json.dumps(a), content_type='application/json')
        return HttpResponseRedirect(reverse('showinfo'))
        #return render(request,'showinfo.html',locals())
@csrf_exempt
def carAjax(request):
    # is_ajax = False
    # if request.is_ajax():
    #     is_ajax = True
    # name_dict = {'twz': 'python and Django',
    #              'abc': 'teach Django', 
    #              'is_ajax': is_ajax}
    # return JsonResponse(name_dict)
    if request.method == 'POST':
        a = {}
        a["result"] = "post_success"
        return HttpResponse(json.dumps(a), content_type='application/json')

def selecAttr(str):
    Now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    #str(Now)
    if str== "comic":
        food1 = { 'id':1,'title':'漫畫一', 'photoid':3, 'content':'漫畫一好吃'}
        food2 = { 'id':2,'title':'漫畫一蒜泥白肉', 'photoid':4, 'content':'漫畫一人氣推薦'}
        return [food1,food2]
    if str== "article":
        food1 = { 'id':1,'title':'文章一', 'photoid':3, 'content':'文章一好吃'}
        food2 = { 'id':2,'title':'文章一蒜泥白肉', 'photoid':4, 'content':'文章一人氣推薦'}
        return [food1,food2]    

def getlist(str, cursor):
    #print(str)
    if str== "comic":
        # Prepare SQL query to select a record from the table.
        sql = "SELECT * FROM CLIST"
        #\
        #    WHERE INCOME > %d" % (1000)
        #print (sql)
        try:
            # Execute the SQL command
            cursor.execute(sql)
            # Fetch all the rows in a list of lists.
            results = cursor.fetchall()
            data={}
            list=[]
            for row in results:
                #print (row)
                id = row[0]
                title = row[1]
                content = row[2]
                photoid = row[3]
                # Now print fetched result
                #print ("id = %s, title = %s, content = %s, photoid = %s" % (id, title, content, photoid ))
                #data.update({"id":row[0], "title":row[1], "content":row[2], "photoid":row[3]})
                #data.setdefault(zip(['id', 'title', 'content', 'photoid'], row))
                data={"id":row[0], "title":row[1], "content":row[2], "photoid":row[3]}
                list.append(data)
            # print(data)
            # print(list)
            return list
        except:
            import traceback
            traceback.print_exc()
            print ("Error: unable to fetch data")
    if str== "article":
        sql = "SELECT * FROM ALIST"
        #\
        #    WHERE INCOME > %d" % (1000)
        #print (sql)
        try:
            # Execute the SQL command
            cursor.execute(sql)
            # Fetch all the rows in a list of lists.
            results = cursor.fetchall()
            data={}
            list=[]
            for row in results:
                #print (row)
                id = row[0]
                title = row[1]
                photoid = row[2]
                price = row[3]
                # Now print fetched result
                #print ("id = %s, title = %s, photoid = %d, price = %d" % (id, title, photoid, price ))
                data={"id":row[0], "title":row[1], "photoid":row[2], "price":row[3]}
                list.append(data)
            return list
        except:
            import traceback
            traceback.print_exc()
            print ("Error: unable to fetch data")
    if str== "store":
        try:
            food1 = { 'id':1,'title':'文章一', 'photoid':3, 'content':'文章一好吃'}
            food2 = { 'id':2,'title':'文章一蒜泥白肉', 'photoid':4, 'content':'文章一人氣推薦'}
            return [food1,food2]
        except:
            import traceback
            traceback.print_exc()
            print ("Error: unable to fetch data")

def index(request):
    return render(request,'index.html')

# def login(request):
#    return render(request,'login.html')
def logout_view(request):
    logout(request)
    #return redirect(request,'index.html')
    #return HttpResponse(reverse('index'))
    return render(request,'index.html')

def register(request):
    """Register a new user."""
    if request.method != 'POST':
        form = UserCreationForm()
    else:
        form = UserCreationForm(data=request.POST)
        if form.is_valid():
            new_user = form.save()
            authenticated_user = auth.authenticate(username=new_user.username, password=request.POST['password1'])
            # auth.login(request, authenticated_user) #進行登入
            #return HttpResponseRedirect(reverse('learning_logs:index'))
            return render(request,'index.html')

    context = {'form': form}
    return render(request, 'register.html', context)
#@csrf_exempt
def showinfo(request, attr):
    db = pymysql.connect(host="localhost", user="test1", password="123", db=attr)
    # if str== "comic":
    #     db = pymysql.connect(host="localhost", user="test1", password="123", db=attr)
    # else:
    #     db = pymysql.connect(host="localhost", user="test1", password="123", db="comic")
    cursor = db.cursor()
    # 按字典返回 
    # cursor = db.cursor(pymysql.cursors.DictCursor)
    list=getlist(attr, cursor)

    db.close()
    if request.method == 'POST':
        print("==========fred: showinfo post=============")
        print(request.path)
        print(request.path_info)
        print(request.content_params)
        print(request.POST)
        result_list = request.POST.getlist('price', '')
        print(result_list)
        result = str(result_list)
        var1 = request.POST.getlist('title', '')
        print(var1)
        var2 = request.POST.getlist('price', '')
        print(var2)
        print(type(var2))
        print(var2[0])
        

        # form = TopicForm(request.POST)
        # if form.is_valid():
        #     new_topic = form.save(commit=False) # 新增區塊
        #     new_topic.owner = request.user # 新增區塊
        #     new_topic.save() # 新增區塊
        # context = {'form': form}
        #return JsonResponse(list)
        alist = {'title': var1[0], 'price': var2[0]}
        #return HttpResponse(json.dumps(alist), content_type='application/json')
        return render(request,'showinfo.html',locals())
    #if request.method!="POST":
    else:
        print("==========fred: showinfo get=============")
        form = TopicForm()
        if attr== "article":
            return render(request,'article.html',locals())
        elif attr== "comic":
            return render(request,'comic.html',locals())
        elif attr== "store":
            return render(request,'showinfo.html',locals())
        else:
            return render(request,'showinfo.html',locals())

@login_required
def car(request):
    print("==========fred=============")
    print(request)
    #print(request.headers)
    COOKIES=request.COOKIES
    get_host=request.get_host
    owner=request.user
    scheme=request.scheme
    method=request.method
    post=request.POST
    path=request.path
    path_info=request.path_info
    topics = Topic.objects.filter(owner=request.user).order_by('date_added')
    context = {'topics': topics}
    return render(request,'car.html',locals())

@login_required
def manager(request,attr):
    if attr== "mycrud":
        return render(request,'mycrud.html')
    elif attr== "order":
        topics = Topic.objects.filter(owner=request.user).order_by('date_added')
        context = {'topics': topics}
        return render(request,'order.html',locals())
    elif attr== "info":
        return render(request,'person.html')
    else:
        return render(request,'member.html')

# def member(request):
#     return render(request,'member.html')
@login_required
def member(request,attr):
    if attr== "manager":
        return render(request,'manager.html')
    return render(request,'member.html')

def comic(request):
    list = selecAttr("comic")
    # food1 = { 'id':1,'title':'漫畫一', 'photoid':3, 'content':'好吃'}
    # food2 = { 'id':2,'title':'蒜泥白肉', 'photoid':4, 'content':'人氣推薦'}
    # comiclist = [food1,food2]
    return render(request,'comic.html',locals())

# def comic(request, data):
#     print(data)
#     print(type(data))
#     #list = selecAttr(attr)
#     # food1 = { 'id':1,'title':'漫畫一', 'photoid':3, 'content':'好吃'}
#     # food2 = { 'id':2,'title':'蒜泥白肉', 'photoid':4, 'content':'人氣推薦'}
#     # comiclist = [food1,food2]
#     # return redirect
#     return render(request,'comic.html',{'abc': "Hello Django "},{locals() } )

def article(request):
    list = selecAttr("article")
    return render(request,'article.html',locals())
#============================owner model==========================
# 顯示所有主題
@login_required
def topics(request):
    print(request.user)
    topics = Topic.objects.filter(owner=request.user).order_by('date_added') #讓 Django 只從資料庫中獲取 owner 屬性為當前使用者的 Topic 物件 #topics = Topic.objects.order_by('date_added')
    context = {'topics': topics}
    return render(request, 'topics.html', locals())

# 顯示個別主題和它的entries
@login_required
def topic(request, topic_id):
    topic = Topic.objects.get(id=topic_id)
    if topic.owner != request.user: # 請求主題與現在使用者不符合
        raise Http404
    entries = topic.entry_set.order_by('-date_added')
    context = {'topic': topic, 'entries': entries}
    return render(request, 'topic.html', locals())

@login_required
def new_topic(request):
    #print(request.user)
    if request.method != 'POST':
        form = TopicForm()
    else:
        #if request.user!="NULL":
        form = TopicForm(request.POST)
        if form.is_valid():
            new_topic = form.save(commit=False)
            new_topic.owner = request.user #必須判斷不是匿名才能save
            new_topic.save()
            return HttpResponseRedirect(reverse('topics'))

    context = {'form': form}
    print(context)
    return render(request, 'new_topic.html', locals())

def new_entry(request, topic_id):
    #topics = Topic.objects.order_by('date_added')    
    #print(topics.id)
    topic = Topic.objects.get(id=topic_id) # 使用topic_id來取得正確主題物件
    #entries = topic.entry_set.order_by('-date_added') #新增:topic底下的entry number+1
    # print(topic)
    # print(topic_id)
    # print(entries)
    
    if request.method != 'POST':
        form = EntryForm()        
    else:
        form = EntryForm(data=request.POST)
        if form.is_valid():
            new_entry = form.save(commit=False)
            #print(new_entry)
            new_entry.topic = topic
            #print(new_entry.topic)
            new_entry.save()
            return HttpResponseRedirect(reverse('topic',args=[topic_id]))
    
    context = {'topic': topic, 'form': form}
    print(context)
    return render(request, 'new_entry.html', locals())

@login_required
def edit_entry(request, entry_id):
    entry = Entry.objects.get(id=entry_id)
    topic = entry.topic
    # print(entry)
    # print(topic)
    # print(topic.id) #編輯完要回到topic頁，所以需要topic id

    if topic.owner != request.user: #@login_required
        raise Http404
    if request.method != 'POST':
        form = EntryForm(instance=entry)
    else:
        form = EntryForm(instance=entry, data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('topic',args=[topic.id]))
        
    context = {'entry': entry, 'topic': topic, 'form': form}
    print(context)
    return render(request, 'edit_entry.html', locals())