for f # iterate over files
do
    for e in Au Ag
    do
        n=$(echo "${f}" | sed s/Cu/${e}/ )
        echo "$f ==> $n with $e subst." 
        cat ${f} | sed s/Cu/${e}/ > $n
    done
done

