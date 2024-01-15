import base64
from email import message
from django.shortcuts import get_object_or_404, render, redirect
from django.http import HttpResponseRedirect,HttpResponse
from django.contrib.auth.models import User, auth
from django.urls import reverse
from .utils import qrc
from myproject.settings import MEDIA_ROOT
import qrcode
from io import BytesIO
from django.core.files import File
from .models import features
from .models import Items
from .models import Racks
from django.urls import reverse
from .forms import ItemForm
from .forms import BoxForm
import cv2
from pyzbar.pyzbar import decode
import time
from django.urls import reverse
import qrcode
from django.http import StreamingHttpResponse
from django.contrib.auth.decorators import login_required
from pyzbar.pyzbar import decode
from django.http import HttpResponseRedirect
from pyzbar.pyzbar import decode  # Assuming you're using pyzbar for QR code decoding
from django.http import HttpResponseRedirect  # Assuming you're using Django
from django.shortcuts import render
from .forms import SearchForm
from .models import Items


def home(request):
    return render(request, 'myapp/home.html')

def login1(request):
    return render(request, 'myapp/login1.html')

@login_required
def rack1(request):
    filtered_features = features.objects.filter(rack_id = 1)
    return render(request,'myapp/rack1.html',{'features':filtered_features})

@login_required
def rack2(request):
    filtered_features = features.objects.filter(rack_id = 2)
    return render(request,'myapp/rack1.html',{'features':filtered_features})

@login_required
def rack3(request):
    filtered_features = features.objects.filter(rack_id = 3)
    return render(request,'myapp/rack1.html',{'features':filtered_features})

@login_required
def rack4(request):
    filtered_features = features.objects.filter(rack_id = 4)
    return render(request,'myapp/rack1.html',{'features':filtered_features})

@login_required
def rack5(request):
    filtered_features = features.objects.filter(rack_id = 5)
    return render(request,'myapp/rack1.html',{'features':filtered_features})

def box_click(request,feature_id):
    feature = features.objects.get(id=feature_id)
    
    # Retrieve the items associated with the clicked feature
    items = Items.objects.filter(box_id=feature)
    user = request.user.username
    if(user == 'admin'):
        return render(request, 'myapp/admin.html', {'items': items})
    else:
        return render(request, 'myapp/box_items.html', {'items': items})

# Racks
@login_required
def index(request):
    all_features = features.objects.all()
    user = request.user.username
    context = {
        'features': all_features,
        'user': user,
    }
    if user == 'admin':
        return render(request, 'myapp/adminInd.html', context)
    else:
        return render(request, 'myapp/index.html', context)

def allQR(request):
    return render(request, 'myapp/allQR.html')

def anchor(request):
    if request.method == 'POST':
        form = SearchForm(request.POST)
        if form.is_valid():
            box_name = form.cleaned_data['name']
            try:
                box = features.objects.get(name = box_name)
                qrcode = box.qr_code_image
                print(qrcode)
                return render(request, 'myapp/allQR.html',{'QRcode' : qrcode})
            except features.DoesNotExist:
                return render(request, 'myapp/allQR.html', {'error_message' : 'Box not found'})
    else:
        form = SearchForm()
    return render(request, 'myapp/allQR.html', {'form': form})

def del_box(request, feature_id):
    box = features.objects.filter(id = feature_id)
    box.delete()
    return render(request, 'myapp/index.html')


def ruq(request):
    return render(request, 'myapp/scanner.html')

def quantity(request, product_id):
    product = Items.objects.get(id=product_id)
    product.Qty += 1
    product.save()
    return redirect('box_click', product.box_id)
    
    
def sub(request, product_id):
    product = Items.objects.get(id=product_id)
    product.Qty -= 1
    product.save()
    return redirect('box_click', product.box_id)


def generate_frame():
    cam = cv2.VideoCapture(0)
    while True:
        success, frame = cam.read()
        if success:
            yield (b'--frame\r\n'
                   b'Content-Type: image/jpeg\r\n\r\n' + cv2.imencode('.jpg', frame)[1].tobytes())
        else:
            break


