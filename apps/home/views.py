# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django import template
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.template import loader, TemplateDoesNotExist
from django.urls import reverse
from django.contrib.auth.models import User
from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from apps.home.models import Quiz, Kelas, Evaluasi
from .forms import EvaluasiForm
import json


# @login_required(login_url="/login/")
def index(request):
    context = {'segment': 'index'}

    html_template = loader.get_template('home/index.html')
    return HttpResponse(html_template.render(context, request))


def pages(request):
    context = {}
    try:
        load_template = request.path.split('/')[-1]

        if load_template == 'admin':
            return HttpResponseRedirect(reverse('admin:index'))
        
        
        if load_template == 'computational-thinking.html':
            form = EvaluasiForm()
            return render(request, 'home/computational-thinking.html', {'form': form})
        
        context['segment'] = load_template

        if load_template == 'dashboard.html':
            return login_required(login_url="/login/")(dashboard_view)(request, context)
        elif load_template == 'user.html':
            return user_view(request, context)
        else:
            html_template = loader.get_template('home/' + load_template)
            return HttpResponse(html_template.render(context, request))

    except TemplateDoesNotExist:
        html_template = loader.get_template('home/page-404.html')
        return HttpResponse(html_template.render(context, request))

    except:
        html_template = loader.get_template('home/page-500.html')
        return HttpResponse(html_template.render(context, request))

@login_required(login_url="/login/")
def dashboard_view(request, context):
    html_template = loader.get_template('home/dashboard.html')
    return HttpResponse(html_template.render(context, request))

def user_view(request, context):
    html_template = loader.get_template('home/user.html')
    users = User.objects.all()
    context = {'users': users}
    return HttpResponse(html_template.render(context, request))

def get_user_data_view(request, user_id):
    try:
        user = User.objects.get(id=user_id)
        user_data = {
            'id': user.id,
            'username': user.username,
            'first_name': user.first_name,
            'last_name': user.last_name,
            'email': user.email,
            'is_staff': user.is_staff,
        }
        return JsonResponse(user_data)
    except User.DoesNotExist:
        return JsonResponse({'error': 'User not found'}, status=404)

def delete_user(request, user_id):
    user = get_object_or_404(User, id=user_id)
    user.delete()
    return user_view(request, {})

#EVALLL
@csrf_exempt
def eval_submission(request):
    if request.method == 'POST':
        # Mengonversi data JSON yang diterima dari JavaScript menjadi dictionary
        data = json.loads(request.body)
        
        # Di sini Anda dapat melakukan apa pun dengan data yang diterima
        # Misalnya, menyimpan data ke dalam database atau melakukan pengolahan lainnya
        
        # Contoh: mencetak data yang diterima ke log
        print(data)
        
        save_eval_data(data)
        
        # Mengirim respons ke JavaScript
        response_data = {'message': 'Data evaluasi berhasil diterima.'}
        return JsonResponse(response_data)
    else:
        # Jika permintaan bukan metode POST, kembalikan respons dengan kode status 405 (Method Not Allowed)
        return JsonResponse({'error': 'Metode yang diperbolehkan adalah POST.'}, status=405)
    
def save_eval_data(jawaban):
    try:
        grup_instance = Kelas.objects.get(id=jawaban['kelas'])
        print("ADA")
    except Kelas.DoesNotExist:
        return {"error": "Grup with the provided ID does not exist."}
    
    evaluasi = Evaluasi.objects.create(
        nama=jawaban['nama'],
        grup=grup_instance,
        jawaban1=jawaban['jawaban1'],
        skor1=0,
        jawaban2=jawaban['jawaban2'],
        skor2=0,
        jawaban3=jawaban['jawaban3'],
        skor3=0,
        jawaban4=jawaban['jawaban4'],
        skor4=0,
        jawaban5=jawaban['jawaban5'],
        skor5=0,
        jawaban6=jawaban['jawaban6'],
        skor6=0,
    )

    
    print(jawaban)
    print("NGENS")


#QUISS
@csrf_exempt
def quiz_submission(request):
    if request.method == 'POST':
        # Mengonversi data JSON yang diterima dari JavaScript menjadi dictionary
        data = json.loads(request.body)
        
        # Di sini Anda dapat melakukan apa pun dengan data yang diterima
        # Misalnya, menyimpan data ke dalam database atau melakukan pengolahan lainnya
        
        # Contoh: mencetak data yang diterima ke log
        print(data)
        
        correction(data)
        
        # Mengirim respons ke JavaScript
        response_data = {'message': 'Data berhasil diterima.'}
        return JsonResponse(response_data)
    else:
        # Jika permintaan bukan metode POST, kembalikan respons dengan kode status 405 (Method Not Allowed)
        return JsonResponse({'error': 'Metode yang diperbolehkan adalah POST.'}, status=405)
    
    
