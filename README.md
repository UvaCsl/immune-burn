# Modeling Systemmic Inflammation in Severe Burn Patients
This study is part of a bigger cause: ultimately assess the effect of Alkaline Phosphatase on Severe Burn Patients

## Introduction

Severe burn injuries can be life-threatening and cause a severe systemic inflammatory response and associated complications. The first stage of treatment is mainly focussed on resuscitation and stabilisation of the patients into a stage where clinical condition is not life-threatening any longer. After the patient becomes stabilised, wound closure has to be achieved. Scar and psychological treatment are subsequent. This project focusses on the first stage of burn care, where patients are concerned with survival from systemic inflammation response and high risk for sepsis following burns. Until now, active pharmaceutical intervention possibilities for this stage in burns are limited. This project aims at studying a novel application of the clinical therapeutic compound (Alkaline Phosphatase). An in-silico study (computer simulation of the inflammatory response) will be performed aimed at optimising clinical care procedures that facilitate intensive care decision processes towards individual patient specific treatment (personalised treatment).

The objectives are to 

1. Assess the safety and preliminary efficacy of Alkaline Phosphatase in reducing the inflammatory reaction in severely burned patients admitted to the intensive care unit
2. To develop a mathematical model of the dynamics of the innate immune response. The study consists of four work packages: 

- WP1: Collection of baseline/referential data from severely burned patients
- WP2: Clinical study of a novel application of the clinical therapeutic compound Alkaline Phosphatase
- WP3: Analysis of blood samples from WP1 and WP2
- WP4: Modelling of all collected data to determine general and specific characteristics of the inflammatory response after severe burn injury, which will allow predicting efficacy of the drug in reducing the inflammatory response.

The project will advance scientific fundamental knowledge on inflammatory aspects of severe burns and the influence of Alkaline Phosphatase on this response. This will allow the development of new treatment strategies to improve health care and quality of life for severe burn wound patients and possibly other fibrotic pathologies, and optimal recovery of severe burn patients will reduce health care costs due to shorter hospital stay and reduced time out of work.


## Set-up

1. Clone this repository to your local
```
git clone git@github.com:UvaCsl/immune-burn.git
```
2. Create an environment named `immune` using the `requirements.txt` file

```
conda create --name <env> --file requirements.txt
```

## Files Included

There are 4 folders in the current repository:
1. `burn` : contains burn package, meaning the necessary codes to run the notebooks
2. `data` :  contains data used for the simulations
3. `notebooks` :  contains the notebooks to run the experiments 
4. `results` :  contains results of the simulations

## Reference
1. [Modelling and modulation of the inflammatory response in severe burns
](https://www.health-holland.com/project/2018/modelling-and-modulation-of-the-inflammatory-response-in-severe-burns)