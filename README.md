# Development of a Python-Based Software for Calculating the Jones Polynomial: Insights into the Behavior of Polymers and Biopolymers

[https://arxiv.org/pdf/2410.22652](https://arxiv.org/abs/2410.22652)

## Abstract

This thesis details a Python-based software designed to calculate the Jones polynomial, a vital mathematical tool from Knot Theory used for characterizing the topological and geometrical complexity of curves in \( \mathbb{R}^3 \), which is essential in understanding physical systems of filaments, including the behavior of polymers and biopolymers. The Jones polynomial serves as a topological invariant capable of distinguishing between different knot structures. This capability is fundamental to characterizing the architecture of molecular chains, such as proteins and DNA. Traditional computational methods for deriving the Jones polynomial have been limited by closure-schemes and high execution costs, which can be impractical for complex structures like those that appear in real life. This software implements methods that significantly reduce calculation times, allowing for more efficient and practical applications in the study of biological polymers. It utilizes a divide-and-conquer approach combined with parallel computing and applies recursive Reidemeister moves to optimize the computation, transitioning from an exponential to a near-linear runtime for specific configurations. This thesis provides an overview of the software's functions, detailed performance evaluations using protein structures as test cases, and a discussion of the implications for future research and potential algorithmic improvements.

## Usage

Basic usage can be ran through main.py. Additional 3-D knot configurations can be found in example-knots.txt

## Acknowledgments

Thesis Advisor: Eleni Panagiotou, Ph.D.
Committee Members: Andrea Richa, Ph.D.

All code was written by Kasturi Barkataki and Caleb Musfeldt
