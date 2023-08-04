for f in *Au*.vasp *Ag*.vasp
do
    echo "$f"
    python md_ase_m3gnet.py "${f}"  
done
