from django.http import HttpResponse, HttpResponseNotAllowed, HttpResponseBadRequest

def multiplyNums(request):
    if request.method == 'GET':
        params = request.GET
        
        if not ('num1' in params and 'num2' in params and params['num1'] and params['num2']):
            html = "<html><body>Wrong parameters. Assumes integers 'num1=' and 'num2='</body></html>"
            return HttpResponseBadRequest(html)
        
        num1 = int(params.get('num1'))
        num2 = int(params.get('num2'))
        mul = num1 * num2 
        return HttpResponse(mul)
    
    return HttpResponseNotAllowed()

def hello(request):
    html = "<html><body>Hello world!!!</body></html>"
    return HttpResponse(html)