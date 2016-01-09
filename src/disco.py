#!/usr/bin/env python3
import random
import copy
import math
import colorsys

import loader

# produces arrays of color (like a rainbow! xD)
def rainbow(n, offset=0, scale=1, revs=1, time=1):
    r = []
    g = []
    b = []
    for i in range(n + 1):
        t = offset + (float(i) / n) * revs
        rgb = colorsys.hsv_to_rgb(t % 1, 1, 1)
        r.append([float(i) / n * time, scale * rgb[0]])
        g.append([float(i) / n * time, scale * rgb[1]])
        b.append([float(i) / n * time, scale * rgb[2]])
    return (r, g, b)

base_mover = loader.loads("""
        {
            "spec" : {
                "red" : 10,
                "green" : 10,
                "blue" : 10,
                "alpha" : 1,
                "dataChannelFormat" : "PositionColorAndAlignVector"

            },
            "bLoop" : true,
            "lifetime" : 100,
            "emitterLifetime" : 10,
            "emissionRate" : 10,
            "useWorldSpace" : true,
            "alignVelocityToSurface" : true,
            "useArcLengthSpace" : true,
            "snapToSurface" : true,
            "snapToSurfaceOffset" : 10,
            "offsetRangeX" : 4082,
            "offsetRangeY" : 4082,
            "offsetZ" : 20,
            "velocityRangeX" : 1,
            "velocityRangeY" : 1,
            "velocityRange" : 20,
            "velocity" : 100,
            "endDistance" : -1
        }
        """)

base_light = loader.loads("""
        {
            "spec": {
              "shape": "pointlight",
"red" : [[0.00,1.00],[0.03,1.00],[0.05,1.00],[0.07,1.00],[0.10,1.00],[0.12,1.00],[0.15,1.00],[0.17,0.95],[0.20,0.80],[0.23,0.65],[0.25,0.50],[0.28,0.35],[0.30,0.20],[0.33,0.05],[0.35,0.00],[0.38,0.00],[0.40,0.00],[0.42,0.00],[0.45,0.00],[0.47,0.00],[0.50,0.00],[0.53,0.00],[0.55,0.00],[0.57,0.00],[0.60,0.00],[0.62,0.00],[0.65,0.00],[0.68,0.05],[0.70,0.20],[0.72,0.35],[0.75,0.50],[0.78,0.65],[0.80,0.80],[0.82,0.95],[0.85,1.00],[0.88,1.00],[0.90,1.00],[0.93,1.00],[0.95,1.00],[0.97,1.00],[1.00,1.00]],
"green" : [[0.00,0.00],[0.03,0.15],[0.05,0.30],[0.07,0.45],[0.10,0.60],[0.12,0.75],[0.15,0.90],[0.17,1.00],[0.20,1.00],[0.23,1.00],[0.25,1.00],[0.28,1.00],[0.30,1.00],[0.33,1.00],[0.35,1.00],[0.38,1.00],[0.40,1.00],[0.42,1.00],[0.45,1.00],[0.47,1.00],[0.50,1.00],[0.53,0.85],[0.55,0.70],[0.57,0.55],[0.60,0.40],[0.62,0.25],[0.65,0.10],[0.68,0.00],[0.70,0.00],[0.72,0.00],[0.75,0.00],[0.78,0.00],[0.80,0.00],[0.82,0.00],[0.85,0.00],[0.88,0.00],[0.90,0.00],[0.93,0.00],[0.95,0.00],[0.97,0.00],[1.00,0.00]],
"blue" : [[0.00,0.00],[0.03,0.00],[0.05,0.00],[0.07,0.00],[0.10,0.00],[0.12,0.00],[0.15,0.00],[0.17,0.00],[0.20,0.00],[0.23,0.00],[0.25,0.00],[0.28,0.00],[0.30,0.00],[0.33,0.00],[0.35,0.10],[0.38,0.25],[0.40,0.40],[0.42,0.55],[0.45,0.70],[0.47,0.85],[0.50,1.00],[0.53,1.00],[0.55,1.00],[0.57,1.00],[0.60,1.00],[0.62,1.00],[0.65,1.00],[0.68,1.00],[0.70,1.00],[0.72,1.00],[0.75,1.00],[0.78,1.00],[0.80,1.00],[0.82,1.00],[0.85,0.90],[0.88,0.75],[0.90,0.60],[0.93,0.45],[0.95,0.30],[0.97,0.15],[1.00,0.00]],
              "alpha": 4
            },
            "type" : "SPHEROID",
            "bLoop" : true,
            "sizeX" : 30,
            "sizeRangeX" : 10,
            "lifetime" : 2,
            "lifetimeRange" : 1,
            "emitterLifetime" : 10,
            "emissionRate" : 10,
            "useWorldSpace" : true,
            "alignVelocityToSurface" : true,
            "useArcLengthSpace" : true,
            "offsetRangeX" : 120,
            "offsetRangeY" : 120,
            "offsetZ" : 20,
            "endDistance" : -1
        }
        """)

