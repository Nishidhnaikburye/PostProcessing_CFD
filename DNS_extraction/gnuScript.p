set datafile separator ','

set title 'RMS Values'
set xlabel 'Time'
set ylabel 'RMS'

set grid

set term png size 1200, 720
set output 'RmsBoersma.png'

plot 'Urms.csv' u 1:2 w lp lw 1.5 lc 7 title 'Urms', \
     'Vrms.csv' u 1:2 w lp lw 1.5 lc 6 title 'Vrms', \
     'Wrms.csv' u 1:2 w lp lw 1.5 lc 5 title 'Wrms'
