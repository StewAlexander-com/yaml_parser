# yaml_parser

```
This python 3 program creates a list of keys from an ingested yaml file,
and then enters / adds the keys as a sorted list in a new file called "keys.txt".
One can search for all partial matches for a key, and once the key or keys are found provide the value pairs.

These values are also added to a file called "output.yaml" for easy retrieval later
```
---
* This code requires python3 and pip3
* This code also requires the pyyaml library, to install install it use "```pip install pyyaml```"
* I created this as I use saltstack to routinely gather the list of interfaces on my network; it returns output in yaml, and this allows
me to gather details for specific systems, regardless of the editor I have available
* Future:
- [x] Search for all the keys with a partial match (Done 10/29)
