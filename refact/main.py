import requests

from src.refund import refund
from src.capture import capture
from src.authorization import authorize
from src.query_transaction import query_transaction

def main():

    print()

    authorization_response = authorize()
    print(authorization_response)
    tid = authorization_response.get("tid")

    query_transaction_response = query_transaction(tid)
    print()
    print(query_transaction_response)
    
    capture_response = capture(tid=tid, amount=2000)
    print()
    print(capture_response)

    query_transaction_response = query_transaction(tid)
    print()
    print(query_transaction_response)

    refund_transaction_response = refund(tid)
    print()
    print(refund_transaction_response)

if __name__ == "__main__":
    main()