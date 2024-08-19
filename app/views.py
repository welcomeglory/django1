# app/views.py
from django.shortcuts import render, redirect
from .models import Contact,Member,Login

def contact_view(request):
   if request.method == 'POST':
       name = request.POST.get('name')
       email = request.POST.get('email')
       message = request.POST.get('message')

       # 데이터베이스에 저장
       Contact.objects.create(name=name, email=email, message=message)

       # 메시지 저장 후 리다이렉트 (또는 감사 페이지로 이동)
       return redirect('thanks')  # 'thanks'는 감사 페이지로 가는 URL 패턴 이름

   return render(request, 'contact.html')

def thanks_view(request):
   return render(request, 'thanks.html')

def main_view(request):
   return render(request, 'main.html')

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        Login.objects.create(username=username, password=password)
        return redirect('thanks')  # 'thanks'는 감사 페이지로 가는 URL 패턴 이름
    return render(request, 'login.html')

def member_view(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        gender = request.POST.get('gender')
        address = request.POST.get('address')

        Member.objects.create(name=name, email=email, phone=phone, gender=gender,address=address)
        return redirect('thanks')  # 'thanks'는 감사 페이지로 가는 URL 패턴 이름

    return render(request, 'member.html')

def member_list(request):
    members = Member.objects.all()  # 모든 Member 데이터를 가져오기
    return render(request, 'member_list.html', {'members': members})
