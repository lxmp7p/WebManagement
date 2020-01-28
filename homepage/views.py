from django.contrib import auth
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django import forms
from .models import Equipment


# Create your views here.
class AddEquip(forms.Form):
    equip_name = forms.CharField(label='equip_name', max_length=100)
    serial_id = forms.CharField(label='serial_id', max_length=100)
    room = forms.CharField(label='room', max_length=100)


def index_page(request):
    if request.method == "POST":
        form = AddEquip(data={'equip_name': request.POST['equip_name'],
                              'serial_id': request.POST['serial_id'],
                              'room': request.POST['room']})
        if form.is_valid():
            entry = Equipment(equip_name=form.cleaned_data['equip_name'],
                              serial_id=form.cleaned_data['serial_id'],
                              room=form.cleaned_data['room'])
            entry.save()
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
                    'stroke="#333333"></polygon></a></svg></div>',
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
}
