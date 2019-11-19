# Mining Dynamic Networks with Generative Models

SDM 2020 Tutorial
Kevin S. Xu (University of Toledo) and James R. Foulds (University of Maryland, Baltimore County)

## Brief Description

Traditional data mining algorithms for networks typically assume that the network is in the form of a single static graph, which either represents a single time snapshot or an aggregate view over time. However, this is often an oversimplification of the underlying network phenomenon. For example, in the age of social media, many of our social interactions are recorded digitally with timestamps, and the *temporal dynamics* can yield as much insight as the graph structure. Thus, it has become increasingly clear that network mining algorithms need to go beyond a single graph to include time information. Generative probabilistic models are well-suited for such analyzing such rich network data, as they provide a natural framework for reasoning collectively over structured data.

This tutorial presents recent advances in generative models for dynamic networks, focusing on models that encode network phenomena with latent (i.e. hidden) attributes, which are subsequently recovered from data. We consider dynamic networks in two different forms: *discrete-time networks*, where the network evolves through a set of snapshots observed at discrete time steps, and *continuous-time networks*, where the network is observed through relational events at arbitrary, irregularly-spaced timestamps. Our focus will be on continuous-time networks, which differ most from static networks due to the absence of graph snapshots. For such networks, model-based analysis using point process models can reveal significant insights about the frequency, burstiness, and ordering of edges in networks that are not possible to uncover using snapshot-based analyses.

## Presenters

Kevin S. Xu (University of Toledo): [Personal website](http://kevinsxu.com)

James R. Foulds (Jimmy) (University of Maryland, Baltimore County): [Personal website](http://jfoulds.informationsystems.umbc.edu)