from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect,HttpResponse
# from django.contrib.auth.models import User, auth
# from django.contrib import messages
from .models import features
from .models import Items
from .forms import ItemForm
from .forms import BoxForm
import cv2
from pyzbar.pyzbar import decode
import time
from django.urls import reverse
import qrcode
# from PIL import Image
from django.http import StreamingHttpResponse


# Create your views here.

def home(request):
    return render(request, 'myapp/home.html')
# def url(request):
#     url = reverse('myapp/rack1.html')
#     context = {
#         'url': url
#     }
#     return render(request,'myapp/home.html',context)

def login1(request):
    return render(request, 'myapp/login1.html')


def add_item(request):
    return render(request, 'myapp/add_item.html')

# Boxes in each rack
def rack1(request):
    filtered_features = features.objects.filter(rack_id = 1)
    return render(request,'myapp/rack1.html',{'features':filtered_features})

def rack2(request):
    filtered_features = features.objects.filter(rack_id = 2)
    return render(request,'myapp/rack1.html',{'features':filtered_features})

def rack3(request):
    filtered_features = features.objects.filter(rack_id = 3)
    return render(request,'myapp/rack1.html',{'features':filtered_features})

def rack4(request):
    filtered_features = features.objects.filter(rack_id = 4)
    return render(request,'myapp/rack1.html',{'features':filtered_features})

def rack5(request):
    filtered_features = features.objects.filter(rack_id = 5)
    return render(request,'myapp/rack1.html',{'features':filtered_features})

# Items in a box
def box_click(request,feature_id):
    feature = features.objects.get(id=feature_id)
    
    # Retrieve the items associated with the clicked feature
    items = Items.objects.filter(box_id=feature)
    return render(request, 'myapp/box_items.html', {'items': items})

# def boxitems(request):
#     return render(request, 'myapp/box_items.html')



def add_item(request):
    if request.method == 'POST':
        form = ItemForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('rack1')  # Redirect to a success page or item list
    else:
        form = ItemForm()
    return render(request, 'myapp/add_item.html', {'form': form})

def add_box(request):
    if request.method == 'POST':
        form = BoxForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('rack1')  # Redirect to a success page or item list
    else:
        form = BoxForm()
    return render(request, 'myapp/add_box.html', {'form': form})



# Racks
def index(request):
    all_features = features.objects.all()
    return render(request, 'myapp/index.html', {'features': all_features})


def generate_frame():
    camera = cv2.VideoCapture(0, cv2.CAP_DSHOW)
    camera.set(3, 640)  # Set width
    camera.set(4, 480)  # Set height

    while True:
        success, frame = camera.read()

        if not success:
            break

        # Convert the frame to JPEG format
        _, jpeg_frame = cv2.imencode('.jpg', frame)

        # Yield the JPEG frame as a byte stream
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + jpeg_frame.tobytes() + b'\r\n\r\n')

    camera.release()

def scanner(request):
    
    cam = cv2.VideoCapture(0)
    cam.set(5, 640)
    cam.set(6, 480)

    camera = True
    link = None  # Initialize link variable outside the loop
    while camera == True:
        success, frame = cam.read()
        
        for i in decode(frame):
            link = i.data.decode('utf-8')  # Decode the data
            print(i.type)
            print(link)
            time.sleep(6)
            cv2.imshow("ourQr_Code_scanner", frame)
            cv2.waitKey(3)
        
        # Check if a link is obtained and redirect if true
        if link is not None:
            return HttpResponseRedirect(link)
        
    return StreamingHttpResponse(generate_frame(), content_type='multipart/x-mixed-replace; boundary=frame')
    
    # # Handle the case where no link is obtained
    # return HttpResponse("No QR code detected.")
         
def link(request):
    feature_id = 1  # Replace with the actual feature_id you want to pass
    url = reverse('box_click', args=[feature_id])
    qrc(url)
    return HttpResponse("QR code generated successfully") 


# Generate QR code
def qrc(link): 
# Encoding data using make() function
    img = qrcode.make(link)
 
# Saving as an image file
    img.save('Box1.png')







