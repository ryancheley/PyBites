for file in *.py
do
    dir="${file%.py}"
    mkdir -- "$dir"
    mv -- "$file" "$dir"
done