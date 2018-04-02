from wsgiref.simple_server import make_server
import os
def application(environ,start_response):
    response_body='The request method was %s'%['REQUEST_METHOD']
    status='200 OK'
    response_headers=[('Content-Type','text/plain')]
    start_response(status,response_headers)
    #cmd_result=os.popen('python printabc.py').read()
    cmd_result=os.popen('ipconfig').read()
    return [cmd_result]

httpd=make_server('',8000,application)
httpd.serve_forever()