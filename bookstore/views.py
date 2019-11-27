from django.shortcuts import render
import urllib.request

def books(request):
    
    client_id = "CJNbcDFvgOnPbjtdXxA_"  # Client-Id
    client_secret = "6EdIJ7Pe2d"        # Client-Secret
    encText = urllib.parse.quote("파이썬")
    
    url = "https://openapi.naver.com/v1/search/book?query=" + encText +"&display=3&sort=count" # 우선은 3씩, 판매량 순
    request_content = urllib.request.Request(url)
    
    request_content.add_header("X-Naver-Client-Id", client_id)
    request_content.add_header("X-Naver-Client-Secret", client_secret)
    response = urllib.request.urlopen(request_content)
    rescode = response.getcode()
    
    if(rescode==200):
        response_body = response.read()
        # print(response_body.decode('utf-8'))
        final_res = response_body
    else:
        # print("Error Code:" + rescode)
        final_res = rescode

    return render(request, 'books.html', {'final_res':final_res})

def books_list(request):

    if request.method == 'POST':
        
        keyword = request.POST['book_search'] # form의 이름이 quote였으니까.
        
        client_id = "CJNbcDFvgOnPbjtdXxA_"  # Client-Id
        client_secret = "6EdIJ7Pe2d"        # Client-Secret
        encText = urllib.parse.quote(keyword)
        
        url = "https://openapi.naver.com/v1/search/book?query=" + encText +"&display=3&sort=count" # 우선은 3씩, 판매량 순
        request_content = urllib.request.Request(url)
        
        request_content.add_header("X-Naver-Client-Id", client_id)
        request_content.add_header("X-Naver-Client-Secret", client_secret)
        response = urllib.request.urlopen(request_content)
        rescode = response.getcode()
        
        if(rescode==200):
            response_body = response.read()
            # print(response_body.decode('utf-8'))
            final_res = response_body
        else:
            # print("Error Code:" + rescode)
            final_res = rescode

        return render(request, 'books.html', {'final_res':final_res})


    # 페이지로 들어온 경우
    else:
        return render(request, 'book_list.html', {}) 

    return render(request, 'book_list.html')