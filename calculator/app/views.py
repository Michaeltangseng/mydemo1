from django.shortcuts import render

# # Create your views here.

import subprocess  #引入子进程模块用于执行发送过来的计算公式
from django.views.decorators.http import require_POST  #获取后台服务器的POST请求权限(否则发过来的请求会被后台服务器阻止)
from django.http import JsonResponse  #将计算得到的结果封装成JSON字符串
from django.views.decorators.csrf import csrf_exempt   #引入csrf_exempt装饰器用于规避csrf校验(防止网站被跨站攻击)

def home(request):
    return render(request,'index.html')


def run_code(code):
    try:
        code = 'print(' + code + ')'
        output = subprocess.check_output(['python','-c',code],
                                         universal_newlines=True,
                                         stderr=subprocess.STDOUT,
                                         timeout=30)
    except subprocess.CalledProcessError as e:
        output = '公式输入有误'
    return output

@csrf_exempt
@require_POST
def compute(request):
    code = request.POST.get('code')
    result = run_code(code)
    return JsonResponse(data={'result':result})
