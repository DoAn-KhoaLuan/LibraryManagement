from flask import jsonify
from twilio.rest import Client
account_sid = 'ACe84806c2d41d2d57794ea24fd042cde5'
auth_token = '57200acc904edc1b9f78507a41283af5'
client = Client(account_sid, auth_token)


def phone(Text):
    message = client.messages.create(
        body=Text,
        from_='+15202171267',
        to='+84865248526'
    )
    return message


def ConvertModelListToDictList(model_list):
    dict_items = []
    # model_list=filter(lambda model_item: model_item.delete_at is None, model_list)
    for item in model_list:
        # if item.delete_at is None:
        dict_items.append(item.serialize())
    return dict_items


def ConvertModelListToJson(model_list):
    return jsonify(list(map(lambda item: item.serialize(), model_list)))

