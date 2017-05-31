for i in `seq 51 70`
do
    ./amg2006 -r 10 10 10 -maxiter $i >> ASUS/original_10
done;
for i in `seq 51 75`
do
    ./amg2006fast -r 10 10 10 -maxiter $i >> ASUS/fast4_10
done;
for i in `seq 51 85`
do
    ./amg2006up -r 10 10 10 -maxiter $i >> ASUS/up_10
done

