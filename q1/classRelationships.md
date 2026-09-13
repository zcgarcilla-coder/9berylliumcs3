# Class Relationships: Association and Multiplicity
## Previous Work
[Part I - Classes and Objects](classObjectUML.md)
[Part II - Class Attributes and Methods](classAttributesMethods.md)
## Existing Class
Class: Movies
Description: This class is an inventory of different movies.
## New Related Class
Class: Genres
Description: This class classifies the movies from the first class into their respective genres.
## Association
Relationship: Movies contain Genres
Explanation: From the first class, the object already has a property for genres. In this class, that property will be used as a classification of these movies.
## Multiplicity

Multiplicity: 1 : many
Explanation: The multiplicity of this relationship is one-to-many. It allows a single object to be identified under several categories which is the genres, as a single movie can have several genres. 
## UML Class Relationship Diagram
![Class Relationship Diagram](images/classRelationshipDiagram.png)
## Python Implementation
[View Python Source](classRelationships.py)
## Test Run
![Relationship Test Run](images/relationshipTestRun.png)
## Object Relationship Diagram
![Object Relationship Diagram](images/objectRelationshipDiagram.png)
## Analysis
### What is the association between your two classes?
### What multiplicity did you choose and why?
### How did you implement the relationship in Python?
### Why did you store an object reference instead of copying its data?
### If your relationship uses many, why is a list appropriate?
