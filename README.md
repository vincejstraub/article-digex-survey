## Updates

22 Nov 2022

Hi Jason, I hope this README and the various notebooks and module docstrings make everything clear to follow :) I've only been able to work on the project on weekends the last month but I will free some time up in December to try and do as much of the analysis as possible pre Christmas. Looking forward to hearing your thoughts on the structure and getting started with the exploratory data anlaysis.
___________________________________________

# Public Attitudes and Ethical Guidelines in Digital Field Experiments (digex)

[![Project Status: Active – The project has reached a stable, usable state and is being actively developed.](https://www.repostatus.org/badges/latest/active.svg)](https://www.repostatus.org/#active) 

The purpose of this survey study is to better understand public attitudes towards the research practices and the use of social media data in academic studies, particularly digital field experiments. This is important because social media data are increasingly used in academic studies despite a lack of clear and consistent ethical standards to guide researchers. Our results provide a guide on what the public think of current academic practices and highlight what factors researchers need to take into account to ensure their studies can best align with and benefit the broader public.

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
