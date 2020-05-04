# esprit
Dataset and documentation for paper on explaining solutions to physical reasoning tasks (ESPRIT))

This repo provides the dataset used to reproduce results in our paper accepted at ACL 2020 -- ESPRIT: Explaining Solutions to Physical ReasonIng Tasks.
Our dataset extends the Physical Reasoning (PHYRE) dataset (https://phyre.ai/) to include annotations for pivotal frames as well as natural language open ended explanations for the solutions to 2D physics simulations.

We note that we only focus on the PHYRE tasks in which the solution involves placing a single red ball and we were able to get solutions for 2,441 of 2500 tasks across 25 different templates (please see our paper for more details).

The repo contains the following datasets:
- Human annotations: This directory includes open-ended text annotations for the initial scene and the sequence of salient events.
- Data tables: This directory includes data about the objects, their attributes , their position, and their velocity.
- Pivotal frames images: This directory includes snapshots of the initial state and sequence of salient events. Note that we used visual data only for collecting human annotations and evaluations.

The dataset is also split according to the phases.
