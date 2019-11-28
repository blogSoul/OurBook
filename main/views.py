from django.shortcuts import render
import urllib.request
import json

def home(request):

    if request.method == 'POST':
        
        keyword = request.POST['search'] 
        
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

            json_rt = response_body.decode('utf-8')
            final_res = json.loads(json_rt)
            return render(request, 'books.html', {'final_res':final_res})
        
        else:
            # print("Error Code:" + rescode)
            final_res = rescode

        final_res = final_res.decode('utf-8')

    return render(request, 'main.html')

def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')
