#!/usr/bin/env python3


import loader


base_mover = loader.load_json_string("""
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

base_light = loader.load_json_string("""
        {
            "spec": {
              "shape": "pointlight",
"red" : [[0.00,1.00],[0.03,1.00],[0.05,1.00],[0.07,1.00],[0.10,1.00],[0.12,1.00],[0.15,1.00],[0.17,0.95],[0.20,0.80],[0.23,0.65],[0.25,0.50],[0.28,0.35],[0.30,0.20],[0.33,0.05],[0.35,0.00],[0.38,0.00],[0.40,0.00],[0.42,0.00],[0.45,0.00],[0.47,0.00],[0.50,0.00],[0.53,0.00],[0.55,0.00],[0.57,0.00],[0.60,0.00],[0.62,0.00],[0.65,0.00],[0.68,0.05],[0.70,0.20],[0.72,0.35],[0.75,0.50],[0.78,0.65],[0.80,0.80],[0.82,0.95],[0.85,1.00],[0.88,1.00],[0.90,1.00],[0.93,1.00],[0.95,1.00],[0.97,1.00],[1.00,1.00]],
"green" : [[0.00,0.00],[0.03,0.15],[0.05,0.30],[0.07,0.45],[0.10,0.60],[0.12,0.75],[0.15,0.90],[0.17,1.00],[0.20,1.00],[0.23,1.00],[0.25,1.00],[0.28,1.00],[0.30,1.00],[0.33,1.00],[0.35,1.00],[0.38,1.00],[0.40,1.00],[0.42,1.00],[0.45,1.00],[0.47,1.00],[0.50,1.00],[0.53,0.85],[0.55,0.70],[0.57,0.55],[0.60,0.40],[0.62,0.25],[0.65,0.10],[0.68,0.00],[0.70,0.00],[0.72,0.00],[0.75,0.00],[0.78,0.00],[0.80,0.00],[0.82,0.00],[0.85,0.00],[0.88,0.00],[0.90,0.00],[0.93,0.00],[0.95,0.00],[0.97,0.00],[1.00,0.00]],
"blue" : [[0.00,0.00],[0.03,0.00],[0.05,0.00],[0.07,0.00],[0.10,0.00],[0.12,0.00],[0.15,0.00],[0.17,0.00],[0.20,0.00],[0.23,0.00],[0.25,0.00],[0.28,0.00],[0.30,0.00],[0.33,0.00],[0.35,0.10],[0.38,0.25],[0.40,0.40],[0.42,0.55],[0.45,0.70],[0.47,0.85],[0.50,1.00],[0.53,1.00],[0.55,1.00],[0.57,1.00],[0.60,1.00],[0.62,1.00],[0.65,1.00],[0.68,1.00],[0.70,1.00],[0.72,1.00],[0.75,1.00],[0.78,1.00],[0.80,1.00],[0.82,1.00],[0.85,0.90],[0.88,0.75],[0.90,0.60],[0.93,0.45],[0.95,0.30],[0.97,0.15],[1.00,0.00]],
              "alpha": 3
            },
            "bLoop" : true,
            "sizeX" : 100,
            "lifetime" : 2,
            "emitterLifetime" : 10,
            "emissionRate" : 500,
            "useWorldSpace" : true,
            "alignVelocityToSurface" : true,
            "useArcLengthSpace" : true,
            "offsetRangeX" : 4082,
            "offsetRangeY" : 4082,
            "offsetZ" : 20,
            "endDistance" : -1
        }
        """)

            #"offsetRangeX" : 4082,
            #"offsetRangeY" : 4082,


def run():
    emitter = { "emitters" : [
                base_light
            ]
        }

    loader.save_json(emitter, "comm_trail.json")

    return [
            { "target" : "/comm_trail.json", "destination" : "/mod/disco_trail.json"},
            {
                "target" : "/pa/units/commanders/base_commander/base_commander.json",
                "patch" : [
                    { "op" : "add", "path" : "/fx_offsets/-", "value" : {
                        "type": "moving",
                        "filename": "/mod/disco_trail.json",
                        "bone": "bone_root",
                        "offset": [0, 0, 0.0],
                        "orientation": [0, 0, 0]
                    }}
                ]
            }
           ]