def correction(jawaban):
    kunci = {
    "Jawaban Soal 1": "option1",
    "Jawaban Soal 2": "option2",
    "Jawaban Soal 3": "option2",
    "Jawaban Soal 4": "option3",
    "Jawaban Soal 5": "option1"
    }
    
    skor = hitung_skor(kunci, jawaban)
    hasil = buat_hasil(jawaban, skor)
    
    print(hasil)
    
def hitung_skor(kunci, jawaban):
    skor = 0
    for key in kunci:
        if key in jawaban and jawaban[key] == kunci[key]:
            skor += 20
    return skor

def buat_hasil(jawaban, skor):
    # Find the Kelas instance by its primary key
    try:
        grup_instance = Kelas.objects.get(id=jawaban['Grup'])
    except Kelas.DoesNotExist:
        return {"error": "Grup with the provided ID does not exist."}
    
    hasil = {
        "Nama": jawaban['Nama'],
        "Grup": grup_instance.nama_kelas,
        "jawaban_soal_1": jawaban['Jawaban Soal 1'],
        "jawaban_soal_2": jawaban['Jawaban Soal 2'],
        "jawaban_soal_3": jawaban['Jawaban Soal 3'],
        "jawaban_soal_4": jawaban['Jawaban Soal 4'],
        "jawaban_soal_5": jawaban['Jawaban Soal 5'],
        "Skor": skor
    }
    
    quiz = Quiz.objects.create(
        nama=jawaban['Nama'],
        grup=grup_instance,
        jawaban_soal_1=jawaban['Jawaban Soal 1'],
        jawaban_soal_2=jawaban['Jawaban Soal 2'],
        jawaban_soal_3=jawaban['Jawaban Soal 3'],
        jawaban_soal_4=jawaban['Jawaban Soal 4'],
        jawaban_soal_5=jawaban['Jawaban Soal 5'],
        skor=skor 
    )

    return hasil

def kelas_list(request):
    # Ambil semua objek Kelas dari database
    kelas_objects = Kelas.objects.all()
    
    # Buat list yang berisi dictionary untuk setiap objek Kelas
    kelas_data = [{'id': kelas.id, 'nama_kelas': kelas.nama_kelas} for kelas in kelas_objects]
    
    # Kirim data dalam bentuk JSON sebagai respons
    return JsonResponse(kelas_data, safe=False)

from django.http import JsonResponse
from .models import Quiz

def quiz_list(request):
    # Ambil semua objek Quiz dari database
    quiz_objects = Quiz.objects.all()
    
    # Buat list yang berisi dictionary untuk setiap objek Quiz
    quiz_data = [
        {
            'id': quiz.id,
            'nama': quiz.nama,
            'grup': quiz.grup.nama_kelas,  # Mengambil nama_kelas dari objek Kelas
            'jawaban_soal_1': quiz.jawaban_soal_1,
            'jawaban_soal_2': quiz.jawaban_soal_2,
            'jawaban_soal_3': quiz.jawaban_soal_3,
            'jawaban_soal_4': quiz.jawaban_soal_4,
            'jawaban_soal_5': quiz.jawaban_soal_5,
            'skor': quiz.skor
        } 
        for quiz in quiz_objects
    ]
    
    # Kirim data dalam bentuk JSON sebagai respons
    return JsonResponse(quiz_data, safe=False)

def eval_list(request):
    # Ambil semua objek Quiz dari database
    eval_objects = Evaluasi.objects.all()
    
    # Buat list yang berisi dictionary untuk setiap objek Quiz
    eval_data = [
        {
            'id': data.id,
            'nama': data.nama,
            'kelas': data.grup.nama_kelas,  # Mengambil nama_kelas dari objek Kelas
            'jawaban1': data.jawaban1,
            'jawaban2': data.jawaban2,
            'jawaban3': data.jawaban3,
            'jawaban4': data.jawaban4,
            'jawaban5': data.jawaban5,
            'jawaban6': data.jawaban6,
        } 
        for data in eval_objects
    ]
    
    # Kirim data dalam bentuk JSON sebagai respons
    return JsonResponse(eval_data, safe=False)



    
# @login_required(login_url="/login/")
# def pages(request):
#     context = {}
#     # All resource paths end in .html.
#     # Pick out the html file name from the url. And load that template.
#     try:

#         load_template = request.path.split('/')[-1]

#         if load_template == 'admin':
#             return HttpResponseRedirect(reverse('admin:index'))
#         context['segment'] = load_template

#         html_template = loader.get_template('home/' + load_template)
#         return HttpResponse(html_template.render(context, request))

#     except template.TemplateDoesNotExist:

#         html_template = loader.get_template('home/page-404.html')
#         return HttpResponse(html_template.render(context, request))

#     except:
#         html_template = loader.get_template('home/page-500.html')
#         return HttpResponse(html_template.render(context, request))
