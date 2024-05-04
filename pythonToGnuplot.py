import os

def generate_gnuplot_script(csv_file1, csv_file2, output_file):
    script = f"""
    set datafile separator ","
    set terminal pngcairo size 800,600 enhanced font 'Verdana,12'
    set output '{output_file}'

    set xlabel 'Time'
    set ylabel 'Shear Stress'
    set title 'Inner and Outer WSS Across Time'

    set grid

    set format y '%.0e'

    plot '{csv_file1}' using 1:2 with lines lw 2 title 'Inner WSS', '{csv_file2}' using 1:2 with lines lw 2 title 'Outer WSS'
    """
    return script

def plot_with_gnuplot(csv_file1, csv_file2, output_file):
    script = generate_gnuplot_script(csv_file1, csv_file2, output_file)
    
    # Write Gnuplot script to a temporary file
    with open('temp_script.gp', 'w') as f:
        f.write(script)
    
    # Execute Gnuplot
    os.system('gnuplot temp_script.gp')

    # Remove temporary Gnuplot script
    os.remove('temp_script.gp')

# Usage example:
csv_file1 = "/home/nishi/Academics/BTU/Academic Notes/Thesis/PostProcessOpenFOAM/csvExport/inner_wss.csv"
csv_file2 = "/home/nishi/Academics/BTU/Academic Notes/Thesis/PostProcessOpenFOAM/csvExport/outer_wss.csv"
output_file = "/home/nishi/Academics/BTU/Academic Notes/Thesis/PostProcessOpenFOAM/plot.png"

plot_with_gnuplot(csv_file1, csv_file2, output_file)