def simple(request):
    cam = cv2.VideoCapture(0)
    cam.set(3, 640)  # Set width
    cam.set(4, 480)  # Set height

    link = None

    while True:
        success, frame = cam.read()
        cv2.imshow("ourQr_Code_scanner", frame)
        cv2.waitKey(1)  # Reduced wait time to make it more responsive

        if success:
            decoded_objects = decode(frame)  # Assuming `decode` returns a list of decoded objects
            for obj in decoded_objects:
                link = obj.data.decode('utf-8')  # Assuming you want the decoded data as a URL

                # Assuming the data follows the pattern 'box_click/X/', where X is an integer
                try:
                    # box_number = int(link.split('/')[-2])
                    # if box_number == 2:
                        cam.release()  # Release the camera
                        cv2.destroyAllWindows()  # Close any open windows
                        return HttpResponseRedirect(link)
                except ValueError:
                    pass

# Assuming you're using Django, you can now use the `simple` function as a view.


    return StreamingHttpResponse(generate_frame(), content_type='multipart/x-mixed-replace; boundary=frame')

# Assuming you're using Django, you can now use the `simple` function as a view.

    

    # return StreamingHttpResponse(generate_frame(), content_type='multipart/x-mixed-replace; boundary=frame')




    
def scanner(request,feature_id):
    cam = cv2.VideoCapture(0)
    cam.set(5, 640)
    cam.set(6, 480)
    camera = True
    link = None  # Initialize link variable outside the loop
    while camera == True:
        success, frame = cam.read()
        time.sleep(6)
        cv2.imshow("ourQr_Code_scanner", frame)
        cv2.waitKey(3)
        for i in decode(frame):
            link = i.data.decode('utf-8')  # Decode the data
            print(i.type)
            print(link)
            # time.sleep(6)
            # cv2.imshow("ourQr_Code_scanner", frame)
            # cv2.waitKey(3)
        if link is not None:
            return HttpResponseRedirect(link)
    


def qrc(url):
  qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,
  )
  qr.add_data(url)
  qr.make(fit=True)
  img = qr.make_image(fill='black', back_color='white')

  buffer = BytesIO()
  img.save(buffer, format='PNG')
  return File(buffer, name='qrcode.png')



def add_box(request):
  if request.method == 'POST':
    form = BoxForm(request.POST, request.FILES)
    if form.is_valid():
      feature = form.save(commit=False)
      box = features.objects.all()
      max_id = 0
      for box in features.objects.all():
        max_id = max(max_id, box.id)
      # Generate and save QR code image to the database
      qr_url = reverse('box_click', args=[feature.id])
      qr_code_image = qrc(qr_url)
      feature.qr_code_image = qr_code_image
      context = {
        'qr_code_image': feature.qr_code_image,
        'max_id': max_id
      }
      feature.save()

      return render(request, 'myapp/qrcode.html', context)
  else:
    form = BoxForm()
    max_id = 0
    for box in features.objects.all():
      max_id = max(max_id, box.id)
  context = {'form': form, 'max_id': max_id}
  return render(request, 'myapp/add_box.html', context)

    

    
def link(box_id):
    try:
        feature = features.objects.get(id=box_id)
    except features.DoesNotExist:
        return HttpResponse("Feature with id {} does not exist".format(box_id))

    url = reverse('box_click', args=[box_id])
    img = qrc(url)
    print(url)
    feature.qr_code_image.save('qrcode.png', img, save=True)
    # feature.qr_code_image = img
    # feature.save()
    return HttpResponse("QR code generated and saved successfully")

def add_item(request):
    if request.method == 'POST':
        form = ItemForm(request.POST)
        if form.is_valid():
            box_id = int(request.POST.get('box_id'))
            box = features.objects.get(id=box_id)
            form.save()
            box.Qty+=1
            box.save()
            return redirect('rack1')  # Redirect to a success page or item list
    else:
        form = ItemForm()
    return render(request, 'myapp/add_item.html', {'form': form})

def search_item(request):
    if request.method == 'POST':
        form = SearchForm(request.POST)
        if form.is_valid():
            item_name = form.cleaned_data['name']
            try:
                item = Items.objects.get(name=item_name) #item
                box_id = item.box_id #item's box id
                rack = box_id.rack_id
                msg = f'Rack id is {rack} and box id is {box_id}'
                return render(request, 'myapp/search_form.html', {'result': msg})
            except Items.DoesNotExist:
                return render(request, 'myapp/search_form.html', {'error_message': 'Item not found'})
    else:
        form = SearchForm()
    return render(request, 'myapp/search_form.html', {'form': form})