base_smoke = copy.deepcopy(base_light)
base_smoke['offsetZ'] = 0

base_smoke['spec']['shape'] = "rectangle"
base_smoke['spec']['shader'] = "particle_transparent"
base_smoke['emissionRate'] = 1
base_smoke['spec']['red'] = 1
base_smoke['spec']['green'] = 1
base_smoke['spec']['blue'] = 1
base_smoke['spec']['alpha'] = [[0, 0 ], [0.2, 0.6 ], [1, 0]]

dt = random.uniform(0, 1)

c = 10

r = []
g = []
b = []
for i in range(c+1):
    v = float(i) / c

    rgb = colorsys.hsv_to_rgb(v + dt, 1, 1)

    r.append([float(i)/c, rgb[0] + 0.6])
    g.append([float(i)/c, rgb[1] + 0.6])
    b.append([float(i)/c, rgb[2] + 0.6])

# base_smoke['spec']['red'] = [[round(x,2) for x in y] for y in r]
# base_smoke['spec']['green'] = [[round(x,2) for x in y] for y in g]
# base_smoke['spec']['blue'] = [[round(x,2) for x in y] for y in b]

base_smoke['spec']['cameraPush'] = 1

base_smoke['spec']['baseTexture'] = "/pa/effects/textures/particles/softBrownSmoke.papa"
base_smoke['spec']['dataChannelFormat'] = "PositionAndColor"


base_smoke['velocityRangeX'] = 1
base_smoke['velocityRangeY'] = 1
base_smoke['velocityRangeZ'] = 1

base_smoke['velocityRange'] = 1

base_smoke['sizeX'] = 15
base_smoke['sizeRangeX'] = 10
base_smoke['emissionRate'] = 10



base_laser = loader.loads("""
        {
            "spec": {
                "shader": "particle_transparent",
                "shape" : "beam",
                "baseTexture" : "/pa/effects/textures/particles/flat.papa",
                "alpha" : [[0.8, 1], [1, 0]]
            },
            "sizeX" : 0.3,
            "bLoop" : true,
            "lifetime" : 0.5,
            "emitterLifetime" : 1,
            "killOnDeactivate" : true,
            "endDistance" : -1
        }
        """)

            #"offsetRangeX" : 4082,
            #"offsetRangeY" : 4082,


_laser_origin = (0, 0, 50)
_laser_origin_vel = (0, 0, 0)


base_orb = loader.loads("""{
    "spec": {
        "shader": "particle_clip",
        "shape": "mesh",
        "facing": "EmitterZ",
        "red": [[0, 100 ], [0.35, 4 ] ],
        "green": [[0, 10 ], [0.35, 2 ] ],
        "blue": [[0, 100 ], [0.35, 20 ] ],
        "alpha": [[0.0, 0.3 ], [1, 0]],
        "size": [[0, 0 ], [0.1, 0.5 ], [0.2, 0.75 ], [0.3, 0.87 ], [0.4, 0.95 ], [0.5, 1 ]],
        "papa": "/pa/effects/fbx/particles/sphere_ico16seg.papa",
        "materialProperties": {
            "Texture": "/pa/effects/textures/particles/fire_puff.papa"
        }
    },
    "red" : 1,
    "green": 1,
    "blue" : 10,
    "sizeX": 10,
    "sizeRangeX": 1,
    "emissionRate": 5,
    "rotationRange": 6.28,
    "lifetime": 0.8,
    "lifetimeRange": 0.15,
    "emitterLifetime": 15,
    "bLoop": true,
    "endDistance": -1
}""")

