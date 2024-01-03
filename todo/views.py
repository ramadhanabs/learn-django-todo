from .models import Task
from app.utils import custom_json_response
from django.forms.models import model_to_dict
from django.views.decorators.csrf import csrf_exempt
import json

# Create your views here.
def index(request):
    try:
        tasks = Task.objects.all().values()
        return custom_json_response(list(tasks), None, 200)
    except Exception as e:
        # Handle other types of exceptions
        print(f"An error occurred: {e}")
        return custom_json_response(None, f"An error occurred: {e}", 500)
    
def task_get(request, task_id):
    try:
        task = Task.objects.get(pk=task_id)
        remapped_task = {**model_to_dict(task), "created_at": task.created_at, "updated_at": task.updated_at}
        return custom_json_response(remapped_task, None, 200)
    except Task.DoesNotExist:
        return custom_json_response(None, "Task not found", 404)

@csrf_exempt
def task_post(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            
            new_task = Task.objects.create(
                title = data.get('title'),
                description = data.get('description'),
                status = data.get('status')
            )
            
            return custom_json_response(model_to_dict(new_task), None, 200)
        except json.JSONDecodeError:
            return custom_json_response(None, "Invalid JSON Format", 400)
        except Exception as e:
            print(f"An error occurred: {e}")
            return custom_json_response(None, f"An error occurred: {e}", 500)
    else:
        return custom_json_response(None, 'Method not allowed', 405)
    
@csrf_exempt
def task_update(request, task_id):
    if request.method == 'PUT':
        try:
            data = json.loads(request.body)
            Task.objects.filter(id = task_id).update(
                title = data.get('title'),
                description = data.get('description'),
                status = data.get('status')
            )
            
            updated_task = Task.objects.get(id = task_id)
            
            return custom_json_response(model_to_dict(updated_task), None, 200)
        except Task.DoesNotExist:
            return custom_json_response(None, "Task not found", 404)
        except json.JSONDecodeError:
            return custom_json_response(None, "Invalid JSON Format", 400)       
        except Exception as e:
            print(f"An error occurred: {e}")
            return custom_json_response(None, f"An error occurred: {e}", 500)
    else:
        return custom_json_response(None, "Method not allowed", 405)

@csrf_exempt
def task_delete(request, task_id):
    if request.method == 'DELETE':
        try: 
            Task.objects.get(id = task_id).delete()
            
            return custom_json_response(None, None, 200)
        except Task.DoesNotExist:
            return custom_json_response(None, "Task not found", 404)
        except Exception as e:
            print(f"An error occurred: {e}")
            return custom_json_response(None, f"An error occurred: {e}", 500)
    else:
        return custom_json_response(None, "Method not allowed", 405)