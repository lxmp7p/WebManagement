from django.contrib import auth
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django import forms
from .models import Equipment


# Create your views here.
class AddEquip(forms.Form):
    id = forms.IntegerField(label='id')
    equip_name = forms.CharField(label='equip_name', max_length=150)
    serial_id = forms.CharField(label='serial_id', max_length=50)
    room = forms.CharField(label='room', max_length=50)


def index_page(request):
    if request.method == "POST":
        if request.POST['addnew'] == 'true':
            form = AddEquip(data={'id': request.POST['id'],
                                  'equip_name': request.POST['equip_name'],
                                  'serial_id': request.POST['serial_id'],
                                  'room': request.POST['room']})
            if form.is_valid():
                entry = Equipment(equip_name=form.cleaned_data['equip_name'],
                                  serial_id=form.cleaned_data['serial_id'],
                                  room=form.cleaned_data['room'])
                entry.save()
                return HttpResponseRedirect('/homepage/')

        elif request.POST['edit'] == 'true':
            form = AddEquip(data={'id': request.POST['id'],
                                  'equip_name': request.POST['equip_name'],
                                  'serial_id': request.POST['serial_id'],
                                  'room': request.POST['room']})
            if form.is_valid():
                editrow = Equipment.objects.get(id=form.cleaned_data['id'])
                editrow.room = form.cleaned_data['room']
                editrow.serial_id = form.cleaned_data['serial_id']
                editrow.equip_name = form.cleaned_data['equip_name']
                editrow.save()
                return HttpResponseRedirect('/homepage/')
        elif request.POST['delete'] == 'true':
            delrow = Equipment.objects.get(id=request.POST['id'])
            delrow.delete()
            return HttpResponseRedirect('/homepage/')

    equipment = Equipment.objects.all()
    return render(request, 'homepage/index.html',
                  {'username': auth.get_user(request).username, 'image': img, 'equipment': equipment})


def articles(request):
    return render(request, 'homepage/articles.html', {'username': auth.get_user(request).username})


