from library import app

@app.after_request
def after_request_func(response):
    # print("after_request is running!")
    # print(response.json)
    # return response
    pass


@app.before_request
def before_request_func():
    pass
    # print("before_request is running!")
