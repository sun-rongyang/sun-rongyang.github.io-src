title: Build Your Own HPC Cluster: (1) Hardware Construction 
date: 2018-02-18 09:23
category: HPC
tags: HPC, cluster, Linux, hardware
## Introduction
High performance computing (HPC) Linux cluster is a powerful tool for scientific research. If you have a research group, it is very convenient to collect your computing resource by building a HPC cluster. In this `Build Your Own HPC Cluster` series, I will introduce how to construct your own HPC cluster using [Centos 7](https://www.centos.org) Linux distribution and [OpenHPC](https://openhpc.community) tools. I select [Slurm](https://slurm.schedmd.com) as job scheduling system.

In the first post of the series, I will introduce something about hardware construction. Roughly, that is how to connect your _computers_ (nodes) together.

## Main node
Main node also called login node, control node or controller which is a computer has two network interfaces, and one of them connects to the Internet, the other connects to a network switch.

## Compute node
Several computers with one network interface are as compute nodes. They are all connected to the same network switch.

## Network structure
Now, we can connect all the nodes together. First, we select a network interface on the login node and connect it to the Internet. Then we connect the other network interface to the network switch. Finally, we connect all the network interfaces on compute nodes to the same network switch.

## Conclusion
That is all requirement for hardware. In the next post, I will introduce how to install CentOS on the main node.
