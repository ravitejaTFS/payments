

from payme.models import Account, Transaction

'''
1. Read SMS 
2. Show Transactions
'''


def parse_sms(message):
    # TODO - return from_number, to_number, decimal of amount
    pass


def make_payment(request):
    from_number, to_number, amount = parse_sms(request.GET['message'])

    from_account = None
    try:
        from_account = Account.objects.get(mobile_number=from_number)
    except Account.DoesNotExist:
        # TODO: return JSON response not a valid from account
        pass

    if from_account.current_balance < amount:
        # TODO: return JSON response with Message
        pass

    to_account = Account.objects.get_or_create(mobile_number=to_number)

