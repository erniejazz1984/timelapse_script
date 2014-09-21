a=1
for i in *.JPG; do
	new=$(printf "D_%04d.JPG" ${a})
	mv ${i} ${new}
	let "a=a+1"
	echo $i
done
