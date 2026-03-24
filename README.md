# Compton Experiment

## Preliminaries: Github settings
- fist add a file named ".gitignore" this will automatically be recognised by Git, so that it ignores all files (pdf for reading, *.log, etc...) that are not required to be shared.
Here is the content of my `.gitignore` file:

```gitignore
# my literature to read (comments in .gitignore)
reading/

# any other pdf, also from .tex
*.pdf

# latex specific
*.out
*.fls
*.log
*.xml
*.sta
*.gz
*.aux
*.bbl
*.fdb_latexmk
*.bcf
*.blg
*.toc

# do not change
.gitignore

# my python environment
analysis-code/.compton_environment/
```


## Report and Latex

Depending on from which directory the "main.tex" will be compiled from, the **figures/picutres will be accessed by a different path**. 

In report/main.tex there is a line that will access all figures from figure/ and, or pictures/ (line 22)
> \graphicspath{{../figures/}{../pictures/}}

run from commandline:
> cd report && pdflatex main.tex



## Python coding

The necessary packages are in "analysis-code/requirements.txt". 

#### Workflow: using pip (venv) 
Create python environment in analysis-code, i.e. with "venv" using BASH:
> python3 -m venv analysis-code/.compton_environment

To activate it type
> source analysis-code/.compton_environment/bin/activate

Use
> which pip
**to make sure you are using the correct environment!**

To **install all packages** for which are used:
> which pip
> pip install -r requirements.txt

If you **add a different package** (make sure your **correct environment is active!**):
> which pip
> pip install PACKAGE_NAME
> pip freeze > requirements.txt

Thus the "requirements.txt is up-to-date, including all packages that might be used.


#### Wrokflow: organisation
The analysis should be carried out in main.py!
Functions should be defined in the appropriate file! Add further files if needed. 
Keep track of packages being used.

Access functions in main.py i.e. by the following:
```python
# main.py
from data_loader import load_spectrum
from calibration import calibrate_energy
from fitting import fit_gaussian
from plotting import plot_spectrum

# Load
channels, counts = load_spectrum("../data/measurement1.txt")

# Calibrate
energies = calibrate_energy(channels, a=0.5, b=10)

# Fit
peak_center, peak_width = fit_gaussian(energies, counts)

# Plot
plot_spectrum(energies, counts, peak_center)
```



## Data, Figures, Pictures, Results

- The meausrements -> data/
- plots (i.e. from analysis) go to figures/
- photos -> pictures/
- results from analysis -> results/

Every directory contains an "orientation.txt" file. This should help to keep log, enabling concise naming of files, with descriptions.