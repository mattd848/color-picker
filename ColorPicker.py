'''
Created on Mar 29, 2013

@author: Naved
'''
from collections import namedtuple
from math import sqrt
import random
try:
    import Image
except ImportError:
    from PIL import Image

Point = namedtuple('Point', ('coords', 'n', 'ct'))
Cluster = namedtuple('Cluster', ('points', 'center', 'n'))
cmap={
'000000':'Black',
'150517':'Gray',
'250517':'Gray',
'2B1B17':'Gray',
'302217':'Gray',
'302226':'Gray',
'342826':'Gray',
'34282C':'Gray',
'382D2C':'Gray',
'3b3131':'Gray',
'3E3535':'Gray',
'413839':'Gray',
'41383C':'Gray',
'463E3F':'Gray',
'4A4344':'Gray',
'4C4646':'Gray',
'4E4848':'Gray',
'504A4B':'Gray',
'544E4F':'Gray',
'565051':'Gray',
'595454':'Gray',
'5C5858':'Gray',
'5F5A59':'Gray',
'625D5D':'Gray',
'646060':'Gray',
'666362':'Gray',
'696565':'Gray',
'6D6968':'Gray',
'6E6A6B':'Gray',
'726E6D':'Gray',
'747170':'Gray',
'736F6E':'Gray',
'616D7E':'Slate Gray',
'657383':'Slate Gray',
'646D7E':'Light Steel Blue',
'6D7B8D':'Light Slate Gray',
'4C787E':'Cadet Blue',
'4C7D7E':'Dark Slate Gray',
'806D7E':'Thistle',
'5E5A80':'Medium Slate Blue',
'4E387E':'Medium Purple',
'151B54':'Midnight Blue',
'2B3856':'Dark Slate Blue',
'25383C':'Dark Slate Gray',
'463E41':'Dim Gray',
'151B8D':'Cornflower Blue',
'15317E':'Royal Blue',
'342D7E':'Slate Blue',
'2B60DE':'Royal Blue',
'306EFF':'Royal Blue',
'2B65EC':'Royal Blue',
'2554C7':'Royal Blue',
'3BB9FF':'Deep Sky Blue',
'38ACEC':'Deep Sky Blue',
'3574EC7':'Slate Blue',
'3090C7':'Deep Sky Blue',
'25587E':'Deep Sky Blue',
'1589FF':'Dodger Blue',
'157DEC':'Dodger Blue',
'1569C7':'Dodger Blue',
'153E7E':'Dodger Blue',
'2B547E':'Steel Blue',
'4863A0':'Steel Blue',
'6960EC':'Slate Blue',
'8D38C9':'Violet',
'7A5DC7':'Medium Purple',
'8467D7':'Medium Purple',
'9172EC':'Medium Purple',
'9E7BFF':'Medium Purple',
'728FCE':'Light Steel Blue',
'488AC7':'Steel Blue',
'56A5EC':'Steel Blue',
'5CB3FF':'Steel Blue',
'659EC7':'Sky Blue',
'41627E':'Sky Blue',
'737CA1':'Slate Blue',
'737CA1':'Slate Blue',
'98AFC7':'Slate Gray',
'F6358A':'Violet Red',
'F6358A':'Violet Red',
'E4317F':'Violet Red',
'F52887':'Deep Pink',
'E4287C':'Deep Pink',
'C12267':'Deep Pink',
'7D053F':'Deep Pink',
'CA226B':'Medium Violet Red',
'C12869':'Violet Red',
'800517':'Firebrick',
'7D0541':'Violet Red',
'7D0552':'Maroon',
'810541':'Maroon',
'C12283':'Maroon',
'E3319D':'Maroon',
'F535AA':'Maroon',
'FF00FF':'Magenta',
'F433FF':'Magenta',
'E238EC':'Magenta',
'C031C7':'Magenta',
'B048B5':'Medium Orchid',
'D462FF':'Medium Orchid',
'C45AEC':'Medium Orchid',
'A74AC7':'Medium Orchid',
'6A287E':'Medium Orchid',
'8E35EF':'Purple',
'893BFF':'Purple',
'7F38EC':'Purple',
'6C2DC7':'Purple',
'461B7E':'Purple',
'571B7e':'Dark Orchid',
'7D1B7E':'Dark Orchid',
'842DCE':'Dark Violet',
'8B31C7':'Dark Orchid',
'A23BEC':'Dark Orchid',
'B041FF':'Dark Orchid',
'7E587E':'Plum',
'D16587':'Pale Violet Red',
'F778A1':'Pale Violet Red',
'E56E94':'Pale Violet Red',
'C25A7C':'Pale Violet Red',
'7E354D':'Pale Violet Red',
'B93B8F':'Plum',
'F9B7FF':'Plum',
'E6A9EC':'Plum',
'C38EC7':'Plum',
'D2B9D3':'Thistle',
'C6AEC7':'Thistle',
'EBDDE2':'Lavendar Blush',
'C8BBBE':'Lavendar Blush',
'E9CFEC':'Thistle',
'FCDFFF':'Thistle',
'E3E4FA':'Lavendar',
'FDEEF4':'Lavendar Blush',
'C6DEFF':'Light Steel Blue',
'ADDFFF':'Light Blue',
'BDEDFF':'Light Blue',
'E0FFFF':'Light Cyan',
'C2DFFF':'Slate Gray',
'B4CFEC':'Slate Gray',
'B7CEEC':'Light Steel Blue',
'52F3FF':'Turquoise',
'00FFFF':'Cyan',
'57FEFF':'Cyan',
'50EBEC':'Cyan',
'4EE2EC':'Turquoise',
'48CCCD':'Medium Turquoise',
'43C6DB':'Turquoise',
'9AFEFF':'Dark Slate Gray',
'8EEBEC':'Dark slate Gray',
'78c7c7':'Dark Slate Gray',
'46C7C7':'Cyan',
'43BFC7':'Turquoise',
'77BFC7':'Cadet Blue',
'92C7C7':'Pale Turquoise',
'AFDCEC':'Light Blue',
'3B9C9C':'Dark Turquoise',
'307D7E':'Cyan',
'3EA99F':'Light Sea Green',
'82CAFA':'Light Sky Blue',
'A0CFEC':'Light Sky Blue',
'87AFC7':'Light Sky Blue',
'82CAFF':'Sky Blue',
'79BAEC':'Sky Blue',
'566D7E':'Light Sky Blue',
'6698FF':'Sky Blue',
'736AFF':'Light Slate Blue',
'CFECEC':'Light Cyan',
'AFC7C7':'Light Cyan',
'717D7D':'Light Cyan',
'95B9C7':'Light Blue',
'5E767E':'Light Blue',
'5E7D7E':'Pale Turquoise',
'617C58':'Dark Sea Green',
'348781':'Medium Aquamarine',
'306754':'Medium Sea Green',
'4E8975':'Sea Green',
'254117':'Dark Green',
'387C44':'Sea Green',
'4E9258':'Forest Green',
'347235':'Medium Forest Green',
'347C2C':'Spring Green',
'667C26':'Dark Olive Green',
'437C17':'Chartreuse',
'347C17':'Green',
'348017':'Medium Spring Green',
'4AA02C':'Spring Green',
'41A317':'Lime Green',
'4AA02C':'Spring Green',
'8BB381':'Dark Sea Green',
'99C68E':'Dark Sea Green',
'4CC417':'Green',
'6CC417':'Chartreuse',
'52D017':'Yellow Green',
'4CC552':'Spring Green',
'54C571':'Sea Green',
'57E964':'Spring Green',
'5EFB6E':'Spring Green',
'64E986':'Sea Green',
'6AFB92':'Sea Green',
'B5EAAA':'Dark Sea Green',
'C3FDB8':'Dark Sea Green',
'00FF00':'Green',
'87F717':'Lawn Green',
'5FFB17':'Green',
'59E817':'Green',
'7FE817':'Chartreuse',
'8AFB17':'Chartreuse',
'B1FB17':'Green Yellow',
'CCFB5D':'Dark Olive Green',
'BCE954':'Dark Olive Green',
'A0C544':'Dark Olive Green',
'FFFF00':'Yellow',
'FFFC17':'Yellow',
'FFF380':'Khaki',
'EDE275':'Khaki',
'EDDA74':'Goldenrod',
'EAC117':'Gold',
'FDD017':'Gold',
'FBB917':'Goldenrod',
'E9AB17':'Goldenrod',
'D4A017':'Gold',
'C7A317':'Gold',
'C68E17':'Goldenrod',
'AF7817':'Dark Goldenrod',
'ADA96E':'Khaki',
'C9BE62':'Khaki',
'827839':'Khaki',
'FBB117':'Dark Goldenrod',
'E8A317':'Dark Goldenrod',
'C58917':'Dark Goldenrod',
'F87431':'Sienna',
'E66C2C':'Sienna',
'F88017':'Dark Orange',
'F87217':'Dark Orange',
'E56717':'Dark Orange',
'C35617':'Dark Orange',
'C35817':'Sienna',
'8A4117':'Sienna',
'7E3517':'Sienna',
'7E2217':'Indian Red',
'7E3117':'Dark Orange',
'7E3817':'Salmon',
'7F5217':'Dark Goldenrod',
'806517':'Gold',
'805817':'Goldenrod',
'7F462C':'Light Salmon',
'C85A17':'Chocolate',
'C34A2C':'Coral',
'E55B3C':'Coral',
'F76541':'Coral',
'E18B6B':'Dark Salmon',
'F88158':'Pale Turquoise',
'E67451':'Salmon',
'C36241':'Salmon',
'C47451':'Light Salmon',
'E78A61':'Light Salmon',
'F9966B':'Light Salmon',
'EE9A4D':'Sandy Brown',
'F660AB':'Hot Pink',
'F665AB':'Hot Pink',
'E45E9D':'Hot Pink',
'C25283':'Hot Pink',
'7D2252':'Hot Pink',
'E77471':'Light Coral',
'F75D59':'Indian Red',
'E55451':'Indian Red',
'C24641':'Indian Red',
'FF0000':'Red',
'F62217':'Red',
'E41B17':'Red',
'F62817':'Firebrick',
'E42217':'Firebrick',
'C11B17':'Firebrick',
'FAAFBE':'Pink',
'FBBBB9':'Rosy Brown',
'E8ADAA':'Rosy Brown',
'E7A1B0':'Pink',
'FAAFBA':'Light Pink',
'F9A7B0':'Light Pink',
'E799A3':'Light Pink',
'C48793':'Pink',
'C5908E':'Rosy Brown',
'B38481':'Rosy Brown',
'C48189':'Light Pink',
'7F5A58':'Rosy Brown',
'7F4E52':'Light Pink',
'7F525D':'Pink',
'817679':'Lavendar Blush',
'817339':'Light Goldenrod',
'827B60':'Lemon Chiffon',
'C9C299':'Lemon Chiffon',
'C8B560':'Light Goldenrod',
'ECD672':'Light Golden',
'ECD872':'Light Goldenrod',
'FFE87C':'Light Goldenrod',
'ECE5B6':'Lemon Chiffon',
'FFF8C6':'Lemon Chiffon',
'FAF8CC':'Light Goldenrod Yellow'
      }
