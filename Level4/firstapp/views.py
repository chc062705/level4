#-*- coding: UTF-8 -*-
from django.shortcuts import render
from firstapp.models import Article
import MySQLdb

# Create your views here.
def index(request):
    page, q = int(request.GET.get("page", 1)), request.GET.get("q", "")
    start, end = (page - 1) * 9, page * 9

    if q:
        articles = Article.objects.filter(author__username__contains=q)[start:end]
        print("sql:%s" %articles.query)
        print("gthsfsfssssssssdfdfdsf")
    else:
        articles = Article.objects.order_by('-creatime')[start:end]
        print("sql:%s" %articles.query)
        print("saaaaaaaaaaaaaaaa")

    context = {}
    context["articles"] = articles
    context["next_page"] = page + 1

    return render(request, 'index.html', context)


def new(request):
    page = int(request.GET.get("page", 1))
    start, end = (page - 1) * 9, page * 9


    conn=MySQLdb.connect(
        host='127.0.0.1',
        port=3306,
        user='root',
        passwd='admin123',
        db='level4',
        charset='utf8'
    )
    cursor=conn.cursor()
    cursor.execute("SELECT*FROM firstapp_article ORDER BY firstapp_article.creatime DESC  LIMIT 9  OFFSET "+ str(start) +" ")
    results=cursor.fetchall()
    articles= []
    for result in results:
        articles.append(
                {
                     'title':result[1],
                     'content':result[2],
                     'like_counts':result[3],
                     'score':result[4],
                     'creatime':result[5],
                     'img':result[7],
                }
        )

    print(results)
    print("qqqqqqqqqqqqqqqqq")
    page = int(request.GET.get("page", 1))
    start, end = (page - 1) * 9, page * 9



    context = {}
    context["articles"] = articles
    context["next_page"] = page + 1
    return render(request, 'new.html', context)


def editors(request):
    # 补充必要的代码，改写成SQL
    page = int(request.GET.get("page", 1))

    start, end = (page - 1) * 9, page * 9
    conn=MySQLdb.connect(
        host='127.0.0.1',
        port=3306,
        user='root',
        passwd='admin123',
        db='level4',
        charset='utf8'
    )
    cursor=conn.cursor()
    cursor.execute("SELECT*FROM firstapp_article WHERE firstapp_article.is_editor = TRUE ORDER BY firstapp_article.creatime DESC  LIMIT 9  OFFSET "+ str(start) +" ")
    results=cursor.fetchall()
    articles= []
    for result in results:
        articles.append(
                {
                     'title':result[1],
                     'content':result[2],
                     'like_counts':result[3],
                     'score':result[4],
                     'creatime':result[5],
                     'img':result[7],
                }
        )


    context = {}
    context["articles"] = articles
    context["next_page"] = page + 1
    return render(request, 'editors.html', context)
