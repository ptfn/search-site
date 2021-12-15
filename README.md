# SearchSite

The utility is designed to search for sites.

## Arguments:

There are two arguments in total:
* 1.Maximum website domain generation
* 2.Alphabet for generating a website domain

## Alphanet:
* BigChar(A..Z) -> b 
* SmallChar(a..z) -> c
* Number(0..9) -> n
* Symbols(!?@#$%^&*=<>()[]/|,.+-_) -> s

## Running:

```
$pip3 install -r requirements.txt
$python3 search_site.py 16 bcns
```

## Stoping:
Ctrl+C - stopping and showing statistics

## Saving:

All sites with names are saved in site.txt
