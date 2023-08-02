for f # iterate over files
do
    for e in Au Ag
    do
        n=$(echo "${f}" | sed s/Cu/${e}/ )
        echo cat "${f}" sed -i '' s/Cu/${e}/ $n
    done
done

