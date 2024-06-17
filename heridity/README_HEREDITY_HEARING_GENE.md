# GJB2 Gene and Hearing Impairment

This project focuses on modeling the genetic inheritance of the GJB2 gene, which is associated with hearing impairment. It employs Bayesian networks to infer the likelihood that an individual carries certain genetic traits based on familial data and observable traits.

## Background
Mutated versions of the GJB2 gene are a significant cause of hearing impairment in newborns. Each individual inherits two copies of the gene, which can be normal or mutated. The presence of these mutations affects the probability of exhibiting traits like hearing impairment. Understanding these probabilities requires modeling the genetic inheritance patterns and mutation probabilities.

## Bayesian Network Model
The project uses a Bayesian network to model the relationships between genetic traits and observable traits (like hearing impairment):

* **Gene Variable:** Represents the number of copies of the GJB2 gene (0, 1, or 2) that an individual carries.
* **Trait Variable:** Indicates whether an individual exhibits a specific trait (e.g., hearing impairment) based on their gene status.
* **Inheritance:** Genes are inherited from parents with specified probabilities. Mutation of genes can occur with a given probability.

## Getting Started
To begin using the project:

1. **Download the Distribution Code:** Clone or download the distribution code from here and unzip it.
   ```git clone <repository-url>```
2. **Change the directory:** Change the directory to where the file is cloned.
  ```cd <repository-directory>```
3. **Understand the Data:** Explore the sample datasets located in the data directory. Each CSV file (e.g., family0.csv) contains information about individuals, their parents, and whether they exhibit the trait.
4. **Explore heredity.py:** Run the file and see the probabilities of them containing the gene.
   ```python heredity.py family2.csv```
**YOU CAN CHANGE THE FAMILY NUMBER DEPENDING ON THE FAMILY YOU WANT THE PROBABILITES FOR**

## Specification
This project requires implementing three core functions in **heredity.py:**

* **joint_probability:** Computes the joint probability of the genetic and trait variables for a given family structure.
* **update:** Updates the probability distributions with newly computed joint probabilities.
* **normalize:** Normalizes the probability distributions to ensure they sum to 1 after updates.
  
These functions use predefined probabilities (PROBS) for gene inheritance, trait expression, and mutation probabilities. Detailed specifications and examples are provided in the heredity.py file to guide implementation.
![Screenshot 2024-06-16 at 7 53 07 PM](https://github.com/naman39/projects/assets/59209974/73d95316-5e6e-4888-905e-d3a2a768fd08)
