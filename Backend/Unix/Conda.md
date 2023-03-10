# Conda commands

## Env Management

- Export an environment to a yml file

```
conda env export | grep -v "^prefix: " > environment.yml
```

- Create an environment from a yml file

```
conda env create -f environment.yml
```

- Update an environment from a yml file

```
conda activate myenv
conda env update --file local.yml --prune
```