img = {
       'mainbuilding': '<div id="sloi-1" style="display: block; background: rgba(0, 0, 0, 0) url(../static/img/map.png) '
                    'no-repeat scroll 0% 0% / 100%; width: 500px; height: 600px;"><svg id="svgmainid-sloi-1" '
                    'xmlns:svg="http://www.w3.org/2000/svg" xmlns="http://www.w3.org/2000/svg" width="500" '
                    'height="600" viewBox="0 0 500 600" preserveAspectRatio="xMinYMin meet" fixpropchecked="true"><a '
                    'href="#poligon" id="apoly-1" onclick="perehodKSloy(\'xoz\')"><polygon id="poly-1" points=" '
                    '168,367 160,384 168,388 174,372" fill="#d2d2d2" fillhover="#e5e5e5" stroke-width="1" '
                    'fill-rule="nonzero" fill-opacity="0.8" stroke-linecap="round" stroke-linejoin="round" '
                    'stroke="#333333"></polygon></a> <a href="#poligon" id="apoly-1"><polygon id="poly-1" points="" fill="#d2d2d2" fillhover="#e5e5e5" stroke-width="1" fill-rule="nonzero" fill-opacity="0.8" stroke-linecap="round" stroke-linejoin="round" stroke="#333333"></polygon></a><a href="#poligon" id="apoly-2"><polygon id="poly-2" points="" fill="#d2d2d2" fillhover="#e5e5e5" stroke-width="1" fill-rule="nonzero" fill-opacity="0.8" stroke-linecap="round" stroke-linejoin="round" stroke="#333333"></polygon></a><a href="#poligon" id="apoly-3"><polygon id="poly-3" points="" fill="#d2d2d2" fillhover="#e5e5e5" stroke-width="1" fill-rule="nonzero" fill-opacity="0.8" stroke-linecap="round" stroke-linejoin="round" stroke="#333333"></polygon></a><a href="#poligon" id="apoly-4" onclick="perehodKSloy(\'lab_1\')"><polygon id="poly-4" points=" 134,394 143,376 131,366 134,357 118,350 116,360 98,354 95,358 76,353 83,336 70,330 67,334 73,337 70,346 62,346 62,351 90,362 88,374 97,380 105,374 128,382 125,390" fill="#d2d2d2" fillhover="#e5e5e5" stroke-width="1" fill-rule="nonzero" fill-opacity="0.8" stroke-linecap="round" stroke-linejoin="round" stroke="#333333"></polygon></a><a href="#poligon" id="apoly-5"><polygon id="poly-5" points="" fill="#d2d2d2" fillhover="#e5e5e5" stroke-width="1" fill-rule="nonzero" fill-opacity="0.8" stroke-linecap="round" stroke-linejoin="round" stroke="#333333"></polygon></a></svg> </svg></div>',
    'xoz_1': '<div id="xoz_1"  style="display: none; background: rgba(0, 0, 0, 0) url(../static/img/f.png) no-repeat '
             'scroll 0% 0% / 100%; width: 500px; height: 500px;"><svg id="svgmainid-sloi-1" '
             'xmlns:svg="http://www.w3.org/2000/svg" xmlns="http://www.w3.org/2000/svg" width="500" height="500" '
             'viewBox="0 0 500 500" preserveAspectRatio="xMinYMin meet" fixpropchecked="true"><a href="#poligon" '
             'id="apoly-4" onclick=filter_table(\'1\')><polygon id="poly-4" points=" 74,41 69,125 213,125 209,'
             '42" fill="#d2d2d2" '
             'fillhover="#e5e5e5" stroke-width="1" fill-rule="nonzero" fill-opacity="0.8" stroke-linecap="round" '
             'stroke-linejoin="round" stroke="#333333"></polygon></a><a href="#poligon" id="apoly-8" '
             'onclick=filter_table(\'2\')><polygon '
             'id="poly-8" points=" 423,127 423,213 355,213 355,128" fill="#d2d2d2" fillhover="#e5e5e5" '
             'stroke-width="1" fill-rule="nonzero" fill-opacity="0.8" stroke-linecap="round" '
             'stroke-linejoin="round" stroke="#333333"></polygon></a><a href="#poligon" id="apoly-9" '
             'onclick=filter_table(\'3\')><polygon '
             'id="poly-9" points=" 228,148 174,148 174,211 228,210" fill="#d2d2d2" fillhover="#e5e5e5" '
             'stroke-width="1" fill-rule="nonzero" fill-opacity="0.8" stroke-linecap="round" '
             'stroke-linejoin="round" stroke="#333333"></polygon></a><a href="#poligon" id="apoly-10" '
             'onclick=filter_table(\'4\')><polygon '
             'id="poly-10" points=" 137,148 173,148 172,211 137,210" fill="#d2d2d2" fillhover="#e5e5e5" '
             'stroke-width="1" fill-rule="nonzero" fill-opacity="0.8" stroke-linecap="round" '
             'stroke-linejoin="round" stroke="#333333"></polygon></a><a href="#poligon" id="apoly-11" '
             'onclick=filter_table(\'5\')><polygon '
             'id="poly-11" points=" 73,128 73,209 135,211 137,129" fill="#d2d2d2" fillhover="#e5e5e5" '
             'stroke-width="1" fill-rule="nonzero" fill-opacity="0.8" stroke-linecap="round" '
             'stroke-linejoin="round" stroke="#333333"></polygon></a><a href="#poligon" id="apoly-12" '
             'onclick=filter_table(\'6\')><polygon '
             'id="poly-12" points=" 213,40 215,124 373,125 373,88 420,85 420,44" fill="#d2d2d2" '
             'fillhover="#e5e5e5" stroke-width="1" fill-rule="nonzero" fill-opacity="0.8" stroke-linecap="round" '
             'stroke-linejoin="round" stroke="#333333"></polygon></a><a href="#poligon" id="apoly-13" '
             'onclick=filter_table(\'7\')><polygon '
             'id="poly-13" points=" 375,88 375,124 420,124 420,90" fill="#d2d2d2" fillhover="#e5e5e5" '
             'stroke-width="1" fill-rule="nonzero" fill-opacity="0.8" stroke-linecap="round" '
             'stroke-linejoin="round" stroke="#333333"></polygon></a><a href="#poligon" id="apoly-14" '
             'onclick=filter_table(\'8\')><polygon '
             'id="poly-14" points=" 314,154 313,208 354,209 354,153" fill="#d2d2d2" fillhover="#e5e5e5" '
             'stroke-width="1" fill-rule="nonzero" fill-opacity="0.8" stroke-linecap="round" '
             'stroke-linejoin="round" stroke="#333333"></polygon></a><a href="#poligon" id="apoly-15" '
             'onclick=filter_table(\'9\')><polygon '
             'id="poly-15" points=" 270,146 270,209 313,209 313,148" fill="#d2d2d2" fillhover="#e5e5e5" '
             'stroke-width="1" fill-rule="nonzero" fill-opacity="0.8" stroke-linecap="round" '
             'stroke-linejoin="round" stroke="#333333"></polygon></a><a href="#poligon" id="apoly-16" '
             'onclick=filter_table(\'10\')><polygon '
             'id="poly-16" points=" 314,129 314,151 353,149 355,130" fill="#d2d2d2" fillhover="#e5e5e5" '
             'stroke-width="1" fill-rule="nonzero" fill-opacity="0.8" stroke-linecap="round" '
             'stroke-linejoin="round" stroke="#333333"></polygon></a><a href="#poligon" id="apoly-17" '
             'onclick=filter_table(\'11\')><polygon '
             'id="poly-17" points="" fill="#d2d2d2" fillhover="#e5e5e5" stroke-width="1" fill-rule="nonzero" '
             'fill-opacity="0.8" stroke-linecap="round" stroke-linejoin="round" '
             'stroke="#333333"></polygon></a></svg></div>',
    'xoz_2': '<div id="xoz_2"  style="display: none; background: rgba(0, 0, 0, 0) url(../static/img/xoz_2.png) '
             'no-repeat '
             'scroll 0% 0% / 100%; width: 700px; height: 500px;"> <svg id="svgmainid-sloi-1" '
             'xmlns:svg="http://www.w3.org/2000/svg" xmlns="http://www.w3.org/2000/svg" width="700" height="500" '
             'viewBox="0 0 700 500" preserveAspectRatio="xMinYMin meet" fixpropchecked="true"><a href="#poligon" '
             'id="apoly-1"><polygon id="poly-1" points="" fill="#d2d2d2" fillhover="#e5e5e5" stroke-width="1" '
             'fill-rule="nonzero" fill-opacity="0.8" stroke-linecap="round" stroke-linejoin="round" '
             'stroke="#333333"></polygon></a><a href="#poligon" id="apoly-4"><polygon id="poly-4" points="" '
             'fill="#d2d2d2" fillhover="#e5e5e5" stroke-width="1" fill-rule="nonzero" fill-opacity="0.8" '
             'stroke-linecap="round" stroke-linejoin="round" stroke="#333333"></polygon></a><a href="#poligon" '
             'id="apoly-6"><polygon id="poly-6" points=" 627,104 628,238 508,241 510,100" fill="#d2d2d2" '
             'fillhover="#e5e5e5" stroke-width="1" fill-rule="nonzero" fill-opacity="0.8" stroke-linecap="round" '
             'stroke-linejoin="round" stroke="#333333"></polygon></a><a href="#poligon" id="apoly-7"><polygon '
             'id="poly-7" points=" 626,239 451,240 452,383 629,381" fill="#d2d2d2" fillhover="#e5e5e5" '
             'stroke-width="1" fill-rule="nonzero" fill-opacity="0.8" stroke-linecap="round" stroke-linejoin="round" '
             'stroke="#333333"></polygon></a><a href="#poligon" id="apoly-8"><polygon id="poly-8" points=" 374,'
             '241 376,379 452,374 450,240" fill="#d2d2d2" fillhover="#e5e5e5" stroke-width="1" fill-rule="nonzero" '
             'fill-opacity="0.8" stroke-linecap="round" stroke-linejoin="round" stroke="#333333"></polygon></a><a '
             'href="#poligon" id="apoly-9"><polygon id="poly-9" points=" 448,100 448,211 508,213 510,'
             '101" fill="#d2d2d2" fillhover="#e5e5e5" stroke-width="1" fill-rule="nonzero" fill-opacity="0.8" '
             'stroke-linecap="round" stroke-linejoin="round" stroke="#333333"></polygon></a><a href="#poligon" '
             'id="apoly-10"><polygon id="poly-10" points=" 386,98 386,210 448,209 448,97" fill="#d2d2d2" '
             'fillhover="#e5e5e5" stroke-width="1" fill-rule="nonzero" fill-opacity="0.8" stroke-linecap="round" '
             'stroke-linejoin="round" stroke="#333333"></polygon></a><a href="#poligon" id="apoly-11"><polygon '
             'id="poly-11" points=" 281,97 284,208 383,210 383,99" fill="#d2d2d2" fillhover="#e5e5e5" '
             'stroke-width="1" fill-rule="nonzero" fill-opacity="0.8" stroke-linecap="round" stroke-linejoin="round" '
             'stroke="#333333"></polygon></a><a href="#poligon" id="apoly-14"><polygon id="poly-14" points=" 169,'
             '97 169,239 55,237 53,99" fill="#d2d2d2" fillhover="#e5e5e5" stroke-width="1" fill-rule="nonzero" '
             'fill-opacity="0.8" stroke-linecap="round" stroke-linejoin="round" stroke="#333333"></polygon></a><a '
             'href="#poligon" id="apoly-15"><polygon id="poly-15" points=" 230,100 229,195 281,193 280,'
             '103" fill="#d2d2d2" fillhover="#e5e5e5" stroke-width="1" fill-rule="nonzero" fill-opacity="0.8" '
             'stroke-linecap="round" stroke-linejoin="round" stroke="#333333"></polygon></a><a href="#poligon" '
             'id="apoly-16"><polygon id="poly-16" points=" 227,99 229,194 168,192 168,98" fill="#d2d2d2" '
             'fillhover="#e5e5e5" stroke-width="1" fill-rule="nonzero" fill-opacity="0.8" stroke-linecap="round" '
             'stroke-linejoin="round" stroke="#333333"></polygon></a><a href="#poligon" id="apoly-17"><polygon '
             'id="poly-17" points=" 54,238 54,381 161,379 159,244" fill="#d2d2d2" fillhover="#e5e5e5" '
             'stroke-width="1" fill-rule="nonzero" fill-opacity="0.8" stroke-linecap="round" stroke-linejoin="round" '
             'stroke="#333333"></polygon></a><a href="#poligon" id="apoly-18"><polygon id="poly-18" points=" 160,'
             '288 228,288 229,375 162,374" fill="#d2d2d2" fillhover="#e5e5e5" stroke-width="1" fill-rule="nonzero" '
             'fill-opacity="0.8" stroke-linecap="round" stroke-linejoin="round" stroke="#333333"></polygon></a><a '
             'href="#poligon" id="apoly-19"><polygon id="poly-19" points=" 304,278 304,375 229,374 231,'
             '274" fill="#d2d2d2" fillhover="#e5e5e5" stroke-width="1" fill-rule="nonzero" fill-opacity="0.8" '
             'stroke-linecap="round" stroke-linejoin="round" stroke="#333333"></polygon></a><a href="#poligon" '
             'id="apoly-20"><polygon id="poly-20" points=" 228,242 228,284 160,285 160,245" fill="#d2d2d2" '
             'fillhover="#e5e5e5" stroke-width="1" fill-rule="nonzero" fill-opacity="0.8" stroke-linecap="round" '
             'stroke-linejoin="round" stroke="#333333"></polygon></a><a href="#poligon" id="apoly-21"><polygon '
             'id="poly-21" points=" 281,196 284,242 173,238 169,192" fill="#d2d2d2" fillhover="#e5e5e5" '
             'stroke-width="1" fill-rule="nonzero" fill-opacity="0.8" stroke-linecap="round" stroke-linejoin="round" '
             'stroke="#333333"></polygon></a><a href="#poligon" id="apoly-22"><polygon id="poly-22" points="" '
             'fill="#d2d2d2" fillhover="#e5e5e5" stroke-width="1" fill-rule="nonzero" fill-opacity="0.8" '
             'stroke-linecap="round" stroke-linejoin="round" stroke="#333333"></polygon></a></svg></div>',
    'xoz': '<div id="xoz"  style="display: none; background: rgba(0, 0, 0, 0) url(../static/img/xoz_build.jpg)  '
           'no-repeat scroll 0% 0% / 100%; width: 700px; height: 500px;"> <svg id="svgmainid-sloi-1" '
           'xmlns:svg="http://www.w3.org/2000/svg" xmlns="http://www.w3.org/2000/svg" width="700" height="500" '
           'viewBox="0 0 700 500" preserveAspectRatio="xMinYMin meet" fixpropchecked="true"><a href="#poligon" '
           'id="apoly-1" onclick="perehodKSloy(\'xoz_1\')><polygon id="poly-1" points="" fill="#d2d2d2" '
           'fillhover="#e5e5e5" stroke-width="1" fill-rule="nonzero" fill-opacity="0.8" stroke-linecap="round" '
           'stroke-linejoin="round" stroke="#333333"></polygon></a><a href="#poligon" id="apoly-2" '
           'onclick="perehodKSloy(\'xoz_1\')"><polygon id="poly-2" points=" 96,205 595,304 606,382 74,'
           '453" fill="#d2d2d2" fillhover="#e5e5e5" stroke-width="1" fill-rule="nonzero" fill-opacity="0.8" '
           'stroke-linecap="round" stroke-linejoin="round" stroke="#333333"></polygon></a><a href="#poligon" '
           'id="apoly-3" onclick="perehodKSloy(\'xoz_2\')"><polygon id="poly-3" points=" 97,197 113,2 588,252 591,'
           '297 589,301" fill="#d2d2d2" fillhover="#e5e5e5" stroke-width="1" fill-rule="nonzero" fill-opacity="0.8" '
           'stroke-linecap="round" stroke-linejoin="round" stroke="#333333"></polygon></a><a href="#poligon" '
           'id="apoly-4"><polygon id="poly-4" points="" fill="#d2d2d2" fillhover="#e5e5e5" stroke-width="1" '
           'fill-rule="nonzero" fill-opacity="0.8" stroke-linecap="round" stroke-linejoin="round" '
           'stroke="#333333"></polygon></a></svg>',
    'lab_1': '<div id="lab_1"  style="display: none; background: rgba(0, 0, 0, 0) url(../static/img/lab/lab_1.png) no-repeat scroll 0% 0% / 100%; width: 900px; height: 700px;"> <svg id="svgmainid-sloi-1" xmlns:svg="http://www.w3.org/2000/svg" xmlns="http://www.w3.org/2000/svg" width="900" height="700" viewBox="0 0 900 700" preserveAspectRatio="xMinYMin meet" fixpropchecked="true"><a href="#poligon" id="apoly-2"><polygon id="poly-2" points=" 188,122 186,144 220,144 220,123" fill="#d2d2d2" fillhover="#e5e5e5" stroke-width="1" fill-rule="nonzero" fill-opacity="0.8" stroke-linecap="round" stroke-linejoin="round" stroke="#333333"></polygon></a><a href="#poligon" id="apoly-3"><polygon id="poly-3" points=" 219,145 218,160 187,160 188,144" fill="#d2d2d2" fillhover="#e5e5e5" stroke-width="1" fill-rule="nonzero" fill-opacity="0.8" stroke-linecap="round" stroke-linejoin="round" stroke="#333333"></polygon></a><a href="#poligon" id="apoly-4"><polygon id="poly-4" points=" 220,160 221,187 187,187 187,160" fill="#d2d2d2" fillhover="#e5e5e5" stroke-width="1" fill-rule="nonzero" fill-opacity="0.8" stroke-linecap="round" stroke-linejoin="round" stroke="#333333"></polygon></a><a href="#poligon" id="apoly-5"><polygon id="poly-5" points=" 219,188 218,204 186,204 188,188" fill="#d2d2d2" fillhover="#e5e5e5" stroke-width="1" fill-rule="nonzero" fill-opacity="0.8" stroke-linecap="round" stroke-linejoin="round" stroke="#333333"></polygon></a><a href="#poligon" id="apoly-6"><polygon id="poly-6" points=" 219,206 218,233 186,233 186,205" fill="#d2d2d2" fillhover="#e5e5e5" stroke-width="1" fill-rule="nonzero" fill-opacity="0.8" stroke-linecap="round" stroke-linejoin="round" stroke="#333333"></polygon></a><a href="#poligon" id="apoly-7"><polygon id="poly-7" points=" 218,234 218,263 188,259 189,234" fill="#d2d2d2" fillhover="#e5e5e5" stroke-width="1" fill-rule="nonzero" fill-opacity="0.8" stroke-linecap="round" stroke-linejoin="round" stroke="#333333"></polygon></a><a href="#poligon" id="apoly-8"><polygon id="poly-8" points=" 220,260 219,275 188,274 188,256" fill="#d2d2d2" fillhover="#e5e5e5" stroke-width="1" fill-rule="nonzero" fill-opacity="0.8" stroke-linecap="round" stroke-linejoin="round" stroke="#333333"></polygon></a><a href="#poligon" id="apoly-9"><polygon id="poly-9" points=" 218,272 220,295 187,294 188,272" fill="#d2d2d2" fillhover="#e5e5e5" stroke-width="1" fill-rule="nonzero" fill-opacity="0.8" stroke-linecap="round" stroke-linejoin="round" stroke="#333333"></polygon></a><a href="#poligon" id="apoly-10"><polygon id="poly-10" points=" 141,277 141,256 126,256 127,277" fill="#d2d2d2" fillhover="#e5e5e5" stroke-width="1" fill-rule="nonzero" fill-opacity="0.8" stroke-linecap="round" stroke-linejoin="round" stroke="#333333"></polygon></a><a href="#poligon" id="apoly-11"><polygon id="poly-11" points=" 111,257 111,273 126,273 126,257" fill="#d2d2d2" fillhover="#e5e5e5" stroke-width="1" fill-rule="nonzero" fill-opacity="0.8" stroke-linecap="round" stroke-linejoin="round" stroke="#333333"></polygon></a><a href="#poligon" id="apoly-12"><polygon id="poly-12" points=" 154,240 155,256 175,256 176,240" fill="#d2d2d2" fillhover="#e5e5e5" stroke-width="1" fill-rule="nonzero" fill-opacity="0.8" stroke-linecap="round" stroke-linejoin="round" stroke="#333333"></polygon></a><a href="#poligon" id="apoly-13"><polygon id="poly-13" points=" 156,225 175,225 174,239 155,238" fill="#d2d2d2" fillhover="#e5e5e5" stroke-width="1" fill-rule="nonzero" fill-opacity="0.8" stroke-linecap="round" stroke-linejoin="round" stroke="#333333"></polygon></a><a href="#poligon" id="apoly-14"><polygon id="poly-14" points=" 175,206 176,225 154,225 155,206" fill="#d2d2d2" fillhover="#e5e5e5" stroke-width="1" fill-rule="nonzero" fill-opacity="0.8" stroke-linecap="round" stroke-linejoin="round" stroke="#333333"></polygon></a><a href="#poligon" id="apoly-15"><polygon id="poly-15" points=" 175,178 175,196 155,196 156,178" fill="#d2d2d2" fillhover="#e5e5e5" stroke-width="1" fill-rule="nonzero" fill-opacity="0.8" stroke-linecap="round" stroke-linejoin="round" stroke="#333333"></polygon></a><a href="#poligon" id="apoly-16"><polygon id="poly-16" points=" 155,161 155,177 175,177 174,161" fill="#d2d2d2" fillhover="#e5e5e5" stroke-width="1" fill-rule="nonzero" fill-opacity="0.8" stroke-linecap="round" stroke-linejoin="round" stroke="#333333"></polygon></a><a href="#poligon" id="apoly-17"><polygon id="poly-17" points=" 153,141 141,142 141,160 153,160" fill="#d2d2d2" fillhover="#e5e5e5" stroke-width="1" fill-rule="nonzero" fill-opacity="0.8" stroke-linecap="round" stroke-linejoin="round" stroke="#333333"></polygon></a><a href="#poligon" id="apoly-18"><polygon id="poly-18" points=" 140,149 123,150 123,160 141,159" fill="#d2d2d2" fillhover="#e5e5e5" stroke-width="1" fill-rule="nonzero" fill-opacity="0.8" stroke-linecap="round" stroke-linejoin="round" stroke="#333333"></polygon></a><a href="#poligon" id="apoly-19"><polygon id="poly-19" points=" 122,150 111,150 111,160 123,160" fill="#d2d2d2" fillhover="#e5e5e5" stroke-width="1" fill-rule="nonzero" fill-opacity="0.8" stroke-linecap="round" stroke-linejoin="round" stroke="#333333"></polygon></a><a href="#poligon" id="apoly-20"><polygon id="poly-20" points=" 141,140 125,138 125,128 140,127" fill="#d2d2d2" fillhover="#e5e5e5" stroke-width="1" fill-rule="nonzero" fill-opacity="0.8" stroke-linecap="round" stroke-linejoin="round" stroke="#333333"></polygon></a><a href="#poligon" id="apoly-21"><polygon id="poly-21" points=" 125,126 124,138 111,138 112,126" fill="#d2d2d2" fillhover="#e5e5e5" stroke-width="1" fill-rule="nonzero" fill-opacity="0.8" stroke-linecap="round" stroke-linejoin="round" stroke="#333333"></polygon></a><a href="#poligon" id="apoly-22"><polygon id="poly-22" points=" 110,138 111,126 93,126 94,139" fill="#d2d2d2" fillhover="#e5e5e5" stroke-width="1" fill-rule="nonzero" fill-opacity="0.8" stroke-linecap="round" stroke-linejoin="round" stroke="#333333"></polygon></a><a href="#poligon" id="apoly-23"><polygon id="poly-23" points=" 125,274 126,287 94,288 95,257 110,257 110,273" fill="#d2d2d2" fillhover="#e5e5e5" stroke-width="1" fill-rule="nonzero" fill-opacity="0.8" stroke-linecap="round" stroke-linejoin="round" stroke="#333333"></polygon></a><a href="#poligon" id="apoly-24"><polygon id="poly-24" points=" 155,256 141,257 141,276 126,276 127,289 153,288" fill="#d2d2d2" fillhover="#e5e5e5" stroke-width="1" fill-rule="nonzero" fill-opacity="0.8" stroke-linecap="round" stroke-linejoin="round" stroke="#333333"></polygon></a><a href="#poligon" id="apoly-27"><polygon id="poly-27" points=" 634,266 661,267 660,298 635,297" fill="#d2d2d2" fillhover="#e5e5e5" stroke-width="1" fill-rule="nonzero" fill-opacity="0.8" stroke-linecap="round" stroke-linejoin="round" stroke="#333333"></polygon></a><a href="#poligon" id="apoly-31"><polygon id="poly-31" points=" 701,266 701,297 661,298 661,267" fill="#d2d2d2" fillhover="#e5e5e5" stroke-width="1" fill-rule="nonzero" fill-opacity="0.8" stroke-linecap="round" stroke-linejoin="round" stroke="#333333"></polygon></a><a href="#poligon" id="apoly-32"><polygon id="poly-32" points=" 723,265 722,297 698,297 700,264" fill="#d2d2d2" fillhover="#e5e5e5" stroke-width="1" fill-rule="nonzero" fill-opacity="0.8" stroke-linecap="round" stroke-linejoin="round" stroke="#333333"></polygon></a><a href="#poligon" id="apoly-33"><polygon id="poly-33" points=" 744,266 745,297 719,298 722,265" fill="#d2d2d2" fillhover="#e5e5e5" stroke-width="1" fill-rule="nonzero" fill-opacity="0.8" stroke-linecap="round" stroke-linejoin="round" stroke="#333333"></polygon></a><a href="#poligon" id="apoly-35"><polygon id="poly-35" points=" 789,267 788,299 746,298 745,266" fill="#d2d2d2" fillhover="#e5e5e5" stroke-width="1" fill-rule="nonzero" fill-opacity="0.8" stroke-linecap="round" stroke-linejoin="round" stroke="#333333"></polygon></a><a href="#poligon" id="apoly-36"><polygon id="poly-36" points=" 790,318 790,340 756,341 758,319" fill="#d2d2d2" fillhover="#e5e5e5" stroke-width="1" fill-rule="nonzero" fill-opacity="0.8" stroke-linecap="round" stroke-linejoin="round" stroke="#333333"></polygon></a><a href="#poligon" id="apoly-37"><polygon id="poly-37" points=" 789,445 790,402 756,404 758,446" fill="#d2d2d2" fillhover="#e5e5e5" stroke-width="1" fill-rule="nonzero" fill-opacity="0.8" stroke-linecap="round" stroke-linejoin="round" stroke="#333333"></polygon></a><a href="#poligon" id="apoly-38"><polygon id="poly-38" points=" 788,404 788,380 756,383 757,401" fill="#d2d2d2" fillhover="#e5e5e5" stroke-width="1" fill-rule="nonzero" fill-opacity="0.8" stroke-linecap="round" stroke-linejoin="round" stroke="#333333"></polygon></a><a href="#poligon" id="apoly-39"><polygon id="poly-39" points=" 790,341 789,362 757,360 759,342" fill="#d2d2d2" fillhover="#e5e5e5" stroke-width="1" fill-rule="nonzero" fill-opacity="0.8" stroke-linecap="round" stroke-linejoin="round" stroke="#333333"></polygon></a><a href="#poligon" id="apoly-40"><polygon id="poly-40" points=" 790,363 790,383 758,384 757,360" fill="#d2d2d2" fillhover="#e5e5e5" stroke-width="1" fill-rule="nonzero" fill-opacity="0.8" stroke-linecap="round" stroke-linejoin="round" stroke="#333333"></polygon></a><a href="#poligon" id="apoly-42"><polygon id="poly-42" points=" 737,448 736,422 705,422 703,446" fill="#d2d2d2" fillhover="#e5e5e5" stroke-width="1" fill-rule="nonzero" fill-opacity="0.8" stroke-linecap="round" stroke-linejoin="round" stroke="#333333"></polygon></a><a href="#poligon" id="apoly-43"><polygon id="poly-43" points=" 737,402 737,384 704,383 706,406" fill="#d2d2d2" fillhover="#e5e5e5" stroke-width="1" fill-rule="nonzero" fill-opacity="0.8" stroke-linecap="round" stroke-linejoin="round" stroke="#333333"></polygon></a><a href="#poligon" id="apoly-44"><polygon id="poly-44" points=" 737,381 737,359 703,360 704,384" fill="#d2d2d2" fillhover="#e5e5e5" stroke-width="1" fill-rule="nonzero" fill-opacity="0.8" stroke-linecap="round" stroke-linejoin="round" stroke="#333333"></polygon></a><a href="#poligon" id="apoly-45"><polygon id="poly-45" points=" 736,405 736,423 704,421 706,405" fill="#d2d2d2" fillhover="#e5e5e5" stroke-width="1" fill-rule="nonzero" fill-opacity="0.8" stroke-linecap="round" stroke-linejoin="round" stroke="#333333"></polygon></a><a href="#poligon" id="apoly-47"><polygon id="poly-47" points=" 660,319 659,351 638,351 639,318" fill="#d2d2d2" fillhover="#e5e5e5" stroke-width="1" fill-rule="nonzero" fill-opacity="0.8" stroke-linecap="round" stroke-linejoin="round" stroke="#333333"></polygon></a><a href="#poligon" id="apoly-48"><polygon id="poly-48" points=" 531,318 532,350 510,350 509,318" fill="#d2d2d2" fillhover="#e5e5e5" stroke-width="1" fill-rule="nonzero" fill-opacity="0.8" stroke-linecap="round" stroke-linejoin="round" stroke="#333333"></polygon></a><a href="#poligon" id="apoly-49"><polygon id="poly-49" points=" 510,297 511,281 511,267 470,267 469,297" fill="#d2d2d2" fillhover="#e5e5e5" stroke-width="1" fill-rule="nonzero" fill-opacity="0.8" stroke-linecap="round" stroke-linejoin="round" stroke="#333333"></polygon></a><a href="#poligon" id="apoly-50"><polygon id="poly-50" points=" 447,266 448,297 471,296 471,266" fill="#d2d2d2" fillhover="#e5e5e5" stroke-width="1" fill-rule="nonzero" fill-opacity="0.8" stroke-linecap="round" stroke-linejoin="round" stroke="#333333"></polygon></a><a href="#poligon" id="apoly-51"><polygon id="poly-51" points=" 427,265 427,297 449,296 446,265" fill="#d2d2d2" fillhover="#e5e5e5" stroke-width="1" fill-rule="nonzero" fill-opacity="0.8" stroke-linecap="round" stroke-linejoin="round" stroke="#333333"></polygon></a><a href="#poligon" id="apoly-52"><polygon id="poly-52" points=" 408,265 408,297 427,298 426,266" fill="#d2d2d2" fillhover="#e5e5e5" stroke-width="1" fill-rule="nonzero" fill-opacity="0.8" stroke-linecap="round" stroke-linejoin="round" stroke="#333333"></polygon></a><a href="#poligon" id="apoly-53"><polygon id="poly-53" points=" 408,264 381,265 381,297 408,297" fill="#d2d2d2" fillhover="#e5e5e5" stroke-width="1" fill-rule="nonzero" fill-opacity="0.8" stroke-linecap="round" stroke-linejoin="round" stroke="#333333"></polygon></a><a href="#poligon" id="apoly-54"><polygon id="poly-54" points=" 415,318 414,339 383,340 383,318" fill="#d2d2d2" fillhover="#e5e5e5" stroke-width="1" fill-rule="nonzero" fill-opacity="0.8" stroke-linecap="round" stroke-linejoin="round" stroke="#333333"></polygon></a><a href="#poligon" id="apoly-55"><polygon id="poly-55" points=" 414,340 414,362 382,361 382,339" fill="#d2d2d2" fillhover="#e5e5e5" stroke-width="1" fill-rule="nonzero" fill-opacity="0.8" stroke-linecap="round" stroke-linejoin="round" stroke="#333333"></polygon></a><a href="#poligon" id="apoly-56"><polygon id="poly-56" points=" 391,362 392,383 414,383 414,363" fill="#d2d2d2" fillhover="#e5e5e5" stroke-width="1" fill-rule="nonzero" fill-opacity="0.8" stroke-linecap="round" stroke-linejoin="round" stroke="#333333"></polygon></a><a href="#poligon" id="apoly-57"><polygon id="poly-57" points=" 390,383 391,433 415,434 414,383" fill="#d2d2d2" fillhover="#e5e5e5" stroke-width="1" fill-rule="nonzero" fill-opacity="0.8" stroke-linecap="round" stroke-linejoin="round" stroke="#333333"></polygon></a><a href="#poligon" id="apoly-58"><polygon id="poly-58" points=" 435,434 458,433 458,404 435,404" fill="#d2d2d2" fillhover="#e5e5e5" stroke-width="1" fill-rule="nonzero" fill-opacity="0.8" stroke-linecap="round" stroke-linejoin="round" stroke="#333333"></polygon></a><a href="#poligon" id="apoly-59"><polygon id="poly-59" points=" 436,381 458,381 458,404 435,403" fill="#d2d2d2" fillhover="#e5e5e5" stroke-width="1" fill-rule="nonzero" fill-opacity="0.8" stroke-linecap="round" stroke-linejoin="round" stroke="#333333"></polygon></a><a href="#poligon" id="apoly-60"><polygon id="poly-60" points=" 435,362 436,379 467,380 466,362" fill="#d2d2d2" fillhover="#e5e5e5" stroke-width="1" fill-rule="nonzero" fill-opacity="0.8" stroke-linecap="round" stroke-linejoin="round" stroke="#333333"></polygon></a><a href="#poligon" id="apoly-61"><polygon id="poly-61" points="" fill="#d2d2d2" fillhover="#e5e5e5" stroke-width="1" fill-rule="nonzero" fill-opacity="0.8" stroke-linecap="round" stroke-linejoin="round" stroke="#333333"></polygon></a></svg>'
}
