from flask import Flask, redirect, url_for, render_template, request
import time

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/bubble", methods = ['GET','POST'])
def bubble():
    if request.method == 'GET':
        return render_template('bubble.html')
    elif request.method == 'POST':
        start_time = time.time()
        list_ = request.form['myList'].split(",")
        for i in range(len(list_)):
            for j in range(len(list_) - 1):
                if list_[j] > list_[j+1]:
                    list_[j], list_[j+1] = list_[j+1], list_[j]
        end_time = time.time()
        final_time = end_time - start_time
        return render_template("bubble.html", list_=list_, final_time=final_time)

@app.route("/merge", methods = ['GET','POST'])
def merge():
    if request.method == 'GET':
        return render_template('merge.html')
    elif request.method == 'POST':
        start_time = time.time()
        list_ = request.form['myList'].split(",")
        list_ = [int(item) for item in list_]
        def mergeSort(arr):
            if len(arr) > 1:
                mid = len(arr)//2
                L = arr[:mid]
                R = arr[mid:]
                mergeSort(L)
                mergeSort(R)
                i = j = k = 0
                while i < len(L) and j < len(R):
                    if L[i] < R[j]:
                        arr[k] = L[i]
                        i += 1
                    else:
                        arr[k] = R[j]
                        j += 1
                    k += 1
                while i < len(L):
                    arr[k] = L[i]
                    i += 1
                    k += 1

                while j < len(R):
                    arr[k] = R[j]
                    j += 1
                    k += 1
                return (arr)
        list__ = mergeSort(list_)
        end_time = time.time()
        final_time1 = end_time - start_time

        return render_template("merge.html", list_=list__, final_time1=final_time1)

@app.route("/linear", methods = ['GET','POST'])
def linear():
    if request.method == 'GET':
        return render_template('linear.html')
    elif request.method == 'POST':
        start_time = time.time()
        list_ = request.form['myList'].split(",")
        list_ = [int(item) for item in list_]
        user = request.form['user']
        user = int(user)
        present = 'False'
        for i in range(len(list_)):
            if list_[i] == user:
                present = 'True'
        end_time = time.time()
        final_time2 = end_time - start_time
        return render_template("linear.html", present=present, final_time2=final_time2)

@app.route("/binary", methods = ['GET','POST'])
def binary():
    if request.method == 'GET':
        return render_template('binary.html')
    elif request.method == 'POST':
        start_time = time.time()
        list_ = request.form['myList'].split(",")
        list_ = [int(item) for item in list_]
        user = request.form['user']
        user = int(user)
        present_ = 'False'
        for j in range(len(list_) - 1):
            if list_[j] > list_[j+1]:
                present = "The list you entered wasn't sorted"
                return render_template("binary.html", present=present_,)
        first = 0
        last = (len(list_) - 1)
        while( first<=last and present_ == 'False'):
            mid = (first + last)//2
            if list_[mid] == user :
                present_ = 'True'

            else:
                if user < list_[mid]:
                    last = mid - 1
                else:
                    first = mid + 1
        end_time = time.time()
        final_time3 = end_time - start_time

        return render_template("binary.html", present1=present_, final_time3=final_time3)

if __name__ == "__main__":
    app.run(Debug=True)
