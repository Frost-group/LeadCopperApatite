rm POTCAR

for i in P   Pb_d    O_h
do
 cat ~/Potpaw_PBE.54/${i}/POTCAR >> POTCAR
done

echo "If not checked it's wrong."
head POSCAR
grep TITEL POTCAR
grep ENMAX POTCAR

