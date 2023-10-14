# Canny Edge Detector

### How to run ?
- Place your intended images inside the `data/` folder to use the implementation or set the path your folder (containing images) in [config.yaml](./src/config.yaml).
- Example run :

    `c = CannyEdgeDetector(config_file_path='config.yaml')`

    For a list of images inside a directory, use 
    `c.detect_edges()`

    For a single image , use 
    `c.detect_edge_of_image("test.jpg")`
- An example notebook is observed in [test.ipynb](./src/test.ipynb)
- You will observe the output edge detected image files in the folder `outputs/`.
- You could modify the [config.yaml](./src/config.yaml) file to modify the configuration settings and the canny edge parameters.

## Example 01
<div style="display: flex;">
    <div style="flex: 1;">
        <img src="./data/bird.jpeg" alt="Raw Bird" style="max-width: 100%;">
    </div>
    <div style="flex: 1;">
        <img src="./outputs/bird.jpeg" alt="Edges Bird" style="max-width: 100%;">
    </div>
</div>

## Example 02
<div style="display: flex;">
    <div style="flex: 1;">
        <img src="./data/face.jpg" alt="Raw Face" style="max-width: 100%;">
    </div>
    <div style="flex: 1;">
        <img src="./outputs/face.jpg" alt="Edges Face" style="max-width: 100%;">
    </div>
</div>

## Example 03
<div style="display: flex;">
    <div style="flex: 1;">
        <img src="./data/car.jpg" alt="Raw Bird" style="max-width: 100%;">
    </div>
    <div style="flex: 1;">
        <img src="./outputs/car.jpg" alt="Edges Bird" style="max-width: 100%;">
    </div>
</div>

## Example 04
<div style="display: flex;">
    <div style="flex: 1;">
        <img src="./data/tree.jpeg" alt="Raw Face" style="max-width: 100%;">
    </div>
    <div style="flex: 1;">
        <img src="./outputs/tree.jpeg" alt="Edges Face" style="max-width: 100%;">
    </div>
</div>

## Example 05
<div style="display: flex;">
    <div style="flex: 1;">
        <img src="./data/building.jpg" alt="Raw Bird" style="max-width: 100%;">
    </div>
    <div style="flex: 1;">
        <img src="./outputs/building.jpg" alt="Edges Bird" style="max-width: 100%;">
    </div>
</div>
