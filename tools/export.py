# re-export tia's drive photos with proper colour management (Display P3 -> sRGB) into the site
from PIL import Image, ImageOps, ImageCms
import pillow_heif, glob, os, io, sys
pillow_heif.register_heif_opener()
OUT='/Users/nickgibbons/markettiaa/assets/img'
SRGB=ImageCms.createProfile('sRGB')
def load(src):
    im=Image.open(src); icc=im.info.get('icc_profile')
    im=ImageOps.exif_transpose(im)
    if im.mode!='RGB': im=im.convert('RGB')
    if icc:
        try:
            prof=ImageCms.ImageCmsProfile(io.BytesIO(icc))
            if 'sRGB' not in (ImageCms.getProfileDescription(prof) or ''):
                im=ImageCms.profileToProfile(im,prof,SRGB,outputMode='RGB',renderingIntent=ImageCms.Intent.PERCEPTUAL)
        except Exception as e: print('icc skip',src,e)
    return im
def save(src,name,maxw=1600,q=86):
    im=load(src); im.thumbnail((maxw,maxw))
    im.save(f'{OUT}/{name}',quality=q,optimize=True,progressive=True,subsampling=0)
    print(name,im.size,os.path.getsize(f'{OUT}/{name}')//1024,'KB')
R=sys.argv[1] if len(sys.argv)>1 and not sys.argv[1].endswith('.jpg') else 'raw'  # folder of downloaded Drive originals
def one(pattern): return sorted(glob.glob(pattern))[0]
JOBS=[
 (f'{R}/front-page/01-main-image','hero-desk.jpg',1800),
 (f'{R}/4-about-me-images/01-fullsizerender.heic','me-friends.jpg',1600),
 (f'{R}/4-about-me-images/02-img-0373.jpg','me-queenstown.jpg',1600),
 (f'{R}/4-about-me-images/03-img-3907.dng','me-opera.jpg',1600),
 (f'{R}/4-about-me-images/04-img-4611.dng','me-sea.jpg',1600),
 (f'{R}/ongoing-vs-one-off/01-one-off-content-creation-image','svc-oneoff.jpg',1600),
 ('raw2/new-ongoing.bin','svc-ongoing.jpg',1600),
]
for i,n in [(1,'cr-sofa'),(2,'cr-group'),(3,'cr-detail'),(4,'cr-door'),(6,'cr-bag'),(7,'cr-robes')]:
    JOBS.append((one(f'{R}/images-for-creators/{i:02d}-*'),f'{n}.jpg',1600))
for i,n in [(1,'lucas-cookies'),(2,'lucas-team'),(3,'lucas-drink'),(4,'lucas-shop-wide'),(5,'lucas-baristas2'),(6,'lucas-shop-autumn'),(7,'lucas-front'),(8,'lucas-drinks')]:
    JOBS.append((one(f'{R}/luca-s-images/{i:02d}-*'),f'{n}.jpg',1600))
for i,n in [(1,'rw-lounge'),(2,'rw-vinyl'),(3,'rw-outside'),(4,'rw-event'),(5,'rw-spritz'),(6,'rw-breakfast'),(7,'rw-overhead'),(8,'rw-room'),(9,'rw-terrace'),(10,'rw-table'),(11,'rw-cake'),(12,'rw-tequila'),(13,'rw-decks')]:
    JOBS.append((one(f'{R}/rockwater-images/{i:02d}-*'),f'{n}.jpg',1600))
only=sys.argv[1:] 
for src,name,mw in JOBS:
    if only and name not in only: continue
    save(src,name,mw)
