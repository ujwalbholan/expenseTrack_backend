from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from .models import Income
import datetime

# Create your views here.

@csrf_exempt
def set_income_view(request):
    if request.method == 'POST':
        try:
            name = request.POST.get('name')
            amount = request.POST.get('amount')
            source = request.POST.get('source')
            date = request.POST.get('date')
            notes = request.POST.get('notes', '')

            print(f"Received data: name={name}, amount={amount}, source={source}, date={date}, notes={notes}")

            if not name or not amount or not source or not date:
                return JsonResponse({'message': 'Missing required fields'}, status=400)

            income = Income.objects.create(
                name=name,
                amount=amount,
                source=source,
                date=datetime.datetime.strptime(date, '%Y-%m-%d').date(),
                notes=notes
            )

            return JsonResponse({'message': 'Income saved successfully'}, status=200)

        except Exception as e:
            return JsonResponse({'message': 'Error processing request', 'error': str(e)}, status=500)

    return JsonResponse({'message': 'Invalid request method'}, status=405)

@csrf_exempt
def get_all_incomes_view(request):
    if request.method == 'GET':
        incomes = Income.objects.all()
        data = []
        for income in incomes:
            data.append({
                'id': income.id,
                'name': income.name,
                'amount': float(income.amount),
                'source': income.source,
                'date': income.date.strftime('%Y-%m-%d'),
                'notes': income.notes,
            })
        return JsonResponse(data, safe=False, status=200)

    return JsonResponse({'message': 'Invalid request method.'}, status=405)

@csrf_exempt
def get_income_view_by_Id(request):
    if request.method == 'GET':
        income_id = request.GET.get('id')

        if not income_id:
            return JsonResponse({'message': 'Income ID is required.'}, status=400)

        try:
            income = Income.objects.get(id=income_id)
            data = {
                'id': income.id,
                'name': income.name,
                'amount': float(income.amount),
                'source': income.source,
                'date': income.date.strftime('%Y-%m-%d'),
                'notes': income.notes,
            }
            return JsonResponse(data, status=200)

        except Income.DoesNotExist:
            return JsonResponse({'message': 'Income not found.'}, status=404)

    return JsonResponse({'message': 'Invalid request method.'}, status=405)

@csrf_exempt
def edit_income_view(request):
    if request.method == 'POST':
        income_id = request.POST.get('id')
        name = request.POST.get('name')
        amount = request.POST.get('amount')
        source = request.POST.get('source')
        date = request.POST.get('date')
        notes = request.POST.get('notes', '')

        if not income_id or not name or not amount or not source or not date:
            return JsonResponse({'message': 'Missing required fields'}, status=400)

        try:
            income = Income.objects.get(id=income_id)
            income.name = name
            income.amount = amount
            income.source = source
            income.date = datetime.datetime.strptime(date, '%Y-%m-%d').date()
            income.notes = notes
            income.save()

            return JsonResponse({'message': 'Income edited successfully'}, status=200)

        except Income.DoesNotExist:
            return JsonResponse({'message': 'Income not found'}, status=404)
        except Exception as e:
            return JsonResponse({'message': 'Error processing request', 'error': str(e)}, status=500)

    return JsonResponse({'message': 'Invalid request method'}, status=405)

@csrf_exempt
def delete_income_view(request):
    if request.method == 'POST':
        income_id = request.POST.get('id')

        if not income_id:
            return JsonResponse({'message': 'Income ID is required'}, status=400)

        try:
            income = Income.objects.get(id=income_id)
            income.delete()
            return JsonResponse({'message': 'Income deleted successfully'}, status=200)

        except Income.DoesNotExist:
            return JsonResponse({'message': 'Income not found'}, status=404)
        except Exception as e:
            return JsonResponse({'message': 'Error processing request', 'error': str(e)}, status=500)

    return JsonResponse({'message': 'Invalid request method'}, status=405)

