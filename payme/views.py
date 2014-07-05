
from django.http import HttpResponse
from payme.models import Account, Transaction


'''
1. Read SMS  [9876543210 200]
2. Show Transactions
'''

def parse_sms(message):
    # TODO - return from_number, to_number, decimal of amount
    pass


def home(request):
    return HttpResponse('Bangalore Payments Hackathon')


def make_payment(request):
    from_number = request.GET('from_number')
    to_number, amount = parse_sms(request.GET['message'])

    try:
        from_account - Account.objects.get(mobile_number=from_number)
    except Account.DoesNotExist:
        # TODO: return JSON response not a valid from account
        pass

    if from_account.current_balance < amount:
        # TODO: return JSON response with Message
        pass

    to_account = Account.objects.get_or_create(mobile_number=to_number)

    # TODO - Update from account & to account balance

    Transaction.objects.create(from_account=from_account,
                               to_account=to_account,
                               amount=amount)

    # TODO: return success response
    return {}