base_laser_source = loader.loads("""
    {
    "spec": {
        "shader": "particle_clip",
        "shape": "mesh",
        "facing": "EmitterZ",
        "red": 10,
        "green": 10,
        "blue": 10,
        "alpha": 1,
        "cameraPush" : 1,
        "papa": "/pa/effects/fbx/particles/sphere_ico16seg.papa",
        "materialProperties": {
            "Texture": "/pa/effects/textures/particles/flat.papa"
        }
    },
    "sizeX": 5,
    "sizeY": 5,
    "lifetime": 2,
    "maxParticles" : 1,
    "emitterLifetime" : 1,
    "bLoop": true,
    "endDistance": 2000
    }
    """)



def make_random_laser_group(num=10, radius=500, lifetime=3):
    base = copy.deepcopy(base_laser)
    num_lasers = num
    laser_radius = radius
    base['lifetime'] = lifetime

    _lasers = []

    def add_laser(r, g, b, x, y, z, vx, vy, vz):
        _lasers.append((r, g, b, x, y, z, vx, vy, vz))

    for i in range(num_lasers):
        r, g, b = colorsys.hsv_to_rgb(random.uniform(0, 1), 1, 1)
        r, g, b = 10 * r, 10 * g, 10 * b

        theta = random.uniform(0, math.pi * 2)
        phi = random.uniform(-math.pi / 2, math.pi / 2)

        x = math.cos(phi) * math.sin(theta) * laser_radius
        y = math.cos(phi) * math.cos(theta) * laser_radius
        z = math.sin(phi) * laser_radius

        theta = theta + random.uniform(-math.pi / 6, math.pi / 6)
        phi = phi + random.uniform(-1.2 * math.pi / 4, math.pi / 4)

        dx = math.cos(phi) * math.sin(theta) * laser_radius
        dy = math.cos(phi) * math.cos(theta) * laser_radius
        dz = math.sin(phi) * laser_radius

        add_laser(r, g, b, x, y, z, dx - x, dy - y, dz - z)

    # offsets for laser beams
    laser_offsetX = []
    laser_offsetY = []
    laser_offsetZ = []

    # velocity direction of beams
    laser_velocityX = []
    laser_velocityY = []
    laser_velocityZ = []
    # actual velocity value
    laser_velocity = []

    # choose the laser colors
    laser_red = []
    laser_green = []
    laser_blue = []

    # keying to remove the connections between laser beams
    laser_alpha = []

    def vec_length(x, y, z):
        return math.sqrt(x * x + y * y + z * z)

    num_lasers = len(_lasers)
    for i, l in enumerate(_lasers):
        t1 = float(i) / (num_lasers - 0.5)
        t2 = float(i + 0.5) / (num_lasers - 0.5)

        # color over time
        laser_red.append([t1, l[0]])
        laser_green.append([t1, l[1]])
        laser_blue.append([t1, l[2]])

        # origin offset
        laser_offsetX.append([t1, _laser_origin[0]])
        laser_offsetY.append([t1, _laser_origin[1]])
        laser_offsetZ.append([t1, _laser_origin[2]])

        # beam endpoint offset
        laser_offsetX.append([t2, _laser_origin[0] + l[3]])
        laser_offsetY.append([t2, _laser_origin[1] + l[4]])
        laser_offsetZ.append([t2, _laser_origin[2] + l[5]])

        # origin velocity
        laser_velocityX.append([t1, _laser_origin_vel[0]])
        laser_velocityY.append([t1, _laser_origin_vel[1]])
        laser_velocityZ.append([t1, _laser_origin_vel[2]])
        laser_velocity.append([t1, vec_length(*_laser_origin_vel)])

        lv = [x / base['lifetime'] for x in l[6:9]]

        # beam velocity
        laser_velocityX.append([t2, lv[0]])
        laser_velocityY.append([t2, lv[1]])
        laser_velocityZ.append([t2, lv[2]])
        laser_velocity.append([t2, vec_length(*lv)])

    # laser flicker
    num_flashes = 5
    laser_alpha = []
    for i in range(num_flashes):
        t1 = float(i) / (num_flashes - 0.5)
        t2 = float(i + 0.5) / (num_flashes - 0.5)

        laser_alpha.append([t1, 1])
        laser_alpha.append([t2, 0])

    base['spec']['alpha'] = {"stepped" : True, "keys" : laser_alpha}


    base['red'] = laser_red
    base['green'] = laser_green
    base['blue'] = laser_blue

    base['offsetX'] = laser_offsetX
    base['offsetY'] = laser_offsetY
    base['offsetZ'] = laser_offsetZ

    base['velocityX'] = laser_velocityX
    base['velocityY'] = laser_velocityY
    base['velocityZ'] = laser_velocityZ
    base['velocity'] = laser_velocity


    base['maxParticles'] = len(_lasers) * 2

    return base

