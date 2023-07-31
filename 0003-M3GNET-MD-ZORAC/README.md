Thu 27 Jul 00:18:47 BST 2023
Sea state: Very high
jarvist@zorac: /home/jarvist/REPOS/LeadCopperApatite/0003-M3GNET-MD-ZORAC

Just a note, that this is using the new PyTorch MGL interface to M3GNET, which
was super easy to get working:

conda create -n mgl
conda activate mgl
conda install pip
pip install matgl
mgl -h

mgl is a little poorly documented currently; but the python primitives
I recognised from ASE & the code is quite readable, so very quickly threw
together something capable of doing MD. 
(While waiting for the queued VASP jobs to run :^)

Doing MD, all 32 cores on Zorac are being occupied, but it's not touching the
GPU. I haven't checked whether it would be possible / any faster to unload
PyTorch to CUDA.

Thu 27 Jul 13:09:46 BST 2023
Sea state: Smooth
jarvist@zorac: /home/jarvist/REPOS/LeadCopperApatite/0003-M3GNET-MD-ZORAC

; pip install --upgrade MDAnalysis

For analysis.