def get_points(img):
    points = []
    w, h = img.size
    for count, color in img.getcolors(w * h):
        points.append(Point(color, 3, count))
    return points

rtoh = lambda rgb: '#%s' % ''.join(('%02x' % p for p in rgb))

def colorz(filename, n=3):
    img = Image.open(filename)
    img.thumbnail((200, 200))
    w, h = img.size

    points = get_points(img)
    clusters = kmeans(points, n, 1)
    rgbs = [map(int, c.center.coords) for c in clusters]
    return map(rtoh, rgbs)

def euclidean(p1, p2):
    return sqrt(sum([
        (p1.coords[i] - p2.coords[i]) ** 2 for i in range(p1.n)
    ]))

def calculate_center(points, n):
    vals = [0.0 for i in range(n)]
    plen = 0
    for p in points:
        plen += p.ct
        for i in range(n):
            vals[i] += (p.coords[i] * p.ct)
    return Point([(v / plen) for v in vals], n, 1)

def kmeans(points, k, min_diff):
    clusters = [Cluster([p], p, p.n) for p in random.sample(points, k)]

    while 1:
        plists = [[] for i in range(k)]

        for p in points:
            smallest_distance = float('Inf')
            for i in range(k):
                distance = euclidean(p, clusters[i].center)
                if distance < smallest_distance:
                    smallest_distance = distance
                    idx = i
            plists[idx].append(p)

        diff = 0
        for i in range(k):
            old = clusters[i]
            center = calculate_center(plists[i], old.n)
            new = Cluster(plists[i], center, old.n)
            clusters[i] = new
            diff = max(diff, euclidean(old.center, new.center))

        if diff < min_diff:
            break

    return clusters

def get_color_name(hx):
    hx=hx.replace('#','')
    # if color is found in dict
    if cmap.has_key(hx):return cmap[hx]

    # else return its closest available color
    m = 16777215
    k = '000000'
    for key in cmap.keys():
        a = int(hx[:2],16)-int(key[:2],16)
        b = int(hx[2:4],16)-int(key[2:4],16)
        c = int(hx[4:],16)-int(key[4:],16)

        v = a*a+b*b+c*c # simple measure for distance between colors

        # v = (r1 - r2)^2 + (g1 - g2)^2 + (b1 - b2)^2

        if v <= m:
            m = v
            k = key

    return cmap[k]

print get_color_name('#008040')