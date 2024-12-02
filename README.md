# Public attitudes towards social media field experiments (digex)

The code contained in this repository was used for an article that now been published and can be accessed via the link below:

> Straub, V.J., Burton, J.W., Geers, M. et al. Public attitudes towards social media field experiments. Sci Rep **14**, 26110 (2024). [https://doi.org/10.1038/s41598-024-76948-z](https://doi.org/10.1038/s41598-024-76948-z)

## Installation and use

Description of files contained in repository:

```
├── code/
│   └── digex_src/  --> This directory contains the source code for the project
│   └── notebooks/  --> This directory contains jupyter notebooks with code for exploratory analysis 
│   └── run_analysis.py  --> This file can be run to reproduce the entire data analysis workflow
├── data/ 
│   └── processed/  -->  This directory contains the CSV file used for the analysis
│   └── raw/   -->  This directory contains the (anonymized) .xlsx file downloaded from Qualtrics
│   └── DATAREADME.txt 
├── docs/  
│   └── resources/
├── reports/   --->  This directory contains all the outputs produced by the analysis
│   └──figures/
│   └── digex-processed-data-report.html
│   └── digex-raw-data-report.html
│   └── variable-table.html
├── requirements.txt   ---> This file contains the requirements needed to reproduce the analysis
```

To reproduce the analysis, clone the repository and run the following command from within the `code/` directory:

```console
foo@bar:~$ python run_analysis.py
```

## Requirements

See the `requirements.txt` file.

Please follow the online instructions to install the required libraries, depending on your operating system and machine specifications. 

## License

MIT License. See the `LICENSE.MD` file for details.
