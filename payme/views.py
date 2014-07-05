
import decimal
import json

from django.http import HttpResponse
from payme.models import Account, Merchant, Product, Transaction


'''
1. Read SMS  [9876543210 200]
2. Show Transactions
'''


def parse_sms(message):
    to_number, amount = message.split()
    return to_number, decimal.Decimal(amount)


def json_response(view_func):
    def inner(request, *args, **kwargs):
        payload = view_func(request, *args, **kwargs)
        return HttpResponse(simplejson.dumps(payload))
    return inner


def home(request):
    return HttpResponse('Bangalore Payments Hackathon')


def update_balance(account, amount, action='add'):
    if action == 'add':
        account.current_balance += amount
        message = 'Account credited with %s' % amount
    elif action == 'sub':
        account.current_balance -= amount
        message = 'Account debited with %s' % amount
    account.save()
    # TODO: send message to account
    return account

@json_response
def make_payment(request):
    from_number = request.GET('from_number')
    to_number, amount = parse_sms(request.GET['message'])

    from_account = None
    try:
        from_account = Account.objects.get(mobile_number=from_number)
    except Account.DoesNotExist:
        return {'status': 'error', 'message': 'Account Does Not Exist'}

    if from_account.current_balance < amount:
        return {'status': 'error', 'message': 'Insufficient Funds'}

    to_account = Account.objects.get_or_create(mobile_number=to_number)

    # TODO - Update from account & to account balance
    update_balance(to_account, amount, action='sub')
    update_balance(from_account, amount, action='add')

    Transaction.objects.create(from_account=from_account,
                               to_account=to_account,
                               amount=amount)
    return {'status': 'success', 'message': 'Transaction Successful'}


def get_product_price(request):
    data = request.GET
    product_id = data.get('product_id')

    if not product_id:
        return_data = {'status': 'error', 'response_data': 'Send product id please.'}
    else:
        try:
            amount = Product.objects.get(product_id=product_id).amount
            return_data = {'status': 'success', 'response_data': {'product_id': product_id, 'amount': amount}}
        except Exception as e:
            return_data = {'status': 'error', 'response_data': str(e)}
    return HttpResponse(json.dumps(return_data))


def get_merchant_number(request):
    data = request.GET
    merchant_id = data.get('merchant_id')

    if not merchant_id:
        return_data = {'status': 'error', 'response_data': 'Send merchant id please.'}
    else:
        try:
            merchant_mobile = Merchant.objects.get(merchant_id=merchant_id).merchant_mobile
            return_data = {'status': 'success', 'response_data': {'product_id': merchant_mobile, 'amount': merchant_mobile}}
        except Exception as e:
            return_data = {'status': 'error', 'response_data': str(e)}
    return HttpResponse(json.dumps(return_data))