def make_orbs():
    global base_orb

    c = [
        (2, 0.1, 0),
        (0, 2, 0),
        (0, 0, 2),
        (1, 0, 0)
    ]

    ret = []
    # there are two orbs
    # make the orb here
    base_orb['emissionRate'] = 3
    base_orb['delay'] = 0
    # def rainbow(n, offset=0, scale=1, revs=1, time=1):
    base_orb['red'], base_orb['green'], base_orb['blue'] = c[0]
    # base_orb['red'], base_orb['green'], base_orb['blue'] = rainbow(40, 0, 10, 1, base_orb['emitterLifetime'])

    ret = ret + [base_orb]

    base_orb['delay'] = 0.25 / base_orb['emissionRate']
    # def rainbow(n, offset=0, scale=1, revs=1, time=1):
    base_orb['red'], base_orb['green'], base_orb['blue'] = c[1]
    # base_orb['red'], base_orb['green'], base_orb['blue'] = rainbow(40, 0.2, 10, 1, base_orb['emitterLifetime'])

    ret = ret + [base_orb]

    base_orb = copy.deepcopy(base_orb)
    base_orb['delay'] = 0.5 / base_orb['emissionRate']
    base_orb['red'], base_orb['green'], base_orb['blue'] = c[2]
    # base_orb['red'], base_orb['green'], base_orb['blue'] = rainbow(40, 0.6, 8, 1, base_orb['emitterLifetime'])

    ret = ret + [base_orb]

    base_orb = copy.deepcopy(base_orb)
    base_orb['delay'] = 0.75 / base_orb['emissionRate']
    base_orb['red'], base_orb['green'], base_orb['blue'] = c[3]
    # base_orb['red'], base_orb['green'], base_orb['blue'] = rainbow(40, 0.8, 11, 1, base_orb['emitterLifetime'])

    ret = ret + [base_orb]

    return ret

def run():
    base_effect = { "emitters" : [
                base_light
            ]
        }

    smoke1 = base_smoke
    smoke2 = copy.deepcopy(smoke1)
    smoke3 = copy.deepcopy(smoke1)
    smoke4 = copy.deepcopy(smoke1)

    smoke2['offsetRangeX'] /= 2
    smoke2['offsetRangeY'] /= 2
    smoke3['offsetRangeX'] /= 4
    smoke3['offsetRangeY'] /= 4
    smoke4['offsetRangeX'] /= 8
    smoke4['offsetRangeY'] /= 8

    base_effect['emitters'].append(smoke1)
    base_effect['emitters'].append(smoke2)
    # base_effect['emitters'].append(smoke3)
    # base_effect['emitters'].append(smoke4)

    base_laser_source['offsetX'] = _laser_origin[0]
    base_laser_source['offsetY'] = _laser_origin[1]
    base_laser_source['offsetZ'] = _laser_origin[2]

    base_effect['emitters'].append(base_laser_source)

    num_laser_groups = 5
    base_laser['emitterLifetime'] = num_laser_groups
    base_laser['emissionBursts'] = 1.0
    base_laser['lifetimeRange'] = 0.5

    for orb in make_orbs():
        orb['offsetX'] = _laser_origin[0]
        orb['offsetY'] = _laser_origin[1]
        orb['offsetZ'] = _laser_origin[2]

        base_effect['emitters'].append(orb)

    for i in range(num_laser_groups * 2):
        l = make_random_laser_group()
        l['delay'] = float(i) / 2

        base_effect['emitters'].append(l)



    loader.dump_effect(base_effect, "comm_trail.json")
    return [
            { "target" : "/comm_trail.json", "destination" : "/mod/disco_trail.json"},
            {
                "target" : "/pa/units/commanders/base_commander/base_commander.json",
                "patch" : [
                    { "op" : "add", "path" : "/fx_offsets/-", "value" : {
                        "type": "idle",
                        "filename": "/mod/disco_trail.json",
                        "bone": "bone_root",
                        "offset": [0, 0, 0],
                        "orientation": [0, 0, 0]
                    }}
                ]
            }
           ]


