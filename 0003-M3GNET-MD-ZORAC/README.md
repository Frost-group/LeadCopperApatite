Thu 27 Jul 00:18:47 BST 2023
Sea state: Very high
jarvist@zorac: /home/jarvist/REPOS/LeadCopperApatite/0003-M3GNET-MD-ZORAC

Just a note, that this is using the new PyTorch MGL interface to M3GNET, which
was super easy to get working:

```sh
conda create -n mgl
conda activate mgl
conda install pip
pip install matgl
mgl -h # to ensure proper installation
```

<details>
<summary>CUDA</summary>

For CUDA to work, you may also need to re-install the `dgl` package to an updated version, see [this page](https://www.dgl.ai/pages/start.html)

To force the reinstall, use flags like this:

```sh
pip install -U --force-reinstall -f https://data.dgl.ai/wheels/cu118/repo.html
```

</details>

mgl is a little poorly documented currently; but the python primitives
I recognised from ASE & the code is quite readable, so very quickly threw
together something capable of doing MD. 
(While waiting for the queued VASP jobs to run :^)

Doing MD, all 32 cores on Zorac are being occupied, but it's not touching the
GPU. I haven't checked whether it would be possible / any faster to unload
PyTorch to CUDA.

