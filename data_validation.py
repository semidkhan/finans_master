def validate_transaction(data):
    return True if data['amount'] > 0 else False
