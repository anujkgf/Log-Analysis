# Log Analysis Project

## Table of Contents

* [Project-Description](#Project-Description)
* [Dependency](#Dependency)
* [Instructions](#Instructions)


## Project-Description

This project involves analysing the given database and then answer the three question.

The database consist of three tables names authors, articles, log.
1. authors table consists information about the authors.
2. articles table consists information about the articles that the authors have written.
3. log table consists of the data about the site usage.M


## Dependency
To run this project you should have the following things on your computer.
1. Python.
2. Virtual box.
3. Vagrant.

## Instructions
- Install virtual box and vagrant.
- Download or clone Udacity full-stack nanodegree vm repository.
- Download the database `newsdata.sql` and put this file in vagrant folder.
---
- Inside the FSND-vm folder open terminal.
- Connect to vagrant using `vagrant up` & `vagrant ssh`.
- Go into vagrant directory using `cd /vagrant`.
---
- Load the database by `psql -d news -f newsdata.sql`

---
- Run `python Log.py` for the answers.
- You can look for the answers in `Answer.txt`.

---
---
**Shubham Sharma**
