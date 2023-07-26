for i in *.vasp
do
 DIR="${i%*.vasp}"
 mkdir $DIR
 cp -a {INCAR,KPOINTS} $DIR
 cp -a $i $DIR/POSCAR
done
