import pyqrcode
import vobject
import logging
import urllib.request
from PIL import Image
import os
import base64

def create_qr(request):
    logging.info(f"Starting execution with payload: {request.args}")
    token = request.args.get("token")
    fn = request.args.get("fn")
    if fn is None:
        fn = "Moshiko Zaguri"
    logging.info(f"Vcard data: {fn} ({token})")
    if len(fn) > 0 and token == "123456":
        j = vobject.vCard()
        
        o = j.add('n')
        o.value = vobject.vcard.Name( family='', given='TLS Marketing' )
        
        o = j.add("fn")
        o.value = fn
        
        o = j.add("title")
        o.value = "Marketing"
        
        o = j.add("email")
        o.value = "info@tls.marketing"
        o.type_param = "Email"
        
        o = j.add("tel")
        o.value = "9179631371"
        
        
        o.type_param = 'Phone'
        
        o = j.add("tel")
        o.value = "9179631371"
        o.type_param = 'Fax'
        
        o = j.add("url")
        o.value = "https://tls.marketing"
        o.type_param = "Website"
        
        o = j.add("url")
        o.value = "http://www.linkedin.com/in/tls"
        o.type_param = "Linkedin"
        
        o = j.add("url")
        o.value = "http://www.facebook.com/tls"
        o.type_param = "Facebook"
        
        o = j.add("url")
        o.value = "http://twitter.com/tls"
        o.type_param = "Twitter"
        
        o = j.add("url")
        o.value = "https://www.instagram.com/tls"
        o.type_param = "Instagram"
        
        o = j.add("url")
        o.value = "https://wa.me/19179631371"
        o.type_param = "Whatsapp"
        
        o = j.add("url")
        o.value = "https://youtube.com/tls"
        o.type_param = "Youtube"
        
        o = j.add("url")
        o.value = "https://t.me/tls"
        o.type_param = "Telegram"
        
        o = j.add("url")
        o.value = "http://www.pinterest.com/tls"
        o.type_param = "Pinterest"
        
        o = j.add("url")
        o.value = "http://www.flickr.com/photos/tls"
        o.type_param = "Flickr"
        
        o = j.add("url")
        o.value = "http://www.myspace.com/tls"
        o.type_param = "My Space"
        
        o = j.add("url")
        o.value = "http://weibo.com/n/tls"
        o.type_param = "Sina Weibo"
        
        o = j.add("url")
        o.value = "https://cutomurl.com"
        o.type_param = "Custom Utl"
        
        o = j.add("adr")
        o.type_param = "Address"
        o.value = vobject.vcard.Address(
            street="80 South West 8th Street",
            city="Miami",
            region="FL",
            code="33130",
            country="United States",
            box="",
            extended=""
        )
        
        o = j.add("note")
        o.value = "This is a business note"
        
        img = Image.open("avatar.jpg")
        new_size = img.resize((40, 40))
        new_size.save('avatar1.jpg')
        image = open("avatar1.jpg", 'rb')
        image.seek(0)
        # print (os.stat("avatar1.jpg").st_size)
        image_read = image.read()
        encoded_string = base64.b64encode(image_read)
        # j.add("photo")
        # j.photo.type_param = "JPEG"
        # j.photo.encoding_param = "base64"
        # j.photo.value = encoded_string.decode('utf-8')
        vcard_input = j.serialize()
        print(vcard_input)
        qr = pyqrcode.create(vcard_input, error="L", version=40)
        qr.png('vcard.png', scale=5)
        # qr.show()
        
        
        
        
        # vcard_file_name = input('hallo.vcf')
        # with open(vcard_file_name, 'r') as myfile:
        #     vcard = myfile.read()
            
        # myfile = open('hallo.vcf', 'r')
        # vcard = myfile.read()
        
        # QR_CODE_TEMPLATE = "http://api.qrserver.com/v1/create-qr-code/?data=%s&size=300x300"
        # vcard_url = QR_CODE_TEMPLATE % (vcard)
        # print(vcard_url)
        # cnxn = urllib.request.urlopen(vcard_url)
        # qr_code = cnxn.read()
        # qr_code.show()
        # cnxn.close()
        # qr_filename = "qr_code.png"
        
        # with open(qr_filename, 'w') as qr_file_hdl:
        #     qr_file_hdl.write(qr_code)
        # print ("Created QR-code %s file." %(qr_filename))
        
        
        
        image_as_str = qr.png_as_base64_str(scale=5)
        html_img = '<img src="data:image/png;base64,{}">'.format(image_as_str)
        # print(html_img)
        logging.info(f"Image generated: {html_img}")
        return html_img


if __name__ == "__main__":
    payload = {
        "token": "123456",
        "fn": "TLS Marketing"
    }
    fake_context = type("fake_class", (object,), {"args": payload})()
    # new_size.show()
    create_qr(fake_context)
