from django.http import JsonResponse

def custom_json_response(data=None, error_message=None, status=200):
    response_data = {
        'data': data,
        'error_message': error_message,
        'status': status
    }
    
    return JsonResponse(response_data, status = status)