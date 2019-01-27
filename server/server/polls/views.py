from django.shortcuts import render
from django.http import HttpResponse
from bson.json_util import dumps
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from pymongo import MongoClient
Client = MongoClient ()
db = Client['Diebrary']
Collection = db['Diseases']


def get (request):
        x = Collection.find()
        print ('maiin pagal hoga hoon ',dumps(x))
        b=HttpResponse (dumps([{"hello":"World"},x]))
        b["Content-Type"] = "application/json"
        print(b)
        return b

    # return HttpResponse(dumps(request))
def post (request):
        # print
        # c = Collection.find({'disease':request.data.body["disease"]})
        # print (dumps(c))
        return HttpResponse(dumps(request.body))
def put ():
    pass

