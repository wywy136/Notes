# Jupyter Notebook

### Display of graphics

Magic function to make matplotlib inline; other style specs must come AFTER

```
%matplotlib inline
```

This enables high resolution PNGs. SVG is preferred, but has problems ``rendering vertical and horizontal lines

```
%config InlineBackend.figure_formats = {'png', 'retina'}
```