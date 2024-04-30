import os

# Load the configuration file
configfile: "config.yaml"

# Get the input directory and output directory from the configuration
input_dir = config["input_dir"]
output_dir = config["output_dir"]
py_env = config["py_env"]

# Get a list of input files in a directory, only including .pdf files
input_files = [f for f in os.listdir(input_dir) if f.endswith('.pdf')]

# Add the directory path to each file name
output_files = [os.path.join(output_dir, f) for f in input_files]

print(output_files)

# Define rule for each input file
rule all:
    input:
        output_files

rule process_file:
    input:
        pdf=os.path.join(input_dir, "{file}")
    output:
        stretched= os.path.join(output_dir, "{file}")
    shell:
        """
        source {py_env}
        python3 cli/pdf_stretch.py {input.pdf} {output.stretched}
        """