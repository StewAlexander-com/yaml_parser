# yaml_parser

```
This python 3 program creates a list of keys from a ingested yaml file,
and then prints the keys in the list in a new file called "keys.txt"
Then one can ask for the value of a key by typing the key name in the terminal, which it also
saves in a yaml file called "outputs.yaml
```
---
* This code requires python3 and pip3
* This code also requires the pyyaml library, to install install it use "```pip install pyyaml```"
* I created this as I use saltstack to routinely gather the list of interfaces on my network; it returns output in yaml, and this allows
me to search the output, regardless of the editor I have available
* Future
[] fuzzy search (partial search) the key list for a key
