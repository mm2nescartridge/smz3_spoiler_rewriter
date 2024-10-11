# smz3_spoiler_rewriter
Python script to rewrite a spoiler log for SMZ3 Randomizer to use the community location names, be actually readable, and be usable for spoiler log races.


## Usage Guide
Download the spoiler log from the seed page and put it in the same directory as the script.
Name the downloaded log `spoiler.yaml` (or something else, and specify the name with `-f [NAME]`)
If you want your output to be named anything other than `output.json`, specify this with `-o [NAME]`
Run the script in Terminal/Command Prompt/whatever. The script should output 'Conversion complete.' in the shell on success.
Your output file will be located in the same directory as the script.

## Modification
If you think some name I created sucks, feel free to modify the values of the corresponding dict. It should (hopefully) be fairly self-explanatory
It should 'Just Work" as long as you leave the keys the same (as these are used to detect which location is which in the original log).

### Requirements
`numpy`, `pyyaml`

## Contact
Please direct all complaints to `mm2nescartridge` on discord.