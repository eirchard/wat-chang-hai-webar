"""Generate an original stylized CAHAYA stupa (not a faithful heritage reconstruction)."""
from pathlib import Path
import math
import numpy as np
import trimesh

out=Path(__file__).resolve().parents[1]/"assets"/"wat-chang-hai-stupa.glb"
scene=trimesh.Scene()
def add(mesh, color):
    mesh.visual.vertex_colors=np.tile(np.array(color,dtype=np.uint8),(len(mesh.vertices),1))
    scene.add_geometry(mesh)
def box(extents,at,color):
    m=trimesh.creation.box(extents=extents);m.apply_translation(at);add(m,color)
def cylinder(r,h,at,color):
    m=trimesh.creation.cylinder(radius=r,height=h,sections=40)
    m.apply_transform(trimesh.transformations.rotation_matrix(-math.pi/2,[1,0,0]))
    m.apply_translation(at);add(m,color)
def cone(r,h,at,color):
    m=trimesh.creation.cone(radius=r,height=h,sections=64)
    m.apply_transform(trimesh.transformations.rotation_matrix(-math.pi/2,[1,0,0]))
    m.apply_translation(at);add(m,color)
stone=(242,230,206,255); gold=(232,177,51,255); bright=(255,218,129,255)
red=(200,72,42,255); dark=(152,88,30,255)
box((.76,.035,.62),(0,.018,0),stone)
box((.69,.02,.57),(0,.048,0),gold)
box((.62,.018,.51),(0,.067,0),stone)
for rad,y,h,c in [(.23,.081,.04,stone),(.22,.122,.02,gold),(.196,.147,.29,red),(.174,.441,.035,dark),(.16,.47,.035,stone),(.142,.51,.025,gold)]:
    cylinder(rad,h,(0,y+h/2,0),c)
cone(.143,.34,(0,.54,0),gold)
for y in np.linspace(.57,.845,16):
    r=max(.008,.148*(.9-(y-.57)/.32*.85))
    cylinder(r,.008,(0,float(y),0),bright if round(y*100)%2 else dark)
cylinder(.006,.060,(0,.91,0),dark)
for x in (-.28,.28):
    box((.17,.12,.22),(x,.15,0),stone)
    box((.20,.018,.25),(x,.22,0),red)
    cone(.045,.1,(x,.23,0),gold)
for x in (-.24,.24):
    for z in (-.19,.19):
        cylinder(.026,.035,(x,.108,z),red)
        cone(.035,.11,(x,.14,z),gold)
out.parent.mkdir(parents=True,exist_ok=True)
out.write_bytes(scene.export(file_type="glb"))
print(f"Created {out}: {out.stat().st_size} bytes")
